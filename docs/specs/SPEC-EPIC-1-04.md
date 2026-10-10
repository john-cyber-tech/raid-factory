# SPEC-EPIC-1-04 — Keep the source excerpt and date with every item

**Story:** EPIC-1-04 · **Covers:** REQ-012, REQ-040 · **Components:** COMP-04, COMP-05
**Build order:** 8 of 25 · **Risk tier:** MEDIUM (Changes what is required before an item can be accepted.) · **Depends on:** SPEC-EPIC-1-01

## Why

As a delivery manager, I want every log item to keep the words it came from and their date, so that I can answer the client when they challenge an item.

When the client challenges an item, the manager must be able to show what was said and when (NEED-07).

## Capabilities

- `store.py`: every item has a `sources` list; each source has `excerpt` and `date`. `add_item` requires one source with both present.
- `review.py`: on accept, if the proposal has no `source_date`, ask "Date of the notes (YYYY-MM-DD):". A valid answer is used. An empty answer cancels the accept and returns to the proposal's question. An invalid date is refused with the expected format and asked again.
- `rules.py`: the first source's excerpt and date can never be set to empty.

## Constraints

- An item cannot be accepted without a source date (DEC-08, REQ-040).
- Sources are a list so a merge can add one; the first is the original (ADR-006, REQ-012).
- "Source date" is the date of the notes, not the date of acceptance (A-8).

## Non-goals

- Guessing a year (DEC-08).
- Showing the excerpt outside review (SPEC-EPIC-2-06).
- Adding sources by merge (SPEC-EPIC-3-04).

## Success signal

Accepting a proposal without a source date asks for one; an empty answer leaves the proposal pending and the log byte-identical.

## Test plan

The Criteria column gives the story's acceptance criterion numbers; CF-n is an item carried forward from the stage 3 review.

| Test | Criteria | Checks |
|---|---|---|
| `test_excerpt_stored_exactly` | 1 | R-001's first source excerpt equals P1's excerpt. REQ-012. |
| `test_date_present_not_asked` | 2 | Proposal carries 2026-10-07: no question; stored date 2026-10-07. REQ-040. |
| `test_date_missing_is_asked` | 3 | Asked; entering 2026-10-07 stores it. REQ-040. |
| `test_empty_date_cancels_accept` | 4 | Proposal still pending; log byte-identical. REQ-040. |
| `test_invalid_date_asked_again` | 5 | `2026-13-40` refused with the format, asked again. REQ-040. |
| `test_source_cannot_be_emptied` | 6 | Store refuses an empty excerpt or date; values unchanged. REQ-012. |
| `test_future_source_date_refused` | 5 | Edge: a notes date after today is refused. |

**Test data:** `no_source_date.json`: P1 with `source_date` null.

## Definition of done

- Every test in the test plan exists and passes under `pytest` on Python 3.13, with no Claude Code session and no network.
- Every test names the REQ or NFR it checks, in its name or docstring (NFR-010).
- The whole suite is still green, and the code uses nothing Python 3.12 lacks (DEC-14).
- Tests are written before the code for this spec, in the same session.
- MEDIUM tier: show the owner the diff before committing.
