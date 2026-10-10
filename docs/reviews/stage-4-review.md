# Stage 4 review — engineering specs and task order

**Date:** 2026-10-10 · **Second pass**, after the owner's answers to P-02, P-05 and P-06. The spec and DAG checks were re-run on the regenerated files with no problems.
**Reviewed:** `docs/specs/` (25 specs, one per story, about 12,900 words) and `docs/task-dag.md`, against the 25 stories (123 acceptance criteria), `docs/requirements.md` (42 REQs, 10 NFRs, DEC-01 to DEC-19), `docs/architecture.md` and ADR-001 to ADR-006.
**How:** the generator checked each spec as it was written, and a second script then read the files on disk independently. I read the specs against their stories for choices that have no upstream source.
**Knowledge used:** EPAM 500 Blocks 2 and 3 (written intent before code, review effort scaled to blast radius) and 600 Blocks 1, 3 and 4 (risk decides test depth, negative cases, synthetic test data). The optional skills were not run.

**Open findings: 0 BLOCKER · 0 MAJOR · 3 MINOR**

## Checks the stage asks for

| Check | Result |
|---|---|
| Each spec has a testable success signal | 25 / 25. Each names a command or function, an input and an observable result |
| Every Constraint cites an upstream id | 25 / 25 specs; every constraint line ends with an ADR, NFR, REQ, DEC, open-question, assumption or limitation id, and every id exists |
| No cycles in the DAG | None. Every task depends only on earlier tasks; 9 waves |
| No unresolved Open Questions in LOW tier tasks | None. The 5 specs that cite an open question (OQ-02, OQ-07, OQ-08, OQ-16, OQ-17, OQ-18) are MEDIUM or HIGH |
| One spec covers the `/raid-extract` command and the `pending.json` schema | SPEC-EPIC-1-05 holds both: the command's behaviour and the contract table. SPEC-EPIC-1-02 builds the schema file from that table and tests that the two agree key for key |
| Tests cover each acceptance criterion | 123 / 123 criteria have at least one named test. 189 tests in total: 173 automated, 16 manual |
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

## Open findings

### BLOCKER (0) · MAJOR (0)

None.

### MINOR (3)

| # | ID | Finding | What you need to do |
|---|---|---|---|
| P-01 | 10 specs | **Spec-level choices with no upstream source**, SA-1 to SA-10 below. Three sit in LOW tier specs (SA-3, SA-4, SA-9). Your reply contained the unfilled placeholder "[list any SA items you want changed, or “accept all”]", so I have not treated it as an answer | Say "accept all", or name the SA items to change |
| P-03 | SPEC-EPIC-2-05, 2-03, 4-01, 1-05 | Five open questions still shape a spec: OQ-02 (is the check note mandatory), OQ-16 (statuses for all types), OQ-07 (PDF), OQ-17 (excerpts in the summary) and OQ-18 (extraction quality target). Each spec builds the proposed default and says so. Your reply contained an unfilled placeholder here too | Say "accept the proposed defaults", or give answers |
| P-04 | whole set | About 13,000 words of specs, far over the 10-minute rule. Stage 3 findings N-12 (how the command reaches a project folder) and N-14 (merge into a Closed item stays Closed) also remain | Read the 6 HIGH specs and the SA list; skim the rest by success signal. N-12 is for stage 6 |

### Spec-level choices (P-01)

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

No BLOCKER or MAJOR findings. P-01 and P-03 are waiting on your answer; if stage 4 is approved without one, the choices and defaults are built as written.
