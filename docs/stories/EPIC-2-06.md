# EPIC-2-06 — View one item in full

**Epic:** EPIC-2 Log management · **Covers:** REQ-034 · **Size:** S · **Build order:** 11 of 25
**Depends on:** EPIC-1-04, EPIC-5-02 · **Open questions:** none

**Story:** As a delivery manager, I want to see everything about one item, including what was said and every change since, so that I can answer the client when they challenge it.

## Acceptance criteria

1. Given R-001 accepted from the excerpt "Tom said the client security review for the new cloud tenant hasn't started" with source date 2026-10-07, when I view R-001, then the output shows its ID, type, title, description, owner, severity, due date and status, that excerpt, and 2026-10-07.
2. Given R-001 whose owner was later set to "Priya Nair" by "Sean Murphy", when I view R-001, then both history entries are shown, oldest first, each with its date and "Sean Murphy".
3. Given a log with no R-099, when I view R-099, then the exit code is non-zero and the message says R-099 does not exist.
4. Given I view R-001, then the log file is byte-identical to before.

## Notes

Decision DEC-06, closing stage 2 finding R-01. Later stories add what they store to this view: closed date and reason (EPIC-2-03), check note and waiting-on (EPIC-2-05), decision mark (EPIC-2-07), merged excerpts (EPIC-3-04).
