# SPEC-EPIC-4-01 — Generate the weekly summary with new and overdue items

**Story:** EPIC-4-01 · **Covers:** REQ-028, REQ-029, REQ-030 · **Components:** COMP-08, COMP-03, COMP-07
**Build order:** 23 of 25 · **Risk tier:** MEDIUM (Two open questions (OQ-07, OQ-17) and a new file written.) · **Depends on:** SPEC-EPIC-3-01, SPEC-EPIC-5-02

## Why

As a delivery manager, I want one command to write this week's RAID summary, so that Friday's update takes minutes instead of 45.

The Friday summary takes 45 minutes by hand (NEED-05).

## Capabilities

- `src/raid/summary.py`: `render(items, today)` returns markdown text. Pure function.
- A title line with the date, then the sections in this order: Top risks, New this week, Overdue, Decisions needed, Blocked and waiting on. This spec fills New this week and Overdue; the others print "None" until SPEC-EPIC-4-02.
- New this week: items created in the 7 days up to and including today. Overdue: the items `flags.py` marks overdue.
- An empty section prints "None". An empty log gives a file that says there are no items.
- `cli.py`: `raid summary` writes `raid-summary-YYYY-MM-DD.md` in the project folder and prints its name. Running it again the same day replaces that file.
- Each item line shows ID, title and severity. Source excerpts are not included.

## Constraints

- Five sections fixed by decision (DEC-03).
- Overdue uses the flagger's rule, not a second copy (REQ-030).
- "This week" is 7 days including today (A-5).
- Markdown only until OQ-07 is answered (OQ-07).
- No source excerpts in the summary until OQ-17 is answered (OQ-17).
- The summary never changes the log (REQ-028, ADR-001).
- The file is written in the project folder (NFR-006).

## Non-goals

- PDF output (OQ-07).
- Sending the summary (brief, non-goals).
- Top risks, dependencies, decisions (SPEC-EPIC-4-02).
- Owners and the word limit (SPEC-EPIC-4-03).

## Success signal

On 2026-10-10, `raid summary` writes `raid-summary-2026-10-10.md` with an item created 2026-10-05 under New this week and not one created 2026-10-02, and the log is byte-identical.

## Test plan

The Criteria column gives the story's acceptance criterion numbers; CF-n is an item carried forward from the stage 3 review.

| Test | Criteria | Checks |
|---|---|---|
| `test_summary_writes_one_file` | 1 | One `.md` file in the folder; log byte-identical. REQ-028. |
| `test_new_this_week_boundary` | 2 | Created 10-05 listed; 10-02 not. REQ-029. |
| `test_new_this_week_day_seven` | 2 | Edge: created 10-04 (7 days including today) listed; 10-03 not. A-5. |
| `test_overdue_matches_flagger` | 3 | Due 10-09 listed; due 10-10 not; equals `flags()` output. REQ-030. |
| `test_empty_sections_say_none` | 4 | Each section present with "None". REQ-028. |
| `test_empty_log_summary` | 5 | File written, says there are no items. REQ-028. |
| `test_same_day_summary_overwrites` | CF-3 | Second run the same day: still one file, with the newer content. |
| `test_summary_has_no_excerpts` | 1 | No source excerpt text appears in the file. OQ-17. |
| `test_closed_items_not_in_new_or_overdue` | 3 | Edge: a Closed item created this week and past due appears in neither. |

**Test data:** Logs built by the test; today 2026-10-10.

## Definition of done

- Every test in the test plan exists and passes under `pytest` on Python 3.13, with no Claude Code session and no network.
- Every test names the REQ or NFR it checks, in its name or docstring (NFR-010).
- The whole suite is still green, and the code uses nothing Python 3.12 lacks (DEC-14).
- The outside-write test from SPEC-EPIC-5-04 now includes `raid summary`.
- Tests are written before the code for this spec, in the same session.
- MEDIUM tier: show the owner the diff before committing.
