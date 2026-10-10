# Stage 3 review — architecture and decision records

**Date:** 2026-10-10 · **This is the fourth pass**, a full re-check of the files as they stand, with no new decisions since the third.
**Reviewed:** `docs/architecture.md` (9 components, about 2,650 words) and `docs/adr/ADR-001` to `ADR-006` (470 to 680 words each), against `docs/requirements.md` (42 REQs, 10 NFRs) and the 25 stories.
**How:** a script checked that every REQ and NFR appears in the mapping tables, every component has requirements and is in the diagram, every cited ID exists, no closed question is still cited as open, and every ADR has its sections, at least two alternatives and stated downsides. Because four stories changed, the stage 2 story checks (form, order, criterion numbering) were re-run too. I then walked each NFR and each failure case by hand.
**Knowledge used:** EPAM 400 Blocks 2 to 4 (diagram as code, simplest shape that fits, ADR format with an agent-readable summary, NFRs with a mechanism and an enforcement). The optional skills were not run.

**Open findings: 0 BLOCKER · 0 MAJOR · 3 MINOR**

## Coverage

| Check | Result |
|---|---|
| Every REQ lands on a component | 42 / 42 |
| Every NFR mapped to a component with a mechanism and a verification | 9 / 10. NFR-001 (performance) has no target, so it has no mechanism; the table says so |
| Components with no requirement, or missing from the diagram | 0 |
| ADRs with at least 2 genuine alternatives, trade-offs, a decision, downsides, and driving REQ/NFR ids | 6 / 6 (3 or 4 options each; 2 or 3 stated downsides each) |
| The three ADRs the stage requires | Storage and atomic writes: ADR-001. Extraction boundary, compared with headless `claude -p` and an API call: ADR-002. Duplicate detection, rule-based against model-assisted: ADR-003 |
| IDs cited that do not exist, or closed questions still cited as open | 0 |

Three further forks earned a record: how `pending.json` is validated (ADR-004, adds one dependency), where the user's name is kept (ADR-005, stage 2 finding T-03), and how history is stored (ADR-006).

## NFR walk-through

| NFR | Is the mechanism plausible? |
|---|---|
| NFR-002 atomic writes | Yes. Write-then-replace in the same folder is all-or-nothing. Tested and supported on macOS only (DEC-16, limitation L-7) |
| NFR-003 never lose items | Yes. Save guard refuses a save that drops an ID; each accept is saved at once; an unreadable log is never overwritten |
| NFR-004 no network or key | Yes. Standard library plus one offline library; enforced by tests with sockets blocked |
| NFR-005 notes are data | Mostly testable. The validator, human review and the command file's allowed tools (REQ-042) can each be checked; the prompt's instruction to treat notes as data cannot. The CLI never interprets proposal text, which is the part that matters most |
| NFR-006 local only | Yes. Four named files, all in the project folder |
| NFR-007 append-only history | Yes against the tool's own mistakes; not against a person editing the file by hand. ADR-006 says so |
| NFR-008 five minutes | Plausible: two commands. Verified only by a timed walkthrough |
| NFR-009 400 words | Yes. Titles are bounded at 80 characters and trimming always terminates: with every item dropped, only headings and "N more" lines remain |
| NFR-010 Python 3.12 or later, pytest | Yes on Python 3.13, where it is built and tested. Compatibility with 3.12 is by a declared minimum version and inspection only (limitation L-5) |

## Failure cases asked for by the stage

| Case | Result in this design |
|---|---|
| `pending.json` malformed | Parse error from the validator; nothing shown; log untouched |
| `pending.json` partly written | Same: it is not valid JSON, so the whole file is rejected |
| `pending.json` contains instructions copied from the notes | Stored and shown as text only. Extra fields and control characters are rejected by the contract. A person decides each item with the excerpt in front of them |
| Crash during a log save | Old or new file, never a mix |
| Crash between saving the log and trimming `pending.json` | Proposal is shown again; the duplicate finder shows the item it became |
| Log file damaged | Commands stop with a message; the file is not overwritten |

## Closed in this pass

| # | Was | Finding | How it was closed |
|---|---|---|---|
| N-01 | MAJOR | `pending.json` after review (OQ-15) | DEC-10: decided proposals are removed, rejections are not recorded. Architecture data flow steps 4 and 5; limitation L-1; ADR-002 consequence |
| N-02 | MINOR | Three commands beyond the brief | DEC-11: `show`, `update`, `close` accepted. Architecture section 9 |
| N-03 | MINOR | `jsonschema` dependency | DEC-12: kept. ADR-004 records the confirmation |
| N-05 | MINOR | Single user (OQ-04) | DEC-13: accepted for v1. Limitation L-2; ADR-001 and ADR-005 reworded from "if" to "decided" |
| N-06 | MINOR | No Python 3.12 on this machine | DEC-14: build on 3.13, code kept 3.12-compatible. `inputs/brief.md` now says "Python 3.12 or later"; NFR-010 and architecture sections 7 and 9 updated; limitation L-5 |
| N-09 | MINOR | Three defaults (OQ-13, OQ-14) | DEC-15: all three accepted. Architecture data flow steps 4 and 6 |

Architecture section 11 is new: six known limitations, L-1 and L-2 being the two you asked for, L-3 to L-6 collected from downsides the ADRs already stated.

**Changes outside the three things you named**, made so the decisions have a parent that stage 4 can cite:
- `docs/requirements.md`: decisions DEC-10 to DEC-15 recorded; one sentence added to the criteria of REQ-007, REQ-011, REQ-018 and REQ-024; NFR-010 reworded; OQ-04, OQ-13, OQ-14 and OQ-15 removed from the open list (10 remain).
- Stories: one criterion added to EPIC-1-01 (pending file emptied, rejection not recorded), one to EPIC-2-02 (type cannot change), two to EPIC-2-03 (reopen with and without a reason), one to EPIC-3-04 (merge keeps existing values). 120 criteria in total; coverage and order unchanged.

Closed in the third pass (decisions DEC-16 to DEC-19):

| # | Was | Finding | How it was closed |
|---|---|---|---|
| N-13 | MINOR | `CLAUDE.md` and the brief's interface line disagreed with decisions | `CLAUDE.md` now says "Python 3.12 or later"; the brief's interface line lists all eight commands |
| N-07 | MINOR | Operating systems unknown (OQ-12) | DEC-16: macOS only for v1. Limitation L-7; ADR-001 consequence |
| N-10 | MINOR | Closed items as duplicates; `raid add` and duplicates (T-04, T-05) | DEC-17: Closed items are offered; `raid add` does not check. REQ-023, EPIC-3-03 criterion 6, EPIC-2-04 criterion 3, ADR-003, limitation L-8 |
| N-11 | MINOR | Severity scale (OQ-01) | DEC-18: High, Medium, Low. REQ-003 states the values; ADR-004 note updated |
| N-04 | MINOR | Extraction command permissions | DEC-19 and new REQ-042: allowed tools limited to reading the notes file and writing `pending.json`. EPIC-1-06 criterion 4 checks the command file; architecture and ADR-002 cite it |
| N-08 | MINOR | Three design behaviours with no story criterion | Carried into stage 4 by your instruction (list below) |

Fixed in the fourth pass: F-03 (MINOR), the data flow in architecture section 4 did not mention `raid add`, although REQ-013 is mapped to the log store; step 6 now covers it, including that it skips the duplicate check (DEC-17).

Fixed in the first pass: F-01 (an item holds a list of sources, settling stage 1 finding R-07) and F-02 (ADR-005 for the name file, stage 2 finding T-03).

## Carried into stage 4

These are agreed actions, not open findings. The stage 4 review will list each one with the spec and criterion that covers it, so you can check them.

| # | From | What stage 4 must add | Where |
|---|---|---|---|
| CF-1 | N-08 | A criterion that a damaged or unreadable `raid-log.json` is never overwritten: the command stops with a message | Spec for EPIC-5-01 |
| CF-2 | N-08 | A criterion that extra fields and control characters in `pending.json` are rejected | Spec for EPIC-1-02 |
| CF-3 | N-08 | A criterion that generating a summary twice on the same day overwrites the earlier file | Spec for EPIC-4-01 |
| CF-4 | N-04, REQ-042 | The spec for the `/raid-extract` command limits its allowed tools to reading the notes file and writing `pending.json`, with an automated check of the command file. Stage 5 confirms how Claude Code enforces it | Spec for EPIC-1-06 |
| CF-6 | DEC-15 | Say which command reopens a Closed item and how the reason is given; the design only says it is possible | Spec for EPIC-2-03 |
| CF-5 | Stage 2 finding T-06 | Three small criteria: a merged-in excerpt is visible when viewing the item; a merged proposal with no source date is asked for one; the thin-slice fixture carries source dates | Specs for EPIC-3-04 and EPIC-1-01 |

## Open findings

### BLOCKER (0) · MAJOR (0)

None.

### MINOR (3)

| # | ID | Finding | What you need to do |
|---|---|---|---|
| N-14 | DEC-15, DEC-17, EPIC-3-04 | A consequence of two of your decisions together: merging a proposal into a Closed item leaves it Closed, because a merge keeps the existing item's values. A risk that has come back has to be reopened as a separate step. Recorded as limitation L-8 | Accept, or say that merging into a Closed item should reopen it |
| N-15 | whole set | The architecture is about 2,650 words and the six decision records about 3,350 more, roughly a 25-minute read against the 10-minute rule in `CLAUDE.md`. Earlier passes did not report this | Nothing, unless you want it cut; read architecture sections 2, 4 and 11 and each record's Decision and Consequences first |
| N-12 | ADR-002 | Nothing yet says how `/raid-extract` gets into the folder where the manager runs Claude Code | Nothing now; it is a handover item for stage 6 |

No BLOCKER or MAJOR findings remain.
