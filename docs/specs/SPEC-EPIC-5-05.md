# SPEC-EPIC-5-05 — Ask for my name once and remember it

**Story:** EPIC-5-05 · **Covers:** REQ-035 · **Components:** COMP-09, COMP-03
**Build order:** 4 of 25 · **Risk tier:** MEDIUM (Writes a new file, `raid-config.json`.) · **Depends on:** SPEC-EPIC-1-01

## Why

As a delivery manager, I want to give my name once, so that every change I make is recorded under it without a login.

The audit trail must say who made each change without a login (NEED-12, DEC-02).

## Capabilities

- `src/raid/identity.py`: `current_user()` reads `raid-config.json` in the project folder; if it holds no name, ask "Your name:" once on the terminal and save the answer.
- Called only by commands that change the log (`review` on the first accept or merge, `add`, `update`, `close`). `list`, `show`, `flag` and `summary` never ask.
- An empty answer stops the command with a message and exit code 1, before anything is written.

## Constraints

- The name lives in `raid-config.json` in the project folder, so it is asked once per project (ADR-005, NFR-006).
- The name is not verified (ADR-005, limitation L-3).
- `raid-config.json` is written by temporary-file-then-replace like the other files (ADR-001).

## Non-goals

- Changing the name later (edit the file by hand).
- A per-user file in the home directory (rejected in ADR-005).

## Success signal

The first accepting command in a new folder asks for a name once; the next one does not ask.

## Test plan

The Criteria column gives the story's acceptance criterion numbers; CF-n is an item carried forward from the stage 3 review.

| Test | Criteria | Checks |
|---|---|---|
| `test_asked_once_and_saved` | 1 | No config: accepting a proposal asks once; `raid-config.json` holds "Sean Murphy". REQ-035. |
| `test_not_asked_again` | 2 | With a stored name, a second changing command reads no name input. REQ-035. |
| `test_read_only_commands_never_ask` | 3 | `raid list` with no config asks nothing and creates no config file. REQ-035. |
| `test_empty_name_stops_command` | 4 | Empty answer: exit 1, message, log and `pending.json` unchanged. REQ-035. |
| `test_whitespace_name_is_empty` | 4 | Edge: a name of spaces is treated as empty. |
| `test_review_with_only_rejects_never_asks` | 3 | Edge: rejecting every proposal changes nothing in the log, so no name is asked. |

**Test data:** Name "Sean Murphy" (fictional, from the interviews).

## Definition of done

- Every test in the test plan exists and passes under `pytest` on Python 3.13, with no Claude Code session and no network.
- Every test names the REQ or NFR it checks, in its name or docstring (NFR-010).
- The whole suite is still green, and the code uses nothing Python 3.12 lacks (DEC-14).
- Tests are written before the code for this spec, in the same session.
- MEDIUM tier: show the owner the diff before committing.
