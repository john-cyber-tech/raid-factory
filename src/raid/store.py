"""Log store (COMP-05): the only code that writes raid-log.json (ADR-001)."""
import copy
import json
import re
from datetime import datetime
from pathlib import Path

from raid.atomic import write_atomic
from raid.rules import RuleError, check

LOG_NAME = "raid-log.json"
SCHEMA_VERSION = 1
PREFIXES = {"Risk": "R", "Assumption": "A", "Issue": "I", "Dependency": "D"}
TYPES = {prefix: item_type for item_type, prefix in PREFIXES.items()}
ID_PATTERN = re.compile(r"([RAID])-(\d+)")
UPDATABLE = ("title", "description", "owner", "severity", "due_date")


class LogError(Exception):
    """The log cannot be read, or a save was refused. Nothing was written."""


def _read(path):
    """Parse and check the log file. Raises LogError naming the problem."""
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (ValueError, OSError) as error:
        raise LogError(
            f"{LOG_NAME} cannot be read as JSON ({error}). The file was not changed."
        ) from error
    problem = _problem(data)
    if problem:
        raise LogError(f"{LOG_NAME} is not a valid log: {problem}. The file was not changed.")
    return data


def _problem(data):
    if not isinstance(data, dict):
        return "the file is not a JSON object"
    if data.get("schema_version") != SCHEMA_VERSION:
        return f"schema_version is not {SCHEMA_VERSION}"
    counters = data.get("next_number")
    if not isinstance(counters, dict):
        return "next_number is missing"
    for item_type in PREFIXES:
        number = counters.get(item_type)
        if type(number) is not int or number < 1:
            return f"next_number has no valid counter for {item_type}"
    items = data.get("items")
    if not isinstance(items, list):
        return "items is not a list"
    for position, item in enumerate(items, start=1):
        if not isinstance(item, dict) or not isinstance(item.get("id"), str):
            return f"item {position} has no id"
        if not isinstance(item.get("history"), list) or not item["history"]:
            return f"{item['id']} has no history"
    # A counter at or below an existing ID would give that ID out a second time (REQ-011).
    for item in items:
        match = ID_PATTERN.fullmatch(item["id"])
        if match:
            item_type = TYPES[match.group(1)]
            if counters[item_type] <= int(match.group(2)):
                return (
                    f"the next {item_type} number is {counters[item_type]} "
                    f"but {item['id']} already exists"
                )
    return None


class LogStore:
    """One project's log. The project folder is given by the caller (REQ-010)."""

    def __init__(self, project_dir, data):
        self._path = Path(project_dir) / LOG_NAME
        self._data = data

    @classmethod
    def load(cls, project_dir):
        path = Path(project_dir) / LOG_NAME
        if path.exists():
            data = _read(path)
        else:
            data = {
                "schema_version": SCHEMA_VERSION,
                "next_number": {item_type: 1 for item_type in PREFIXES},
                "items": [],
            }
        return cls(project_dir, data)

    def all(self):
        return list(self._data["items"])

    def add_item(self, *, type, title, description, owner, severity, due_date,
                 source_excerpt, source_date, user, now):
        """Add an Open item with the next ID for its type and its creation entry, in one save."""
        data = copy.deepcopy(self._data)
        number = data["next_number"][type]
        item = {
            "id": f"{PREFIXES[type]}-{number:03d}",
            "type": type,
            "title": title,
            "description": description,
            "owner": owner,
            "severity": severity,
            "due_date": due_date,
            "status": "Open",
            "sources": [{"excerpt": source_excerpt, "date": source_date}],
            "history": [_entry("created", user, now)],
        }
        data["next_number"][type] = number + 1
        data["items"].append(item)
        self._save(data)
        return item

    def update_item(self, item_id, changes, *, user, now):
        """Change fields of one item, adding one history entry per changed field (REQ-020).

        Every change is checked first; if any is refused, nothing is changed.
        A field set to the value it already has adds no entry.
        """
        data = copy.deepcopy(self._data)
        item = next((item for item in data["items"] if item["id"] == item_id), None)
        if item is None:
            raise LogError(f"There is no item {item_id} in {LOG_NAME}.")
        for field, value in changes.items():
            if field not in UPDATABLE:
                raise LogError(f"{field} cannot be changed. Nothing was changed.")
            try:
                check(field, value)
            except RuleError as error:
                raise LogError(f"{error}. Nothing was changed.") from error
        changed = False
        for field, value in changes.items():
            if item[field] != value:
                item["history"].append(
                    _entry("updated", user, now, field=field, old=item[field], new=value)
                )
                item[field] = value
                changed = True
        if changed:
            self._save(data)
        return item

    def _save(self, data):
        """The one routine that writes the log: save guard, then write-temporary-then-replace."""
        if self._path.exists():
            on_disk = _read(self._path)["items"]
            new = {item["id"]: item for item in data["items"]}
            # Save guard: no item ID on disk may be missing from the new content (NFR-003).
            lost = sorted(item["id"] for item in on_disk if item["id"] not in new)
            if lost:
                raise LogError(
                    f"Save refused: it would remove {', '.join(lost)} from {LOG_NAME}. "
                    "The file was not changed."
                )
            # And no history entry on disk may be different or missing (NFR-007).
            for item in on_disk:
                kept = new[item["id"]]["history"][:len(item["history"])]
                if kept != item["history"]:
                    raise LogError(
                        f"Save refused: it would alter the history of {item['id']} in {LOG_NAME}. "
                        "The file was not changed."
                    )
        write_atomic(self._path, json.dumps(data, indent=2, ensure_ascii=False) + "\n")
        self._data = data


def _entry(kind, user, now, **details):
    return {"kind": kind, "timestamp": now.isoformat(timespec="seconds"), "user": user, **details}


def created_on(item):
    """The date of the item's first history entry."""
    return datetime.fromisoformat(item["history"][0]["timestamp"]).date()


def last_changed_on(item):
    """The date of the item's last history entry."""
    return datetime.fromisoformat(item["history"][-1]["timestamp"]).date()
