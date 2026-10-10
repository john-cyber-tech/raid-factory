# EPIC-2-01 — List only my items

**Epic:** EPIC-2 Log management · **Covers:** REQ-015 · **Size:** S · **Build order:** 13 of 25
**Depends on:** EPIC-1-01 · **Open questions:** none

**Story:** As a project manager, I want to see only the items assigned to me, so that I can find what I need to update quickly.

## Acceptance criteria

1. Given a log with 5 items of which 2 have owner "Priya Nair", when I list items for owner "Priya Nair", then exactly those 2 are shown.
2. Given the same log, when I list items for owner "priya nair", then the same 2 are shown.
3. Given the same log, when I list items for owner "Priya", then no items are shown.
4. Given the same log, when I list items for owner "Lena", then no items are shown, a message says none were found, and the exit code is zero.

## Notes

Exact match ignoring case, by decision DEC-07. Consequence to be aware of: the sample notes use first names, so an item extracted with owner "Priya" is not found by a search for "Priya Nair" unless the owner is corrected in review.
