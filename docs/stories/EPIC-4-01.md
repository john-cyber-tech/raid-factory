# EPIC-4-01 — Generate the weekly summary with new and overdue items

**Epic:** EPIC-4 Weekly summary · **Covers:** REQ-028, REQ-029, REQ-030 · **Size:** M · **Build order:** 23 of 25
**Depends on:** EPIC-3-01, EPIC-5-02 · **Open questions:** OQ-07, OQ-17

**Story:** As a delivery manager, I want one command to write this week's RAID summary, so that Friday's update takes minutes instead of 45.

## Acceptance criteria

1. Given a log with items, when I run `raid summary`, then exactly one `.md` file is written in the project folder and the log is byte-identical to before.
2. Given today is 2026-10-10 and items created on 2026-10-05 and 2026-10-02, then the first appears under "New this week" and the second does not.
3. Given today is 2026-10-10 and open items due 2026-10-09 and 2026-10-10, then only the first appears under "Overdue".
4. Given a log where no item is new or overdue, then each section is present and says "None".
5. Given an empty log, when I run `raid summary`, then a file is still written and says there are no items.

## Notes

"This week" is the 7 days up to and including today (assumption A-5). The five v1 sections are fixed by decision DEC-03; this story delivers two of them. PDF is OQ-07; whether excerpts appear is OQ-17 (criteria assume they do not).
