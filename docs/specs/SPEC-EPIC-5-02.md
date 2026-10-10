# SPEC-EPIC-5-02 — Every change to an item is recorded in an append-only history

**Story:** EPIC-5-02 · **Covers:** REQ-020, NFR-007 · **Components:** COMP-05
**Build order:** 5 of 25 · **Risk tier:** HIGH (Extends the save guard and changes the shape of every stored item.) · **Depends on:** SPEC-EPIC-1-01, SPEC-EPIC-5-01, SPEC-EPIC-5-05

## Why

As a project manager, I want each item to carry a record of when it was created and every change since, so that the client's PMO can audit the log.

The client's PMO needs who raised an item, when, and every change after that (NEED-12); stale flags and "new this week" read their dates from it.

## Capabilities

- `src/raid/store.py`: every item has a `history` list. `add_item` appends a `created` entry; `update_item` appends one entry per changed field with the old and new value.
- Each entry has a timestamp (local date and time), the user's name from `identity.current_user()`, and what changed.
- Validation happens before anything is appended, so a refused change leaves no entry.
- The save guard also refuses a save in which any existing history entry is different or missing.
- `created_on(item)` and `last_changed_on(item)` read the first and last entries; no separate date fields are stored.

## Constraints

- History is append-only and has no editing interface (ADR-006, NFR-007).
- Item and history are written in the same save (ADR-006, NFR-002).
- The name is the stored, unverified one (ADR-005, DEC-02).

## Non-goals

- Tamper-proofing against hand edits (limitation L-3).
- Showing history to the user (SPEC-EPIC-2-06).

## Success signal

Accepting a proposal and changing its owner yields exactly two history entries, the second naming the field, old value, new value, time and "Sean Murphy".

## Test plan

The Criteria column gives the story's acceptance criterion numbers; CF-n is an item carried forward from the stage 3 review.

| Test | Criteria | Checks |
|---|---|---|
| `test_creation_entry_has_time_and_name` | 1 | One entry of kind created, with a timestamp and "Sean Murphy". REQ-020. |
| `test_update_entry_records_old_and_new` | 2 | Second entry: field `owner`, old empty, new "Priya Nair", timestamp, name. REQ-020. |
| `test_existing_entries_never_change` | 3 | After each command built so far, earlier entries are byte-identical. NFR-007. |
| `test_refused_update_adds_no_entry` | 4 | An invalid value is refused and the history length is unchanged. REQ-020. |
| `test_save_guard_refuses_altered_history` | 3 | Failure path: a save with an edited or removed entry is refused; file unchanged. NFR-007. |
| `test_no_op_update_adds_no_entry` | 4 | Edge: setting a field to the value it already has adds no entry. |
| `test_created_and_last_changed_come_from_history` | 2 | `created_on` and `last_changed_on` equal the first and last entry dates. |

**Test data:** Timestamps fixed by passing the clock in; name "Sean Murphy".

## Definition of done

- Every test in the test plan exists and passes under `pytest` on Python 3.13, with no Claude Code session and no network.
- Every test names the REQ or NFR it checks, in its name or docstring (NFR-010).
- The whole suite is still green, and the code uses nothing Python 3.12 lacks (DEC-14).
- Items created by SPEC-EPIC-1-01's tests now carry a creation entry; those tests still pass.
- HIGH tier, gate 1: write this spec's tests and test data first, and show them to the owner for approval before writing any implementation code. For manual checks, show the fixtures and the written check steps. The tests must fail for the right reason before the code exists.
- HIGH tier, gate 2: stop for the owner's approval of the implementation before committing.
