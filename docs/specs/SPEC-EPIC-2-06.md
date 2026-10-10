# SPEC-EPIC-2-06 — View one item in full

**Story:** EPIC-2-06 · **Covers:** REQ-034 · **Components:** COMP-03, COMP-05
**Build order:** 11 of 25 · **Risk tier:** LOW (Read-only output.) · **Depends on:** SPEC-EPIC-1-04, SPEC-EPIC-5-02

## Why

As a delivery manager, I want to see everything about one item, including what was said and every change since, so that I can answer the client when they challenge it.

The manager needs to see what was actually said and every change since (NEED-07, NEED-12).

## Capabilities

- `cli.py`: `raid show <ID>` prints all the item's fields, then each source (excerpt and date), then the history oldest first, each entry with its date, the name and what changed.
- `store.py`: `get(id)`; an unknown ID is an error the CLI reports with exit code 1.
- Fields that later specs add (closed date and reason, check note, waiting-on, decision mark) are printed when present.

## Constraints

- `show` never writes (ADR-001, NFR-003).
- History is displayed, never edited (ADR-006, NFR-007).

## Non-goals

- Filtering or searching history.
- Any output format other than plain text.

## Success signal

`raid show R-001` prints the item's fields, its excerpt, its source date and both history entries, and the log file is byte-identical afterwards.

## Test plan

The Criteria column gives the story's acceptance criterion numbers; CF-n is an item carried forward from the stage 3 review.

| Test | Criteria | Checks |
|---|---|---|
| `test_show_fields_and_source` | 1 | Output has the eight fields, the excerpt and 2026-10-07. REQ-034. |
| `test_show_history_oldest_first` | 2 | Two entries in order, each with date and "Sean Murphy". REQ-034. |
| `test_show_unknown_id` | 3 | R-099: exit 1, message says it does not exist. REQ-034. |
| `test_show_changes_nothing` | 4 | Log byte-identical. REQ-034. |
| `test_show_id_is_case_insensitive` | 3 | Edge: `r-001` finds R-001. |

**Test data:** A log with R-001 from P1, owner later set to "Priya Nair".

## Definition of done

- Every test in the test plan exists and passes under `pytest` on Python 3.13, with no Claude Code session and no network.
- Every test names the REQ or NFR it checks, in its name or docstring (NFR-010).
- The whole suite is still green, and the code uses nothing Python 3.12 lacks (DEC-14).
- Tests are written before the code for this spec, in the same session.
- LOW tier: proceed to the next spec once the tests are green, then commit.
