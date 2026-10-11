"""Shared test helpers: fixed date, fixture paths and a runner for the CLI."""
import io
import json
import shutil
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
