"""Identity (COMP-09): the user's name, asked once per project and not verified (ADR-005)."""
import json
from pathlib import Path

from raid.atomic import write_atomic

CONFIG_NAME = "raid-config.json"
QUESTION = "Your name: "


class NameRequired(Exception):
    """No name was given, so the command that needed one must stop."""


def current_user(project_dir, *, stdin, stdout):
    """Return the stored name; if there is none, ask once and save the answer (REQ-035)."""
    path = Path(project_dir) / CONFIG_NAME
    name = _stored_name(path)
    if name:
        return name

    stdout.write(QUESTION)
    stdout.flush()
    name = stdin.readline().strip()
    if not name:
        raise NameRequired("\nA name is needed to record who makes a change. The change was not made.")
    write_atomic(path, json.dumps({"name": name}, indent=2, ensure_ascii=False) + "\n")
    return name


def _stored_name(path):
    """The name in the config file, or None when the file holds no name."""
    try:
        name = json.loads(path.read_text(encoding="utf-8"))["name"]
    except (OSError, ValueError, KeyError, TypeError):
        return None
    return name.strip() if isinstance(name, str) else None
