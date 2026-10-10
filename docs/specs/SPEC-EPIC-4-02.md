# SPEC-EPIC-4-02 — Summary shows top risks, what is blocked by whom, and decisions needed

**Story:** EPIC-4-02 · **Covers:** REQ-031, REQ-032, REQ-037 · **Components:** COMP-08
**Build order:** 24 of 25 · **Risk tier:** LOW (Three more sections in the pure render function.) · **Depends on:** SPEC-EPIC-4-01, SPEC-EPIC-2-05, SPEC-EPIC-2-07

## Why

As a client sponsor, I want the summary to show the biggest risks and what is waiting on whom, so that I know what could hurt the project and where it is stuck.

The sponsor wants to know what could hurt the project, what is blocked and by whom, and what needs deciding (NEED-05).

## Capabilities

- `summary.py`: Top risks = Risk items, not Closed, severity High.
- Blocked and waiting on = Dependency items, not Closed; each line shows the title and the waiting-on party, or "waiting on: not recorded".
- Decisions needed = items, not Closed, with the decision mark set.

## Constraints

- Severity scale is High, Medium, Low; "top" means High (DEC-18, REQ-031).
- Section list is fixed (DEC-03).
- Decisions needed is driven by the mark (A-9, REQ-037).
- Closed items appear in none of these sections (A-4).

## Non-goals

- Sections for go-live threats or client actions (DEC-03).
- Ranking and limits (SPEC-EPIC-4-03).

## Success signal

With open risks R-001 High and R-002 Medium and closed R-003 High, Top risks lists R-001 only.

## Test plan

The Criteria column gives the story's acceptance criterion numbers; CF-n is an item carried forward from the stage 3 review.

| Test | Criteria | Checks |
|---|---|---|
| `test_top_risks_high_and_open_only` | 1 | R-001 only. REQ-031. |
| `test_dependency_shows_waiting_on` | 2 | Title and "Acme finance team" on one line. REQ-032. |
| `test_closed_dependency_not_listed` | 3 | Not in the section. REQ-032. |
| `test_decisions_needed_marked_and_open` | 4 | R-001 and I-001 only. REQ-037. |
| `test_dependency_without_waiting_on` | 2 | Edge: prints "waiting on: not recorded". |
| `test_high_issue_is_not_a_top_risk` | 1 | Edge: a High Issue is not under Top risks. |

**Test data:** Logs built by the test.

## Definition of done

- Every test in the test plan exists and passes under `pytest` on Python 3.13, with no Claude Code session and no network.
- Every test names the REQ or NFR it checks, in its name or docstring (NFR-010).
- The whole suite is still green, and the code uses nothing Python 3.12 lacks (DEC-14).
- Tests are written before the code for this spec, in the same session.
- LOW tier: proceed to the next spec once the tests are green, then commit.
