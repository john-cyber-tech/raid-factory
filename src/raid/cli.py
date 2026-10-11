"""CLI (COMP-03): parses commands, prints results, sets exit codes."""
import argparse
import sys
from datetime import datetime, time
from pathlib import Path

from raid.identity import NameRequired
from raid.review import review
from raid.store import LogError, LogStore

LIST_COLUMNS = (
    ("ID", "id"),
    ("Type", "type"),
    ("Title", "title"),
    ("Owner", "owner"),
    ("Severity", "severity"),
    ("Due date", "due_date"),
    ("Status", "status"),
)


def main(argv, *, today, stdin, stdout, project_dir, now=None):
    """Run one command. Returns 0 on success, 1 on a refused or failed action.

    `today` is the date the rules use; `now` is the date and time written to
    history. Without `now` the time is midnight of `today`. Both must be the same day.
    """
    if now is None:
        now = datetime.combine(today, time.min)
    elif now.date() != today:
        raise ValueError(f"now ({now.isoformat()}) is not on today's date ({today.isoformat()})")

    parser = argparse.ArgumentParser(prog="raid", description="RAID Log Manager")
    commands = parser.add_subparsers(dest="command", required=True)
    commands.add_parser("review", help="decide each proposal in pending.json")
    commands.add_parser("list", help="list the items in this folder's log")
    args = parser.parse_args(argv)

    try:
        store = LogStore.load(project_dir)
        if args.command == "review":
            return review(project_dir, store, stdin=stdin, stdout=stdout, now=now)
        return _list(store, stdout)
    except (LogError, NameRequired) as error:
        print(error, file=stdout)
        return 1


def _list(store, stdout):
    rows = [[item[key] or "-" for _, key in LIST_COLUMNS] for item in store.all()]
    header = [label for label, _ in LIST_COLUMNS]
    widths = [max(len(row[i]) for row in [header, *rows]) for i in range(len(header))]
    for row in [header, *rows]:
        print("  ".join(cell.ljust(width) for cell, width in zip(row, widths)).rstrip(),
              file=stdout)
    return 0


def entry():
    """Console command `raid`: the system clock, read once, and the current folder (REQ-010)."""
    now = datetime.now()
    return main(
        sys.argv[1:],
        today=now.date(),
        now=now,
        stdin=sys.stdin,
        stdout=sys.stdout,
        project_dir=Path.cwd(),
    )
