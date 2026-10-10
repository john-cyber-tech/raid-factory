# SPEC-EPIC-5-01 — Log writes are atomic and never lose accepted items

**Story:** EPIC-5-01 · **Covers:** NFR-002, NFR-003 · **Components:** COMP-05, COMP-04
**Build order:** 2 of 25 · **Risk tier:** HIGH (The save routine: file writes and atomicity.) · **Depends on:** SPEC-EPIC-1-01

## Why

As a delivery manager, I want the log to survive a crash in the middle of a save, so that I never lose items I have already accepted.

The log must survive a crash in the middle of a save and never lose an accepted item (NFR-002, NFR-003).

## Capabilities

- `src/raid/store.py`: one `_save()` used by every write: serialise, write to a temporary file in the same folder, flush and sync it to disk, then replace `raid-log.json` in one step.
- Save guard, run before the replace: every item ID in the file on disk must be in the new content; otherwise the save is refused with an error and nothing is replaced.
- `load()` on a file that is not valid JSON, or not a valid log, raises an error naming the problem; the CLI prints it and exits 1. No command writes after a failed load.
- `pending.json` is rewritten by the same temporary-file-then-replace technique.
- A leftover temporary file from an earlier crash is ignored on load and overwritten by the next save.

## Constraints

- Write-temporary-then-replace is the only way the log is written (ADR-001, NFR-002).
- No existing item ID may disappear in a save (NFR-003, REQ-019).
- Each accept is saved before the next proposal is shown (A-6, NFR-003).
- Supported and tested on macOS only (DEC-16).

## Non-goals

- Guarding history entries (SPEC-EPIC-5-02 extends the guard).
- Locking or detecting a second writer (limitation L-2).
- Backups of the log.

## Success signal

A test that makes the save fail at each of its steps always finds the log equal to the complete before state or the complete after state, and never loses an ID.

## Test plan

The Criteria column gives the story's acceptance criterion numbers; CF-n is an item carried forward from the stage 3 review.

| Test | Criteria | Checks |
|---|---|---|
| `test_failure_before_replace_keeps_old_log` | 1 | Fail after the temporary file is written: log parses and holds exactly R-001 and R-002. NFR-002. |
| `test_failure_at_each_step_is_all_or_nothing` | 2 | Parametrised over write, sync and replace: log equals before or after. NFR-002. |
| `test_interrupted_review_keeps_accepted` | 3 | Accept the first of three, end input: R-001 is in the log and two proposals remain pending. NFR-003. |
| `test_no_id_lost_across_command_sequences` | 4 | Run sequences of all commands built so far; the set of IDs never shrinks. NFR-003. |
| `test_save_guard_refuses_dropped_item` | 4 | Failure path: a save whose content lacks an existing ID is refused and the file is unchanged. |
| `test_damaged_log_is_never_overwritten` | CF-1 | Log file containing `{not json`: `raid review` and `raid list` exit 1 with a message naming the file; the file is byte-identical afterwards. |
| `test_leftover_temp_file_is_harmless` | 2 | Edge: a stray temporary file exists; load ignores it and the next save succeeds. |

**Test data:** Logs built in a temporary folder by the test; failure injection by replacing the write, sync and replace calls with ones that raise.

## Definition of done

- Every test in the test plan exists and passes under `pytest` on Python 3.13, with no Claude Code session and no network.
- Every test names the REQ or NFR it checks, in its name or docstring (NFR-010).
- The whole suite is still green, and the code uses nothing Python 3.12 lacks (DEC-14).
- The simple save from SPEC-EPIC-1-01 is gone; `grep` finds one place in `src/` that opens the log for writing.
- HIGH tier, gate 1: write this spec's tests and test data first, and show them to the owner for approval before writing any implementation code. For manual checks, show the fixtures and the written check steps. The tests must fail for the right reason before the code exists.
- HIGH tier, gate 2: stop for the owner's approval of the implementation before committing.
