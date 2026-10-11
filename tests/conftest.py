import hashlib
import socket
import sys
from pathlib import Path

import pytest

# Tests import the package from src/ without needing an install.
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))


@pytest.fixture(autouse=True)
def block_sockets(monkeypatch):
    """Every test runs with socket creation replaced by a failure (NFR-004).

    Each attempt is recorded, and the test fails at the end if any is on record,
    so an attempt is caught even when the code under test swallows the failure.
    """
    attempts = []

    def no_sockets(*args, **kwargs):
        attempts.append((args, kwargs))
        pytest.fail("NFR-004: the code under test tried to open a network socket")

    monkeypatch.setattr(socket, "socket", no_sockets)
    yield attempts
    assert attempts == [], f"NFR-004: {len(attempts)} socket attempt(s) during this test"


class OutsideWatch:
    """A project folder inside a watched parent folder (NFR-006)."""

    def __init__(self, parent):
        self.parent = parent
        self.project = parent / "project"
        self.sentinel = parent / "sentinel.txt"
        self.project.mkdir()
        self.sentinel.write_text("must not change", encoding="utf-8")
        self._before = self._snapshot()

    def _snapshot(self):
        seen = {}
        for path in self.parent.rglob("*"):
            if path == self.project or self.project in path.parents:
                continue
            name = path.relative_to(self.parent).as_posix()
            seen[name] = hashlib.sha256(path.read_bytes()).hexdigest() if path.is_file() else "folder"
        return seen

    def changes(self):
        """What was created, changed or removed outside the project folder since the start."""
        now = self._snapshot()
        found = [f"created: {name}" for name in now if name not in self._before]
        found += [f"removed: {name}" for name in self._before if name not in now]
        found += [
            f"changed: {name}"
            for name in now
            if name in self._before and now[name] != self._before[name]
        ]
        return sorted(found)


@pytest.fixture
def outside_watch(tmp_path, monkeypatch):
    """Snapshot a parent folder around the project folder; the home folder and the
    current folder are moved inside it so a stray write to either is seen."""
    parent = tmp_path / "watched"
    home = parent / "home"
    elsewhere = parent / "elsewhere"
    home.mkdir(parents=True)
    elsewhere.mkdir()
    monkeypatch.setenv("HOME", str(home))
    monkeypatch.chdir(elsewhere)
    return OutsideWatch(parent)
