# SPEC-EPIC-2-04 — Add an item by hand

**Story:** EPIC-2-04 · **Covers:** REQ-013, REQ-041 · **Components:** COMP-03, COMP-05
**Build order:** 16 of 25 · **Risk tier:** MEDIUM (One spec-level choice to confirm: severity is optional when adding by hand.) · **Depends on:** SPEC-EPIC-1-04, SPEC-EPIC-5-02, SPEC-EPIC-2-06

## Why

As a delivery manager, I want to add an item directly when it did not come from notes, so that the log is complete.

Not every item comes from notes; the log must still be complete (NEED-01).

## Capabilities

- `cli.py`: `raid add --type <type> --title "..."` with optional `--description`, `--owner`, `--severity`, `--due`, `--check-note`, `--waiting-on`.
- `store.py`: the item is created with one source, excerpt "Added manually" and date = today, status Open, and a creation history entry with the user's name.
- Type and title are required. The field rules from `rules.py` apply.
- No duplicate check is run.

## Constraints

- Source is "Added manually" plus the date and the user's name (DEC-05).
- `raid add` does not run the duplicate check (DEC-17).
- Titles are at most 80 characters (DEC-09, REQ-041).
- Severity may be left empty on a hand-added item; an empty severity ranks below Low in the summary. This is a spec-level choice, listed as SA-1 in the stage 4 review (REQ-013).

## Non-goals

- Duplicate warnings on add (limitation L-8).
- Importing items in bulk.

## Success signal

`raid add --type Risk --title "Key analyst on leave in November"` in a log holding R-001 creates R-002, Open, with source "Added manually" and today's date.

## Test plan

The Criteria column gives the story's acceptance criterion numbers; CF-n is an item carried forward from the stage 3 review.

| Test | Criteria | Checks |
|---|---|---|
| `test_add_creates_next_id` | 1 | R-002 with the title, status Open. REQ-013. |
| `test_add_without_title_refused` | 2 | Refused; log unchanged. REQ-013. |
| `test_add_title_81_refused` | 2 | Refused stating the limit. REQ-041. |
| `test_add_same_title_no_duplicate_prompt` | 3 | Added as R-002; output mentions no duplicate. DEC-17. |
| `test_add_source_and_history` | 4 | `show R-002`: "Added manually", 2026-10-10, one creation entry by "Sean Murphy". REQ-013. |
| `test_add_bad_type_refused` | 2 | Failure path: type `Question` refused listing the four values. |
| `test_add_without_severity` | 1 | Edge: accepted with empty severity (SA-1). |

**Test data:** A log holding R-001 "Key analyst on leave in November"; today 2026-10-10; name "Sean Murphy".

## Definition of done

- Every test in the test plan exists and passes under `pytest` on Python 3.13, with no Claude Code session and no network.
- Every test names the REQ or NFR it checks, in its name or docstring (NFR-010).
- The whole suite is still green, and the code uses nothing Python 3.12 lacks (DEC-14).
- Tests are written before the code for this spec, in the same session.
- MEDIUM tier: show the owner the diff before committing.
