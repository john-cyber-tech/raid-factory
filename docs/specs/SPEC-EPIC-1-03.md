# SPEC-EPIC-1-03 — Edit a proposal before accepting it

**Story:** EPIC-1-03 · **Covers:** REQ-009, REQ-041 · **Components:** COMP-04, COMP-05
**Build order:** 7 of 25 · **Risk tier:** MEDIUM (Extends the interactive review flow.) · **Depends on:** SPEC-EPIC-1-01, SPEC-EPIC-1-02

## Why

As a delivery manager, I want to correct a proposal during review, so that what enters the log is right the first time.

What enters the log should be right the first time, and the manager corrects the type herself (NEED-02, NEED-13).

## Capabilities

- `review.py`: a third answer, `e` edit. It asks which field, then the new value, and returns to the same proposal's question.
- `src/raid/rules.py`: one set of field rules (allowed types, High/Medium/Low, 80-character one-line title, real dates) used by review edits here and by `add` and `update` later.
- An edit that breaks a rule is refused with the rule stated; the proposal keeps its previous value and is still awaiting a decision.
- The ID prefix comes from the type at the moment of acceptance.

## Constraints

- Field rules match the contract exactly (ADR-004).
- Severity is High, Medium or Low (DEC-18).
- Titles are at most 80 characters (DEC-09, REQ-041).
- An edit changes nothing in the log until accept (ADR-002, REQ-008).

## Non-goals

- Editing an item already in the log (SPEC-EPIC-2-02).
- Editing the source excerpt: it is what was said.

## Success signal

Editing "Test environment down" from Risk to Issue with owner "Priya Nair" and accepting creates I-001 with that owner.

## Test plan

The Criteria column gives the story's acceptance criterion numbers; CF-n is an item carried forward from the stage 3 review.

| Test | Criteria | Checks |
|---|---|---|
| `test_edit_type_and_owner_then_accept` | 1 | Log item is I-001, owner "Priya Nair". REQ-009. |
| `test_edit_to_bad_type_refused` | 2 | Type `Question` refused listing the four values; proposal still pending. REQ-009. |
| `test_edit_title_81_refused` | 3 | Refused stating the 80-character limit; still pending. REQ-041. |
| `test_edit_then_reject_adds_nothing` | 4 | Log unchanged. REQ-008. |
| `test_excerpt_cannot_be_edited` | 2 | Failure path: choosing `source_excerpt` as the field to edit is refused. |
| `test_edit_severity_to_bad_value_refused` | 2 | Edge: severity `Critical` refused listing High, Medium, Low. DEC-18. |

**Test data:** `valid_three.json` plus `risk_no_owner.json` ("Test environment down" typed Risk, owner empty).

## Definition of done

- Every test in the test plan exists and passes under `pytest` on Python 3.13, with no Claude Code session and no network.
- Every test names the REQ or NFR it checks, in its name or docstring (NFR-010).
- The whole suite is still green, and the code uses nothing Python 3.12 lacks (DEC-14).
- Tests are written before the code for this spec, in the same session.
- MEDIUM tier: show the owner the diff before committing.
