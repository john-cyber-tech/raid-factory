# SPEC-EPIC-5-03 — Items are never deleted

**Story:** EPIC-5-03 · **Covers:** REQ-019 · **Components:** COMP-03, COMP-05
**Build order:** 22 of 25 · **Risk tier:** LOW (Tests only; no new behaviour.) · **Depends on:** SPEC-EPIC-2-03, SPEC-EPIC-3-04

## Why

As a project manager, I want closed and merged items to stay in the log, so that the audit trail is complete.

The client's PMO checks the audit trail; nothing may disappear (NEED-12).

## Capabilities

- `tests/test_no_delete.py`: assertions over the finished CLI and store.
- No code is added. If a delete path exists anywhere, this spec removes it.

## Constraints

- The CLI has no delete command (REQ-019).
- The save guard refuses a save that drops an item or a history entry (ADR-001, ADR-006, NFR-003, NFR-007).

## Non-goals

- Archiving old items.
- Hiding Closed items from `raid list`.

## Success signal

`raid --help` lists only the commands built so far (all eight once `summary` exists), none of them delete or remove, and closed and merged items are still listed with their full history.

## Test plan

The Criteria column gives the story's acceptance criterion numbers; CF-n is an item carried forward from the stage 3 review.

| Test | Criteria | Checks |
|---|---|---|
| `test_help_has_no_delete_command` | 1 | Help lists exactly the built commands (add, review, list, show, update, close, flag; plus summary once SPEC-EPIC-4-01 is built) and nothing else. REQ-019. |
| `test_closed_and_merged_items_still_listed` | 2 | R-001 closed and R-002 merged into: both in `raid list`. REQ-019. |
| `test_history_intact_after_close_and_merge` | 3 | Every earlier entry still present. REQ-019. |
| `test_store_has_no_delete_function` | 1 | Edge: `store.py` exposes no function whose name contains delete or remove. |
| `test_unknown_command_is_refused` | 1 | Failure path: `raid delete R-001` exits non-zero and changes nothing. |

**Test data:** A log with R-001 closed and a proposal merged into R-002.

## Definition of done

- Every test in the test plan exists and passes under `pytest` on Python 3.13, with no Claude Code session and no network.
- Every test names the REQ or NFR it checks, in its name or docstring (NFR-010).
- The whole suite is still green, and the code uses nothing Python 3.12 lacks (DEC-14).
- The help test lists the commands that exist when this spec is built and is updated to all eight when `raid summary` lands in SPEC-EPIC-4-01.
- Tests are written before the code for this spec, in the same session.
- LOW tier: proceed to the next spec once the tests are green, then commit.
