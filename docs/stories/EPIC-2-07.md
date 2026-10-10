# EPIC-2-07 — Mark an item as needing a decision

**Epic:** EPIC-2 Log management · **Covers:** REQ-036 · **Size:** S · **Build order:** 17 of 25
**Depends on:** EPIC-2-02, EPIC-2-06 · **Open questions:** none

**Story:** As a delivery manager, I want to mark the items that need a decision from the sponsor, so that the weekly summary can put them in front of them.

## Acceptance criteria

1. Given R-001 unmarked, when I mark it as needing a decision, then viewing R-001 shows the mark and one history entry records the change.
2. Given R-001 marked, when I clear the mark, then viewing R-001 no longer shows it and one more history entry is added.
3. Given a log with no R-099, when I mark R-099, then the exit code is non-zero and the log is unchanged.

## Notes

A yes/no mark is assumption A-9: no source says how 'decisions needed' items are identified.
