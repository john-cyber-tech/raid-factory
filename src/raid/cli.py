"""CLI (COMP-03): parses commands, prints results, sets exit codes."""
import argparse
import sys
from datetime import date
from pathlib import Path

from raid.review import review
from raid.store import LogStore

LIST_COLUMNS = (
    ("ID", "id"),
    ("Type", "type"),
    ("Title", "title"),
    ("Owner", "owner"),
    ("Severity", "severity"),
    ("Due date", "due_date"),
    ("Status", "status"),
)


def main(argv, *, today, stdin, stdout, project_dir):
    """Run one command. Returns 0 on success, 1 on a refused or failed action."""
    parser = argparse.ArgumentParser(prog="raid", description="RAID Log Manager")
    commands = parser.add_subparsers(dest="command", required=True)
    commands.add_parser("review", help="decide each proposal in pending.json")
    commands.add_parser("list", help="list the items in this folder's log")
    args = parser.parse_args(argv)

    store = LogStore.load(project_dir)
    if args.command == "review":
        return review(project_dir, store, stdin=stdin, stdout=stdout)
    return _list(store, stdout)


def _list(store, stdout):
    rows = [[item[key] or "-" for _, key in LIST_COLUMNS] for item in store.all()]
    header = [label for label, _ in LIST_COLUMNS]
    widths = [max(len(row[i]) for row in [header, *rows]) for i in range(len(header))]
    for row in [header, *rows]:
        print("  ".join(cell.ljust(width) for cell, width in zip(row, widths)).rstrip(),
              file=stdout)
    return 0


def entry():
    """Console command `raid`: the system date and the current folder (REQ-010)."""
    return main(
        sys.argv[1:],
        today=date.today(),
        stdin=sys.stdin,
        stdout=sys.stdout,
        project_dir=Path.cwd(),
    )
