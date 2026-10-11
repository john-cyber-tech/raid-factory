"""SPEC-EPIC-5-02 — Every change to an item is recorded in an append-only history.

Story EPIC-5-02. Covers REQ-020, NFR-007. Timestamps are fixed by passing the
clock in; the name "Sean Murphy" is fictional. `raid update` does not exist yet
(SPEC-EPIC-2-02), so changes are made through the log store's `update_item`.
"""
import io
import json
import sys
from datetime import date, datetime

import pytest

from helpers import (
    ANOTHER_RISK,
    TODAY,
    USER,
    fail_at,
    log_items,
    log_path,
    new_project,
    pending_proposals,
    run,
    write_pending,
)

NOW = datetime(2026, 10, 10, 9, 30, 0)
LATER = datetime(2026, 10, 14, 16, 5, 0)
NOW_TEXT = "2026-10-10T09:30:00"
LATER_TEXT = "2026-10-14T16:05:00"


def run_at(folder, *argv, answers="", now=NOW):
    """Run one `raid` command with the clock fixed at `now`."""
    from raid.cli import main

    out = io.StringIO()
    code = main(
        list(argv),
        today=now.date(),
        now=now,
        stdin=io.StringIO(answers),
        stdout=out,
        project_dir=folder,
    )
    return code, out.getvalue()


def store_for(folder):
    from raid.store import LogStore

    return LogStore.load(folder)


def update(folder, item_id, changes, now=LATER, user=USER):
    """One change made the way a later `raid update` will make it: load, update, save."""
    store_for(folder).update_item(item_id, changes, user=user, now=now)


def history(folder, item_id="R-001"):
    return log_items(folder)[item_id]["history"]


def project_with_r_001(tmp_path, name="project"):
    """A log holding R-001 (owner empty, severity High), accepted at NOW by Sean Murphy."""
    folder = new_project(tmp_path, name)
    code, _ = run_at(folder, "review", answers="a\nr\nr\n")
    assert code == 0
    return folder


def test_creation_entry_has_time_and_name(tmp_path):
    """REQ-020: an accepted item has one history entry recording its creation, with a timestamp and the name (criterion 1)."""
    folder = project_with_r_001(tmp_path)

    assert history(folder) == [{"kind": "created", "timestamp": NOW_TEXT, "user": USER}]

    # The name typed at the first accept is the one recorded.
    asked = new_project(tmp_path, "asked", user=None)
    code, _ = run_at(asked, "review", answers="a\nPriya Nair\nr\nr\n")
    assert code == 0
    assert history(asked) == [{"kind": "created", "timestamp": NOW_TEXT, "user": "Priya Nair"}]


def test_update_entry_records_old_and_new(tmp_path):
    """REQ-020: changing the owner adds a second entry with the field, old value, new value, timestamp and name (criterion 2)."""
    folder = project_with_r_001(tmp_path)
    created = history(folder)[0]

    update(folder, "R-001", {"owner": "Priya Nair"})

    entries = history(folder)
    assert len(entries) == 2
    assert entries[0] == created
    second = entries[1]
    assert second["kind"] == "updated"
    assert second["field"] == "owner"
    assert not second["old"]  # the owner was empty
    assert second["new"] == "Priya Nair"
    assert second["timestamp"] == LATER_TEXT
    assert second["user"] == USER
    assert log_items(folder)["R-001"]["owner"] == "Priya Nair"

    # Several fields in one change: one entry per field.
    update(folder, "R-001", {"severity": "Low", "due_date": "2026-11-01"})

    entries = history(folder)
    assert len(entries) == 4
    assert {(e["field"], e["old"], e["new"]) for e in entries[2:]} == {
        ("severity", "High", "Low"),
        ("due_date", None, "2026-11-01"),
    }
    # Fields changed in one update share one timestamp and one name.
    assert [(e["kind"], e["timestamp"], e["user"]) for e in entries[2:]] == [
        ("updated", LATER_TEXT, USER),
        ("updated", LATER_TEXT, USER),
    ]


def test_existing_entries_never_change(tmp_path):
    """NFR-007: after each command built so far, R-001's earlier entries are byte-identical (criterion 3)."""
    folder = project_with_r_001(tmp_path)
    update(folder, "R-001", {"owner": "Priya Nair"})
    before = json.dumps(history(folder), sort_keys=True)

    def unchanged():
        now = json.dumps(history(folder)[:2], sort_keys=True)
        return now == before

    assert run_at(folder, "list")[0] == 0
    assert unchanged()
    write_pending(folder, [ANOTHER_RISK, dict(ANOTHER_RISK, title="Rejected risk")])
    assert run_at(folder, "review", answers="a\nr\n", now=LATER)[0] == 0
    assert unchanged()
    assert run_at(folder, "review", now=LATER)[0] == 0  # nothing to review
    assert unchanged()
    write_pending(folder, [ANOTHER_RISK])
    assert run_at(folder, "review", answers="", now=LATER)[0] == 1  # input ends
    assert unchanged()
    update(folder, "R-002", {"owner": "Tom Brennan"})  # a change to another item
    assert unchanged()
    update(folder, "R-001", {"severity": "Medium"})  # a later change to R-001 itself
    assert unchanged()
    assert len(history(folder)) == 3


@pytest.mark.parametrize(
    "item_id, changes",
    [
        ("R-001", {"severity": "Critical"}),
        ("R-001", {"owner": "Priya Nair", "severity": "Critical"}),
        ("R-001", {"type": "Issue"}),
        ("R-001", {"id": "R-009"}),
        ("R-001", {"history": []}),
        ("R-001", {"colour": "red"}),
        ("R-999", {"owner": "Priya Nair"}),
    ],
    ids=["bad value", "one bad of two", "type", "id", "history", "unknown field", "unknown item"],
)
def test_refused_update_adds_no_entry(tmp_path, item_id, changes):
    """REQ-020: a refused update changes nothing and adds no history entry (criterion 4)."""
    folder = project_with_r_001(tmp_path)
    before = log_path(folder).read_bytes()
    store = store_for(folder)

    with pytest.raises(Exception):
        store.update_item(item_id, changes, user=USER, now=LATER)

    assert log_path(folder).read_bytes() == before
    assert len(history(folder)) == 1

    # Nothing was left half-applied in memory either: the same store's next
    # valid change adds exactly its own entry.
    store.update_item("R-001", {"description": "Checked with Tom."}, user=USER, now=LATER)
    entries = history(folder)
    assert [e["kind"] for e in entries] == ["created", "updated"]
    assert entries[1]["field"] == "description"
    item = log_items(folder)["R-001"]
    assert item["owner"] is None and item["severity"] == "High" and item["type"] == "Risk"


def test_save_guard_refuses_altered_history(tmp_path):
    """NFR-007: a save in which an existing history entry is different or missing is refused; the file is unchanged (criterion 3, failure path)."""
    folder = project_with_r_001(tmp_path)

    # An entry that differs: this copy does not know of the owner change on disk,
    # so its second entry for R-001 would replace the one already written.
    stale = store_for(folder)
    update(folder, "R-001", {"owner": "Priya Nair"})
    before = log_path(folder).read_bytes()
    with pytest.raises(Exception) as refused:
        stale.update_item("R-001", {"severity": "Low"}, user=USER, now=LATER)
    assert "R-001" in str(refused.value) and "history" in str(refused.value).lower()
    assert log_path(folder).read_bytes() == before

    # Entries that are missing: this copy holds one entry for R-001, the disk three.
    stale = store_for(project_with_r_001(tmp_path, "second"))
    second = tmp_path / "second"
    update(second, "R-001", {"owner": "Priya Nair"})
    update(second, "R-001", {"severity": "Low"})
    before = log_path(second).read_bytes()
    with pytest.raises(Exception) as refused:
        stale.add_item(
            type="Issue",
            title="Test environment down",
            description="",
            owner=None,
            severity="High",
            due_date=None,
            source_excerpt="The test environment has been down since Monday.",
            source_date="2026-10-07",
            user=USER,
            now=LATER,
        )
    assert "R-001" in str(refused.value) and "history" in str(refused.value).lower()
    assert log_path(second).read_bytes() == before
    assert len(history(second)) == 3


def test_no_op_update_adds_no_entry(tmp_path):
    """REQ-020: setting a field to the value it already has adds no entry (criterion 4, edge; SA-8)."""
    folder = project_with_r_001(tmp_path)
    update(folder, "R-001", {"owner": "Priya Nair"})
    before = log_path(folder).read_bytes()

    update(folder, "R-001", {"owner": "Priya Nair"})
    update(folder, "R-001", {"severity": "High"})

    # A no-op adds no entry and writes nothing at all.
    assert len(history(folder)) == 2
    assert log_path(folder).read_bytes() == before

    # A change that is partly a no-op records only the field that changed.
    update(folder, "R-001", {"owner": "Priya Nair", "severity": "Low"})
    entries = history(folder)
    assert len(entries) == 3
    assert entries[2]["field"] == "severity"


def test_created_and_last_changed_come_from_history(tmp_path):
    """REQ-020: created_on and last_changed_on are read from the first and last entries; no separate dates are stored (criterion 2)."""
    from raid.store import created_on, last_changed_on

    folder = project_with_r_001(tmp_path)
    item = log_items(folder)["R-001"]
    assert created_on(item) == date(2026, 10, 10)
    assert last_changed_on(item) == date(2026, 10, 10)

    update(folder, "R-001", {"owner": "Priya Nair"}, now=LATER)

    item = log_items(folder)["R-001"]
    assert created_on(item) == date(2026, 10, 10)
    assert last_changed_on(item) == date(2026, 10, 14)
    assert not [key for key in item if "created" in key or "changed" in key]


@pytest.mark.parametrize("step", ["write", "sync", "replace"])
def test_change_and_its_history_are_one_write(tmp_path, monkeypatch, step):
    """NFR-007, NFR-002: a failed save never leaves a change without its entry or an entry without its change (ADR-006)."""
    folder = project_with_r_001(tmp_path)
    before = log_path(folder).read_bytes()

    # An update that fails: neither the new owner nor its entry is on disk.
    fired = fail_at(monkeypatch, step)
    with pytest.raises(Exception):
        update(folder, "R-001", {"owner": "Priya Nair"})
    monkeypatch.undo()
    assert fired == [step]
    assert log_path(folder).read_bytes() == before

    # An accept that fails: neither the item nor its creation entry is on disk.
    write_pending(folder, [ANOTHER_RISK])
    fired = fail_at(monkeypatch, step)
    try:
        code, _ = run_at(folder, "review", answers="a\n", now=LATER)
    except OSError:
        code = 1
    monkeypatch.undo()
    assert fired == [step] and code == 1
    assert log_path(folder).read_bytes() == before
    assert [p["title"] for p in pending_proposals(folder)] == [ANOTHER_RISK["title"]]

    # After the failure the same change goes through, and item and entry arrive together.
    update(folder, "R-001", {"owner": "Priya Nair"})
    item = log_items(folder)["R-001"]
    assert item["owner"] == "Priya Nair"
    assert [e["kind"] for e in item["history"]] == ["created", "updated"]


def test_item_saved_before_pending_is_trimmed_has_its_history(tmp_path, monkeypatch):
    """NFR-007, NFR-003: if the log is saved and trimming pending.json then fails, the new item is complete with its creation entry."""
    folder = project_with_r_001(tmp_path)
    write_pending(folder, [ANOTHER_RISK])

    fired = fail_at(monkeypatch, "pending")
    try:
        code, _ = run_at(folder, "review", answers="a\n", now=LATER)
    except OSError:
        code = 1
    monkeypatch.undo()

    assert fired == ["pending"] and code == 1
    assert history(folder, "R-002") == [{"kind": "created", "timestamp": LATER_TEXT, "user": USER}]
    assert len(history(folder, "R-001")) == 1
    assert [p["title"] for p in pending_proposals(folder)] == [ANOTHER_RISK["title"]]


def test_item_without_history_is_a_damaged_log(tmp_path):
    """NFR-007: a log holding an item with no history is refused on load and never overwritten."""
    folder = project_with_r_001(tmp_path)
    data = json.loads(log_path(folder).read_text(encoding="utf-8"))
    del data["items"][0]["history"]
    log_path(folder).write_text(json.dumps(data, indent=2), encoding="utf-8")
    before = log_path(folder).read_bytes()

    code, output = run_at(folder, "list")

    assert code == 1
    assert "raid-log.json" in output and "R-001" in output and "history" in output.lower()
    assert log_path(folder).read_bytes() == before


def test_crash_between_name_save_and_log_save(tmp_path, monkeypatch):
    """REQ-035, NFR-003: the name is saved, then the log save fails; the name is kept, nothing else is, and the retry records it."""
    folder = new_project(tmp_path, user=None)
    pending_before = (folder / "pending.json").read_bytes()

    fired = fail_at(monkeypatch, "log")
    try:
        code, _ = run_at(folder, "review", answers=f"a\n{USER}\n")
    except OSError:
        code = 1
    monkeypatch.undo()

    assert fired == ["log"] and code == 1
    assert json.loads((folder / "raid-config.json").read_text(encoding="utf-8"))["name"] == USER
    assert not log_path(folder).exists()
    assert (folder / "pending.json").read_bytes() == pending_before

    # The retry is not asked for the name again and records it on the item.
    code, output = run_at(folder, "review", answers="a\nr\nr\n", now=LATER)

    assert code == 0
    assert "Your name:" not in output
    assert history(folder) == [{"kind": "created", "timestamp": LATER_TEXT, "user": USER}]


def test_now_is_optional_and_must_match_today(tmp_path):
    """NFR-010: the clock is passed in; with no `now` the time is midnight of `today`, and a `now` on another day is refused."""
    from raid.cli import main

    # helpers.run passes `today` only.
    folder = new_project(tmp_path)
    assert run(folder, "review", answers="a\nr\nr\n")[0] == 0
    assert history(folder)[0]["timestamp"] == "2026-10-10T00:00:00"

    other = new_project(tmp_path, "other")
    pending_before = (other / "pending.json").read_bytes()
    with pytest.raises(ValueError):
        main(
            ["review"],
            today=TODAY,
            now=datetime(2026, 10, 11, 0, 5, 0),
            stdin=io.StringIO("a\na\na\n"),
            stdout=io.StringIO(),
            project_dir=other,
        )
    assert not log_path(other).exists()
    assert (other / "pending.json").read_bytes() == pending_before


def test_entry_point_reads_the_clock_once(tmp_path, monkeypatch, capsys):
    """NFR-010: the real entry point takes today's date and the time from a single clock read."""
    import raid.cli

    reads = []

    class OneClock(datetime):
        @classmethod
        def now(cls, tz=None):
            reads.append(tz)
            return datetime(2026, 10, 14, 23, 59, 59)

    class NoSecondClock(date):
        @classmethod
        def today(cls):
            raise AssertionError("the date must come from the same clock read as the time")

    folder = new_project(tmp_path)
    monkeypatch.setattr(raid.cli, "datetime", OneClock)
    monkeypatch.setattr(raid.cli, "date", NoSecondClock, raising=False)
    monkeypatch.setattr(sys, "argv", ["raid", "review"])
    monkeypatch.setattr(sys, "stdin", io.StringIO("a\nr\nr\n"))
    monkeypatch.chdir(folder)

    assert raid.cli.entry() == 0

    assert reads == [None]
    assert history(folder) == [{"kind": "created", "timestamp": "2026-10-14T23:59:59", "user": USER}]
    assert "R-001" in capsys.readouterr().out
