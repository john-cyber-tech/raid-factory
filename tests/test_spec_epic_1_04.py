"""SPEC-EPIC-1-04 — Keep the source excerpt and date with every item.

Story EPIC-1-04. Covers REQ-012, REQ-040. The source date is the date of the
notes, not the date of acceptance (A-8). An item cannot be accepted without one
(DEC-08): when a proposal has none, the manager is asked at accept.
"""
import io
import json
from datetime import datetime

import pytest

from helpers import (
    FIXTURES,
    TODAY,
    USER,
    VALID_THREE,
    log_items,
    log_path,
    new_project,
    pending_proposals,
    run,
    write_pending,
)

NO_SOURCE_DATE = FIXTURES / "no_source_date.json"
P1 = json.loads(VALID_THREE.read_text(encoding="utf-8"))["proposals"][0]
DATE_QUESTION = "Date of the notes (YYYY-MM-DD):"
DECISION_QUESTION = "(a/e/r)"
NOW = datetime(2026, 10, 14, 16, 5)


def undated(tmp_path, name="project", user=USER):
    """One pending proposal, P1, with no source date. Today is 2026-10-10."""
    return new_project(tmp_path, name, fixture=NO_SOURCE_DATE, user=user)


def first_source(folder, item_id="R-001"):
    return log_items(folder)[item_id]["sources"][0]


def test_excerpt_stored_exactly(tmp_path):
    """REQ-012: the accepted item's first source holds exactly the proposal's excerpt (criterion 1)."""
    folder = new_project(tmp_path)

    code, _ = run(folder, "review", answers="a\nr\nr\n")

    assert code == 0
    sources = log_items(folder)["R-001"]["sources"]
    assert len(sources) == 1
    assert sources[0]["excerpt"] == P1["source_excerpt"]
    assert sources[0]["excerpt"].startswith(
        "Tom said the client security review for the new cloud tenant hasn't started"
    )


def test_date_present_not_asked(tmp_path):
    """REQ-040: a proposal that carries 2026-10-07 is not asked for a date, and that date is stored (criterion 2)."""
    folder = new_project(tmp_path)

    code, output = run(folder, "review", answers="a\nr\nr\n")

    assert code == 0
    assert DATE_QUESTION not in output
    assert first_source(folder)["date"] == "2026-10-07"


@pytest.mark.parametrize("how", ["null", "absent"])
def test_date_missing_is_asked(tmp_path, how):
    """REQ-040: a proposal with no source date asks for one at accept, and the answer is stored (criterion 3)."""
    folder = undated(tmp_path)
    if how == "absent":
        proposal = dict(P1)
        del proposal["source_date"]
        write_pending(folder, [proposal])

    code, output = run(folder, "review", answers="a\n2026-10-07\n")

    assert code == 0
    assert output.count(DATE_QUESTION) == 1
    assert first_source(folder)["date"] == "2026-10-07"
    assert first_source(folder)["excerpt"] == P1["source_excerpt"]
    assert pending_proposals(folder) == []


def test_empty_date_cancels_accept(tmp_path):
    """REQ-040: an empty answer to the date question cancels the accept; the proposal is still awaiting a decision and the log is byte-identical (criterion 4)."""
    # With an existing log, so "byte-identical" is checked against real content.
    folder = new_project(tmp_path)
    assert run(folder, "review", answers="r\na\nr\n")[0] == 0  # log holds I-001
    write_pending(folder, json.loads(NO_SOURCE_DATE.read_text(encoding="utf-8"))["proposals"])
    log_before = log_path(folder).read_bytes()
    pending_before = (folder / "pending.json").read_bytes()

    code, output = run(folder, "review", answers="a\n\n")  # then the input ends

    assert code == 1
    assert output.count(DATE_QUESTION) == 1
    assert output.count(DECISION_QUESTION) == 2  # back at the same proposal's question
    assert log_path(folder).read_bytes() == log_before
    assert (folder / "pending.json").read_bytes() == pending_before

    # The decision is still open: it can be rejected, or accepted with a date.
    code, _ = run(folder, "review", answers="a\n   \na\n2026-10-07\n")
    assert code == 0
    assert sorted(log_items(folder)) == ["I-001", "R-001"]
    assert first_source(folder)["date"] == "2026-10-07"


@pytest.mark.parametrize("bad", ["2026-13-40", "2026-02-30", "07/10/2026", "20261007", "7 Oct", "yesterday"])
def test_invalid_date_asked_again(tmp_path, bad):
    """REQ-040: an invalid date is refused with the expected format and the question is asked again (criterion 5)."""
    folder = undated(tmp_path)

    code, output = run(folder, "review", answers=f"a\n{bad}\n2026-10-07\n")

    assert code == 0
    assert output.count(DATE_QUESTION) == 2
    refusal = output.split(DATE_QUESTION)[1]
    assert "YYYY-MM-DD" in refusal
    assert bad not in refusal  # the rule is stated; the value is not repeated
    assert first_source(folder)["date"] == "2026-10-07"


def test_invalid_date_then_input_ends(tmp_path):
    """REQ-040: an invalid date never reaches the log; if the input then ends, the proposal is still pending (criterion 5)."""
    folder = undated(tmp_path)
    pending_before = (folder / "pending.json").read_bytes()

    code, _ = run(folder, "review", answers="a\n2026-13-40\n")

    assert code == 1
    assert not log_path(folder).exists()
    assert (folder / "pending.json").read_bytes() == pending_before


@pytest.mark.parametrize(
    "changes",
    [{"sources": []}, {"sources": [{"excerpt": "", "date": ""}]}, {"source_excerpt": ""}, {"source_date": ""},
     {"source_date": None}, {"excerpt": ""}, {"date": None}],
    ids=["sources emptied", "sources blanked", "source_excerpt", "source_date empty", "source_date null", "excerpt", "date"],
)
def test_source_cannot_be_emptied(tmp_path, changes):
    """REQ-012: the store refuses any change that would empty an item's excerpt or source date; the stored values are unchanged (criterion 6)."""
    from raid.store import LogStore

    folder = new_project(tmp_path)
    assert run(folder, "review", answers="a\nr\nr\n")[0] == 0
    before = log_path(folder).read_bytes()

    with pytest.raises(Exception):
        LogStore.load(folder).update_item("R-001", changes, user=USER, now=NOW)

    assert log_path(folder).read_bytes() == before
    assert first_source(folder) == {"excerpt": P1["source_excerpt"], "date": "2026-10-07"}


@pytest.mark.parametrize(
    "excerpt, source_date",
    [("", "2026-10-07"), ("   ", "2026-10-07"), (None, "2026-10-07"),
     ("Tom said so.", None), ("Tom said so.", ""), ("Tom said so.", "2026-13-40"), ("Tom said so.", "7 Oct")],
    ids=["empty excerpt", "blank excerpt", "no excerpt", "no date", "empty date", "impossible date", "date without year"],
)
def test_store_requires_a_source_to_add_an_item(tmp_path, excerpt, source_date):
    """REQ-012, REQ-040: the store adds no item without an excerpt and a real source date, whoever calls it (DEC-08)."""
    from raid.store import LogStore

    folder = new_project(tmp_path, fixture=None)

    with pytest.raises(Exception) as refused:
        LogStore.load(folder).add_item(
            type="Risk", title="A risk", description="", owner=None, severity="Low", due_date=None,
            source_excerpt=excerpt, source_date=source_date, user=USER, now=NOW,
        )

    assert "source" in str(refused.value).lower()
    assert not log_path(folder).exists()


def test_future_source_date_refused(tmp_path):
    """REQ-040: a notes date after today is refused and asked again; today's date is allowed (criterion 5, edge; SA-2)."""
    folder = undated(tmp_path)  # today is 2026-10-10

    code, output = run(folder, "review", answers="a\n2026-10-11\n2027-01-01\n2026-10-10\n")

    assert code == 0
    assert output.count(DATE_QUESTION) == 3
    assert "today" in output.split(DATE_QUESTION)[1]
    assert first_source(folder)["date"] == "2026-10-10"


def test_date_is_asked_before_the_name(tmp_path):
    """REQ-040, REQ-035: the date is settled first, so a cancelled accept asks for no name and writes nothing at all."""
    folder = undated(tmp_path, user=None)

    code, output = run(folder, "review", answers=f"a\n2026-10-07\n{USER}\n")

    assert code == 0
    assert output.index(DATE_QUESTION) < output.index("Your name:")
    assert first_source(folder)["date"] == "2026-10-07"
    assert log_items(folder)["R-001"]["history"][0]["user"] == USER

    cancelled = undated(tmp_path, "cancelled", user=None)
    code, output = run(cancelled, "review", answers="a\n\nr\n")

    assert code == 0
    assert "Your name:" not in output
    assert sorted(path.name for path in cancelled.iterdir()) == ["pending.json"]


def test_input_ends_at_the_date_question(tmp_path):
    """REQ-040: if the input ends at the date question nothing is accepted: exit 1, log absent, proposal still pending."""
    folder = undated(tmp_path)
    pending_before = (folder / "pending.json").read_bytes()

    code, output = run(folder, "review", answers="a\n")

    assert code == 1
    assert output.count(DATE_QUESTION) == 1
    assert not log_path(folder).exists()
    assert (folder / "pending.json").read_bytes() == pending_before


@pytest.mark.parametrize(
    "sources",
    [None, [], [{}], [{"excerpt": "", "date": "2026-10-07"}], [{"excerpt": "Tom said so.", "date": None}],
     [{"excerpt": "Tom said so.", "date": "2026-13-40"}], "Tom said so."],
    ids=["missing", "empty list", "empty source", "empty excerpt", "no date", "impossible date", "not a list"],
)
def test_item_without_a_source_is_a_damaged_log(tmp_path, sources):
    """REQ-012: a log holding an item with no excerpt or no real source date is refused on load and never overwritten."""
    folder = new_project(tmp_path)
    assert run(folder, "review", answers="a\nr\nr\n")[0] == 0
    data = json.loads(log_path(folder).read_text(encoding="utf-8"))
    if sources is None:
        del data["items"][0]["sources"]
    else:
        data["items"][0]["sources"] = sources
    log_path(folder).write_text(json.dumps(data, indent=2), encoding="utf-8")
    before = log_path(folder).read_bytes()

    code, output = run(folder, "list")

    assert code == 1
    assert "raid-log.json" in output and "R-001" in output and "source" in output.lower()
    assert log_path(folder).read_bytes() == before


class CountingInput(io.StringIO):
    """Scripted answers that count how often the tool reads after they have run out."""

    reads_after_end = 0

    def readline(self, *args):
        line = super().readline(*args)
        if line == "":
            self.reads_after_end += 1
            assert self.reads_after_end < 5, "the tool keeps asking after the input has ended"
        return line


@pytest.mark.parametrize("answers", ["a\n", "a\n2026-13-40\n", "a\n2099-01-01\n"],
                         ids=["at once", "after an invalid date", "after a future date"])
def test_end_of_input_at_the_date_question_does_not_loop(tmp_path, answers):
    """REQ-040: when the input ends at the date question the accept is cancelled at once: one read, no further question, exit 1."""
    from raid.cli import main

    folder = undated(tmp_path)
    pending_before = (folder / "pending.json").read_bytes()
    stdin, stdout = CountingInput(answers), io.StringIO()

    code = main(["review"], today=TODAY, stdin=stdin, stdout=stdout, project_dir=folder)

    output = stdout.getvalue()
    assert code == 1
    assert stdin.reads_after_end == 1
    assert output.count(DATE_QUESTION) == answers.count("\n")  # asked once per answer given, then once more
    assert output.count(DECISION_QUESTION) == 1  # not sent back to the proposal's question
    assert "Your name:" not in output
    assert not log_path(folder).exists()
    assert (folder / "pending.json").read_bytes() == pending_before


def test_source_date_is_shown_on_the_review_screen(tmp_path):
    """REQ-007, REQ-012: the review screen shows the date of the notes, so the manager sees what will be stored (G-15)."""
    folder = new_project(tmp_path)

    _, output = run(folder, "review", answers="")

    lines = output.splitlines()
    assert "  Source date: 2026-10-07" in lines
    # It sits with the excerpt, after the other fields, in the same column as they do.
    assert lines.index("  Source date: 2026-10-07") == lines.index("  Due date:    -") + 2
    assert lines[lines.index("  Due date:    -") + 1].startswith('  Source:      "Tom said')

    _, output = run(undated(tmp_path, "undated"), "review", answers="")
    assert "  Source date: -" in output.splitlines()


def created_entry(folder, item_id="R-001"):
    entries = log_items(folder)[item_id]["history"]
    assert len(entries) == 1
    return entries[0]


def edit(field, value):
    return f"e\n{field}\n{value}\n"


def test_unedited_creation_entry_is_unchanged(tmp_path):
    """REQ-020 (G-14): a proposal accepted as extracted has the plain creation entry, with no `edited` key."""
    folder = new_project(tmp_path)

    assert run(folder, "review", answers="a\nr\nr\n")[0] == 0

    assert created_entry(folder) == {"kind": "created", "timestamp": "2026-10-10T00:00:00", "user": USER}


def test_creation_entry_names_fields_edited_before_accept(tmp_path):
    """REQ-020, REQ-009 (G-14): fields changed during review are named on the creation entry; names only, never values."""
    folder = new_project(tmp_path)

    answers = edit("owner", "Priya Nair") + edit("type", "Issue") + edit("title", "Security review not started") + "a\nr\nr\n"
    assert run(folder, "review", answers=answers)[0] == 0

    entry = created_entry(folder, "I-001")
    assert entry == {
        "kind": "created",
        "timestamp": "2026-10-10T00:00:00",
        "user": USER,
        # In the order the fields are shown, not the order they were edited.
        "edited": ["type", "title", "owner"],
    }
    text = json.dumps(entry)
    assert "Priya" not in text and "Security" not in text and "Risk" not in text


EDITS_THAT_LEAVE_NOTHING_CHANGED = {
    "changed and changed back": edit("severity", "Low") + edit("severity", "High"),
    "cleared and already empty": edit("owner", ""),
    "set to the value it had": edit("type", "Risk"),
    "refused edit": edit("title", "x" * 81) + edit("severity", "Critical"),
    "set, then cleared again": edit("owner", "Priya Nair") + edit("owner", ""),
    "excerpt and source date refused": "e\nsource_excerpt\ne\nsource_date\n",
}


@pytest.mark.parametrize("edits", EDITS_THAT_LEAVE_NOTHING_CHANGED.values(), ids=EDITS_THAT_LEAVE_NOTHING_CHANGED.keys())
def test_reverted_and_refused_edits_are_not_listed(tmp_path, edits):
    """REQ-020 (G-14): only a field whose accepted value differs from the extracted one is listed; otherwise there is no `edited` key."""
    folder = new_project(tmp_path)

    assert run(folder, "review", answers=edits + "a\nr\nr\n")[0] == 0

    assert created_entry(folder) == {"kind": "created", "timestamp": "2026-10-10T00:00:00", "user": USER}


def test_only_the_changed_field_is_listed(tmp_path):
    """REQ-020 (G-14): a reverted edit beside a real one lists only the real one, and each proposal has its own list."""
    folder = new_project(tmp_path)

    answers = (
        edit("severity", "Low") + edit("severity", "High") + edit("due_date", "2026-10-28") + "a\n"  # P1
        + "a\n"                                                                                        # P2 as extracted
        + edit("owner", "Tom Brennan") + "a\n"                                                         # P3
    )
    assert run(folder, "review", answers=answers)[0] == 0

    assert created_entry(folder, "R-001")["edited"] == ["due_date"]
    assert "edited" not in created_entry(folder, "I-001")
    assert created_entry(folder, "D-001")["edited"] == ["owner"]


def test_typed_source_date_is_not_listed_as_an_edit(tmp_path):
    """REQ-040, REQ-020 (G-14): a date of the notes typed at accept is not an edit of an extracted value and is not listed."""
    folder = undated(tmp_path)

    assert run(folder, "review", answers="a\n2026-10-07\n")[0] == 0

    assert created_entry(folder) == {"kind": "created", "timestamp": "2026-10-10T00:00:00", "user": USER}
    assert first_source(folder)["date"] == "2026-10-07"


def test_typed_source_date_is_marked_on_the_source(tmp_path):
    """REQ-040, REQ-012 (G-14): a date of the notes that the manager typed is marked on the source; one the notes stated is not."""
    typed = undated(tmp_path, "typed")
    assert run(typed, "review", answers="a\n2026-10-07\n")[0] == 0
    assert first_source(typed) == {
        "excerpt": P1["source_excerpt"], "date": "2026-10-07", "date_entered": True,
    }

    # A refused answer on the way does not change the outcome.
    retried = undated(tmp_path, "retried")
    assert run(retried, "review", answers="a\n2026-13-40\n\na\n2026-10-09\n")[0] == 0
    assert first_source(retried) == {
        "excerpt": P1["source_excerpt"], "date": "2026-10-09", "date_entered": True,
    }

    stated = new_project(tmp_path, "stated")
    assert run(stated, "review", answers="a\na\na\n")[0] == 0
    for item_id in ("R-001", "I-001", "D-001"):
        assert set(first_source(stated, item_id)) == {"excerpt", "date"}


def future_dated(tmp_path, name="project", user=USER):
    """One pending proposal, P1, whose notes are dated the day after today (2026-10-10)."""
    folder = new_project(tmp_path, name, fixture=None, user=user)
    write_pending(folder, [dict(P1, source_date="2026-10-11")])
    return folder


def test_carried_future_source_date_is_refused_at_accept(tmp_path):
    """REQ-040 (G-15, SA-2): a source date in pending.json that is after today is refused at accept and the date is asked for."""
    folder = future_dated(tmp_path)

    code, output = run(folder, "review", answers="a\n2026-10-07\n")

    assert code == 0
    assert "  Source date: 2026-10-11" in output.splitlines()  # shown as it arrived
    refusal = output.split(DECISION_QUESTION)[1].split(DATE_QUESTION)[0]
    assert "2026-10-11" in refusal and "today" in refusal
    assert output.count(DATE_QUESTION) == 1
    # The date the manager typed replaces it and is marked as typed.
    assert first_source(folder) == {
        "excerpt": P1["source_excerpt"], "date": "2026-10-07", "date_entered": True,
    }


def test_carried_future_source_date_never_reaches_the_log(tmp_path):
    """REQ-040 (G-15): whatever is answered, the future date is not stored: empty cancels, another future date is asked again, end of input stops."""
    cancelled = future_dated(tmp_path, "cancelled", user=None)
    pending_before = (cancelled / "pending.json").read_bytes()
    code, output = run(cancelled, "review", answers="a\n\nr\n")
    assert code == 0
    assert output.count(DECISION_QUESTION) == 2 and "Your name:" not in output
    assert not log_path(cancelled).exists()

    ended = future_dated(tmp_path, "ended")
    pending_before = (ended / "pending.json").read_bytes()
    code, _ = run(ended, "review", answers="a\n")
    assert code == 1
    assert not log_path(ended).exists()
    assert (ended / "pending.json").read_bytes() == pending_before  # still carries what arrived

    again = future_dated(tmp_path, "again")
    code, output = run(again, "review", answers="a\n2026-10-11\n2026-10-10\n")
    assert code == 0
    assert output.count(DATE_QUESTION) == 2
    assert first_source(again)["date"] == "2026-10-10"


def test_carried_source_date_of_today_or_earlier_is_not_asked(tmp_path):
    """REQ-040 (G-15): a carried source date of today or any earlier day is accepted as it is, unmarked."""
    for day in ("2026-10-10", "2026-10-09", "2019-01-01"):
        folder = new_project(tmp_path, day, fixture=None)
        write_pending(folder, [dict(P1, source_date=day)])

        code, output = run(folder, "review", answers="a\n")

        assert code == 0, day
        assert DATE_QUESTION not in output, day
        assert first_source(folder) == {"excerpt": P1["source_excerpt"], "date": day}, day
