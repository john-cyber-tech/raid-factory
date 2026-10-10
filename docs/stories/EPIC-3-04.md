# EPIC-3-04 — Merge a proposal into an existing item

**Epic:** EPIC-3 Flags and duplicates · **Covers:** REQ-024 · **Size:** S · **Build order:** 21 of 25
**Depends on:** EPIC-3-03, EPIC-5-02 · **Open questions:** OQ-13

**Story:** As a delivery manager, I want to merge a repeated proposal into the item that already exists, so that the log shows one item with all the places it was raised.

## Acceptance criteria

1. Given R-001 shown as a likely duplicate, when I choose merge, then the log still has exactly one Risk, R-001 has gained the proposal's source excerpt and source date in addition to its own, and R-001's history has a new entry recording the merge.
2. Given R-001 shown as a likely duplicate, when I choose keep separate and accept, then the proposal becomes R-002 and R-001 is unchanged.
3. Given R-001 shown as a likely duplicate, when I reject the proposal, then the log is unchanged.

## Notes

Which values win when the proposal and R-001 differ is OQ-13. Stage 1 finding R-07 (an item with more than one excerpt) is settled in stage 3.
