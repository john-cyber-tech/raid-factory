# EPIC-1-04 — Keep the source excerpt and date with every item

**Epic:** EPIC-1 Extraction and review · **Covers:** REQ-012, REQ-040 · **Size:** S · **Build order:** 8 of 25
**Depends on:** EPIC-1-01 · **Open questions:** none

**Story:** As a delivery manager, I want every log item to keep the words it came from and their date, so that I can answer the client when they challenge an item.

## Acceptance criteria

1. Given the proposal P1 with excerpt "Tom said the client security review for the new cloud tenant hasn't started", when I accept it, then R-001 in the log file holds exactly that excerpt.
2. Given a proposal that carries the source date 2026-10-07, when I accept it, then I am not asked for a date and the item's source date in the log file is 2026-10-07.
3. Given a proposal with an empty source date, when I accept it, then I am asked for the source date, and entering 2026-10-07 stores 2026-10-07 on the item.
4. Given I am asked for the source date, when I enter nothing, then the proposal is not accepted, it is still awaiting my decision, and the log is byte-identical to before.
5. Given I am asked for the source date, when I enter `2026-13-40`, then it is refused with a message giving the expected date format and I am asked again.
6. Given R-001, when any later command tries to set its excerpt or source date to empty, then it is refused and the stored values are unchanged.

## Notes

Decision DEC-08: an item cannot be accepted without a source date. Displaying the excerpt and date outside review is EPIC-2-06.
