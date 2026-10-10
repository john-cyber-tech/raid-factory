# SPEC-EPIC-3-03 — Show likely duplicates during review

**Story:** EPIC-3-03 · **Covers:** REQ-023 · **Components:** COMP-06, COMP-04
**Build order:** 20 of 25 · **Risk tier:** MEDIUM (The threshold and the common-word list are assumptions to tune (A-10).) · **Depends on:** SPEC-EPIC-1-03

## Why

As a delivery manager, I want to be told when a proposal looks like something already in the log, so that the same risk is not recorded three times.

The same risk raised in three calls ends up three times in the sheet; this is Sean's main complaint (NEED-04).

## Capabilities

- `src/raid/dedup.py`: `find(proposal, items)` returns the IDs of likely duplicates. Pure function.
- Rule: same type, and either titles identical after lower-casing and removing spacing and punctuation, or at least 2 shared key words that make up at least half of the shorter title's key words.
- Key words: the title's words in lower case, minus a fixed list of common words kept as one constant (a, an, the, of, to, in, on, for, and, or, is, are, be, may, might, will, has, have, with, by, at, from).
- `review.py`: show likely duplicates under the proposal with ID, title and status, Closed items marked "(Closed)". Re-run after an edit to type or title.
- Showing a duplicate changes nothing; the manager is still asked for a decision.

## Constraints

- Deterministic rule in Python; no model, and the command does not read the log (ADR-003).
- Same type only; suggest only (DEC-01).
- Closed items are offered (DEC-17).
- Threshold and word list are constants to tune in stage 5 (A-10).

## Non-goals

- Detecting reworded duplicates (limitation L-4).
- Merging (SPEC-EPIC-3-04).
- Checking on `raid add` (DEC-17).

## Success signal

With R-001 "Client security review may delay cutover" in the log, a Risk proposal "Security review delay raised again" is shown with R-001 beside it, and an Issue proposal with the identical title is not.

## Test plan

The Criteria column gives the story's acceptance criterion numbers; CF-n is an item carried forward from the stage 3 review.

| Test | Criteria | Checks |
|---|---|---|
| `test_identical_title_ignoring_case_and_spacing` | 1 | R-001 shown with ID and title. REQ-023. |
| `test_three_of_five_keywords` | 2 | "Security review delay raised again" shows R-001. REQ-023. |
| `test_no_shared_keywords` | 3 | "Key analyst on leave in November" shows nothing. REQ-023. |
| `test_different_type_not_matched` | 4 | Issue with the same title shows nothing. REQ-023. |
| `test_edit_type_reruns_check` | 5 | After editing to Risk, R-001 is shown. REQ-023. |
| `test_closed_item_offered` | 6 | Closed R-001 shown and marked "(Closed)". DEC-17. |
| `test_nothing_merged_automatically` | 7 | Decision is still asked; log unchanged until answered. REQ-023. |
| `test_one_shared_keyword_not_enough` | 3 | Edge: titles sharing only "security" do not match. |
| `test_title_of_only_common_words` | 3 | Edge: a title with no key words matches only an identical title. |
| `test_several_duplicates_all_listed` | 1 | Edge: two matching items are both shown. |

**Test data:** A log with R-001 "Client security review may delay cutover"; proposals from `dup_cases.json`.

## Definition of done

- Every test in the test plan exists and passes under `pytest` on Python 3.13, with no Claude Code session and no network.
- Every test names the REQ or NFR it checks, in its name or docstring (NFR-010).
- The whole suite is still green, and the code uses nothing Python 3.12 lacks (DEC-14).
- Tests are written before the code for this spec, in the same session.
- MEDIUM tier: show the owner the diff before committing.
