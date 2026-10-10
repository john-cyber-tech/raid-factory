# EPIC-1-03 — Edit a proposal before accepting it

**Epic:** EPIC-1 Extraction and review · **Covers:** REQ-009, REQ-041 · **Size:** S · **Build order:** 7 of 25
**Depends on:** EPIC-1-01, EPIC-1-02 · **Open questions:** OQ-01

**Story:** As a delivery manager, I want to correct a proposal during review, so that what enters the log is right the first time.

## Acceptance criteria

1. Given the proposal "Test environment down" typed Risk with an empty owner, when I edit type to Issue and owner to "Priya Nair" and then accept, then the log item is I-001 with owner "Priya Nair".
2. Given a proposal under review, when I edit its type to `Question`, then the edit is refused with the four allowed values and the proposal is still awaiting my decision.
3. Given a proposal under review, when I edit its title to one of 81 characters, then the edit is refused with a message stating the 80-character limit and the proposal is still awaiting my decision.
4. Given a proposal I have edited, when I reject it, then nothing is added to the log.

## Notes

Which severity values an edit may set depends on OQ-01.
