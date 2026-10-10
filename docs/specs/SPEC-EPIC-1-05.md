# SPEC-EPIC-1-05 — `/raid-extract` writes proposals from a notes file

**Story:** EPIC-1-05 · **Covers:** REQ-001, REQ-002, REQ-003, REQ-004, REQ-039 · **Components:** COMP-01, COMP-02
**Build order:** 9 of 25 · **Risk tier:** HIGH (Writes the extraction command prompt and fixes the contract.) · **Depends on:** SPEC-EPIC-1-02, SPEC-EPIC-1-04

## Why

As a delivery manager, I want to run one command on my call notes and get a list of candidate RAID items, so that I stop missing things I meant to write down.

The manager misses about one item in five when writing notes up from memory (NEED-01). This spec gives him candidates to review and defines the only hand-off between the model and the tool.

## Capabilities

- `.claude/commands/raid-extract.md`: a Claude Code command taking one argument, the notes file path. It reads that file and writes a complete `pending.json` in the current folder, following the contract below.
- The prompt gives the definitions: Risk = might happen; Issue = has already happened; Assumption = taken as true without confirmation; Dependency = waiting on someone or something.
- Owner and due date are `null` unless the notes state them. Dates without a year take the year of the notes' own date; if the notes give no year anywhere, the date is `null`.
- `source_date` is set only when the notes state their date in full with a year.
- An item the notes raise more than once is proposed once, using the fuller statement as the excerpt.
- The excerpt is copied word for word; the title is at most 80 characters.

## Constraints

- The command never reads or writes `raid-log.json` (ADR-002, REQ-002).
- Its allowed tools are limited to reading the notes file and writing `pending.json` (DEC-19, REQ-042).
- Output must satisfy the contract; the CLI rejects anything else (ADR-004).
- Repeated items once, year rule, source-date rule (DEC-07, DEC-08).
- No extraction quality threshold is set for v1; found and missed items are reported against the answer key in stage 5 (OQ-18).

## Non-goals

- Duplicate detection against the log (ADR-003 keeps the command away from the log).
- Calling the command from the CLI (ADR-002).
- Resisting instructions hidden in notes (SPEC-EPIC-1-06).

## The `pending.json` contract

This section is the single definition of a valid `pending.json`. `src/raid/schemas/pending.schema.json` (built in SPEC-EPIC-1-02) encodes it exactly, and the command is told to follow it.

The file is one JSON object with exactly one key, `proposals`, a list. Each proposal is an object with exactly these keys:

| Key | Required | Allowed value |
|---|---|---|
| `type` | yes | `Risk`, `Assumption`, `Issue` or `Dependency` |
| `title` | yes | Text, 1 to 80 characters, one line |
| `description` | yes | Text, may be empty |
| `owner` | yes | Text, or `null` when the notes name nobody |
| `severity` | yes | `High`, `Medium` or `Low` |
| `due_date` | yes | `YYYY-MM-DD`, or `null` when the notes give no full date |
| `source_excerpt` | yes | Text, not empty, copied word for word from the notes |
| `source_date` | no | `YYYY-MM-DD`, or `null`, or absent. Set only when the notes state their date in full with a year |

No other keys are allowed at either level. Text may not contain control characters, except that `description` and `source_excerpt` may contain line breaks and tabs. Dates must be real calendar dates.

## Success signal

Running `/raid-extract inputs/sample-meeting-notes.md` produces a `pending.json` that `raid review` accepts as valid and that contains the five expected proposals with the expected types.

## Test plan

The Criteria column gives the story's acceptance criterion numbers; CF-n is an item carried forward from the stage 3 review.

| Test | Criteria | Checks |
|---|---|---|
| `MANUAL-extract-writes-pending-only` | 1 | Run on the sample notes beside a 3-item log; `pending.json` written; log checksum unchanged. REQ-001, REQ-002. |
| `MANUAL-extract-output-validates` | 2 | `raid review` shows the first proposal. REQ-003. |
| `MANUAL-extract-five-items-typed` | 3 | Five proposals with types Risk, Assumption, Issue, Dependency, Risk. REQ-001, REQ-004. |
| `MANUAL-extract-owner-and-due` | 4 | Test-environment owner "Priya", due empty; CSV-export owner empty. REQ-003. |
| `MANUAL-extract-repeat-proposed-once` | 5 | Exactly one security-review proposal. DEC-07. |
| `MANUAL-extract-year-rule` | 6, 7 | Sample notes: due dates and source dates empty. Copy headed "7 Oct 2026": year-end close due 2026-10-25, source dates 2026-10-07. REQ-039. |
| `MANUAL-extract-source-date-asked` | 8 | Accepting the first proposal from the sample notes asks for the source date. REQ-040. |
| `test_extract_output_check` | 9 | Automated helper `tests/check_extract_output.py`, run on a saved `pending.json` and its notes file: seven fields present, titles at most 80 characters, each excerpt found word for word in the notes. |
| `test_command_file_names_contract_fields` | 2 | Automated: the command file mentions every key in the schema, so prompt and contract cannot drift. |
| `MANUAL-extract-empty-notes` | 2 | Edge: notes with no RAID content give a valid file with an empty `proposals` list. |
| `MANUAL-extract-missing-notes-file` | 1 | Failure path: a path that does not exist; the command says so and writes no `pending.json`. |

**Test data:** `inputs/sample-meeting-notes.md` and `tests/fixtures/notes/sample_with_year.md` (the same notes headed "7 Oct 2026"). The manual runs are recorded in `docs/reviews/stage-5-extract-runs.md` with the output file and a pass or fail per check. `inputs/expected/` is not read when writing the prompt.

## Definition of done

- Every test in the test plan exists and passes under `pytest` on Python 3.13, with no Claude Code session and no network.
- Every test names the REQ or NFR it checks, in its name or docstring (NFR-010).
- The whole suite is still green, and the code uses nothing Python 3.12 lacks (DEC-14).
- Each MANUAL check has a recorded run with its result.
- The owner has seen the command prompt before it is committed (HIGH tier).
- HIGH tier, gate 1: write this spec's tests and test data first, and show them to the owner for approval before writing any implementation code. For manual checks, show the fixtures and the written check steps. The tests must fail for the right reason before the code exists.
- HIGH tier, gate 2: stop for the owner's approval of the implementation before committing.
