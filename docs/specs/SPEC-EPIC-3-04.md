# SPEC-EPIC-3-04 — Merge a proposal into an existing item

**Story:** EPIC-3-04 · **Covers:** REQ-024 · **Components:** COMP-04, COMP-05
**Build order:** 21 of 25 · **Risk tier:** MEDIUM (Adds a new kind of write to an existing item.) · **Depends on:** SPEC-EPIC-3-03, SPEC-EPIC-5-02

## Why

As a delivery manager, I want to merge a repeated proposal into the item that already exists, so that the log shows one item with all the places it was raised.

The log should show one item with all the places it was raised (NEED-04).

## Capabilities

- `review.py`: when likely duplicates are shown, a fourth answer `m` merge; if several are shown, ask which ID.
- `store.py`: `merge_source(id, excerpt, date)` appends a source to the item and one history entry of kind merged. No other value of the item changes.
- A proposal with no source date is asked for one before merging, as for accept.
- Accept with a duplicate shown means keep separate: a new ID is created.
- `raid show` lists every source, the original first.

## Constraints

- A merge keeps the existing item's title, owner, severity, due date and status (DEC-15).
- A merge happens only when the manager chooses it (DEC-01, ADR-003).
- Merging into a Closed item leaves it Closed (DEC-15, DEC-17; limitation L-8).
- A source needs a date (DEC-08).

## Non-goals

- Merging two items already in the log (limitation L-4).
- Reopening on merge.

## Success signal

Choosing merge for a proposal shown against R-001 leaves exactly one Risk, with two sources and a merged entry in its history.

## Test plan

The Criteria column gives the story's acceptance criterion numbers; CF-n is an item carried forward from the stage 3 review.

| Test | Criteria | Checks |
|---|---|---|
| `test_merge_adds_source_and_history` | 1 | One Risk; R-001 has two sources; history has a merged entry. REQ-024. |
| `test_merge_keeps_existing_values` | 2 | Owner "Priya Nair", High, title and due date unchanged. DEC-15. |
| `test_keep_separate_creates_new_id` | 3 | Proposal becomes R-002; R-001 unchanged. REQ-024. |
| `test_reject_with_duplicate_shown` | 4 | Log unchanged. REQ-024. |
| `test_merged_excerpt_visible_in_show` | CF-5 | `show R-001` prints both excerpts, original first. |
| `test_merge_without_source_date_is_asked` | CF-5 | Proposal with no date: asked before the merge; empty answer cancels. |
| `test_merge_into_closed_stays_closed` | 2 | Edge: Closed R-001 is still Closed after a merge. L-8. |
| `test_merge_not_offered_without_duplicate` | 4 | Failure path: `m` with no duplicate shown repeats the question. |

**Test data:** R-001 owner "Priya Nair", High; proposal with empty owner, Low, same title.

## Definition of done

- Every test in the test plan exists and passes under `pytest` on Python 3.13, with no Claude Code session and no network.
- Every test names the REQ or NFR it checks, in its name or docstring (NFR-010).
- The whole suite is still green, and the code uses nothing Python 3.12 lacks (DEC-14).
- Tests are written before the code for this spec, in the same session.
- MEDIUM tier: show the owner the diff before committing.
