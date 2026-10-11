"""Log store (COMP-05): the only code that writes raid-log.json (ADR-001)."""
import json
from pathlib import Path

LOG_NAME = "raid-log.json"
SCHEMA_VERSION = 1
PREFIXES = {"Risk": "R", "Assumption": "A", "Issue": "I", "Dependency": "D"}


class LogStore:
    """One project's log. The project folder is given by the caller (REQ-010)."""

    def __init__(self, project_dir, data):
        self._path = Path(project_dir) / LOG_NAME
        self._data = data

    @classmethod
    def load(cls, project_dir):
        path = Path(project_dir) / LOG_NAME
        if path.exists():
            data = json.loads(path.read_text(encoding="utf-8"))
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
                 source_excerpt, source_date):
        """Add an Open item with the next ID for its type and save (REQ-011)."""
        number = self._data["next_number"][type]
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
        }
        self._data["next_number"][type] = number + 1
        self._data["items"].append(item)
        self._save()
        return item

    def _save(self):
        # Simple save for the thin slice; SPEC-EPIC-5-01 replaces it with the atomic one.
        self._path.write_text(
            json.dumps(self._data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
        )
