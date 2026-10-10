# SPEC-EPIC-2-02 — Update an item

**Story:** EPIC-2-02 · **Covers:** REQ-011, REQ-016, REQ-041, NFR-008 · **Components:** COMP-03, COMP-05
**Build order:** 12 of 25 · **Risk tier:** LOW (Uses the store's existing update path and the shared field rules.) · **Depends on:** SPEC-EPIC-5-02

## Why

As a project manager, I want to update my items in a few seconds each, so that keeping the log current costs me under five minutes a week.

The project manager must keep her items current in under five minutes a week (NEED-10, NEED-14).

## Capabilities

- `cli.py`: `raid update <ID>` with options `--title`, `--description`, `--owner`, `--severity`, `--due`. Several options may be given at once.
- `store.py`: `update_item(id, changes)` checks every change with `rules.py` first; if any is invalid nothing is changed.
- There is no option to change the type; asking for it is refused with "a type cannot change after acceptance; close this item and raise a new one".
- `--owner ""` and `--due ""` clear the value.

## Constraints

- A type cannot change after acceptance (DEC-15, REQ-011).
- Titles are at most 80 characters (DEC-09, REQ-041).
- Every accepted change adds exactly one history entry per field; a refused change adds none (ADR-006, REQ-020).
- Single user: updates are made on the machine that holds the log (DEC-13).

## Non-goals

- Status changes and closing (SPEC-EPIC-2-03).
- Check note, waiting-on and decision mark (SPEC-EPIC-2-05, SPEC-EPIC-2-07).
- Bulk updates.

## Success signal

`raid update R-001 --due 2026-10-23` makes `raid list` show the new date, keeps the ID, and adds one history entry.

## Test plan

The Criteria column gives the story's acceptance criterion numbers; CF-n is an item carried forward from the stage 3 review.

| Test | Criteria | Checks |
|---|---|---|
| `test_update_due_date` | 1 | List shows 2026-10-23; ID unchanged. REQ-016. |
| `test_update_each_field_adds_one_entry` | 2 | Title, description, owner, severity: stored, listed, one entry each. REQ-016. |
| `test_update_unknown_id` | 3 | R-099: exit 1, message, log unchanged. REQ-016. |
| `test_update_bad_date_refused` | 4 | `2026-13-40` refused; stored date unchanged. REQ-016. |
| `test_update_type_refused` | 5 | Refused with the type message; R-001 unchanged. REQ-011. |
| `test_update_title_81_refused` | 6 | Refused stating the limit. REQ-041. |
| `test_update_two_fields_one_invalid_changes_nothing` | 4 | Edge: valid owner plus invalid date: neither is applied, no history entry. |
| `test_update_clears_owner` | 2 | Edge: `--owner ""` empties the owner and records it. |
| `MANUAL-weekly-update-walkthrough` | 7 | Timed at the stage 6 demo: list own items and update 4 of 10 in under 5 minutes. NFR-008. |

**Test data:** A log of 10 items, 4 owned by "Priya Nair", built by a test helper.

## Definition of done

- Every test in the test plan exists and passes under `pytest` on Python 3.13, with no Claude Code session and no network.
- Every test names the REQ or NFR it checks, in its name or docstring (NFR-010).
- The whole suite is still green, and the code uses nothing Python 3.12 lacks (DEC-14).
- Tests are written before the code for this spec, in the same session.
- LOW tier: proceed to the next spec once the tests are green, then commit.
