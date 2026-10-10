# SPEC-EPIC-3-02 — Flag stale items

**Story:** EPIC-3-02 · **Covers:** REQ-027 · **Components:** COMP-07
**Build order:** 19 of 25 · **Risk tier:** LOW (Extends the pure flag function.) · **Depends on:** SPEC-EPIC-3-01, SPEC-EPIC-5-02

## Why

As a project manager, I want items nobody has touched for two weeks pointed out, so that old risks do not quietly rot.

Risks raised in August that nobody has touched must be pointed out (NEED-11).

## Capabilities

- `flags.py`: add `stale` when today minus the date of the item's last history entry is 14 days or more.
- An item can carry several flags; `raid flag` prints them together.

## Constraints

- Stale starts on day 14; any recorded change resets it (A-5, REQ-027).
- Last changed is read from history (ADR-006).
- Closed items are never flagged (A-4).

## Non-goals

- A configurable number of days.
- Nudges or reminders (brief, non-goals).

## Success signal

On 2026-10-24 an item last changed on 2026-10-10 is flagged stale and one last changed on 2026-10-11 is not.

## Test plan

The Criteria column gives the story's acceptance criterion numbers; CF-n is an item carried forward from the stage 3 review.

| Test | Criteria | Checks |
|---|---|---|
| `test_stale_at_14_days` | 1 | Last changed 10-10, today 10-24: stale. REQ-027. |
| `test_not_stale_at_13_days` | 2 | Last changed 10-11: not stale. REQ-027. |
| `test_update_clears_stale` | 3 | After any update the same day, not stale. REQ-027. |
| `test_unowned_and_stale_together` | 4 | Both flags on one line. REQ-027. |
| `test_closed_stale_item_not_flagged` | 1 | Edge: a Closed item untouched for 30 days is not flagged. |
| `test_refused_update_does_not_clear_stale` | 3 | Failure path: a refused update leaves the item stale. |

**Test data:** Items with history timestamps set by passing the clock in.

## Definition of done

- Every test in the test plan exists and passes under `pytest` on Python 3.13, with no Claude Code session and no network.
- Every test names the REQ or NFR it checks, in its name or docstring (NFR-010).
- The whole suite is still green, and the code uses nothing Python 3.12 lacks (DEC-14).
- Tests are written before the code for this spec, in the same session.
- LOW tier: proceed to the next spec once the tests are green, then commit.
