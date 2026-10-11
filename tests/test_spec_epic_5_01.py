"""SPEC-EPIC-5-01 — Log writes are atomic and never lose accepted items.

Story EPIC-5-01. Covers NFR-002, NFR-003. Logs are built in a temporary folder
by each test. A failed save is simulated by replacing the operating-system
write, sync and replace calls with ones that raise.
"""
import itertools
import json
import os

import pytest

from helpers import (
    ANOTHER_RISK,
    P2_TITLE,
    P3_TITLE,
    log_items,
    log_path,
    new_project,
    pending_proposals,
    run,
    write_pending,
)

TEMP_NAME = "raid-log.json.tmp"


class InjectedFailure(OSError):
    """Stands in for a crash or disk error at one step of a save."""


def risk(title):
    return dict(ANOTHER_RISK, title=title)


def project_with_two_risks(tmp_path):
    """A project whose log holds exactly R-001 and R-002."""
    folder = new_project(tmp_path, fixture=None)
    write_pending(folder, [risk("First risk"), risk("Second risk")])
    code, _ = run(folder, "review", answers="a\na\n")
    assert code == 0
    assert sorted(log_items(folder)) == ["R-001", "R-002"]
    return folder


def fail_at(monkeypatch, step):
    """Make one step of the save raise. `pending` fails only the pending.json replace.

    Returns a list that gains one entry each time the failure fires.
    """
    fired = []

    def boom(*args, **kwargs):
        fired.append(step)
        raise InjectedFailure(f"injected failure at {step}")

    if step == "write":
        monkeypatch.setattr(os, "write", boom)
    elif step == "sync":
        monkeypatch.setattr(os, "fsync", boom)
    elif step == "replace":
        monkeypatch.setattr(os, "replace", boom)
    elif step == "pending":
        real_replace = os.replace

        def replace_unless_pending(src, dst, *args, **kwargs):
            if os.fspath(dst).endswith("pending.json"):
                boom()
            return real_replace(src, dst, *args, **kwargs)

        monkeypatch.setattr(os, "replace", replace_unless_pending)
    else:
        raise ValueError(step)
    return fired


def run_expecting_failure(folder, *argv, answers=""):
    """The command must not succeed: it either exits 1 or lets the failure out."""
    try:
        code, _ = run(folder, *argv, answers=answers)
    except InjectedFailure:
        return
    assert code == 1


def test_failure_before_replace_keeps_old_log(tmp_path, monkeypatch):
    """NFR-002: a save that fails after the new content is written leaves R-001 and R-002 intact (criterion 1)."""
    folder = project_with_two_risks(tmp_path)
    write_pending(folder, [risk("Third risk")])

    fired = fail_at(monkeypatch, "replace")
    run_expecting_failure(folder, "review", answers="a\n")
    monkeypatch.undo()

    assert fired == ["replace"]

    assert sorted(log_items(folder)) == ["R-001", "R-002"]
    code, output = run(folder, "list")
    assert code == 0
    assert "R-001" in output and "R-002" in output and "R-003" not in output


@pytest.mark.parametrize("step", ["write", "sync", "replace", "pending"])
def test_failure_at_each_step_is_all_or_nothing(tmp_path, monkeypatch, step):
    """NFR-002, NFR-003: after a failure at any step the log is the complete before or the complete after state (criterion 2)."""
    folder = project_with_two_risks(tmp_path)
    write_pending(folder, [risk("Third risk")])
    before = log_path(folder).read_bytes()

    fired = fail_at(monkeypatch, step)
    run_expecting_failure(folder, "review", answers="a\n")
    monkeypatch.undo()

    assert fired == [step]

    after = log_path(folder).read_bytes()
    ids = sorted(log_items(folder))  # also proves the file parses
    if step == "pending":
        # The log was already saved; only trimming pending.json failed.
        assert ids == ["R-001", "R-002", "R-003"]
    else:
        assert after == before
        assert ids == ["R-001", "R-002"]
    # Either way the decision is not lost: the proposal is still there to decide.
    assert [p["title"] for p in pending_proposals(folder)] == ["Third risk"]


def test_interrupted_review_keeps_accepted(tmp_path):
    """NFR-003: accept the first of three, input ends; R-001 is in the log on the next run (criterion 3)."""
    folder = new_project(tmp_path)

    code, _ = run(folder, "review", answers="a\n")

    assert code == 1
    assert sorted(log_items(folder)) == ["R-001"]
    assert [p["title"] for p in pending_proposals(folder)] == [P2_TITLE, P3_TITLE]
    code, output = run(folder, "list")
    assert code == 0
    assert "R-001" in output


@pytest.mark.parametrize(
    "answers", ["".join(combo) for combo in itertools.product(["a\n", "r\n", ""], repeat=3)]
)
def test_no_id_lost_across_command_sequences(tmp_path, answers):
    """NFR-003: over sequences of every command built so far, the set of item IDs never shrinks (criterion 4)."""
    folder = project_with_two_risks(tmp_path)
    seen = set(log_items(folder))

    def step(*argv, answers=""):
        nonlocal seen
        run(folder, *argv, answers=answers)
        now = set(log_items(folder))
        assert seen <= now, f"lost {seen - now} after {argv} {answers!r}"
        seen = now

    new_project_fixture = json.loads(
        (new_project(tmp_path, "source") / "pending.json").read_text(encoding="utf-8")
    )
    write_pending(folder, new_project_fixture["proposals"])
    step("review", answers=answers)
    step("list")
    step("review", answers="x\na\n")
    step("review")
    write_pending(folder, [risk("Late risk")])
    step("review", answers="r\n")
    step("list")


def test_save_guard_refuses_dropped_item(tmp_path):
    """NFR-003: a save whose content lacks an ID that is on disk is refused and the file is unchanged (criterion 4, failure path)."""
    from raid.store import LogStore

    folder = new_project(tmp_path, fixture=None)
    stale = LogStore.load(folder)  # knows of no items
    write_pending(folder, [risk("First risk")])
    assert run(folder, "review", answers="a\n")[0] == 0
    before = log_path(folder).read_bytes()

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
        )

    assert "R-001" in str(refused.value)
    assert log_path(folder).read_bytes() == before
    assert sorted(log_items(folder)) == ["R-001"]


@pytest.mark.parametrize(
    "damaged",
    ["", "{not json", "[]", '{"schema_version": 1}', '{"schema_version": 1, "next_number": {}, "items": "none"}'],
)
def test_damaged_log_is_never_overwritten(tmp_path, damaged):
    """NFR-003 (CF-1): with a damaged log, review and list exit 1 naming the file, and nothing is written."""
    folder = new_project(tmp_path)
    log_path(folder).write_text(damaged, encoding="utf-8")
    log_before = log_path(folder).read_bytes()
    pending_before = (folder / "pending.json").read_bytes()

    for argv, answers in ((("review",), "a\na\na\n"), (("list",), "")):
        code, output = run(folder, *argv, answers=answers)

        assert code == 1
        assert "raid-log.json" in output
        assert log_path(folder).read_bytes() == log_before
        assert (folder / "pending.json").read_bytes() == pending_before
    assert sorted(path.name for path in folder.iterdir()) == [
        "pending.json", "raid-config.json", "raid-log.json"
    ]


def test_leftover_temp_file_is_harmless(tmp_path):
    """NFR-002: a stray temporary file from an earlier crash is ignored on load and replaced by the next save (criterion 2, edge)."""
    folder = project_with_two_risks(tmp_path)
    (folder / TEMP_NAME).write_text('{"items": [half-writ', encoding="utf-8")

    code, output = run(folder, "list")
    assert code == 0
    assert "R-001" in output and "R-002" in output

    write_pending(folder, [risk("Third risk")])
    code, _ = run(folder, "review", answers="a\n")

    assert code == 0
    assert sorted(log_items(folder)) == ["R-001", "R-002", "R-003"]
    assert not (folder / TEMP_NAME).exists()
