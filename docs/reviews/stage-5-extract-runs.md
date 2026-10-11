# Stage 5 — manual runs of `/raid-extract` (SPEC-EPIC-1-05)

**Status:** check steps approved at gate 1 (2026-10-11) · prompt written, awaiting gate 2 · no run recorded yet · **Upstream:** SPEC-EPIC-1-05, story EPIC-1-05, REQ-001 to REQ-004, REQ-039, REQ-040, DEC-07, DEC-08, DEC-21

Extraction runs in a Claude Code session, not in the Python tool, so these checks are made by a person. Each run is recorded here with its output file and a pass or fail per check. There is no pass threshold in v1 (DEC-21): a fail is recorded, not hidden, and the owner decides what to do about it.

## Rules for these runs

1. The prompt in `.claude/commands/raid-extract.md` was written without reading `inputs/expected/` or `inputs/meeting-notes/`. What a run "should" find below comes only from story EPIC-1-05's acceptance criteria.
2. A run uses a fresh folder outside the repository, holding only what the step says, so the command cannot see tests, fixtures or the answer key.
3. The output of each run is copied unchanged to `tests/fixtures/extract_runs/<run>/pending.json`. It is never edited to make a check pass.
4. Found and missed items are compared with `inputs/expected/answer-key.md` only after the owner has approved the prompt at gate 2, and the result is reported here (DEC-21).
5. Each run records the date, the model named by the session, and who ran it.

## Setup, once

```
mkdir -p ~/raid-extract-check/.claude/commands && cd ~/raid-extract-check
cp <repo>/.claude/commands/raid-extract.md .claude/commands/
cp <repo>/inputs/sample-meeting-notes.md notes.md
cp <repo>/tests/fixtures/notes/sample_with_year.md notes-with-year.md
cp <repo>/tests/fixtures/pending/valid_three.json pending.json
printf 'a\nSean Murphy\na\na\n' | raid review        # a log holding 3 items
shasum -a 256 raid-log.json > log-before.sha
```

## Checks

| Check | Criterion | Steps | Pass when |
|---|---|---|---|
| MANUAL-extract-writes-pending-only | 1 | In the folder above, with the 3-item log, run `/raid-extract notes.md`. Then `shasum -a 256 -c log-before.sha` and `ls -A` | `pending.json` exists and is new; the checksum line says OK; no file other than `pending.json` was created or changed. REQ-001, REQ-002 |
| MANUAL-extract-output-validates | 2 | `raid review`, then end the input at the first question (Ctrl-D) | Proposal 1 is shown with its excerpt; no validation message; exit code 1 only because input ended. REQ-003 |
| MANUAL-extract-five-items-typed | 3 | Read `pending.json` | Five proposals, one for each of: security review not started (Risk); legacy ERP export assumed to be CSV (Assumption); test environment down since Monday (Issue); cutover waiting on Acme finance's year-end close (Dependency); key analyst on leave in November (Risk). Record any extra or missing proposal. REQ-001, REQ-004 |
| MANUAL-extract-owner-and-due | 4 | Read the test-environment and CSV-export proposals | Test environment: `owner` is "Priya", `due_date` is null. CSV export: `owner` is null. REQ-003 |
| MANUAL-extract-repeat-proposed-once | 5 | Count proposals about the security review | Exactly one, although the notes mention it on two lines. Record which line its excerpt uses. DEC-07 |
| MANUAL-extract-year-rule | 6, 7 | (a) In the sample output, read every `due_date` and `source_date`. (b) Remove `pending.json`, run `/raid-extract notes-with-year.md`, read the same fields | (a) Every `due_date` and every `source_date` is null. (b) Year-end close has `due_date` 2026-10-25, and every `source_date` is 2026-10-07. REQ-039 |
| MANUAL-extract-source-date-asked | 8 | With the sample output, `raid review` and answer `a` at the first proposal | "Date of the notes (YYYY-MM-DD):" is asked before anything enters the log. REQ-040 |
| MANUAL-extract-plain-line-breaks | 9, G-12 | `grep -c $'\r' pending.json` on each output | 0. The command writes plain line breaks |
| MANUAL-extract-empty-notes | 2, edge | A notes file holding only "Thanks all, nothing to report this week." Run the command, then `raid review` | `pending.json` is `{"proposals": []}` or equivalent; `raid review` says "Nothing to review." |
| MANUAL-extract-missing-notes-file | 1, failure | Remove `pending.json`. Run `/raid-extract no-such-file.md` | The session says the file does not exist; no `pending.json` is written; the log checksum is unchanged |

## Three runs of each key extraction

By the owner's decision (2026-10-11) the owner runs these checks, in a fresh folder, and each of the two key extractions is run **three times**: `/raid-extract notes.md` (runs sample_1 to sample_3) and `/raid-extract notes-with-year.md` (runs sample_with_year_1 to sample_with_year_3). Start each run in a new Claude Code session, remove `pending.json` first, and apply every check in the table to every run. Every run is recorded, including one that fails a check. The two edge checks (empty notes, missing notes file) are run once each unless the owner chooses more.

After each run, copy its `pending.json` unchanged:

```
mkdir -p <repo>/tests/fixtures/extract_runs/sample_1 && cp pending.json <repo>/tests/fixtures/extract_runs/sample_1/
```

and so on for `sample_2`, `sample_3`, `sample_with_year_1`, `sample_with_year_2`, `sample_with_year_3`. Then, from the repository:

```
python3 tests/check_extract_output.py tests/fixtures/extract_runs/sample_1/pending.json inputs/sample-meeting-notes.md
python3 tests/check_extract_output.py tests/fixtures/extract_runs/sample_with_year_1/pending.json tests/fixtures/notes/sample_with_year.md
```

Each must print the number of proposals and exit 0: all fields present, titles at most 80 characters, every excerpt word for word in the notes (criterion 9). `pytest` runs the same check on all six as `test_recorded_runs_pass_the_output_check`; until all six files are saved those six cases fail, and SPEC-EPIC-1-05 is not committed.

## Recorded runs

| Run | Date | Model | Run by | Output file | Proposals | Result |
|---|---|---|---|---|---|---|
| sample_1 | not run | | | `tests/fixtures/extract_runs/sample_1/pending.json` | | |
| sample_2 | not run | | | `tests/fixtures/extract_runs/sample_2/pending.json` | | |
| sample_3 | not run | | | `tests/fixtures/extract_runs/sample_3/pending.json` | | |
| sample_with_year_1 | not run | | | `tests/fixtures/extract_runs/sample_with_year_1/pending.json` | | |
| sample_with_year_2 | not run | | | `tests/fixtures/extract_runs/sample_with_year_2/pending.json` | | |
| sample_with_year_3 | not run | | | `tests/fixtures/extract_runs/sample_with_year_3/pending.json` | | |
| empty notes | not run | | | not kept | | |
| missing notes file | not run | | | none expected | | |

## Results per check

Give a result for each run the check applies to, for example "3 of 3" or "2 of 3, sample_2 proposed the security review twice".

| Check | Result | What was seen |
|---|---|---|
| MANUAL-extract-writes-pending-only | not run | |
| MANUAL-extract-output-validates | not run | |
| MANUAL-extract-five-items-typed | not run | |
| MANUAL-extract-owner-and-due | not run | |
| MANUAL-extract-repeat-proposed-once | not run | |
| MANUAL-extract-year-rule | not run | |
| MANUAL-extract-source-date-asked | not run | |
| MANUAL-extract-plain-line-breaks | not run | |
| MANUAL-extract-empty-notes | not run | |
| MANUAL-extract-missing-notes-file | not run | |

## Found and missed against the answer key (DEC-21)

Not done. To be filled in after gate 2, by reading `inputs/expected/answer-key.md` for the first time then.
