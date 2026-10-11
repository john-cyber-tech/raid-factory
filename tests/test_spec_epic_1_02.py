"""SPEC-EPIC-1-02 — Reject invalid extraction output.

Story EPIC-1-02. Covers REQ-005, REQ-006, REQ-041 (and NFR-005 through CF-2).
`pending.json` is the only way model output enters the tool, so anything that
does not match the contract in SPEC-EPIC-1-05 is refused whole: exit 1, a
message naming the proposal and field, no proposal shown, nothing written.
"""
import ast
import copy
import json
import re
import tomllib
import unicodedata

import pytest

from helpers import (
    FIXTURES,
    P1_TITLE,
    P2_TITLE,
    P3_TITLE,
    REPO,
    VALID_THREE,
    log_items,
    log_path,
    new_project,
    run,
    write_pending,
)

SCHEMA = REPO / "src" / "raid" / "schemas" / "pending.schema.json"
CONTRACT_SPEC = REPO / "docs" / "specs" / "SPEC-EPIC-1-05.md"
SRC = REPO / "src" / "raid"

VALID = json.loads(VALID_THREE.read_text(encoding="utf-8"))["proposals"]
ANSWERS = "a\n" * 5  # would accept everything if a review were allowed to start


def proposal(**changes):
    """P1 from the valid fixture with some keys changed."""
    return dict(copy.deepcopy(VALID[0]), **changes)


def without(key):
    changed = copy.deepcopy(VALID[0])
    del changed[key]
    return changed


def rejected(folder):
    """Run `raid review`; assert the whole file was refused and nothing was written. Returns the output."""
    log_before = log_path(folder).read_bytes() if log_path(folder).exists() else None
    pending_before = (folder / "pending.json").read_bytes()

    code, output = run(folder, "review", answers=ANSWERS)

    assert code == 1
    assert "pending.json" in output
    # No proposal was shown for a decision, and no name was asked for.
    assert "Accept or reject" not in output
    assert "Your name:" not in output
    for title in (P1_TITLE, P2_TITLE, P3_TITLE):
        assert f"Title:       {title}" not in output
    # The log is untouched and the bad file is left as it was for inspection.
    log_after = log_path(folder).read_bytes() if log_path(folder).exists() else None
    assert log_after == log_before
    assert (folder / "pending.json").read_bytes() == pending_before
    return output


def project_with(tmp_path, fixture_name):
    return new_project(tmp_path, fixture=FIXTURES / fixture_name)


def test_not_json_is_rejected(tmp_path):
    """REQ-006: a pending.json that is not JSON is refused, naming the file and the parse error; the log is unchanged (criterion 1)."""
    # A log already exists, so "unchanged" is checked against real content.
    folder = new_project(tmp_path)
    assert run(folder, "review", answers="a\nr\na\n")[0] == 0
    (folder / "pending.json").write_bytes((FIXTURES / "not_json.json").read_bytes())

    output = rejected(folder)

    assert "not valid JSON" in output
    assert "line 1" in output
    assert sorted(log_items(folder)) == ["D-001", "R-001"]


def test_missing_title_is_rejected(tmp_path):
    """REQ-006: a proposal with no title is refused, naming `title` and proposal 1 (criterion 2)."""
    output = rejected(project_with(tmp_path, "missing_title.json"))

    assert "proposal 1" in output
    assert "title" in output
    assert "missing" in output


def test_bad_type_is_rejected(tmp_path):
    """REQ-006: a proposal of type Question is refused, naming `type` and the four allowed values (criterion 3)."""
    output = rejected(project_with(tmp_path, "bad_type.json"))

    assert "proposal 1" in output
    assert "type" in output
    for allowed in ("Risk", "Assumption", "Issue", "Dependency"):
        assert allowed in output


def test_one_bad_proposal_rejects_all(tmp_path):
    """REQ-005: the second proposal is invalid, so nothing is shown for a decision, not even the valid first one (criterion 4)."""
    output = rejected(project_with(tmp_path, "second_invalid.json"))

    assert "proposal 2" in output
    assert "severity" in output
    assert "proposal 1" not in output and "proposal 3" not in output


def test_title_81_rejected_80_accepted(tmp_path):
    """REQ-041: an 81-character title is refused naming `title` and the limit of 80; exactly 80 is valid (criterion 5)."""
    output = rejected(project_with(tmp_path, "title_81.json"))

    assert "proposal 1" in output
    assert "title" in output and "81" in output and "80" in output

    folder = new_project(tmp_path, "exactly_80", fixture=FIXTURES / "title_80.json")
    code, _ = run(folder, "review", answers="a\n")
    assert code == 0
    assert len(log_items(folder)["R-001"]["title"]) == 80


def test_extra_field_is_rejected(tmp_path):
    """NFR-005 (CF-2): a proposal with an extra key `accepted: true` is refused, naming the key."""
    output = rejected(project_with(tmp_path, "extra_field.json"))

    assert "proposal 1" in output
    assert "accepted" in output


def test_control_characters_are_rejected(tmp_path):
    """NFR-005 (CF-2): a title containing an escape character is refused, naming `title`, and the character is not echoed."""
    output = rejected(project_with(tmp_path, "control_char.json"))

    assert "proposal 1" in output
    assert "title" in output
    assert "\x1b" not in output


@pytest.mark.parametrize(
    "field, value",
    [
        ("due_date", "2026-13-40"),
        ("due_date", "2026-02-30"),
        ("due_date", "25 Oct"),
        ("due_date", "2026-10-25T00:00:00"),
        ("source_date", "2026-02-30"),
        ("source_date", "07/10/2026"),
        # Forms Python's own date parser would accept; only exact YYYY-MM-DD is allowed.
        ("due_date", "20261007"),
        ("source_date", "20261007"),
        ("due_date", "2026-W41-3"),
        ("source_date", "2026-W41-3"),
        ("due_date", "2026-10-07\n"),
        ("source_date", "2026-10-07\n"),
        ("due_date", " 2026-10-07"),
        ("due_date", "\uff12\uff10\uff12\uff16-10-07"),  # full-width digits
        ("due_date", "2026-1-7"),
        ("due_date", "0000-01-01"),
    ],
)
def test_impossible_date_is_rejected(tmp_path, field, value):
    """REQ-006: a date that is not a real calendar date in YYYY-MM-DD form is refused, naming the field (criterion 2, edge)."""
    folder = new_project(tmp_path, fixture=None)
    write_pending(folder, [proposal(**{field: value})])

    output = rejected(folder)

    assert "proposal 1" in output
    assert field in output


def test_impossible_date_fixture_is_rejected(tmp_path):
    """REQ-006: the `bad_date.json` fixture (due_date 2026-13-40) is refused, naming `due_date` (criterion 2, edge)."""
    output = rejected(project_with(tmp_path, "bad_date.json"))

    assert "proposal 1" in output and "due_date" in output


def test_partly_written_file_is_rejected(tmp_path):
    """REQ-006: a file cut off mid-object is reported as a parse error (criterion 1, edge)."""
    output = rejected(project_with(tmp_path, "truncated.json"))

    assert "not valid JSON" in output


def test_valid_fixture_passes(tmp_path):
    """REQ-005: valid_three.json validates and the first proposal is shown (criterion 4)."""
    from raid.validator import validate

    proposals, errors = validate(VALID_THREE)
    assert errors == []
    assert [p["title"] for p in proposals] == [P1_TITLE, P2_TITLE, P3_TITLE]

    folder = new_project(tmp_path)
    code, output = run(folder, "review", answers="")  # input ends at the first question
    assert code == 1
    assert f"Title:       {P1_TITLE}" in output


def test_every_error_is_listed(tmp_path):
    """REQ-006: a file with two bad proposals lists both, each with its number and field (criterion 2, edge)."""
    output = rejected(project_with(tmp_path, "two_invalid.json"))

    assert "proposal 1" in output and "type" in output
    assert "proposal 3" in output and "source_excerpt" in output
    assert "proposal 2" not in output


CONTRACT_VIOLATIONS = {
    # Shape of the file
    "empty file": ("", ["not valid JSON"]),
    "top level is a list": (json.dumps(VALID), ["proposals"]),
    "no proposals key": ("{}", ["proposals"]),
    "extra top-level key": (json.dumps({"proposals": VALID, "approved": True}), ["approved"]),
    "proposals is not a list": (json.dumps({"proposals": "none"}), ["proposals"]),
    "a proposal is not an object": (json.dumps({"proposals": ["accept all"]}), ["proposal 1"]),
    # Required keys (description, owner and due_date may be empty or null but must be present)
    "missing description": ([without("description")], ["proposal 1", "description"]),
    "missing owner": ([without("owner")], ["proposal 1", "owner"]),
    "missing due_date": ([without("due_date")], ["proposal 1", "due_date"]),
    "missing severity": ([without("severity")], ["proposal 1", "severity"]),
    "missing source_excerpt": ([without("source_excerpt")], ["proposal 1", "source_excerpt"]),
    # Allowed values
    "type in lower case": ([proposal(type="risk")], ["proposal 1", "type"]),
    "severity Critical": ([proposal(severity="Critical")], ["proposal 1", "severity", "High", "Medium", "Low"]),
    "severity null": ([proposal(severity=None)], ["proposal 1", "severity"]),
    "empty title": ([proposal(title="")], ["proposal 1", "title"]),
    "title null": ([proposal(title=None)], ["proposal 1", "title"]),
    "title is a number": ([proposal(title=42)], ["proposal 1", "title"]),
    "title on two lines": ([proposal(title="Client security review\nmay delay cutover")], ["proposal 1", "title"]),
    "tab in title": ([proposal(title="Client security\treview")], ["proposal 1", "title"]),
    "description null": ([proposal(description=None)], ["proposal 1", "description"]),
    "owner is a list": ([proposal(owner=["Priya", "Tom"])], ["proposal 1", "owner"]),
    "owner on two lines": ([proposal(owner="Priya\nTom")], ["proposal 1", "owner"]),
    "empty source_excerpt": ([proposal(source_excerpt="")], ["proposal 1", "source_excerpt"]),
    "source_excerpt null": ([proposal(source_excerpt=None)], ["proposal 1", "source_excerpt"]),
    "escape in description": ([proposal(description="Fine\u001b[31m text")], ["proposal 1", "description"]),
    "null byte in source_excerpt": ([proposal(source_excerpt="Tom said\u0000 so")], ["proposal 1", "source_excerpt"]),
    "due_date is a number": ([proposal(due_date=20261025)], ["proposal 1", "due_date"]),
    # JSON true where text is expected
    "title true": ([proposal(title=True)], ["proposal 1", "title"]),
    "severity true": ([proposal(severity=True)], ["proposal 1", "severity"]),
    "due_date true": ([proposal(due_date=True)], ["proposal 1", "due_date"]),
    "source_date true": ([proposal(source_date=True)], ["proposal 1", "source_date"]),
    # Line and control characters beyond the plain line break and tab
    "carriage return in title": ([proposal(title="Client security\rreview")], ["proposal 1", "title"]),
    "U+2028 in title": ([proposal(title="Client security\u2028review")], ["proposal 1", "title"]),
    "U+0085 in title": ([proposal(title="Client security\u0085review")], ["proposal 1", "title"]),
    "C1 control in title": ([proposal(title="Client security\u009b2Jreview")], ["proposal 1", "title"]),
    "carriage return in owner": ([proposal(owner="Priya\r")], ["proposal 1", "owner"]),
    "lone carriage return in description": ([proposal(description="First line.\rSecond line.")], ["proposal 1", "description"]),
    "carriage return at the end of description": ([proposal(description="First line.\r")], ["proposal 1", "description"]),
    "carriage return then tab in description": ([proposal(description="First line.\r\tSecond line.")], ["proposal 1", "description"]),
    "two carriage returns then a line break": ([proposal(description="First line.\r\r\nSecond line.")], ["proposal 1", "description"]),
    "Windows line ending in title": ([proposal(title="Client security\r\nreview")], ["proposal 1", "title"]),
    "Windows line ending in owner": ([proposal(owner="Priya\r\nTom")], ["proposal 1", "owner"]),
    "U+2028 in description": ([proposal(description="First line.\u2028Second line.")], ["proposal 1", "description"]),
    "U+0085 in description": ([proposal(description="First line.\u0085Second line.")], ["proposal 1", "description"]),
    "C1 control in description": ([proposal(description="Fine\u009b31m text")], ["proposal 1", "description"]),
    "lone carriage return in source_excerpt": ([proposal(source_excerpt="Tom said so.\rLena agreed.")], ["proposal 1", "source_excerpt"]),
    # (2) Bidirectional controls can make text read differently from what is stored
    "bidi override in title": ([proposal(title="Review \u202egnissim\u202c on track")], ["proposal 1", "title"]),
    "bidi embedding in owner": ([proposal(owner="\u202aPriya\u202c")], ["proposal 1", "owner"]),
    "bidi isolate in description": ([proposal(description="Low risk \u2066not\u2069 really")], ["proposal 1", "description"]),
    "bidi override in source_excerpt": ([proposal(source_excerpt="Tom said \u202dso")], ["proposal 1", "source_excerpt"]),
    "U+202A in title": ([proposal(title="A\u202aB")], ["proposal 1", "title"]),
    "U+202B in title": ([proposal(title="A\u202bB")], ["proposal 1", "title"]),
    "U+202C in title": ([proposal(title="A\u202cB")], ["proposal 1", "title"]),
    "U+202D in title": ([proposal(title="A\u202dB")], ["proposal 1", "title"]),
    "U+202E in title": ([proposal(title="A\u202eB")], ["proposal 1", "title"]),
    "U+2066 in title": ([proposal(title="A\u2066B")], ["proposal 1", "title"]),
    "U+2067 in title": ([proposal(title="A\u2067B")], ["proposal 1", "title"]),
    "U+2068 in title": ([proposal(title="A\u2068B")], ["proposal 1", "title"]),
    "U+2069 in title": ([proposal(title="A\u2069B")], ["proposal 1", "title"]),
    # (3) Duplicate keys: JSON allows them and a plain reader keeps the last one silently
    "duplicate title": (
        json.dumps({"proposals": [VALID[0]]}).replace('"title":', '"title": "Low priority, ignore", "title":', 1),
        ["proposal 1", "title", "more than once"],
    ),
    "duplicate severity with the same value": (
        json.dumps({"proposals": [VALID[0]]}).replace('"severity":', '"severity": "High", "severity":', 1),
        ["proposal 1", "severity", "more than once"],
    ),
    "duplicate key in the third proposal": (
        json.dumps({"proposals": VALID}).replace('"owner": null, "severity": "Medium"', '"owner": null, "owner": "Tom", "severity": "Medium"', 1),
        ["proposal 3", "owner", "more than once"],
    ),
    "duplicate proposals key": (
        '{"proposals": [], "proposals": ' + json.dumps(VALID) + "}",
        ["proposals", "more than once"],
    ),
    "U+2028 in source_excerpt": ([proposal(source_excerpt="Tom said so.\u2028Lena agreed.")], ["proposal 1", "source_excerpt"]),
    "C1 control in source_excerpt": ([proposal(source_excerpt="Tom said\u0090 so")], ["proposal 1", "source_excerpt"]),
    # Length is counted in Unicode code points
    "81 accented characters": ([proposal(title="\u00e9" * 81)], ["proposal 1", "title", "81", "80"]),
    "80 characters then an emoji": ([proposal(title="x" * 80 + "\U0001f525")], ["proposal 1", "title", "81", "80"]),
    "joined emoji takes it past 80": ([proposal(title="x" * 78 + "\U0001f469\u200d\U0001f4bb")], ["proposal 1", "title", "81", "80"]),
    # Keys the log owns must not come in from outside
    "extra key id": ([proposal(id="R-001")], ["proposal 1", "id"]),
    "extra key status": ([proposal(status="Closed")], ["proposal 1", "status"]),
    "extra key history": ([proposal(history=[])], ["proposal 1", "history"]),
}


@pytest.mark.parametrize("content, expected", CONTRACT_VIOLATIONS.values(), ids=CONTRACT_VIOLATIONS.keys())
def test_contract_violations_are_rejected(tmp_path, content, expected):
    """REQ-005, REQ-006, NFR-005: anything outside the SPEC-EPIC-1-05 contract refuses the whole file, naming what is wrong."""
    folder = new_project(tmp_path, fixture=None)
    if isinstance(content, str):
        (folder / "pending.json").write_text(content, encoding="utf-8")
    else:
        write_pending(folder, content)

    output = rejected(folder)

    for text in expected:
        assert text in output


VALID_EDGES = {
    "source_date absent": without("source_date"),
    "source_date null": proposal(source_date=None),
    "description empty": proposal(description=""),
    "line breaks and tabs in description": proposal(description="First line.\n\tSecond line."),
    "line break in source_excerpt": proposal(source_excerpt="Tom said the review hasn't started;\nLena thinks 3-4 weeks."),
    "owner null and due_date null": proposal(owner=None, due_date=None),
    "accents and symbols": proposal(title="Révision sécurité — cutover at risk (£)", owner="Zoë Ångström"),
    "leap day": proposal(due_date="2028-02-29"),
    "80 accented characters": proposal(title="\u00e9" * 80),
    "79 characters then an emoji": proposal(title="x" * 79 + "\U0001f525"),
    "Windows line endings in description": proposal(description="First line.\r\nSecond line.\r\n"),
    "Windows line endings in source_excerpt": proposal(source_excerpt="Tom said so.\r\nLena agreed."),
    "zero-width joiner in title": proposal(title="Analyst \U0001f469\u200d\U0001f4bb on leave in November"),
    "zero-width joiner in description": proposal(description="Owner: \U0001f469\u200d\U0001f4bb"),
}


@pytest.mark.parametrize("valid", VALID_EDGES.values(), ids=VALID_EDGES.keys())
def test_valid_edge_cases_pass(tmp_path, valid):
    """REQ-005: everything the SPEC-EPIC-1-05 contract allows is accepted, so the validator refuses nothing it should not."""
    folder = new_project(tmp_path, fixture=None)
    write_pending(folder, [valid])

    code, output = run(folder, "review", answers="r\n")

    assert code == 0
    assert "Rejected." in output


UNPRINTABLE_VALUES = {
    "escape in type": proposal(type="Risk\u001b[2J"),
    "escape in severity": proposal(severity="\u001b[31mHigh"),
    "escape in due_date": proposal(due_date="\u001b[31m2026-10-25"),
    "escape in an extra key name": dict(proposal(), **{"acc\u001b[2Jepted": True}),
    "escape and C1 in title": proposal(title="Review\u001b[2J\u009b2J\u2028done"),
    "bell and backspace in owner": proposal(owner="Priya\u0007\u0008"),
    "escape in an extra key value": dict(proposal(), note="\u001b]0;owned\u0007"),
}


@pytest.mark.parametrize("bad", UNPRINTABLE_VALUES.values(), ids=UNPRINTABLE_VALUES.keys())
def test_bad_values_are_not_echoed_raw(tmp_path, bad):
    """NFR-005: a refused value or key containing an escape or other control character is never written raw into the message."""
    folder = new_project(tmp_path, fixture=None)
    write_pending(folder, [bad])

    output = rejected(folder)

    assert "proposal 1" in output
    raw = sorted({
        f"U+{ord(ch):04X}" for ch in output
        if ch != "\n" and (unicodedata.category(ch) in ("Cc", "Cf", "Zl", "Zp"))
    })
    assert raw == []


def test_windows_line_endings_are_stored_as_given(tmp_path):
    """REQ-012, NFR-005: an accepted excerpt with Windows line endings is stored exactly as it came, not rewritten."""
    excerpt = "Tom said so.\r\nLena agreed."
    folder = new_project(tmp_path, fixture=None)
    write_pending(folder, [proposal(source_excerpt=excerpt)])

    code, _ = run(folder, "review", answers="a\n")

    assert code == 0
    assert log_items(folder)["R-001"]["sources"][0]["excerpt"] == excerpt


def test_missing_file_is_still_nothing_to_review(tmp_path):
    """REQ-005, REQ-007: with no pending.json there is nothing to validate; the command says nothing to review and exits 0."""
    folder = new_project(tmp_path, fixture=None)

    code, output = run(folder, "review", answers=ANSWERS)

    assert code == 0
    assert "nothing to review" in output.lower()
    assert sorted(path.name for path in folder.iterdir()) == ["raid-config.json"]


def test_empty_proposals_list_is_valid(tmp_path):
    """REQ-005: a pending.json with zero proposals is valid and there is nothing to review."""
    folder = new_project(tmp_path, fixture=None)
    write_pending(folder, [])

    code, output = run(folder, "review")

    assert code == 0
    assert "nothing to review" in output.lower()


def contract_table():
    """Key -> required (True/False), read from the contract table in SPEC-EPIC-1-05."""
    rows = re.findall(r"^\| `(\w+)` \| (yes|no) \|", CONTRACT_SPEC.read_text(encoding="utf-8"), re.M)
    return {key: required == "yes" for key, required in rows}


def test_schema_matches_the_contract_table():
    """REQ-005 (ADR-004): the schema file and the contract table in SPEC-EPIC-1-05 agree key for key, with no external references."""
    table = contract_table()
    assert len(table) == 8, "the contract table in SPEC-EPIC-1-05 was not read"
    text = SCHEMA.read_text(encoding="utf-8")
    schema = json.loads(text)

    assert list(schema["properties"]) == ["proposals"]
    assert schema["required"] == ["proposals"]
    assert schema["additionalProperties"] is False
    item = schema["properties"]["proposals"]["items"]
    assert set(item["properties"]) == set(table)
    assert set(item["required"]) == {key for key, required in table.items() if required}
    assert item["additionalProperties"] is False
    assert item["properties"]["type"]["enum"] == ["Risk", "Assumption", "Issue", "Dependency"]
    assert item["properties"]["severity"]["enum"] == ["High", "Medium", "Low"]
    assert item["properties"]["title"]["maxLength"] == 80
    # The schema travels with the installed package, not only the source tree.
    pyproject = tomllib.loads((REPO / "pyproject.toml").read_text(encoding="utf-8"))
    assert pyproject["tool"]["setuptools"]["package-data"]["raid"] == ["schemas/*.json"]
    # Offline: nothing in the schema points outside the file (NFR-004).
    assert "$ref" not in text and "http" not in text.replace("https://json-schema.org/", "")


def imports_of(path):
    tree = ast.parse(path.read_text(encoding="utf-8"))
    names = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            names.update(alias.name for alias in node.names)
        elif isinstance(node, ast.ImportFrom) and node.module:
            names.add(node.module)
    return names


def test_proposal_rules_are_separate_from_the_log_check():
    """REQ-005 (ADR-004): proposal validity lives in the schema and validator only; the log structure check in the store is separate."""
    validator_imports = imports_of(SRC / "validator.py")
    store_imports = imports_of(SRC / "store.py")

    assert not [name for name in validator_imports if name.startswith("raid.store")]
    assert not [name for name in store_imports if name.startswith(("raid.validator", "jsonschema"))]
    # The validator is the only module that uses jsonschema.
    users = sorted(path.name for path in SRC.glob("*.py") if "jsonschema" in imports_of(path))
    assert users == ["validator.py"]
