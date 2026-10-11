# Stage 5 review — Build (in progress)

**Status:** in progress · **Started:** 2026-10-11 · **Upstream:** `docs/specs/`, `docs/task-dag.md`
**Progress:** 1 of 25 specs built and committed (SPEC-EPIC-1-01, gate 2 approved 2026-10-11). Next: SPEC-EPIC-5-01.

## Spec → tests → result

| Spec | Tier | Tests | Result | Acceptance criteria covered |
|---|---|---|---|---|
| SPEC-EPIC-1-01 | HIGH | 12 in `tests/test_spec_epic_1_01.py` (the 11 in the test plan plus `test_real_entry_point_exit_codes`, added at gate 1 by the owner) | 12 passed on Python 3.13.9 | Story EPIC-1-01 criteria 1 to 8, CF-5 |

Gate 1 for SPEC-EPIC-1-01: tests approved by the owner on 2026-10-11. Before any code existed the run was 10 failed, 2 passed, 12 collected with no collection error; 9 failed on `No module named 'raid'` and the entry-point test on the missing `pyproject.toml`.

## Open spec gaps

| # | Spec | Gap | What the code does meanwhile | What you need to do |
|---|---|---|---|---|
| G-01 | SPEC-EPIC-1-01, REQ-014 | Nothing says how an empty owner or an empty due date is displayed in `raid list` or in the review screen | Prints `-`. No test pins this | Confirm `-`, or say what to show |
| G-02 | SPEC-EPIC-1-01, REQ-014 | Nothing says what `raid list` prints when the log has no items | Prints the header line with no rows, exit 0. No test pins this | Confirm, or give a message to print |

## Choices pinned by tests, approved at gate 1

| # | Choice | Why it needed deciding |
|---|---|---|
| T-1 | `raid-log.json` has an `items` list; each item has `id`, `type`, `title`, `status` | The spec and ADR-001 say "list of items" but name no keys |
| T-2 | `main(...)` returns the exit code as an integer; the console command passes it to the shell | The spec gives the signature but not the return |
| T-3 | The no-proposals message contains "nothing to review" | Story criterion 7 gives the meaning, not the words |
| T-4 | `raid list` prints a header naming the seven columns, then one line per item starting with its ID | REQ-014 lists the columns, not the layout |
| T-5 | After a full review `pending.json` may be a file with an empty list or absent; the code leaves a file with an empty list | The spec says only "has no proposals" |

## Notes for later specs

| # | Spec | Note |
|---|---|---|
| N-01 | SPEC-EPIC-1-01, SPEC-EPIC-1-04 | Items already store their excerpt and date in a `sources` list (`excerpt`, `date`), following architecture section 5, because an accepted item has to keep them somewhere. SPEC-EPIC-1-04 is where that list is formally specified; it adds the rules (a source is required, the first can never be emptied) and their tests. No SPEC-EPIC-1-01 test reads `sources` |
| N-02 | SPEC-EPIC-1-01, SPEC-EPIC-1-02 | `jsonschema` is declared and pinned (4.25.0) in `pyproject.toml` now, as SPEC-EPIC-1-01's capabilities ask, but nothing imports it until SPEC-EPIC-1-02 |

## Defects

None so far.

## Deviations from spec or ADR

None. Two things in SPEC-EPIC-1-01 are simple on purpose and replaced by later specs, as its Non-goals say: the save is a plain write (SPEC-EPIC-5-01 makes it atomic), and `pending.json` is read without validation (SPEC-EPIC-1-02), so a malformed file currently ends in a Python error.
