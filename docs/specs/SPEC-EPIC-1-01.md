# SPEC-EPIC-1-01 — Review fixture proposals into the log and list them (thin slice)

**Story:** EPIC-1-01 · **Covers:** REQ-007, REQ-008, REQ-010, REQ-011, REQ-014, NFR-010 · **Components:** COMP-03, COMP-04, COMP-05
**Build order:** 1 of 25 · **Risk tier:** HIGH (First code that writes `raid-log.json` and rewrites `pending.json`.) · **Depends on:** nothing

## Why

As a delivery manager, I want to accept or reject each proposed item and then see the accepted ones in my project's log, so that nothing enters the log without my decision.

The delivery manager must decide every item that enters the log (NEED-02) and see the result. This is the thin slice every other spec builds on.

## Capabilities

- `pyproject.toml`: package `raid`, `requires-python >= 3.12`, console command `raid`, dependencies `jsonschema` (pinned) and `pytest` for tests.
- `src/raid/cli.py`: `main(argv, *, today, stdin, stdout, project_dir)` with sub-commands `review` and `list`; the real entry point passes the system date and the current folder. Exit code 0 on success, 1 on a refused or failed action.
- `src/raid/review.py`: read `pending.json` from the project folder; for each proposal print its fields and source excerpt, then read one answer: `a` accept or `r` reject. Any other answer repeats the question.
- `src/raid/store.py`: `load()`, `add_item()`, `all()`. `add_item` gives the next ID for the type from a per-type counter kept in the file (R-001, A-001, I-001, D-001). New items have status Open.
- After each decision, remove that proposal from `pending.json`. A rejected proposal is written nowhere.
- `raid list`: one row per item with ID, type, title, owner, severity, due date, status.

## Constraints

- Only `store.py` writes `raid-log.json` (ADR-001).
- Nothing reaches the log except by an explicit accept (ADR-002, REQ-008).
- Decided proposals are removed from `pending.json`; rejections are not recorded (DEC-10).
- The project folder is the folder the command runs in; one log per folder (REQ-010, NFR-006).
- The clock is passed in from the CLI so tests fix the date (NFR-010).

## Non-goals

- Schema validation (SPEC-EPIC-1-02).
- Editing a proposal (SPEC-EPIC-1-03).
- Asking for a missing source date (SPEC-EPIC-1-04).
- Atomic save and history (SPEC-EPIC-5-01, SPEC-EPIC-5-02): this spec may save simply; the next two specs replace the save routine.

## Success signal

Running `raid review` on the three-proposal fixture with answers accept, reject, accept leaves a log with exactly R-001 and D-001, an empty `pending.json`, and `raid list` prints those two rows.

## Test plan

The Criteria column gives the story's acceptance criterion numbers; CF-n is an item carried forward from the stage 3 review.

| Test | Criteria | Checks |
|---|---|---|
| `test_review_accept_reject_accept` | 1 | Log holds exactly R-001 (P1 title) and D-001 (P3 title); no I- item. REQ-007, REQ-008. |
| `test_review_shows_excerpt_and_waits` | 2 | Output contains each excerpt; an answer of `x` repeats the question for the same proposal. REQ-007. |
| `test_pending_emptied_and_rejection_not_recorded` | 3 | `pending.json` has no proposals; P2's title appears in no file in the folder. DEC-10. |
| `test_list_shows_seven_columns` | 4 | Two rows; each has ID, type, title, owner, severity, due date, status. REQ-014. |
| `test_ids_are_sequential_per_type` | 5 | A second accepted Risk is R-002; R-001 unchanged. REQ-011. |
| `test_projects_are_independent` | 6 | Accepting in folder A leaves folder B's log byte-identical. REQ-010. |
| `test_no_pending_file` | 7 | Message says nothing to review; exit code 0; log unchanged. |
| `test_empty_proposals_list` | 7 | Edge: `pending.json` with zero proposals behaves the same as no file. |
| `test_input_ends_mid_review` | 2 | Failure path: input ends after the first answer; the first decision is kept, the other two proposals stay in `pending.json`, exit 1. |
| `test_suite_runs_from_fixtures` | 8 | The suite passes with no Claude Code session; a helper asserts every test in this file cites a REQ. NFR-010. |
| `test_thin_slice_fixture_has_source_dates` | CF-5 | Every proposal in `valid_three.json` carries `source_date`, so later specs do not break this fixture. |

**Test data:** `tests/fixtures/pending/valid_three.json`: P1 Risk "Client security review may delay cutover" (owner empty, High), P2 Issue "Test environment down" (owner "Priya", High), P3 Dependency "Acme finance year-end close" (owner empty, Medium, due 2026-10-25); each with its excerpt from `inputs/sample-meeting-notes.md` and `source_date` 2026-10-07. All data is fictional.

## Definition of done

- Every test in the test plan exists and passes under `pytest` on Python 3.13, with no Claude Code session and no network.
- Every test names the REQ or NFR it checks, in its name or docstring (NFR-010).
- The whole suite is still green, and the code uses nothing Python 3.12 lacks (DEC-14).
- `raid review` and `raid list` run from a shell in an empty folder.
- HIGH tier, gate 1: write this spec's tests and test data first, and show them to the owner for approval before writing any implementation code. For manual checks, show the fixtures and the written check steps. The tests must fail for the right reason before the code exists.
- HIGH tier, gate 2: stop for the owner's approval of the implementation before committing.
