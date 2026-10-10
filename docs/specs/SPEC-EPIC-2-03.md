# SPEC-EPIC-2-03 — Status, and closing an item with a reason

**Story:** EPIC-2-03 · **Covers:** REQ-016, REQ-017, REQ-018 · **Components:** COMP-03, COMP-05
**Build order:** 14 of 25 · **Risk tier:** MEDIUM (The rule that makes "closed" trustworthy.) · **Depends on:** SPEC-EPIC-2-02, SPEC-EPIC-2-06

## Why

As a project manager, I want each item to have a status and to give a reason when I close it, so that 'closed' in the log can be trusted.

"If your tool says something is closed and it isn't, that's worse than no tool" (NEED-15). Closing must be deliberate and explained (NEED-12).

## Capabilities

- `cli.py`: `raid update <ID> --status Open|Mitigating` and `raid close <ID> --reason "..."`.
- `store.py`: closing sets status Closed, closed date = today, and stores the reason; one history entry records it.
- `raid update <ID> --status Closed` is refused with a pointer to `raid close`.
- Reopening: `raid update <ID> --status Open --reason "..."` on a Closed item. Without `--reason` it is refused. The history entry records the reopening and the reason; the earlier closed date and reason stay in the history.
- `rules.py`: status is one of Open, Mitigating, Closed.

## Constraints

- Three statuses, new items Open (REQ-017).
- Closing needs a reason and records the date (REQ-018).
- A Closed item can be reopened only with a reason (DEC-15).
- The same three statuses apply to all four types (DEC-21).
- Closed items stay in the log (REQ-019, ADR-001).

## Non-goals

- Deleting items (SPEC-EPIC-5-03).
- Type-specific statuses.

## Success signal

`raid close I-001 --reason "Test environment restored by infra"` on 2026-10-10 makes `raid show I-001` print Closed, 2026-10-10 and the reason; closing without a reason is refused.

## Test plan

The Criteria column gives the story's acceptance criterion numbers; CF-n is an item carried forward from the stage 3 review.

| Test | Criteria | Checks |
|---|---|---|
| `test_new_item_is_open` | 1 | Status Open after accept. REQ-017. |
| `test_update_status_mitigating` | 2 | List shows Mitigating; one entry Open → Mitigating. REQ-016. |
| `test_bad_status_refused` | 3 | `Done` refused listing the three values. REQ-017. |
| `test_close_without_reason_refused` | 4 | Status still Open. REQ-018. |
| `test_close_with_reason` | 5 | Closed, closed date 2026-10-10, reason shown by `show`. REQ-018. |
| `test_reopen_without_reason_refused` | 6 | Status still Closed. DEC-15. |
| `test_reopen_with_reason` | 7, CF-6 | Status Open; one entry records reopening and "Environment down again". DEC-15. |
| `test_update_status_closed_points_to_close` | 4 | Failure path: `--status Closed` refused with the pointer. |
| `test_close_already_closed_refused` | 4 | Edge: closing a Closed item is refused; no entry added. |
| `test_closed_to_mitigating_needs_reason` | 6 | Edge: any move away from Closed needs a reason. |

**Test data:** I-001 "Test environment down"; today fixed at 2026-10-10.

## Definition of done

- Every test in the test plan exists and passes under `pytest` on Python 3.13, with no Claude Code session and no network.
- Every test names the REQ or NFR it checks, in its name or docstring (NFR-010).
- The whole suite is still green, and the code uses nothing Python 3.12 lacks (DEC-14).
- Tests are written before the code for this spec, in the same session.
- MEDIUM tier: show the owner the diff before committing.
