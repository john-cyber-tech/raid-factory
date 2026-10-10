# Stage 1 review — `docs/requirements.md`

**Date:** 2026-10-10 · **Reviewed:** 16 needs, 33 REQs, 10 NFRs, 20 open questions, 8 assumptions
**Inputs used:** `inputs/brief.md`, the three files in `inputs/stakeholder-interviews/`, and `inputs/sample-meeting-notes.md` (only to confirm the REQ-001 fixture contains RAID content). `inputs/meeting-notes/` and `inputs/expected/` were not read.
**Knowledge used:** EPAM 200 Blocks 3 and 6, EPAM 600 Block 2, and the `requirements-writer` and `nfr-elicitor` skills. The skills' method was followed; the factory's ID scheme (NEED-nn, REQ-nnn, NFR-nnn) and single file were kept instead of the skills' own file names and prefixes.

## Scores

| Check | Result | Notes |
|---|---|---|
| Unambiguous | 31 / 33 REQs | REQ-023 and REQ-031 depend on an open question (below) |
| Testable | 33 / 33 REQs, 8 / 10 NFRs | NFR-001 has no target by design; NFR-009 has no length number yet |
| Atomic | 32 / 33 | REQ-016 covers six fields under one "update" behaviour, accepted as one requirement |
| Traceable to a NEED | 33 / 33 REQs | Every NEED-01 to NEED-16 is cited by at least one REQ or NFR (NEED-14 by NFR-008 only) |
| No duplicates | 33 / 33 after fixes | See F-06 |

## Findings fixed in this pass

| # | Severity | ID | Finding | What changed |
|---|---|---|---|---|
| F-01 | MAJOR | REQ-007 | Said "exactly one decision: accept, edit, or reject", which contradicted REQ-009 where an edit is followed by an accept | Reworded: final decision is accept or reject; editing first is REQ-009. Criterion now checks the review does not move on without a decision |
| F-02 | MAJOR | REQ-012 | Required a source date on every item, but the brief's seven proposal fields contain no date, so the criterion had nothing to check against | Criterion now requires a valid calendar date; added OQ-20 asking where the date comes from; A-8 reworded |
| F-03 | MAJOR | REQ-031 | "Highest severity value in use" would list Low risks as "top risks" when no High ones exist | Criterion rewritten with a concrete example (open High only), marked as written against the OQ-01 default |
| F-04 | MINOR | REQ-019 | Criterion spoke of "both IDs" after a merge, but a merged proposal never gets an ID | Reworded to name R-001 and R-002 |
| F-05 | MINOR | REQ-033 | Interview-derived but not marked | Marked *(interview)* and added to OQ-19 |
| F-06 | MINOR | REQ-005 / REQ-006 | REQ-005's criterion repeated REQ-006's rejection check | REQ-005 now tests ordering only: one bad proposal means none is shown |
| F-07 | MINOR | REQ-013 | Proposed as Should although `raid add` is named in the brief's Stack | Added to OQ-19 for your call |

Re-check after fixes: no BLOCKER and no MAJOR finding remains that I can fix without an answer from you.

## Findings still open

| # | Severity | ID | Finding | Suggested fix |
|---|---|---|---|---|
| R-01 | MAJOR | REQ-020 | The audit trail cannot record *who* without contradicting "no logins" (conflict C-1). Tom says Acme's PMO requires it | Answer OQ-03 |
| R-02 | MAJOR | REQ-015, REQ-016 | The brief has the project manager updating items, but nothing says how she reaches a local single-user file (conflict C-2) | Answer OQ-04 |
| R-03 | MAJOR | REQ-029 to REQ-032 | Three summary sections the stakeholders asked for are left out because the log has no data to drive them; Tom's three questions are only one-third covered | Answer OQ-05 |
| R-04 | MAJOR | REQ-023 | Only the two extreme cases are testable; the rule for "likely" is undefined | Answer OQ-10 |
| R-05 | MINOR | NFR-009 | "One page" has no number | Answer OQ-06 |
| R-06 | MINOR | NFR-001 | No performance or capacity target exists in any source | Answer OQ-11 or accept "none" |
| R-07 | MINOR | REQ-024, REQ-012 | After a merge an item holds more than one source excerpt, while REQ-012 speaks of "the" excerpt | Settle with OQ-13 in stage 3 |
| R-08 | MINOR | REQ-027 | A Must requirement needs a last-changed timestamp, which overlaps with history (REQ-020, Should) | Confirm priorities under OQ-19 |
| R-09 | MINOR | NFR-005 | Verification relies on a human judging an extraction run; it cannot be a pytest test because the CLI never runs extraction | Accept, or define the trap fixture and pass rule in stage 4 |
| R-10 | MINOR | NFR-006 | "No telemetry" restates NFR-004 | Accept the overlap or drop the phrase |
| R-11 | MINOR | whole document | About 4,300 words, roughly a 20-minute read, over the 10-minute rule in `CLAUDE.md` | Read sections 1 (conflicts table) and 4 first; or tell me to split the NFRs into their own file |

## Open questions that are release-relevant rather than build-relevant

OQ-08 (Acme and Legal approval for processing notes in Claude Code) does not block building, because all test inputs are fictional. It does block use on real client notes and is yours to sign off.

## Amendment after approval (2026-10-10)

The owner answered five open questions and asked for one new requirement. `docs/requirements.md` section 4 now has a Decisions table (DEC-01 to DEC-07).

| Change | Detail |
|---|---|
| Open findings closed | R-01 (who made a change, DEC-02), R-03 (summary sections, DEC-03), R-04 (duplicate rule, DEC-01), R-05 (one page = 400 words, DEC-04) |
| Requirements changed | REQ-013 (hand-added source values), REQ-020 (user name in history), REQ-023 (duplicate rule), NFR-009 (400 words) |
| Requirements added | REQ-034 view one item, REQ-035 ask for name once, REQ-036 mark as needing a decision, REQ-037 "Decisions needed" section, REQ-038 cap per section with "more items" line |
| Assumptions added | A-9 (decision mark), A-10 (key-word threshold), A-11 (order within a capped section). These hold numbers and rules the answers did not give |
| Still open | R-02 (OQ-04, how the project manager reaches the file) is the only MAJOR left; 15 open questions remain, none blocking |

Re-check of the five new requirements: each is atomic, has a concrete criterion and cites a NEED. REQ-038's cap of 5 and REQ-023's threshold are flagged as my numbers.

## Second amendment (2026-10-10)

Decisions DEC-08 (source date) and DEC-09 (summary word limit) were applied. Added REQ-039, REQ-040, REQ-041; changed REQ-012, REQ-038, NFR-009, A-8, A-11; OQ-20 closed. Totals are now 41 REQs, 10 NFRs, 11 assumptions, 14 open questions. Each new requirement is atomic, has a concrete criterion and cites a NEED. Details and remaining findings are in `docs/reviews/stage-2-review.md`.
