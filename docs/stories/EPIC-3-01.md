# EPIC-3-01 — Flag unowned and overdue items

**Epic:** EPIC-3 Flags and duplicates · **Covers:** REQ-025, REQ-026 · **Size:** S · **Build order:** 18 of 25
**Depends on:** EPIC-2-03 · **Open questions:** none

**Story:** As a delivery manager, I want items with no owner or a missed due date pointed out, so that I can fix them before the client asks.

## Acceptance criteria

1. Given 3 open items of which only R-002 has an empty owner, when I run `raid flag`, then exactly R-002 is flagged "unowned".
2. Given today is 2026-10-10 and open items due 2026-10-09, due 2026-10-10 and with no due date, when I run `raid flag`, then only the first is flagged "overdue".
3. Given a Closed item with an empty owner and a due date of 2026-10-01, when I run `raid flag` on 2026-10-10, then it is not flagged.
4. Given a log where nothing qualifies, when I run `raid flag`, then a message says there are no flags and the exit code is zero.

## Notes

Closed items are excluded by assumption A-4.
