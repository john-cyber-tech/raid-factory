# SPEC-EPIC-2-05 — Check note on assumptions, waiting-on party on dependencies

**Story:** EPIC-2-05 · **Covers:** REQ-021, REQ-022 · **Components:** COMP-04, COMP-05, COMP-03
**Build order:** 15 of 25 · **Risk tier:** MEDIUM (One open question (OQ-02): whether the check note is mandatory.) · **Depends on:** SPEC-EPIC-1-03, SPEC-EPIC-2-02, SPEC-EPIC-2-06

## Why

As a delivery manager, I want every assumption to say how we will check it and every dependency to say who we are waiting on, so that they do not sit in the log forever.

Assumptions "just sit there forever" without a way to check them, and a dependency must say who we are waiting on (NEED-09).

## Capabilities

- `store.py`: Assumption items have an optional `check_note`; Dependency items have an optional `waiting_on`.
- `review.py`: when accepting an Assumption, ask "How will we check this? (Enter to skip)"; when accepting a Dependency, ask "Who are we waiting on? (Enter to skip)".
- `cli.py`: `raid update <ID> --check-note "..."` and `--waiting-on "..."`; `raid show` prints them.
- Setting a check note on a non-Assumption, or waiting-on on a non-Dependency, is refused.

## Constraints

- The check note is optional until OQ-02 is answered; if it becomes mandatory, only the Enter-to-skip path changes (OQ-02).
- Each change adds one history entry (ADR-006, REQ-020).
- These two fields are not in the `pending.json` contract; they are asked in review (ADR-004).

## Non-goals

- A validation date for assumptions (OQ-02).
- Having extraction propose these fields.

## Success signal

Accepting the CSV-export Assumption with the note "Confirm format with the ERP vendor" makes `raid show A-001` print that note.

## Test plan

The Criteria column gives the story's acceptance criterion numbers; CF-n is an item carried forward from the stage 3 review.

| Test | Criteria | Checks |
|---|---|---|
| `test_accept_assumption_with_check_note` | 1 | `show A-001` prints the note. REQ-021. |
| `test_accept_dependency_with_waiting_on` | 2 | `show D-001` prints "Acme finance team". REQ-022. |
| `test_update_check_note` | 3 | New note stored; one history entry. REQ-021. |
| `test_check_note_on_risk_refused` | 3 | Failure path: `--check-note` on R-001 refused; log unchanged. |
| `test_skip_check_note` | 1 | Edge: Enter at the question accepts the item with no note. |
| `test_waiting_on_on_assumption_refused` | 2 | Failure path: `--waiting-on` on A-001 refused. |

**Test data:** `assumption_and_dependency.json`: the CSV-export Assumption and the year-end-close Dependency from the sample notes.

## Definition of done

- Every test in the test plan exists and passes under `pytest` on Python 3.13, with no Claude Code session and no network.
- Every test names the REQ or NFR it checks, in its name or docstring (NFR-010).
- The whole suite is still green, and the code uses nothing Python 3.12 lacks (DEC-14).
- Tests are written before the code for this spec, in the same session.
- MEDIUM tier: show the owner the diff before committing.
