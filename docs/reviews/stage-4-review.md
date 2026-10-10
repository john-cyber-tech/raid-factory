# Stage 4 review — engineering specs and task order

**Date:** 2026-10-10 · **Fourth pass**, after the owner's decision on N-14 (DEC-22). The spec and DAG checks were re-run on the regenerated files with no problems.
**Reviewed:** `docs/specs/` (25 specs, one per story, about 12,900 words) and `docs/task-dag.md`, against the 25 stories (128 acceptance criteria), `docs/requirements.md` (42 REQs, 10 NFRs, DEC-01 to DEC-22), `docs/architecture.md` and ADR-001 to ADR-006.
**How:** the generator checked each spec as it was written, and a second script then read the files on disk independently. I read the specs against their stories for choices that have no upstream source.
**Knowledge used:** EPAM 500 Blocks 2 and 3 (written intent before code, review effort scaled to blast radius) and 600 Blocks 1, 3 and 4 (risk decides test depth, negative cases, synthetic test data). The optional skills were not run.

**Open findings: 0 BLOCKER · 0 MAJOR · 1 MINOR** (N-12, a stage 6 handover item)

## Checks the stage asks for

| Check | Result |
|---|---|
| Each spec has a testable success signal | 25 / 25. Each names a command or function, an input and an observable result |
| Every Constraint cites an upstream id | 25 / 25 specs; every constraint line ends with an ADR, NFR, REQ, DEC, open-question, assumption or limitation id, and every id exists |
| No cycles in the DAG | None. Every task depends only on earlier tasks; 9 waves. Re-checked after SPEC-EPIC-3-04 gained a dependency on SPEC-EPIC-2-03 |
| No unresolved Open Questions in LOW tier tasks | None. After DEC-21 only one spec cites an open question: SPEC-EPIC-5-04 (MEDIUM) names OQ-08, the owner's sign-off on client approval, as out of its scope |
| One spec covers the `/raid-extract` command and the `pending.json` schema | SPEC-EPIC-1-05 holds both: the command's behaviour and the contract table. SPEC-EPIC-1-02 builds the schema file from that table and tests that the two agree key for key |
| Tests cover each acceptance criterion | 128 / 128 criteria have at least one named test. 198 tests in total: 182 automated, 16 manual |
| Every REQ and NFR appears in a spec | 42 / 42 REQs, 9 / 10 NFRs (NFR-001 performance has no target) |
| Every spec has at least 2 edge or failure tests | 25 / 25 |

Every spec has all seven sections the stage requires, plus named test data. All test data is fictional.

## Risk tiers

| Tier | Count | Specs |
|---|---|---|
| HIGH (two stops: tests approved before any code, then the implementation approved before committing) | 6 | EPIC-1-01 first log writes; EPIC-5-01 save routine; EPIC-5-02 history and save guard; EPIC-1-02 contract and validator; EPIC-1-05 and EPIC-1-06 extraction command |
| MEDIUM (show you the diff) | 11 | EPIC-5-04, 5-05, 1-03, 1-04, 2-03, 2-05, 2-04, 3-03, 3-04, 4-01, 4-03 |
| LOW (proceed when green) | 8 | EPIC-2-06, 2-02, 2-01, 2-07, 3-01, 3-02, 5-03, 4-02 |

## Carried forward from stage 3: where each item landed

You asked for these to be listed here so you can check them.

| # | What was owed | Spec | Test |
|---|---|---|---|
| CF-1 | A damaged or unreadable `raid-log.json` is never overwritten | SPEC-EPIC-5-01 | `test_damaged_log_is_never_overwritten`: a log containing `{not json` makes `raid review` and `raid list` exit 1 naming the file, and the file is byte-identical afterwards |
| CF-2 | Extra fields and control characters in `pending.json` are rejected | SPEC-EPIC-1-02 | `test_extra_field_is_rejected` (a proposal with `accepted: true`) and `test_control_characters_are_rejected` (an escape character in a title) |
| CF-3 | A second summary on the same day overwrites the first | SPEC-EPIC-4-01 | `test_same_day_summary_overwrites`: still one file, with the newer content |
| CF-4 | `/raid-extract` allowed tools limited to reading the notes file and writing `pending.json` (REQ-042) | SPEC-EPIC-1-06 | `test_command_allowed_tools` and `test_allowed_tools_check_catches_extra_tool` (automated, on the command file); `MANUAL-confirm-permission-behaviour` records what Claude Code does when the command tries another tool, closing stage 3 finding N-04 |
| CF-5 | Merged excerpt visible; merged proposal without a source date is asked; thin-slice fixture carries source dates | SPEC-EPIC-3-04, SPEC-EPIC-1-01 | `test_merged_excerpt_visible_in_show`, `test_merge_without_source_date_is_asked`, `test_thin_slice_fixture_has_source_dates` |
| CF-6 | Which command reopens a Closed item | SPEC-EPIC-2-03 | `raid update <ID> --status Open --reason "..."`; `test_reopen_with_reason`, `test_reopen_without_reason_refused` |

## Fixed in this pass

| # | Severity | Finding | What changed |
|---|---|---|---|
| F-01 | MAJOR | Five specs (EPIC-1-01, 1-05, 1-06, 2-01, 3-01) had fewer than two edge or failure tests, so their test plans leaned on the happy path | One failure-path test added to each: input ending mid-review, a missing notes file, the tool check catching an extra tool, and a damaged log for `list --owner` and `flag` |
| F-02 | MINOR | SPEC-EPIC-5-03 said the help output lists eight commands, but it is built before `raid summary` exists | Signal and test now say "the commands built so far", updated to eight when SPEC-EPIC-4-01 lands |

## Closed in the second pass

| # | Finding | How it was closed |
|---|---|---|
| P-02 | 16 manual tests | Accepted by the owner. Runs are recorded in `docs/reviews/stage-5-extract-runs.md` |
| P-05 | Decision records still "Proposed" | All six now read "Accepted (2026-10-10, with the approval of stage 3)". The architecture's header line that said "all Proposed" was changed to match |
| P-06 | Test independence | For the six HIGH specs, a first gate was added to each Definition of done: tests and test data are written first and shown to the owner, and no implementation code is written until they are approved. The existing stop before committing is now gate 2. MEDIUM and LOW specs say tests are written first in the same session. `docs/task-dag.md` has a "Stops for you" column and states the total: 12 stops and 11 diffs |

## Closed in the third pass

| # | Finding | How it was closed |
|---|---|---|
| P-01 | Ten spec-level choices, SA-1 to SA-10 | **Resolved by the owner's decision: all ten accepted** (DEC-20). The specs are built as written. The list is kept below for reference |
| P-03 | Five open questions shaping specs | **Resolved by the owner's decision: proposed defaults accepted** (DEC-21). OQ-02, OQ-07, OQ-16, OQ-17 and OQ-18 are closed in `docs/requirements.md`; three questions remain open there (OQ-08, OQ-11, OQ-19), none of which shapes a spec |
| P-04 | Specs far over the 10-minute rule | Acknowledged by the owner, who will read the six HIGH specs and the SA list. The two stage 3 findings it mentioned are listed separately below |

## Found and fixed in the third pass

| # | Severity | Finding | What changed |
|---|---|---|---|
| F-03 | MAJOR | **My statement in P-03 was wrong for OQ-02.** I wrote that each spec "builds the proposed default". The proposed default for OQ-02 was "note mandatory on accept, validation date optional", but SPEC-EPIC-2-05 had the note optional and listed a validation date as a non-goal. Accepting the default therefore changed behaviour | SPEC-EPIC-2-05: an Assumption cannot be accepted without a check note; an optional validation date is asked for, can be updated and is shown. Four tests added. SPEC-EPIC-2-04: `raid add --type Assumption` requires `--check-note`; one test added. Upstream: REQ-021's criterion states the rule, and story EPIC-2-05 gained criteria 4 and 5. The other four defaults (markdown only, three statuses for all types, no excerpts in the summary, no extraction threshold) were already what the specs built; only their citations changed from the question to DEC-21 |

Applying the rule to `raid add` as well as to review is my reading of "mandatory on accept": otherwise an Assumption could enter the log without a note by the other route.

## Closed in the fourth pass: N-14, merge into a Closed item

Decision DEC-22: merging a proposal into a Closed item reopens it.

| What | Change |
|---|---|
| Requirement | REQ-024's criterion now states the warning, the reopening, the history entry and the decline path |
| Story EPIC-3-04 | Criteria 5, 6 and 7 added; size raised from S to M; depends on EPIC-2-03 as well, because it needs status and reopening |
| SPEC-EPIC-3-04 capabilities | For a Closed item the review prints "R-001 is Closed. Merging will reopen it." and asks "Merge and reopen? (y/n)" before anything is written. On `y` the source is added and the status set to Open in one save, with two history entries: the merge, and the reopening with the reason "reopened by merge of a new proposal", the date and the user's name. On anything else nothing is written |
| SPEC-EPIC-3-04 tests | `test_merge_into_closed_stays_closed` removed. Added: `test_merge_into_closed_warns_before_confirm` (the warning and question are shown and the log is still byte-identical at that point), `test_merge_into_closed_reopens_and_writes_history` (status Open; exactly two new entries; reason, date 2026-10-10 and "Sean Murphy" on the reopening), `test_merge_into_closed_declined_changes_nothing`, `test_merge_into_open_item_has_no_reopen_prompt`, `test_merge_reopen_is_one_save` (a failed save leaves the item Closed with one source), `test_reopened_by_merge_shown_in_show` |
| Limitation L-8 | Removed from the architecture. Its other half, that an item added by hand is not checked for duplicates, is still true, so it was moved into L-4 |
| Architecture and ADR-003 | Data flow step 4 describes the reopening. ADR-003 is Accepted, so its decision was left alone; the one consequence line that said such an item stays Closed was replaced with a dated note citing DEC-22 |

**Tier re-check for SPEC-EPIC-3-04: stays MEDIUM.** It can now change the status of a Closed item, which touches the "closed means closed" concern (NEED-15). I kept it MEDIUM because the change only goes in the safe direction (to Open), needs an explicit confirmation, adds no new write path (it uses the store's existing save, guard and reopening rule), and has a failure-injection test that both changes land together or not at all. If you would rather approve it before it is committed, say so and I will make it HIGH, which adds two stops.

## Open findings

### BLOCKER (0) · MAJOR (0)

None.

### MINOR (1), inherited from stage 3

| # | ID | Finding | What you need to do |
|---|---|---|---|
| N-12 | ADR-002 | Nothing yet says how `/raid-extract` gets into the folder where the manager runs Claude Code | Nothing now; left as a handover item for stage 6 by the owner's decision |

### Spec-level choices (P-01), all accepted by decision DEC-20

| # | Spec | Choice I made | Why it needed deciding |
|---|---|---|---|
| SA-1 | EPIC-2-04, EPIC-4-03 | A hand-added item may have no severity; it ranks below Low in the summary | REQ-013 requires only a title to add an item |
| SA-2 | EPIC-1-04 | A source date later than today is refused | Notes cannot be from the future; prevents a typo becoming the audit date |
| SA-3 | EPIC-2-01 (LOW) | `raid list --owner ""` is refused with a hint to use `raid flag` | Otherwise it would silently list unowned items |
| SA-4 | EPIC-2-06 (LOW) | IDs are accepted in any letter case (`r-001`) | Convenience; costs nothing |
| SA-5 | EPIC-2-03 | `raid update --status Closed` is refused and points to `raid close`; closing an already Closed item is refused | Keeps one way to close, so a reason is never skipped |
| SA-6 | EPIC-1-01 | Review answers are single letters: `a` accept, `e` edit, `m` merge, `r` reject. If input ends mid-review, decisions made so far are kept and the command exits with code 1 | The stories say "accept, edit, reject" but not how |
| SA-7 | all | Exit code 0 on success, 1 when something is refused or fails | REQ-006 says only "non-zero" |
| SA-8 | EPIC-5-02 | History timestamps are local date and time; setting a field to the value it already has adds no entry | REQ-020 says "timestamp" |
| SA-9 | EPIC-2-02 (LOW) | `--owner ""` and `--due ""` clear the value; several fields can change in one command, and if any is invalid none is applied | REQ-016 does not cover clearing or multi-field updates |
| SA-10 | EPIC-3-03, EPIC-4-02 | The common-word list for duplicates is 22 words, given in the spec; a Dependency with no waiting-on party prints "waiting on: not recorded" | A-10 left the list open; REQ-032 does not cover the empty case |

No BLOCKER or MAJOR findings. No finding raised in stage 4 remains open.
