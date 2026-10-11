"""SPEC-EPIC-5-04 — The tool stays local: no network, no API key.

Story EPIC-5-04. Covers NFR-004, NFR-006. These are suite-wide safety nets;
they add no product behaviour. Later specs add their commands to COMMANDS.
"""
import os
import re
import socket
import tomllib
import unicodedata

import pytest

from helpers import REPO, VALID_THREE, log_items, run

SRC = REPO / "src"

# Every command built so far, with the answers it needs, in an order that works
# on a fresh project holding the three-proposal fixture and no stored name:
# the first accept is asked for the name, so raid-config.json is written too.
COMMANDS = [
    (("review",), "a\nSean Murphy\nr\na\n"),
    (("list",), ""),
]

KEY_VARIABLE = re.compile(r".*_API_KEY$|^ANTHROPIC_.*")


def test_suite_runs_with_sockets_blocked(request, block_sockets):
    """NFR-004: the socket block is active for every test, and a socket attempt fails the test (criterion 1)."""
    unprotected = [
        item.nodeid for item in request.session.items if "block_sockets" not in item.fixturenames
    ]
    assert unprotected == []

    # Canary: opening a socket must fail the test that tries it.
    with pytest.raises(pytest.fail.Exception, match="NFR-004"):
        socket.socket()
    with pytest.raises(pytest.fail.Exception, match="NFR-004"):
        socket.create_connection(("127.0.0.1", 9))

    # Both attempts were recorded. They are this test's own, so clear them:
    # any attempt still on record when a test ends fails that test.
    assert len(block_sockets) == 2
    block_sockets.clear()


def test_no_network_imports_in_src():
    """NFR-004: no file under src/ imports a network module, a model client or subprocess, or starts a shell command (criterion 2)."""
    from boundary_check import forbidden_imports

    files = sorted(SRC.rglob("*.py"))
    assert files, "no source files found to check"
    found = [problem for path in files for problem in forbidden_imports(path)]
    assert found == []


@pytest.mark.parametrize(
    "line, module",
    [
        ("import urllib.request", "urllib"),
        ("from urllib import request", "urllib"),
        ("import socket", "socket"),
        ("from http import client", "http"),
        ("import http.client as web", "http"),
        ("import requests", "requests"),
        ("import httpx", "httpx"),
        ("import subprocess", "subprocess"),
        ("import anthropic", "anthropic"),
        ("from anthropic.types import Message", "anthropic"),
        ("def late():\n    import urllib.request", "urllib"),
        ("import asyncio", "asyncio"),
        ("import ssl", "ssl"),
        ("import smtplib", "smtplib"),
        ("import ftplib", "ftplib"),
        ("import urllib3", "urllib3"),
        ("import aiohttp", "aiohttp"),
        ("import openai", "openai"),
        ("import os\nos.system('claude -p hello')", "os.system"),
        ("import os\nos.popen('claude -p hello')", "os.popen"),
        ("from os import system", "os.system"),
        ("from os import popen", "os.popen"),
    ],
)
def test_import_check_catches_a_planted_import(tmp_path, line, module):
    """NFR-004: the import check flags a sample file that imports a forbidden module or starts a shell command (criterion 2, failure path)."""
    from boundary_check import forbidden_imports

    planted = tmp_path / "planted.py"
    planted.write_text(f"import json\n{line}\n", encoding="utf-8")
    clean = tmp_path / "clean.py"
    clean.write_text("import json\nfrom pathlib import Path\n", encoding="utf-8")

    problems = forbidden_imports(planted)

    assert len(problems) == 1
    assert module in problems[0] and "planted.py" in problems[0]
    assert forbidden_imports(clean) == []


def test_no_writes_outside_project_folder(outside_watch):
    """NFR-006: raid review and raid list create or change nothing outside the project folder (criterion 3)."""
    folder = outside_watch.project
    (folder / "pending.json").write_bytes(VALID_THREE.read_bytes())

    for argv, answers in COMMANDS:
        code, _ = run(folder, *argv, answers=answers)
        assert code == 0
        assert outside_watch.changes() == [], f"after raid {' '.join(argv)}"

    # The commands did write, and only inside the project folder.
    assert sorted(log_items(folder)) == ["D-001", "R-001"]


def test_outside_watch_catches_a_planted_write(outside_watch):
    """NFR-006: the outside-write check notices a new file, a changed file and a removed file (criterion 3, failure path)."""
    assert outside_watch.changes() == []

    (outside_watch.project / "inside.txt").write_text("allowed", encoding="utf-8")
    assert outside_watch.changes() == []

    (outside_watch.parent / "stray.txt").write_text("leak", encoding="utf-8")
    outside_watch.sentinel.write_text("changed", encoding="utf-8")
    assert sorted(outside_watch.changes()) == ["changed: sentinel.txt", "created: stray.txt"]

    outside_watch.sentinel.unlink()
    assert "removed: sentinel.txt" in outside_watch.changes()


def test_commands_work_without_api_keys(tmp_path, monkeypatch):
    """NFR-004: each command built so far exits 0 with every *_API_KEY and ANTHROPIC_* variable removed (criterion 4)."""
    monkeypatch.setenv("ANTHROPIC_API_KEY", "set-only-to-prove-it-is-removed")
    monkeypatch.setenv("EXAMPLE_API_KEY", "set-only-to-prove-it-is-removed")
    for name in [name for name in os.environ if KEY_VARIABLE.match(name)]:
        monkeypatch.delenv(name)
    assert not [name for name in os.environ if KEY_VARIABLE.match(name)]

    folder = tmp_path / "project"
    folder.mkdir()
    (folder / "pending.json").write_bytes(VALID_THREE.read_bytes())

    for argv, answers in COMMANDS:
        code, output = run(folder, *argv, answers=answers)
        assert code == 0, f"raid {' '.join(argv)}"
        assert "key" not in output.lower()


def test_only_declared_dependency_is_jsonschema():
    """NFR-004 (DEC-12): pyproject.toml lists exactly one runtime dependency, a pinned jsonschema (criterion 2, edge)."""
    project = tomllib.loads((REPO / "pyproject.toml").read_text(encoding="utf-8"))["project"]

    assert len(project["dependencies"]) == 1
    assert re.fullmatch(r"jsonschema==[\d.]+", project["dependencies"][0])


def test_no_invisible_characters_in_source():
    """NFR-005: no file under src/, tests/ (fixtures included) or docs/ holds a literal control, line-separator or text-direction character; they are written as escapes."""
    assert (REPO / "tests" / "fixtures" / "pending" / "control_char.json").is_file()
    assert (REPO / "docs" / "task-dag.md").is_file()
    found = []
    for folder in (SRC, REPO / "tests", REPO / "docs"):
        for path in sorted(folder.rglob("*")):
            if path.suffix not in (".py", ".json", ".toml", ".md"):
                continue
            for number, line in enumerate(path.read_text(encoding="utf-8").split("\n"), start=1):
                bad = sorted({
                    f"U+{ord(ch):04X}" for ch in line
                    if ch != "\t" and unicodedata.category(ch) in ("Cc", "Cf", "Zl", "Zp")
                })
                if bad:
                    found.append(f"{path.relative_to(REPO)}:{number}: {', '.join(bad)}")
    assert found == []
