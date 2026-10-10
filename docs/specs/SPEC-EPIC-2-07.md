# SPEC-EPIC-2-07 — Mark an item as needing a decision

**Story:** EPIC-2-07 · **Covers:** REQ-036 · **Components:** COMP-03, COMP-05
**Build order:** 17 of 25 · **Risk tier:** LOW (One yes/no field through the existing update path.) · **Depends on:** SPEC-EPIC-2-02, SPEC-EPIC-2-06

## Why

As a delivery manager, I want to mark the items that need a decision from the sponsor, so that the weekly summary can put them in front of them.

The sponsor's summary must show what needs a decision; something has to mark those items (NEED-05, DEC-03).

## Capabilities

- `store.py`: every item has `needs_decision`, false by default.
- `cli.py`: `raid update <ID> --needs-decision yes|no`; `raid show` prints "Needs a decision" when it is set.

## Constraints

- A yes/no mark set by the user is how "decisions needed" items are identified (A-9, REQ-036).
- Each change adds one history entry (ADR-006, REQ-020).

## Non-goals

- Recording what the decision is or who must make it.
- Having extraction set the mark.

## Success signal

Marking R-001 makes `raid show R-001` print "Needs a decision" and adds one history entry; clearing it removes the line and adds one more.

## Test plan

The Criteria column gives the story's acceptance criterion numbers; CF-n is an item carried forward from the stage 3 review.

| Test | Criteria | Checks |
|---|---|---|
| `test_mark_needs_decision` | 1 | Shown by `show`; one entry. REQ-036. |
| `test_clear_needs_decision` | 2 | No longer shown; one more entry. REQ-036. |
| `test_mark_unknown_id` | 3 | R-099: exit 1; log unchanged. REQ-036. |
| `test_mark_twice_adds_one_entry` | 1 | Edge: marking an already marked item adds no entry. |
| `test_mark_bad_value_refused` | 3 | Failure path: `--needs-decision maybe` refused. |

**Test data:** A log with R-001.

## Definition of done

- Every test in the test plan exists and passes under `pytest` on Python 3.13, with no Claude Code session and no network.
- Every test names the REQ or NFR it checks, in its name or docstring (NFR-010).
- The whole suite is still green, and the code uses nothing Python 3.12 lacks (DEC-14).
- Tests are written before the code for this spec, in the same session.
- LOW tier: proceed to the next spec once the tests are green, then commit.
