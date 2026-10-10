# SPEC-EPIC-1-02 — Reject invalid extraction output

**Story:** EPIC-1-02 · **Covers:** REQ-005, REQ-006, REQ-041 · **Components:** COMP-02, COMP-04
**Build order:** 6 of 25 · **Risk tier:** HIGH (The trust boundary: what the tool accepts from model output.) · **Depends on:** SPEC-EPIC-1-01

## Why

As a delivery manager, I want a broken `pending.json` refused with a clear message, so that bad extraction output can never reach my log.

Bad extraction output must never reach the log, and the manager must be told what is wrong (NEED-15).

## Capabilities

- `src/raid/schemas/pending.schema.json`: the contract defined in SPEC-EPIC-1-05, in JSON Schema, with no external references.
- `src/raid/validator.py`: `validate(path)` parses the file, checks it against the schema with `jsonschema`, then checks that dates are real calendar dates. Returns the proposals or a list of errors.
- Each error names the file, the proposal number (first is 1), the field and the reason in plain words, for example "proposal 2: title is 81 characters; the limit is 80".
- `review.py` calls `validate` first. On any error it prints every error, exits 1, and shows no proposal.

## Constraints

- `pending.schema.json` is the single definition of valid; no check elsewhere may contradict it (ADR-004).
- The whole file is rejected on any failure (A-2, REQ-005).
- Extra keys and control characters are rejected (ADR-002, NFR-005).
- Titles are at most 80 characters (DEC-09, REQ-041).
- `jsonschema` runs offline; the schema has no external references (ADR-004, NFR-004).

## Non-goals

- Repairing or partly accepting a bad file.
- Checking that an excerpt really appears in the notes (the CLI does not read notes).

## Success signal

Each invalid fixture makes `raid review` exit 1 with a message naming the proposal and field, shows no proposal, and leaves the log byte-identical.

## Test plan

The Criteria column gives the story's acceptance criterion numbers; CF-n is an item carried forward from the stage 3 review.

| Test | Criteria | Checks |
|---|---|---|
| `test_not_json_is_rejected` | 1 | Message names `pending.json` and the parse error; exit 1; log unchanged. REQ-006. |
| `test_missing_title_is_rejected` | 2 | Message names `title` and proposal 1. REQ-006. |
| `test_bad_type_is_rejected` | 3 | Message names `type` and lists the four allowed values. REQ-006. |
| `test_one_bad_proposal_rejects_all` | 4 | Second proposal invalid: nothing is shown for a decision. REQ-005. |
| `test_title_81_rejected_80_accepted` | 5 | 81 characters: rejected naming `title` and 80. Exactly 80: valid. REQ-041. |
| `test_extra_field_is_rejected` | CF-2 | A proposal with an extra key `accepted: true` is rejected naming the key. NFR-005. |
| `test_control_characters_are_rejected` | CF-2 | A title containing an escape character is rejected naming `title`. NFR-005. |
| `test_impossible_date_is_rejected` | 2 | Edge: `due_date` of `2026-13-40` is rejected naming `due_date`. |
| `test_partly_written_file_is_rejected` | 1 | Edge: a file cut off mid-object is reported as a parse error. |
| `test_valid_fixture_passes` | 4 | `valid_three.json` validates and the first proposal is shown. |
| `test_every_error_is_listed` | 2 | Edge: a file with two bad proposals lists both. |

**Test data:** `tests/fixtures/pending/`: `not_json.json`, `missing_title.json`, `bad_type.json` (type `Question`), `second_invalid.json`, `title_81.json`, `title_80.json`, `extra_field.json`, `control_char.json`, `bad_date.json`, `truncated.json`.

## Definition of done

- Every test in the test plan exists and passes under `pytest` on Python 3.13, with no Claude Code session and no network.
- Every test names the REQ or NFR it checks, in its name or docstring (NFR-010).
- The whole suite is still green, and the code uses nothing Python 3.12 lacks (DEC-14).
- The schema file and the contract table in SPEC-EPIC-1-05 agree key for key; a test loads the schema and compares the key list.
- HIGH tier, gate 1: write this spec's tests and test data first, and show them to the owner for approval before writing any implementation code. For manual checks, show the fixtures and the written check steps. The tests must fail for the right reason before the code exists.
- HIGH tier, gate 2: stop for the owner's approval of the implementation before committing.
