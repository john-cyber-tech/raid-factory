# EPIC-2-04 — Add an item by hand

**Epic:** EPIC-2 Log management · **Covers:** REQ-013, REQ-041 · **Size:** S · **Build order:** 16 of 25
**Depends on:** EPIC-1-04, EPIC-5-02, EPIC-2-06 · **Open questions:** none

**Story:** As a delivery manager, I want to add an item directly when it did not come from notes, so that the log is complete.

## Acceptance criteria

1. Given a log holding R-001, when I add a Risk by hand with the title "Key analyst on leave in November", then the log holds R-002 with that title and status Open.
2. Given the same command without a title, or with a title of 81 characters, then it is refused and the log is unchanged.
3. Given a log holding R-001 "Key analyst on leave in November", when I add a Risk by hand with the same title, then it is added as R-002 and no likely duplicate is shown.
4. Given R-002 added by hand on 2026-10-10 by "Sean Murphy", when I view R-002, then its source excerpt is "Added manually", its source date is 2026-10-10, and its one history entry shows creation by "Sean Murphy".

## Notes

Source values are decision DEC-05. Adding by hand does not run the duplicate check (decision DEC-17).
