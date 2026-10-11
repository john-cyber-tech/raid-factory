"""Shared test helpers: fixed date, fixture paths and a runner for the CLI."""
import io
import json
import os
import shutil
from datetime import date
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
FIXTURES = Path(__file__).resolve().parent / "fixtures" / "pending"
VALID_THREE = FIXTURES / "valid_three.json"
SAMPLE_NOTES = REPO / "inputs" / "sample-meeting-notes.md"

TODAY = date(2026, 10, 10)

USER = "Sean Murphy"

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


def store_name(folder, user=USER):
    """Give the project a stored user name, so commands do not ask for one."""
    (folder / "raid-config.json").write_text(json.dumps({"name": user}), encoding="utf-8")


def new_project(tmp_path, name="project", fixture=VALID_THREE, user=USER):
    """A project folder. `user=None` leaves it with no stored name."""
    folder = tmp_path / name
    folder.mkdir()
    if user is not None:
        store_name(folder, user)
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


class InjectedFailure(OSError):
    """Stands in for a crash or disk error at one step of a save."""


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
