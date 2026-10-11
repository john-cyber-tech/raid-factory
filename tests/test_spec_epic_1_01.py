"""SPEC-EPIC-1-01 — Review fixture proposals into the log and list them (thin slice).

Story EPIC-1-01. Covers REQ-007, REQ-008, REQ-010, REQ-011, REQ-014, NFR-010.
Every test drives the CLI through `raid.cli.main` with a fixed date, scripted
answers and a temporary project folder. No Claude Code session, no network.
"""
import inspect
import io
import json
import re
import os
import shutil
import subprocess
import sys
import tomllib
from datetime import date
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
FIXTURES = Path(__file__).resolve().parent / "fixtures" / "pending"
VALID_THREE = FIXTURES / "valid_three.json"
SAMPLE_NOTES = REPO / "inputs" / "sample-meeting-notes.md"

TODAY = date(2026, 10, 10)

P1_TITLE = "Client security review may delay cutover"
P2_TITLE = "Test environment down"
P3_TITLE = "Acme finance year-end close"

ANOTHER_RISK = {
    "type": "Risk",
    "title": "Key analyst on leave in November",
    "description": "A key analyst on Acme's side is on leave in November.",
    "owner": None,
    "severity": "Medium",
    "due_date": None,
    "source_excerpt": "Possible risk: key analyst on Acme's side is on leave in November.",
    "source_date": "2026-10-07",
}


def run(project_dir, *argv, answers=""):
    """Run one `raid` command. Returns (exit code, everything printed)."""
    from raid.cli import main

    out = io.StringIO()
    code = main(
        list(argv),
        today=TODAY,
        stdin=io.StringIO(answers),
        stdout=out,
        project_dir=project_dir,
    )
    return code, out.getvalue()


def new_project(tmp_path, name="project", fixture=VALID_THREE):
    folder = tmp_path / name
    folder.mkdir()
    if fixture is not None:
        shutil.copy(fixture, folder / "pending.json")
    return folder


def write_pending(folder, proposals):
    (folder / "pending.json").write_text(
        json.dumps({"proposals": proposals}, indent=2), encoding="utf-8"
    )


def pending_proposals(folder):
    path = folder / "pending.json"
    if not path.exists():
        return []
    return json.loads(path.read_text(encoding="utf-8"))["proposals"]


def log_path(folder):
    return folder / "raid-log.json"


def log_items(folder):
    """Items in the log, keyed by ID."""
    data = json.loads(log_path(folder).read_text(encoding="utf-8"))
    return {item["id"]: item for item in data["items"]}


def reviewed_project(tmp_path, name="project"):
    """A project after the accept, reject, accept run of criterion 1."""
    folder = new_project(tmp_path, name)
    code, _ = run(folder, "review", answers="a\nr\na\n")
    assert code == 0
    return folder


def test_review_accept_reject_accept(tmp_path):
    """REQ-007, REQ-008: only accepted proposals reach the log (criterion 1)."""
    folder = new_project(tmp_path)

    code, _ = run(folder, "review", answers="a\nr\na\n")

    assert code == 0
    items = log_items(folder)
    assert sorted(items) == ["D-001", "R-001"]
    assert items["R-001"]["title"] == P1_TITLE
    assert items["R-001"]["type"] == "Risk"
    assert items["R-001"]["status"] == "Open"
    assert items["D-001"]["title"] == P3_TITLE
    assert items["D-001"]["type"] == "Dependency"
    assert items["D-001"]["status"] == "Open"
    assert not any(item_id.startswith("I-") for item_id in items)


def test_review_shows_excerpt_and_waits(tmp_path):
    """REQ-007: each excerpt is shown, and an unknown answer is not a decision (criterion 2)."""
    folder = new_project(tmp_path)
    excerpts = [p["source_excerpt"] for p in pending_proposals(folder)]

    # `x` is not an answer: P1 must be asked again, so the next three answers
    # still land on P1, P2, P3 in that order.
    code, output = run(folder, "review", answers="x\na\nr\na\n")

    assert code == 0
    for excerpt in excerpts:
        assert excerpt in output
    assert sorted(log_items(folder)) == ["D-001", "R-001"]
    assert pending_proposals(folder) == []


def test_pending_emptied_and_rejection_not_recorded(tmp_path):
    """REQ-007, DEC-10: decided proposals leave pending.json; a rejection is written nowhere (criterion 3)."""
    folder = reviewed_project(tmp_path)

    assert pending_proposals(folder) == []
    for path in folder.rglob("*"):
        if path.is_file():
            assert P2_TITLE not in path.read_text(encoding="utf-8"), path.name


def test_list_shows_seven_columns(tmp_path):
    """REQ-014: one row per item with ID, type, title, owner, severity, due date, status (criterion 4)."""
    folder = reviewed_project(tmp_path)

    code, output = run(folder, "list")

    assert code == 0
    lines = output.splitlines()
    rows = [line for line in lines if re.match(r"\s*[RAID]-\d{3}\b", line)]
    assert len(rows) == 2

    header = next(line.lower() for line in lines if "title" in line.lower())
    for column in ("id", "type", "title", "owner", "severity", "due", "status"):
        assert column in header

    risk_row = next(row for row in rows if "R-001" in row)
    for value in ("Risk", P1_TITLE, "High", "Open"):
        assert value in risk_row
    dependency_row = next(row for row in rows if "D-001" in row)
    for value in ("Dependency", P3_TITLE, "Medium", "2026-10-25", "Open"):
        assert value in dependency_row
    assert P2_TITLE not in output


def test_ids_are_sequential_per_type(tmp_path):
    """REQ-011: a second accepted Risk is R-002 and R-001 is unchanged (criterion 5)."""
    folder = reviewed_project(tmp_path)
    r_001_before = log_items(folder)["R-001"]
    write_pending(folder, [ANOTHER_RISK])

    code, _ = run(folder, "review", answers="a\n")

    assert code == 0
    items = log_items(folder)
    assert sorted(items) == ["D-001", "R-001", "R-002"]
    assert items["R-002"]["title"] == ANOTHER_RISK["title"]
    assert items["R-001"] == r_001_before


def test_projects_are_independent(tmp_path):
    """REQ-010: accepting in folder A leaves folder B's log byte-identical (criterion 6)."""
    folder_b = reviewed_project(tmp_path, "b")
    b_before = log_path(folder_b).read_bytes()
    folder_a = new_project(tmp_path, "a")

    code, _ = run(folder_a, "review", answers="a\na\na\n")

    assert code == 0
    assert sorted(log_items(folder_a)) == ["D-001", "I-001", "R-001"]
    assert log_path(folder_b).read_bytes() == b_before


def test_no_pending_file(tmp_path):
    """REQ-007: with no pending.json there is nothing to review and the log is unchanged (criterion 7)."""
    folder = reviewed_project(tmp_path)
    (folder / "pending.json").unlink(missing_ok=True)
    before = log_path(folder).read_bytes()

    code, output = run(folder, "review")

    assert code == 0
    assert "nothing to review" in output.lower()
    assert log_path(folder).read_bytes() == before


def test_empty_proposals_list(tmp_path):
    """REQ-007: a pending.json with zero proposals behaves the same as no file (criterion 7, edge)."""
    folder = reviewed_project(tmp_path)
    write_pending(folder, [])
    before = log_path(folder).read_bytes()

    code, output = run(folder, "review")

    assert code == 0
    assert "nothing to review" in output.lower()
    assert log_path(folder).read_bytes() == before


def test_input_ends_mid_review(tmp_path):
    """REQ-007, REQ-008: input ends after one answer; that decision is kept, the rest stay pending, exit 1 (criterion 2, failure path)."""
    folder = new_project(tmp_path)

    code, _ = run(folder, "review", answers="a\n")

    assert code == 1
    assert sorted(log_items(folder)) == ["R-001"]
    assert [p["title"] for p in pending_proposals(folder)] == [P2_TITLE, P3_TITLE]


def run_entry_point(project_dir, *argv, answers=""):
    """Run the `raid` console command's own target, as the installed script would."""
    pyproject = tomllib.loads((REPO / "pyproject.toml").read_text(encoding="utf-8"))
    module, _, function = pyproject["project"]["scripts"]["raid"].partition(":")
    script = f"import sys; from {module} import {function}; sys.exit({function}())"
    env = dict(os.environ, PYTHONPATH=str(REPO / "src"))
    return subprocess.run(
        [sys.executable, "-c", script, *argv],
        cwd=project_dir,
        input=answers,
        capture_output=True,
        text=True,
        env=env,
    )


def test_real_entry_point_exit_codes(tmp_path):
    """REQ-007, REQ-010: the real entry point uses the current folder and exits non-zero on failure (SA-7)."""
    folder = new_project(tmp_path)

    failed = run_entry_point(folder, "review", answers="a\n")

    assert failed.returncode != 0
    assert sorted(log_items(folder)) == ["R-001"]

    finished = run_entry_point(folder, "review", answers="r\na\n")

    assert finished.returncode == 0
    assert sorted(log_items(folder)) == ["D-001", "R-001"]
    assert run_entry_point(folder, "list").returncode == 0


def test_suite_runs_from_fixtures():
    """NFR-010: tests run from fixture files only, and every test in this file cites a requirement (criterion 8)."""
    assert VALID_THREE.is_file()

    module = sys.modules[__name__]
    tests = [
        (name, obj)
        for name, obj in inspect.getmembers(module, inspect.isfunction)
        if name.startswith("test_")
    ]
    assert len(tests) == 12
    for name, obj in tests:
        assert re.search(r"\b(REQ|NFR)-\d{3}\b", obj.__doc__ or ""), name


def test_thin_slice_fixture_has_source_dates():
    """REQ-012 (CF-5): every proposal in valid_three.json carries a source date and a verbatim excerpt."""
    proposals = json.loads(VALID_THREE.read_text(encoding="utf-8"))["proposals"]
    notes = SAMPLE_NOTES.read_text(encoding="utf-8")

    assert [p["title"] for p in proposals] == [P1_TITLE, P2_TITLE, P3_TITLE]
    for proposal in proposals:
        assert proposal["source_date"] == "2026-10-07"
        assert proposal["source_excerpt"] in notes
