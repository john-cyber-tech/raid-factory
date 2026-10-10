# EPIC-3-04 — Merge a proposal into an existing item

**Epic:** EPIC-3 Flags and duplicates · **Covers:** REQ-024 · **Size:** M · **Build order:** 21 of 25
**Depends on:** EPIC-3-03, EPIC-5-02, EPIC-2-03 · **Open questions:** none

**Story:** As a delivery manager, I want to merge a repeated proposal into the item that already exists, so that the log shows one item with all the places it was raised.

## Acceptance criteria

1. Given R-001 shown as a likely duplicate, when I choose merge, then the log still has exactly one Risk, R-001 has gained the proposal's source excerpt and source date in addition to its own, and R-001's history has a new entry recording the merge.
2. Given R-001 with owner "Priya Nair" and severity High, and a proposal with an empty owner and severity Low, when I choose merge, then R-001 still has owner "Priya Nair" and severity High, and its title and due date are unchanged.
3. Given R-001 shown as a likely duplicate, when I choose keep separate and accept, then the proposal becomes R-002 and R-001 is unchanged.
4. Given R-001 shown as a likely duplicate, when I reject the proposal, then the log is unchanged.
5. Given Closed R-001 shown as a likely duplicate, when I choose merge, then before I confirm I am told that R-001 is Closed and that merging will reopen it.
6. Given that warning, when I confirm on 2026-10-10 as "Sean Murphy", then R-001 is Open, it has gained the proposal's source, and its history has a merge entry and a reopening entry with the reason "reopened by merge of a new proposal", the date 2026-10-10 and the name "Sean Murphy".
7. Given that warning, when I do not confirm, then R-001 is still Closed with no new source or history entry, and the proposal is still awaiting my decision.

## Notes

Merging into a Closed item reopens it, by decision DEC-22. Raised from S to M for the confirm step and the reopening. The existing item's title, owner, severity and due date are kept on merge (decision DEC-15). An item holds a list of sources, so the merged excerpt sits beside the original (architecture section 5).
