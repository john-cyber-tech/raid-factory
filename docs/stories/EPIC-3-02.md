# EPIC-3-02 — Flag stale items

**Epic:** EPIC-3 Flags and duplicates · **Covers:** REQ-027 · **Size:** S · **Build order:** 19 of 25
**Depends on:** EPIC-3-01, EPIC-5-02 · **Open questions:** none

**Story:** As a project manager, I want items nobody has touched for two weeks pointed out, so that old risks do not quietly rot.

## Acceptance criteria

1. Given today is 2026-10-24 and an open item last changed on 2026-10-10, when I run `raid flag`, then it is flagged "stale".
2. Given today is 2026-10-24 and an open item last changed on 2026-10-11, then it is not flagged "stale".
3. Given a stale item, when I update any field and run `raid flag` the same day, then it is no longer flagged "stale".
4. Given an item that is both unowned and stale, then it is shown with both flags.

## Notes

"Last changed" is the newest history entry (EPIC-5-02). Day 14 is the boundary by assumption A-5.
