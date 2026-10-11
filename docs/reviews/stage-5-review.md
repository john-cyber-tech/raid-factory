# Stage 5 review — Build (in progress)

**Status:** in progress · **Started:** 2026-10-11 · **Upstream:** `docs/specs/`, `docs/task-dag.md`
**Progress:** 3 of 25 specs committed (SPEC-EPIC-1-01, SPEC-EPIC-5-01, SPEC-EPIC-5-04). Next: SPEC-EPIC-5-05.

## Spec → tests → result

| Spec | Tier | Tests | Result | Acceptance criteria covered |
|---|---|---|---|---|
| SPEC-EPIC-1-01 | HIGH | 12 in `tests/test_spec_epic_1_01.py` (the 11 in the test plan plus `test_real_entry_point_exit_codes`, added at gate 1 by the owner) | 12 passed on Python 3.13.9 | Story EPIC-1-01 criteria 1 to 8, CF-5 |
| SPEC-EPIC-5-01 | HIGH | 7 in `tests/test_spec_epic_5_01.py`, 40 cases with parametrisation (4 failure steps, 27 command sequences, 5 damaged logs) | 40 passed; whole suite 52 passed | Story EPIC-5-01 criteria 1 to 4, CF-1 |
| SPEC-EPIC-5-04 | MEDIUM | 7 in `tests/test_boundaries.py`, 28 cases with parametrisation (22 planted imports and shell calls): the 6 in the test plan plus `test_outside_watch_catches_a_planted_write` | 28 passed; whole suite 80 passed | Story EPIC-5-04 criteria 1 to 4 |

Gate 1 for SPEC-EPIC-1-01: tests approved by the owner on 2026-10-11. Before any code existed the run was 10 failed, 2 passed, 12 collected with no collection error; 9 failed on `No module named 'raid'` and the entry-point test on the missing `pyproject.toml`.

Gate 1 for SPEC-EPIC-5-01: tests approved by the owner on 2026-10-11 with changes (shared helpers moved to `tests/helpers.py`, a zero-byte log case, each failure test asserts its injected failure fired). Before the code existed the run was 11 failed, 40 passed, 51 collected with no collection error; the zero-byte case then made it 52.

SPEC-EPIC-5-04 (MEDIUM): tests written first. Before the fixtures and the import check existed the run was 13 failed, 2 errors, 2 passed, 69 collected with no collection error. The two that passed (`test_commands_work_without_api_keys`, `test_only_declared_dependency_is_jsonschema`) check behaviour that SPEC-EPIC-1-01 already has. The owner approved the diff on 2026-10-11 with changes: the socket block records every attempt and fails the test at its end if any is on record; the import check also refuses `asyncio`, `ssl`, `smtplib`, `ftplib`, `urllib3`, `aiohttp` and `openai`, and calls to `os.system` and `os.popen`, each with a planted case that failed before the check was extended.

## Open spec gaps

| # | Spec | Gap | What the code does meanwhile | What you need to do |
|---|---|---|---|---|
| G-01 | SPEC-EPIC-1-01, REQ-014 | Nothing says how an empty owner or an empty due date is displayed in `raid list` or in the review screen | Prints `-`. No test pins this | Confirm `-`, or say what to show |
| G-02 | SPEC-EPIC-1-01, REQ-014 | Nothing says what `raid list` prints when the log has no items | Prints the header line with no rows, exit 0. No test pins this | Confirm, or give a message to print |
| G-03 | SPEC-EPIC-5-01, NFR-003, architecture section 8 | Two gaps around a save that fails. (a) **Duplicate on retry:** if the log is saved but trimming `pending.json` then fails, the proposal is shown again next time. Architecture section 8 relies on the duplicate finder to show the item it already became, but that is SPEC-EPIC-3-03 (build order 20); until then, accepting it again creates a second item with a new ID. (b) **Exit code of a failed save:** the spec says what the CLI does when a load fails (message, exit 1) but not when a save fails with a disk error | (a) Nothing prevents the second accept; the test checks only that the log is complete and the proposal is still pending. (b) The disk error is not caught: Python prints its error trace and the shell sees a non-zero exit. A save refused by the guard is caught: message, exit 1 | (a) Accept until SPEC-EPIC-3-03, or ask for a check in review now. (b) Say whether a failed save should print a plain message and exit 1 |
| G-04 | SPEC-EPIC-5-01, SPEC-EPIC-1-01, REQ-006 | No spec, requirement or ADR says whether error messages go to standard output or standard error. SPEC-EPIC-1-01's `main(argv, *, today, stdin, stdout, project_dir)` has no error stream | Every message, including the damaged-log one, is printed to the `stdout` passed to `main`; the tests read it there | Confirm, or ask for a `stderr` parameter (a change to SPEC-EPIC-1-01's signature) |
| G-05 | SPEC-EPIC-5-01, REQ-011, ADR-001 | The loader checks that each type's counter is a whole number of 1 or more, but not that it is higher than the highest existing ID of that type. A hand-edited log with R-003 and a Risk counter of 2 loads as valid | The next accepted Risk would get R-002 or, once the counter reaches it, a second R-003: two items with one ID. The save guard does not catch this, because no ID disappears. No test covers it | Say whether such a log should be refused on load as damaged (my suggestion), or leave it as part of limitation L-3 (hand edits are not protected against) |

## Choices pinned by tests, approved at gate 1

| # | Choice | Why it needed deciding |
|---|---|---|
| T-1 | `raid-log.json` has an `items` list; each item has `id`, `type`, `title`, `status` | The spec and ADR-001 say "list of items" but name no keys |
| T-2 | `main(...)` returns the exit code as an integer; the console command passes it to the shell | The spec gives the signature but not the return |
| T-3 | The no-proposals message contains "nothing to review" | Story criterion 7 gives the meaning, not the words |
| T-4 | `raid list` prints a header naming the seven columns, then one line per item starting with its ID | REQ-014 lists the columns, not the layout |
| T-5 | After a full review `pending.json` may be a file with an empty list or absent; the code leaves a file with an empty list | The spec says only "has no proposals" |
| T-6 | The save's three steps go through `os.write`, `os.fsync` and `os.replace` | That is where the tests inject failures |
| T-7 | The temporary file is `raid-log.json.tmp`, a fixed name, gone after a successful save | The spec says a leftover is "overwritten by the next save", which needs a known name |
| T-8 | After a failed log save during review the proposal stays in `pending.json` and the log is byte-identical | Follows from NFR-003; the spec does not state it |
| T-9 | A fourth failure case, `pending`: the log is saved, trimming `pending.json` fails, the log holds the new item and the proposal is still pending | The only case that reaches the "after" state (architecture section 8) |
| T-10 | Damaged-log cases: zero bytes, `{not json`, `[]`, no `items`, `items` not a list. The message names `raid-log.json` and no file is created or changed | The spec's test names only `{not json`; its capability says "or not a valid log" |
| T-11 | A save refused by the guard names the ID it would lose | The spec says "refused with an error" |

## Notes for later specs

| # | Spec | Note |
|---|---|---|
| N-01 | SPEC-EPIC-1-01, SPEC-EPIC-1-04 | Items already store their excerpt and date in a `sources` list (`excerpt`, `date`), following architecture section 5, because an accepted item has to keep them somewhere. SPEC-EPIC-1-04 is where that list is formally specified; it adds the rules (a source is required, the first can never be emptied) and their tests. No SPEC-EPIC-1-01 test reads `sources` |
| N-03 | SPEC-EPIC-5-01 | The temporary-file-then-replace routine is `src/raid/atomic.py`, used by the store's `_save()` for the log and by the review flow for `pending.json`. It is the one place in `src/` that opens a file for writing. A valid log is: an object with `schema_version` 1, a `next_number` counter of 1 or more for each of the four types, and an `items` list whose entries each have an `id`. Later specs that add fields should extend this check. This covers the structure of `raid-log.json` only; it is not the validation of proposals in `pending.json`, which is SPEC-EPIC-1-02 |
| N-04 | SPEC-EPIC-5-01, ADR-001 | The save syncs the temporary file's content to disk and then replaces the log, as the spec and ADR-001 describe. It does not sync the folder after the replace. After a power loss the log is still either the complete old or the complete new file, but the very last save may not have reached the disk even though the command reported success. A process crash is not affected |
| N-05 | SPEC-EPIC-5-01 | The message for a zero-byte or unparseable log carries the JSON parser's wording, for example "Expecting value: line 1 column 1 (char 0)". This is cosmetic: the file is named, the exit code is 1 and nothing is written. Plain wording could be added without changing behaviour |
| N-06 | SPEC-EPIC-5-04 | Three limits of the safety net. The socket block works inside the test process only, so the one test that starts a child process (`test_real_entry_point_exit_codes`) is not covered by it. The import check reads `import` statements and direct `os.system` / `os.popen` calls; it would not see a module loaded by name at run time, or `os` used under another name. It refuses every `subprocess` import in `src/`, which is stricter than the spec's "`subprocess` used to start a model", because the tool has no other use for it |
| N-07 | SPEC-EPIC-5-04 | The import check lives in `tests/boundary_check.py`, beside `tests/test_boundaries.py`, not inside it as the spec words it, so the tests can import it one at a time. The outside-write fixture also moves the home folder and the current folder inside the watched folder, so a stray write to either would be seen. New commands are added to `COMMANDS` in `tests/test_boundaries.py` |
| N-08 | SPEC-EPIC-5-04, NFR-006 | `outside_watch` sees only the watched parent folder, which holds the project folder, a sentinel file, the home folder and the current folder. A write to an absolute path elsewhere on the machine, for example a fixed path under `/tmp` or `/var`, would not be caught. What stands against that today is the grep of `src/` showing that `atomic.py` is the only code that writes a file, and that both its callers build the path from the project folder |
| N-02 | SPEC-EPIC-1-01, SPEC-EPIC-1-02 | `jsonschema` is declared and pinned (4.25.0) in `pyproject.toml` now, as SPEC-EPIC-1-01's capabilities ask, but nothing imports it until SPEC-EPIC-1-02 |

## Defects

None so far.

## Deviations from spec or ADR

None. One thing in SPEC-EPIC-1-01 is simple on purpose and replaced by a later spec, as its Non-goals say: `pending.json` is read without validation (SPEC-EPIC-1-02), so a malformed file currently ends in a Python error. The plain save from SPEC-EPIC-1-01 is gone (SPEC-EPIC-5-01).
