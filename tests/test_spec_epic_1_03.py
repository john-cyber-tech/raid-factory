"""SPEC-EPIC-1-03 — Edit a proposal before accepting it.

Story EPIC-1-03. Covers REQ-009, REQ-041 (and REQ-008, DEC-18). During review
the answer `e` asks which field and the new value, then returns to the same
proposal's question. Nothing reaches the log until accept.
"""
import json
from datetime import datetime

import pytest

from helpers import (
    FIXTURES,
    P2_TITLE,
    REPO,
    USER,
    log_items,
    log_path,
    new_project,
    pending_proposals,
    run,
)

RISK_NO_OWNER = FIXTURES / "risk_no_owner.json"
SCHEMA = REPO / "src" / "raid" / "schemas" / "pending.schema.json"
EXCERPT = json.loads(RISK_NO_OWNER.read_text(encoding="utf-8"))["proposals"][0]["source_excerpt"]


def project(tmp_path, name="project"):
    """One pending proposal: "Test environment down", typed Risk, owner empty, severity High."""
    return new_project(tmp_path, name, fixture=RISK_NO_OWNER)


def edit(field, value):
    return f"e\n{field}\n{value}\n"


def test_edit_type_and_owner_then_accept(tmp_path):
    """REQ-009: editing type to Issue and owner to Priya Nair, then accepting, creates I-001 with that owner (criterion 1)."""
    folder = project(tmp_path)

    code, output = run(folder, "review", answers=edit("type", "Issue") + edit("owner", "Priya Nair") + "a\n")

    assert code == 0
    items = log_items(folder)
    assert list(items) == ["I-001"]  # the prefix comes from the type at the moment of acceptance
    item = items["I-001"]
    assert item["type"] == "Issue" and item["owner"] == "Priya Nair" and item["title"] == P2_TITLE
    assert item["sources"][0]["excerpt"] == EXCERPT
    # Edits made before acceptance are not history: the item starts with its creation only.
    assert [entry["kind"] for entry in item["history"]] == ["created"]
    assert pending_proposals(folder) == []
    # After each edit the proposal is shown again with the new value, before the decision.
    assert "Type:        Issue" in output
    assert "Owner:       Priya Nair" in output
    assert output.index("Owner:       Priya Nair") < output.index("Accepted as I-001")


def test_edit_to_bad_type_refused(tmp_path):
    """REQ-009: editing the type to Question is refused with the four allowed values; the proposal is still awaiting a decision (criterion 2)."""
    folder = project(tmp_path)
    pending_before = (folder / "pending.json").read_bytes()

    code, output = run(folder, "review", answers=edit("type", "Question"))  # then the input ends

    assert code == 1
    for allowed in ("Risk", "Assumption", "Issue", "Dependency"):
        assert allowed in output.split("New value:")[-1]
    assert not log_path(folder).exists()
    assert (folder / "pending.json").read_bytes() == pending_before

    # The previous value is kept: accepting now gives a Risk.
    code, _ = run(folder, "review", answers=edit("type", "Question") + "a\n")
    assert code == 0
    assert list(log_items(folder)) == ["R-001"]


def test_edit_title_81_refused(tmp_path):
    """REQ-041: editing the title to 81 characters is refused stating the 80-character limit; the proposal keeps its title (criterion 3)."""
    folder = project(tmp_path)

    code, output = run(folder, "review", answers=edit("title", "x" * 81) + "a\n")

    assert code == 0
    refusal = output.split("New value:")[1]
    assert "80" in refusal and "81" in refusal
    assert log_items(folder)["R-001"]["title"] == P2_TITLE

    # Exactly 80 is accepted.
    second = project(tmp_path, "second")
    assert run(second, "review", answers=edit("title", "y" * 80) + "a\n")[0] == 0
    assert log_items(second)["R-001"]["title"] == "y" * 80


def test_edit_then_reject_adds_nothing(tmp_path):
    """REQ-008: a proposal that was edited and then rejected adds nothing to the log (criterion 4)."""
    folder = new_project(tmp_path, fixture=RISK_NO_OWNER, user=None)

    code, output = run(folder, "review", answers=edit("type", "Issue") + edit("owner", "Priya Nair") + "r\n")

    assert code == 0
    assert "Your name:" not in output
    assert not log_path(folder).exists()
    assert pending_proposals(folder) == []
    for path in folder.iterdir():
        assert "Priya Nair" not in path.read_text(encoding="utf-8")


def test_excerpt_cannot_be_edited(tmp_path):
    """REQ-009, REQ-012: choosing source_excerpt as the field to edit is refused; it is what was said (criterion 2, failure path)."""
    folder = project(tmp_path)

    # No new value is asked for, so the next answer is the decision.
    code, output = run(folder, "review", answers="e\nsource_excerpt\na\n")

    assert code == 0
    assert "source_excerpt" in output.split("Field to edit")[1]
    assert "New value:" not in output
    assert log_items(folder)["R-001"]["sources"][0]["excerpt"] == EXCERPT


def test_source_date_cannot_be_edited(tmp_path):
    """REQ-012, REQ-040: source_date is the date of the notes and cannot be changed by an edit (G-13)."""
    folder = project(tmp_path)

    # No new value is asked for, so the next answer is the decision.
    code, output = run(folder, "review", answers="e\nsource_date\na\n")

    assert code == 0
    assert "source_date" in output.split("Field to edit")[1].split(": ", 1)[1]
    assert "New value:" not in output
    assert "source_date" not in output.split("Field to edit (")[1].split(")")[0]  # not offered
    assert log_items(folder)["R-001"]["sources"][0]["date"] == "2026-10-07"


def test_only_owner_and_due_date_can_be_cleared(tmp_path):
    """REQ-009: an empty answer clears owner and due date; it never clears a field that must have a value (G-13)."""
    folder = new_project(tmp_path)  # P1, P2 (owner Priya), P3 (due 2026-10-25)

    answers = "r\n" + edit("owner", "") + "a\n" + edit("due_date", "") + "a\n"
    code, _ = run(folder, "review", answers=answers)

    assert code == 0
    items = log_items(folder)
    assert items["I-001"]["owner"] is None
    assert items["D-001"]["due_date"] is None


def test_edit_severity_to_bad_value_refused(tmp_path):
    """REQ-009 (DEC-18): editing severity to Critical is refused listing High, Medium, Low (criterion 2, edge)."""
    folder = project(tmp_path)

    code, output = run(folder, "review", answers=edit("severity", "Critical") + edit("severity", "Low") + "a\n")

    assert code == 0
    refusal = output.split("New value:")[1]
    for allowed in ("High", "Medium", "Low"):
        assert allowed in refusal
    assert log_items(folder)["R-001"]["severity"] == "Low"


def test_unknown_field_refused(tmp_path):
    """REQ-009: a field name that does not exist is refused, naming the fields that can be edited."""
    folder = project(tmp_path)

    code, output = run(folder, "review", answers="e\ncolour\na\n")

    assert code == 0
    listed = output.split("Field to edit")[-1]
    for field in ("type", "title", "description", "owner", "severity", "due_date"):
        assert field in listed
    assert "New value:" not in output
    assert list(log_items(folder)) == ["R-001"]


REFUSED_EDITS = {
    "empty title": ("title", ""),
    "escape in title": ("title", "Test environment\x1b[2J down"),
    "bidi control in owner": ("owner", "Priya\u202e Nair"),
    "impossible date": ("due_date", "2026-02-30"),
    "date without a year": ("due_date", "25 Oct"),
    "compact date": ("due_date", "20261025"),
    "lower-case type": ("type", "issue"),
    "lower-case severity": ("severity", "high"),
    # An empty answer does not clear a field that must have a value.
    "empty severity": ("severity", ""),
    "empty type": ("type", ""),
    "spaces only as title": ("title", "   "),
}


@pytest.mark.parametrize("field, value", REFUSED_EDITS.values(), ids=REFUSED_EDITS.keys())
def test_edit_that_breaks_a_rule_is_refused(tmp_path, field, value):
    """REQ-009, REQ-041: an edit that breaks a contract rule is refused and the proposal keeps its previous value (ADR-004)."""
    folder = project(tmp_path)
    before = pending_proposals(folder)[0]

    code, output = run(folder, "review", answers=edit(field, value) + "a\n")

    assert code == 0
    assert field in output.split("New value:")[1]  # the refusal names the field
    assert "\x1b" not in output and "\u202e" not in output
    item = log_items(folder)["R-001"]
    assert item["title"] == before["title"] and item["owner"] is None
    assert item["due_date"] is None and item["severity"] == "High"
    assert item["type"] == "Risk"


ALLOWED_EDITS = {
    "title": ("title", "Test environment still down", "title", "Test environment still down"),
    "description": ("description", "Down since Monday; infra chasing.", "description", "Down since Monday; infra chasing."),
    "severity": ("severity", "Medium", "severity", "Medium"),
    "due date": ("due_date", "2026-10-16", "due_date", "2026-10-16"),
    "accented owner": ("owner", "Zoë Ångström", "owner", "Zoë Ångström"),
}


@pytest.mark.parametrize("field, value, key, stored", ALLOWED_EDITS.values(), ids=ALLOWED_EDITS.keys())
def test_edit_of_each_field_is_stored_on_accept(tmp_path, field, value, key, stored):
    """REQ-009: any proposal field except the excerpt can be changed during review, and the accepted item carries the change."""
    folder = project(tmp_path)

    code, _ = run(folder, "review", answers=edit(field, value) + "a\n")

    assert code == 0
    assert log_items(folder)["R-001"][key] == stored


def test_input_ends_during_an_edit(tmp_path):
    """REQ-008: if the input ends part-way through an edit, nothing is written and the proposal is still pending unchanged."""
    for name, answers in (("at field", "e\n"), ("at value", "e\ntitle\n"), ("after an edit", edit("owner", "Priya Nair"))):
        folder = project(tmp_path, name)
        pending_before = (folder / "pending.json").read_bytes()

        code, _ = run(folder, "review", answers=answers)

        assert code == 1, name
        assert not log_path(folder).exists(), name
        # An edit is held only until the decision: pending.json is not rewritten.
        assert (folder / "pending.json").read_bytes() == pending_before, name


def test_rules_match_the_contract():
    """REQ-009 (ADR-004): the field rules used for edits are the contract's own values, so the two cannot drift apart."""
    from raid import rules

    properties = json.loads(SCHEMA.read_text(encoding="utf-8"))["properties"]["proposals"]["items"]["properties"]

    assert list(rules.TYPES) == properties["type"]["enum"]
    assert list(rules.SEVERITIES) == properties["severity"]["enum"]
    assert rules.TITLE_LIMIT == properties["title"]["maxLength"]
    assert rules.FORBIDDEN_IN_ONE_LINE.pattern == properties["title"]["not"]["pattern"]
    assert rules.FORBIDDEN_IN_ONE_LINE.pattern == properties["owner"]["not"]["pattern"]
    assert rules.FORBIDDEN_IN_LONG_TEXT.pattern == properties["description"]["not"]["pattern"]
    assert rules.FORBIDDEN_IN_LONG_TEXT.pattern == properties["source_excerpt"]["not"]["pattern"]
    assert "^" + rules.DATE_FORMAT.pattern + "$" == properties["due_date"]["pattern"]


@pytest.mark.parametrize(
    "changes",
    [{"title": "x" * 81}, {"title": ""}, {"title": "Two\nlines"}, {"due_date": "2026-02-30"},
     {"due_date": "25 Oct"}, {"owner": "Priya\u202e Nair"}, {"severity": "Critical"}],
    ids=["title 81", "empty title", "title on two lines", "impossible date", "date without year", "bidi in owner", "severity"],
)
def test_store_updates_use_the_same_rules(tmp_path, changes):
    """REQ-041, REQ-009: the log store applies the same field rules to a later change as review applies to an edit (N-14)."""
    from raid.store import LogStore

    folder = project(tmp_path)
    assert run(folder, "review", answers="a\n")[0] == 0
    before = log_path(folder).read_bytes()

    with pytest.raises(Exception):
        LogStore.load(folder).update_item("R-001", changes, user=USER, now=datetime(2026, 10, 14, 16, 5))

    assert log_path(folder).read_bytes() == before
