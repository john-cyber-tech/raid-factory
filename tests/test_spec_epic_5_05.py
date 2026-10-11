"""SPEC-EPIC-5-05 — Ask for my name once and remember it.

Story EPIC-5-05. Covers REQ-035. The name "Sean Murphy" is fictional.
"""
import json

import pytest

from helpers import (
    ANOTHER_RISK,
    P1_TITLE,
    P2_TITLE,
    USER,
    log_items,
    log_path,
    new_project,
    pending_proposals,
    run,
    store_name,
    write_pending,
)

NAME_QUESTION = "Your name:"


def config_path(folder):
    return folder / "raid-config.json"


def project_with_log_but_no_name(tmp_path):
    """A log holding R-001 and D-001, with the stored name then taken away."""
    folder = new_project(tmp_path)
    assert run(folder, "review", answers="a\nr\na\n")[0] == 0
    config_path(folder).unlink()
    return folder


def test_asked_once_and_saved(tmp_path):
    """REQ-035: with no stored name, the first accept asks once and the name is saved (criterion 1)."""
    folder = new_project(tmp_path, user=None)

    code, output = run(folder, "review", answers=f"a\n{USER}\nr\na\n")

    assert code == 0
    assert output.count(NAME_QUESTION) == 1
    # Order: the first proposal is shown and accepted, then the name is asked,
    # and only then is the second proposal shown.
    assert output.index(P1_TITLE) < output.index(NAME_QUESTION) < output.index(P2_TITLE)
    assert json.loads(config_path(folder).read_text(encoding="utf-8"))["name"] == USER
    assert sorted(log_items(folder)) == ["D-001", "R-001"]
    # Written by temporary-file-then-replace: nothing is left behind (ADR-001).
    assert sorted(path.name for path in folder.iterdir()) == [
        "pending.json", "raid-config.json", "raid-log.json"
    ]


def test_not_asked_again(tmp_path):
    """REQ-035: with a stored name, a second changing command reads no name input (criterion 2)."""
    folder = new_project(tmp_path, user=None)
    assert run(folder, "review", answers=f"a\n{USER}\nr\na\n")[0] == 0
    config_before = config_path(folder).read_bytes()
    write_pending(folder, [ANOTHER_RISK])

    # Only the accept is supplied: a name question would find no input and fail.
    code, output = run(folder, "review", answers="a\n")

    assert code == 0
    assert NAME_QUESTION not in output
    assert sorted(log_items(folder)) == ["D-001", "R-001", "R-002"]
    assert config_path(folder).read_bytes() == config_before


def test_read_only_commands_never_ask(tmp_path):
    """REQ-035: raid list with no stored name asks nothing and creates no config file (criterion 3)."""
    empty = new_project(tmp_path, "empty", fixture=None, user=None)
    with_log = project_with_log_but_no_name(tmp_path)

    for folder in (empty, with_log):
        code, output = run(folder, "list")

        assert code == 0
        assert NAME_QUESTION not in output
        assert not config_path(folder).exists()


@pytest.mark.parametrize("answers", ["a\n\n", "a\n"], ids=["empty line", "input ends"])
def test_empty_name_stops_command(tmp_path, answers):
    """REQ-035: an empty name stops the command with a message and exit 1, before anything is written (criterion 4)."""
    folder = project_with_log_but_no_name(tmp_path)
    write_pending(folder, [ANOTHER_RISK])
    log_before = log_path(folder).read_bytes()
    pending_before = (folder / "pending.json").read_bytes()

    code, output = run(folder, "review", answers=answers)

    assert code == 1
    assert output.count(NAME_QUESTION) == 1
    assert "name" in output.split(NAME_QUESTION)[-1].lower()  # a message after the question
    assert log_path(folder).read_bytes() == log_before
    assert (folder / "pending.json").read_bytes() == pending_before
    assert not config_path(folder).exists()


@pytest.mark.parametrize("blank", ["   ", "\t"], ids=["spaces", "tab"])
def test_whitespace_name_is_empty(tmp_path, blank):
    """REQ-035: a name of only spaces is treated as empty (criterion 4, edge)."""
    folder = new_project(tmp_path, user=None)
    pending_before = (folder / "pending.json").read_bytes()

    code, output = run(folder, "review", answers=f"a\n{blank}\na\na\n")

    assert code == 1
    assert output.count(NAME_QUESTION) == 1
    assert not log_path(folder).exists()
    assert (folder / "pending.json").read_bytes() == pending_before
    assert not config_path(folder).exists()


def test_review_with_only_rejects_never_asks(tmp_path):
    """REQ-035: rejecting every proposal changes nothing in the log, so no name is asked (criterion 3, edge)."""
    folder = new_project(tmp_path, user=None)

    code, output = run(folder, "review", answers="r\nr\nr\n")

    assert code == 0
    assert NAME_QUESTION not in output
    assert pending_proposals(folder) == []
    assert not log_path(folder).exists()
    assert not config_path(folder).exists()


def test_stored_name_is_used_without_asking(tmp_path):
    """REQ-035: a name already in raid-config.json is enough; the first accept does not ask (criterion 2, edge)."""
    folder = new_project(tmp_path, user=None)
    store_name(folder, USER)

    code, output = run(folder, "review", answers="a\nr\na\n")

    assert code == 0
    assert NAME_QUESTION not in output
    assert sorted(log_items(folder)) == ["D-001", "R-001"]
