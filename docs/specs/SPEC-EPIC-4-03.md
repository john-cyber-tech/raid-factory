# SPEC-EPIC-4-03 — Summary shows owners and never exceeds 400 words

**Story:** EPIC-4-03 · **Covers:** REQ-033, REQ-038, NFR-009 · **Components:** COMP-08
**Build order:** 25 of 25 · **Risk tier:** MEDIUM (The trimming rule is the hardest logic in the tool and rests on assumption A-11.) · **Depends on:** SPEC-EPIC-4-02

## Why

As a client sponsor, I want every item to show who owns it in a summary that always fits one page on my phone, so that I can see who is doing what without scrolling or asking.

The sponsor reads the summary on a phone and wants one page with owners shown (NEED-05, NEED-03).

## Capabilities

- `summary.py`: every item line ends with the owner, or "unowned".
- Ranking inside a section: severity High, Medium, Low, then empty; within a severity, oldest created first.
- Each section shows at most 5 items. If items are left out, the section ends with "N more items in the log".
- After the cap, count the words in the whole text (split on white space). While over 400, drop the lowest-ranked shown item across all sections (lowest severity, then newest; between equals, from the section showing the most items) and add it to that section's N.

## Constraints

- 400 words is a hard limit (DEC-09, NFR-009).
- At most 5 per section, ranked by severity then age (DEC-09, REQ-038).
- Titles are at most 80 characters, which bounds the worst case (REQ-041).
- Age is oldest created first; drop order and word counting as stated (A-11).
- Owner is shown on every item (REQ-033).

## Non-goals

- Shortening titles.
- A configurable limit.
- Judging plain English automatically.

## Success signal

A summary rendered from the worst-case 40-item log is at most 400 words, and every section that omits items states exactly how many.

## Test plan

The Criteria column gives the story's acceptance criterion numbers; CF-n is an item carried forward from the stage 3 review.

| Test | Criteria | Checks |
|---|---|---|
| `test_owner_or_unowned_on_every_line` | 1 | "Priya Nair" and "unowned" shown. REQ-033. |
| `test_cap_and_ranking` | 2 | 8 overdue: 2 High then 3 Medium, oldest first; "3 more items in the log". REQ-038. |
| `test_five_items_no_more_line` | 3 | All 5 listed; no "more items" line. REQ-038. |
| `test_worst_case_is_at_most_400_words` | 4 | 40 open items, 80-character titles, all qualifying: word count ≤ 400. NFR-009. |
| `test_more_line_counts_are_exact` | 5 | For each section, N = qualifying − shown. REQ-038. |
| `test_dropped_items_are_lowest_ranked` | 6 | No shown item ranks below an omitted item in the same section. REQ-038. |
| `test_small_log_untrimmed` | 7 | 3 items: under 400 words, all shown, no "more items" line. NFR-009. |
| `test_exactly_400_words_not_trimmed` | 4 | Edge: a text of exactly 400 words drops nothing. |
| `test_empty_severity_ranks_last` | 2 | Edge: a hand-added item with no severity ranks below Low (SA-1). |
| `MANUAL-plain-english-read` | 8 | At the stage 6 demo the delivery manager reads a generated summary and confirms it is plain English. NFR-009. |

**Test data:** `worst_case_log()` test helper: 30 Risks and 10 Dependencies, each with an 80-character title, High, overdue, created this week, marked as needing a decision.

## Definition of done

- Every test in the test plan exists and passes under `pytest` on Python 3.13, with no Claude Code session and no network.
- Every test names the REQ or NFR it checks, in its name or docstring (NFR-010).
- The whole suite is still green, and the code uses nothing Python 3.12 lacks (DEC-14).
- Tests are written before the code for this spec, in the same session.
- MEDIUM tier: show the owner the diff before committing.
