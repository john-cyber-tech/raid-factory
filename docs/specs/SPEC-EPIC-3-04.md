# SPEC-EPIC-3-04 — Merge a proposal into an existing item

**Story:** EPIC-3-04 · **Covers:** REQ-024 · **Components:** COMP-04, COMP-05
**Build order:** 21 of 25 · **Risk tier:** MEDIUM (Adds a new kind of write to an existing item and can reopen a Closed one; it goes through the store's existing save and adds no new write path.) · **Depends on:** SPEC-EPIC-3-03, SPEC-EPIC-5-02, SPEC-EPIC-2-03

## Why

As a delivery manager, I want to merge a repeated proposal into the item that already exists, so that the log shows one item with all the places it was raised.

The log should show one item with all the places it was raised (NEED-04).

## Capabilities

- `review.py`: when likely duplicates are shown, a fourth answer `m` merge; if several are shown, ask which ID.
- `store.py`: `merge_source(id, excerpt, date)` appends a source to the item and one history entry of kind merged. No other value of the item changes.
- A proposal with no source date is asked for one before merging, as for accept.
- Accept with a duplicate shown means keep separate: a new ID is created.
- `raid show` lists every source, the original first.
- If the chosen item is Closed: before anything is written, print "R-001 is Closed. Merging will reopen it." and ask "Merge and reopen? (y/n)". On `y`, `store.py` adds the source and sets the status to Open in one save, appending two history entries: the merge, and the reopening with the reason "reopened by merge of a new proposal". On anything else, nothing is written and the proposal's question is asked again.
- Merging into an item that is not Closed asks no extra question.

## Constraints

- A merge keeps the existing item's title, owner, severity and due date (DEC-15).
- A merge happens only when the manager chooses it (DEC-01, ADR-003).
- Merging into a Closed item reopens it, after a warning and the manager's confirmation; the history records the reopening with the reason "reopened by merge of a new proposal", the date and the user's name (DEC-22).
- The added source and the reopening are written in one save, so a crash cannot leave one without the other (ADR-001, NFR-002).
- A reopening always carries a reason (DEC-15, REQ-018).
- A source needs a date (DEC-08).

## Non-goals

- Merging two items already in the log (limitation L-4).
- Reopening an item in any way other than by merge or by `raid update` (SPEC-EPIC-2-03).

## Success signal

Choosing merge for a proposal shown against R-001 leaves exactly one Risk, with two sources and a merged entry in its history. If R-001 was Closed, the prompt warns that merging will reopen it, and after confirming R-001 is Open with a reopening entry whose reason is "reopened by merge of a new proposal".

## Test plan

The Criteria column gives the story's acceptance criterion numbers; CF-n is an item carried forward from the stage 3 review.

| Test | Criteria | Checks |
|---|---|---|
| `test_merge_adds_source_and_history` | 1 | One Risk; R-001 has two sources; history has a merged entry. REQ-024. |
| `test_merge_keeps_existing_values` | 2 | Owner "Priya Nair", High, title and due date unchanged. DEC-15. |
| `test_keep_separate_creates_new_id` | 3 | Proposal becomes R-002; R-001 unchanged. REQ-024. |
| `test_reject_with_duplicate_shown` | 4 | Log unchanged. REQ-024. |
| `test_merged_excerpt_visible_in_show` | CF-5 | `show R-001` prints both excerpts, original first. |
| `test_merge_without_source_date_is_asked` | CF-5 | Proposal with no date: asked before the merge; empty answer cancels. |
| `test_merge_into_closed_warns_before_confirm` | 5 | Output contains "R-001 is Closed. Merging will reopen it." and the y/n question, and at that point the log file is byte-identical to before. DEC-22. |
| `test_merge_into_closed_reopens_and_writes_history` | 6 | After `y` on 2026-10-10 as "Sean Murphy": status Open; two sources; history gained exactly two entries, a merge and a reopening with reason "reopened by merge of a new proposal", date 2026-10-10 and name "Sean Murphy". DEC-22. |
| `test_merge_into_closed_declined_changes_nothing` | 7 | After `n`: R-001 still Closed, no new source, no new history entry; the proposal is asked about again and is still in `pending.json`. DEC-22. |
| `test_merge_into_open_item_has_no_reopen_prompt` | 1 | Edge: merging into an Open or Mitigating item prints no warning and adds only the merge entry. |
| `test_merge_reopen_is_one_save` | 6 | Failure path: the save fails during a confirmed merge into a Closed item; R-001 is still Closed with one source, and the proposal is still pending. NFR-002. |
| `test_reopened_by_merge_shown_in_show` | 6 | `show R-001` prints the reopening entry with its reason, and the earlier closing entry with its reason is still there. |
| `test_merge_not_offered_without_duplicate` | 4 | Failure path: `m` with no duplicate shown repeats the question. |

**Test data:** R-001 owner "Priya Nair", High; proposal with empty owner, Low, same title. A second log where R-001 was closed on 2026-10-08 with the reason "Security review completed"; today 2026-10-10; name "Sean Murphy".

## Definition of done

- Every test in the test plan exists and passes under `pytest` on Python 3.13, with no Claude Code session and no network.
- Every test names the REQ or NFR it checks, in its name or docstring (NFR-010).
- The whole suite is still green, and the code uses nothing Python 3.12 lacks (DEC-14).
- Tests are written before the code for this spec, in the same session.
- MEDIUM tier: show the owner the diff before committing.
