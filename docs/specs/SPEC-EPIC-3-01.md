# SPEC-EPIC-3-01 — Flag unowned and overdue items

**Story:** EPIC-3-01 · **Covers:** REQ-025, REQ-026 · **Components:** COMP-07, COMP-03
**Build order:** 18 of 25 · **Risk tier:** LOW (A pure function plus read-only output.) · **Depends on:** SPEC-EPIC-2-03

## Why

As a delivery manager, I want items with no owner or a missed due date pointed out, so that I can fix them before the client asks.

Clients ask "who is doing this?" and overdue items must be obvious (NEED-03, NEED-11).

## Capabilities

- `src/raid/flags.py`: `flags(items, today)` returns, per item, any of `unowned` and `overdue`. Pure function, no file access.
- Unowned: owner empty or only spaces. Overdue: due date earlier than today. Closed items get no flags.
- `cli.py`: `raid flag` prints each flagged item with its flags; if there are none, "No flags" and exit 0.

## Constraints

- Closed items are never flagged (A-4).
- Due today is not overdue (REQ-026).
- `flag` never writes (ADR-001).
- Today is passed in (NFR-010).

## Non-goals

- Stale flag (SPEC-EPIC-3-02).
- Notifications of any kind (brief, non-goals).

## Success signal

On 2026-10-10, `raid flag` flags the item due 2026-10-09 as overdue and not the one due 2026-10-10.

## Test plan

The Criteria column gives the story's acceptance criterion numbers; CF-n is an item carried forward from the stage 3 review.

| Test | Criteria | Checks |
|---|---|---|
| `test_flag_unowned` | 1 | Exactly R-002 is unowned. REQ-025. |
| `test_flag_overdue_boundary` | 2 | Due 10-09 flagged; due 10-10 and no due date not. REQ-026. |
| `test_closed_items_not_flagged` | 3 | Closed, unowned, overdue item gets nothing. A-4. |
| `test_no_flags_message` | 4 | "No flags", exit 0. |
| `test_whitespace_owner_is_unowned` | 1 | Edge: owner of spaces counts as unowned. |
| `test_flag_does_not_write` | 4 | Log byte-identical. |
| `test_flag_on_damaged_log` | 4 | Failure path: an unreadable log gives exit 1 and a message, not "No flags". |

**Test data:** Logs built by the test with today fixed at 2026-10-10.

## Definition of done

- Every test in the test plan exists and passes under `pytest` on Python 3.13, with no Claude Code session and no network.
- Every test names the REQ or NFR it checks, in its name or docstring (NFR-010).
- The whole suite is still green, and the code uses nothing Python 3.12 lacks (DEC-14).
- Tests are written before the code for this spec, in the same session.
- LOW tier: proceed to the next spec once the tests are green, then commit.
