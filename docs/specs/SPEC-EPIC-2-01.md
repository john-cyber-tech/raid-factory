# SPEC-EPIC-2-01 — List only my items

**Story:** EPIC-2-01 · **Covers:** REQ-015 · **Components:** COMP-03
**Build order:** 13 of 25 · **Risk tier:** LOW (A read-only filter.) · **Depends on:** SPEC-EPIC-1-01

## Why

As a project manager, I want to see only the items assigned to me, so that I can find what I need to update quickly.

The project manager wants to see only what is assigned to her (NEED-10).

## Capabilities

- `cli.py`: `raid list --owner <name>` shows only items whose owner equals the name, ignoring upper and lower case and surrounding spaces.
- When nothing matches, print "No items found for owner <name>" and exit 0.

## Constraints

- Exact match ignoring case; "Priya" does not match "Priya Nair" (DEC-07).
- `list` never writes (ADR-001).

## Non-goals

- Partial or fuzzy name matching.
- Filtering by type, status or severity.

## Success signal

With 5 items of which 2 are owned by "Priya Nair", `raid list --owner "priya nair"` shows exactly those 2.

## Test plan

The Criteria column gives the story's acceptance criterion numbers; CF-n is an item carried forward from the stage 3 review.

| Test | Criteria | Checks |
|---|---|---|
| `test_list_owner_exact` | 1 | Exactly the 2 items. REQ-015. |
| `test_list_owner_ignores_case` | 2 | `priya nair` gives the same 2. REQ-015. |
| `test_list_owner_partial_no_match` | 3 | `Priya` shows none. REQ-015. |
| `test_list_owner_none_found` | 4 | `Lena`: message, exit 0. REQ-015. |
| `test_list_owner_does_not_match_unowned` | 3 | Edge: `--owner ""` is refused with a hint to use `raid flag` for unowned items. |
| `test_list_owner_on_damaged_log` | 4 | Failure path: an unreadable log gives exit 1 and a message, not an empty list. |

**Test data:** A log of 5 items: 2 owned by "Priya Nair", 1 by "Priya", 1 by "Tom Brennan", 1 unowned.

## Definition of done

- Every test in the test plan exists and passes under `pytest` on Python 3.13, with no Claude Code session and no network.
- Every test names the REQ or NFR it checks, in its name or docstring (NFR-010).
- The whole suite is still green, and the code uses nothing Python 3.12 lacks (DEC-14).
- Tests are written before the code for this spec, in the same session.
- LOW tier: proceed to the next spec once the tests are green, then commit.
