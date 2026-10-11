"""Stage 6 threat review findings F-01, F-02, F-04 and F-05 (docs/threat-review.md).

F-01 (TH-02, NFR-005, stage 5 choice T-24): nothing from a file reaches the terminal raw.
F-02 (TH-03, NFR-003, CF-1): a log item with a missing field is a damaged log.
F-04, F-05 (TH-05, NFR-006): the data files are private to the user and kept out of git.
Logs are built by a review in a temporary folder and then edited by hand.
"""
import io
import json
import stat

import pytest

from helpers import REPO, log_path, new_project, reviewed_project, run

ESCAPE = "\u001b"
RIGHT_TO_LEFT_OVERRIDE = "\u202e"
ISOLATE = "\u2066"
RAW = (ESCAPE, RIGHT_TO_LEFT_OVERRIDE, ISOLATE, "\u0007", "\u009b", "\u2028")
ITEM_FIELDS = ("type", "title", "description", "owner", "severity", "due_date", "status")


def edit_log(folder, change):
    """Edit raid-log.json by hand: `change` gets the first item."""
    data = json.loads(log_path(folder).read_text(encoding="utf-8"))
    change(data["items"][0])
    log_path(folder).write_text(json.dumps(data), encoding="utf-8")


def mode(path):
    return stat.S_IMODE(path.stat().st_mode)


@pytest.mark.parametrize("field", ["title", "owner", "severity", "due_date", "status", "type"])
@pytest.mark.parametrize("raw", RAW + ("\n", "\t", "\r"))
def test_list_masks_control_and_direction_characters(tmp_path, field, raw):
    """F-01, NFR-005: `raid list` shows `?` for a control or text-direction character in a hand-edited log."""
    folder = reviewed_project(tmp_path)
    edit_log(folder, lambda item: item.update({field: f"be{raw}fore"}))

    code, output = run(folder, "list")

    assert code == 0
    assert raw not in output.replace("\n", "") or raw == "\n"
    assert "be?fore" in output
    # One line for the header and one per item: a line break in a field adds none.
    assert len(output.splitlines()) == 3


@pytest.mark.parametrize("field", ["type", "title", "owner", "severity", "due_date", "source_date"])
@pytest.mark.parametrize("raw", RAW + ("\n", "\t"))
def test_review_screen_masks_one_line_fields(field, raw):
    """F-01, NFR-005: the review screen shows `?` for such a character in a one-line field,
    even if a proposal reached it unchecked."""
    from raid.review import _show

    out = io.StringIO()
    proposal = {"type": "Risk", "title": "T", "description": "D", "owner": "O", "severity": "High",
                "due_date": None, "source_excerpt": "E", "source_date": "2026-10-07"}
    proposal[field] = f"be{raw}fore"

    _show(proposal, 1, 1, out)

    assert "be?fore" in out.getvalue()
    assert f"be{raw}fore" not in out.getvalue()


@pytest.mark.parametrize("field", ["description", "source_excerpt"])
def test_review_screen_masks_long_text_but_keeps_line_breaks(field):
    """F-01, NFR-005: in a description or excerpt a line break and a tab are shown, anything else is `?`."""
    from raid.review import _show

    out = io.StringIO()
    proposal = {"type": "Risk", "title": "T", "description": "D", "owner": None, "severity": "High",
                "due_date": None, "source_excerpt": "E", "source_date": "2026-10-07"}
    proposal[field] = "one\ntwo\tthree" + "".join(f" x{raw}y" for raw in RAW)

    _show(proposal, 1, 1, out)

    shown = out.getvalue()
    assert "one\ntwo\tthree" in shown
    assert shown.count("x?y") == len(RAW)
    assert not any(raw in shown for raw in RAW)


def test_damaged_log_message_masks_the_item_id(tmp_path):
    """F-01, NFR-005: an ID quoted in the damaged-log message is masked too."""
    folder = reviewed_project(tmp_path)

    def damage(item):
        item["id"] = f"R-{ESCAPE}[31m{RIGHT_TO_LEFT_OVERRIDE}"
        item["history"] = []

    edit_log(folder, damage)

    code, output = run(folder, "list")

    assert code == 1
    assert "R-?[31m? has no history" in output
    assert ESCAPE not in output and RIGHT_TO_LEFT_OVERRIDE not in output


@pytest.mark.parametrize("field", ITEM_FIELDS)
def test_log_item_with_a_missing_field_is_a_damaged_log(tmp_path, field):
    """F-02, NFR-003 (CF-1): list and review give the damaged-log message, exit 1, and write nothing."""
    folder = reviewed_project(tmp_path)
    edit_log(folder, lambda item: item.pop(field))
    before = log_path(folder).read_bytes()

    for argv, answers in ((("list",), ""), (("review",), "a\n")):
        code, output = run(folder, *argv, answers=answers)

        assert code == 1
        assert "raid-log.json is not a valid log" in output
        assert f"R-001 has no {field}" in output
        assert "The file was not changed." in output
        assert log_path(folder).read_bytes() == before


@pytest.mark.parametrize("field, value", [
    ("title", 5), ("title", None), ("title", ["a"]), ("type", {}), ("status", 1),
    ("description", None), ("severity", True), ("owner", 7), ("due_date", 20261010),
])
def test_log_item_with_a_field_that_is_not_text_is_a_damaged_log(tmp_path, field, value):
    """F-02, NFR-003: a field holding something other than text is refused the same way.
    Only owner and due date may be empty (null)."""
    folder = reviewed_project(tmp_path)
    edit_log(folder, lambda item: item.update({field: value}))
    before = log_path(folder).read_bytes()

    code, output = run(folder, "list")

    assert code == 1
    assert "raid-log.json is not a valid log" in output
    assert f"R-001 has no {field}" in output
    assert log_path(folder).read_bytes() == before


def test_empty_owner_and_due_date_are_still_a_valid_log(tmp_path):
    """F-02: null owner and due date are how the tool stores "none"; the log still loads."""
    folder = reviewed_project(tmp_path)
    edit_log(folder, lambda item: item.update({"owner": None, "due_date": None}))

    code, output = run(folder, "list")

    assert code == 0
    assert "R-001" in output


def test_data_files_are_created_private(tmp_path):
    """F-04, NFR-006: the log, the name file and the trimmed pending.json are readable by their owner only."""
    folder = new_project(tmp_path, user=None)

    code, _ = run(folder, "review", answers="a\nSean Murphy\nr\nr\n")

    assert code == 0
    for name in ("raid-log.json", "raid-config.json", "pending.json"):
        assert mode(folder / name) == 0o600, name
    assert sorted(path.name for path in folder.iterdir()) == [
        "pending.json", "raid-config.json", "raid-log.json"
    ]


def test_wider_file_and_leftover_temp_become_private_on_next_save(tmp_path):
    """F-04, NFR-006: a log made readable by others, or a leftover temporary file that is, ends up private after a save."""
    folder = new_project(tmp_path)
    assert run(folder, "review", answers="a\n")[0] == 1  # input ends; one item saved
    log_path(folder).chmod(0o644)
    leftover = folder / "raid-log.json.tmp"
    leftover.write_text("{half", encoding="utf-8")
    leftover.chmod(0o644)

    assert run(folder, "review", answers="a\n")[0] == 1

    assert mode(log_path(folder)) == 0o600
    assert not leftover.exists()


def test_gitignore_keeps_the_data_files_out_of_this_repo():
    """F-05, NFR-006: the three data files are ignored when the tool is run in this repo's folder."""
    lines = [line.strip().lstrip("/") for line in (REPO / ".gitignore").read_text(encoding="utf-8").splitlines()]

    for name in ("raid-log.json", "pending.json", "raid-config.json"):
        assert name in lines, name
