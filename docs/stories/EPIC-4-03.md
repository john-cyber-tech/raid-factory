# EPIC-4-03 — Summary shows owners and never exceeds 400 words

**Epic:** EPIC-4 Weekly summary · **Covers:** REQ-033, REQ-038, NFR-009 · **Size:** M · **Build order:** 25 of 25
**Depends on:** EPIC-4-02 · **Open questions:** none

**Story:** As a client sponsor, I want every item to show who owns it in a summary that always fits one page on my phone, so that I can see who is doing what without scrolling or asking.

## Acceptance criteria

1. Given a summary containing R-001 with owner "Priya Nair" and R-002 with no owner, then R-001 shows "Priya Nair" and R-002 shows "unowned".
2. Given 8 open overdue items with short titles (2 High, 3 Medium, 3 Low, each created on a different day), then "Overdue" lists exactly 5: the 2 High then the 3 Medium, oldest created first within each severity, followed by the line "3 more items in the log".
3. Given 5 open overdue items, then all 5 are listed and no "more items" line appears in that section.
4. Given a worst-case log of 40 open items (30 Risks and 10 Dependencies with a waiting-on party), each with an 80-character title, High severity, overdue, created this week and marked as needing a decision, when the summary is generated, then the file contains at most 400 words, counted as whitespace-separated words.
5. Given the same worst-case log, then every section that leaves items out ends with "N more items in the log", where N is exactly the number of items that qualify for that section and are not shown.
6. Given a log where the 5-per-section cap alone would give more than 400 words, then no item shown in a section is ranked lower than an item left out of that same section.
7. Given a log of 3 open items, then the summary is under 400 words, every qualifying item is shown, and no "more items" line appears.
8. Given a summary generated from the stage 6 demo log, when the delivery manager reads it, then they confirm it is plain English with no tool jargon.

## Notes

Decision DEC-09: 400 words is the hard limit; sections show at most 5 items ranked by severity then age; if still over, the lowest-ranked items are dropped. The 80-character title limit that makes the worst case bounded is REQ-041 (EPIC-1-02, EPIC-2-02, EPIC-2-04). "Age" as oldest-created-first, the order in which items are dropped across sections, and the word-count method are assumption A-11. Severity ranking uses High/Medium/Low (DEC-18). Raised from S to M: the trimming rule is the hardest logic in this epic.
