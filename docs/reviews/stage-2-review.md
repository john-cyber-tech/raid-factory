# Stage 2 review — epics, stories, traceability

**Date:** 2026-10-10 · **This is the fourth pass**, a full re-check of the files after decisions DEC-08 and DEC-09.
**Reviewed:** `docs/epics.md` (5 epics), `docs/stories/` (25 stories: 19 S, 6 M), `docs/traceability.md`, against `docs/requirements.md` (41 REQs, 10 NFRs, 16 needs, decisions DEC-01 to DEC-09).
**How:** a script read the files on disk (not the generator's data) and checked coverage, orphans, unknown IDs, build order, references to closed questions, and the form of every criterion. I then read every story against its requirements for contradictions and gaps.
**Not read:** `inputs/meeting-notes/`, `inputs/expected/`. The optional skills were not run.

**Open findings: 0 BLOCKER · 0 MAJOR · 18 MINOR**

## Coverage

| Check | Result |
|---|---|
| Every REQ maps to at least one epic and story | 41 / 41 |
| Every NFR maps to at least one epic and story | 9 / 10. NFR-001 (performance, "none identified") has nothing to build |
| Orphan epics or stories | 0 |
| Every NEED reaches at least one story | 16 / 16 |
| Stories citing an unknown REQ, NFR, story, assumption or decision, or a question that is already answered | 0 |
| `docs/epics.md` and `docs/traceability.md` agree with the story files | Yes |

## INVEST

| Criterion | Result | Notes |
|---|---|---|
| Independent | 25 / 25 buildable in the listed order | No story precedes one it depends on |
| Negotiable | Pass | Criteria describe behaviour; command names come from the brief's Stack |
| Valuable | Pass | EPIC-5-01 and EPIC-5-04 are safety stories whose value is the absence of a failure |
| Estimable | 25 / 25 | No story waits on an unanswered question to be sized |
| Small | Pass | No story larger than M. EPIC-4-03 went from S to M because of the trimming rule |
| Testable | 25 / 25 | Two criteria are human checks by design (EPIC-2-02 timed walkthrough, EPIC-4-03 plain-English read) and EPIC-1-05/1-06 are run by hand in Claude Code |

All 115 acceptance criteria are in Given/When/Then form with a stated outcome. None restates its story title, and every story has at least one refusal or empty-case criterion.

## Order

EPIC-1-01 is first and is an end-to-end thin slice: fixture proposals → `raid review` → log with stable IDs → `raid list`.

## Closed in this pass

| # | Was | ID | How it was closed |
|---|---|---|---|
| T-01 | MAJOR | EPIC-1-04, EPIC-1-05, REQ-012 | Decision DEC-08. New REQ-039 (extraction gives the notes date only when stated in full with a year) and REQ-040 (manager is asked at review; no acceptance without a source date). EPIC-1-04 now has 6 criteria covering asked / not asked / empty / invalid; EPIC-1-05 has 2 new criteria, including that the sample notes (no year) lead to being asked at review |
| T-02 | MAJOR | EPIC-4-03, REQ-038, NFR-009 | Decision DEC-09. 400 words is the hard limit; new REQ-041 caps titles at 80 characters; REQ-038 ranks by severity then age and drops the lowest-ranked items when still over. EPIC-4-03 has a testable word-limit criterion on a worst-case log (criterion 4) plus criteria for the "N more" count, for which items are left out, and for a small log |
| S-02 | MINOR | REQ-038 | Replaced by your ranking rule (severity then age); what is left of it is U-02 |

Stories changed beyond the three you named, because the 80-character title limit has to be enforced where titles enter the log: one criterion each in EPIC-1-02 (validation), EPIC-1-03 (edit in review), EPIC-2-02 (update) and EPIC-2-04 (add by hand).

Earlier passes: F-01 to F-05 fixed; the first pass's six MAJOR findings closed by DEC-01 to DEC-06.

## Open findings

### BLOCKER (0) · MAJOR (0)

None.

### MINOR (18)

| # | ID | Finding | What you need to do |
|---|---|---|---|
| U-01 | REQ-041, EPIC-1-02 | You said titles are capped at 80 characters. I read that as: a longer title is refused wherever it enters, which means one 81-character title in `pending.json` rejects the whole file (A-2) | Confirm, or say you would rather shorten it during review |
| U-02 | REQ-038, EPIC-4-03, A-11 | Three details of the trimming rule are mine: "age" means oldest created first; items are dropped lowest-ranked first across all sections, taking from the fullest section between equals; words are counted as whitespace-separated tokens | Confirm or replace |
| U-03 | REQ-003, REQ-039 | REQ-003 still says proposals have "seven fields"; with DEC-08 a proposal can also carry a source date | Nothing; I will reword REQ-003 to "seven fields plus an optional source date" if you agree |
| T-03 | EPIC-5-05, EPIC-5-04, REQ-035, NFR-006 | The name is kept in "a local configuration file", but NFR-006 says the tool writes only inside the project folder | Choose per-project (asked once per project) or per-user (NFR-006 changes), or leave it to stage 3 |
| T-04 | EPIC-3-03, EPIC-3-04 | Nothing says what happens when the likely duplicate is a Closed item | Decide: still show it, and if so whether merging reopens it |
| T-05 | EPIC-2-04, REQ-023 | Duplicates are only checked during review, never for an item added by hand | Decide whether `raid add` should also show likely duplicates |
| T-06 | EPIC-3-04, EPIC-1-01 | Three small criteria are missing: a merged-in excerpt is visible when viewing the item; a merged proposal with no source date is asked for one (follows from DEC-08); the thin-slice fixture carries source dates | Nothing; I will add them in stage 4 unless you object |
| S-01 | EPIC-3-03, REQ-023 | Duplicate threshold is my number: at least 2 shared key words making up half of the shorter title (A-10) | Confirm, or leave it to be tuned in stage 5 |
| S-03 | EPIC-2-07, REQ-036 | "Decisions needed" is driven by a yes/no mark I introduced (A-9) | Confirm |
| S-04 | EPIC-1-05 | With no year in the sample notes, every due date extracted from them is empty (the source date is now asked for at review, the due date is not) | Accept, or change the due-date rule |
| S-05 | EPIC-2-01 | An item with owner "Priya" is not found by a search for "Priya Nair" | Accept; owners are corrected in review |
| S-06 | EPIC-4-02 | Tom's "what could hurt go-live" and "what Acme needs to do" have no section of their own (DEC-03) | Accept, or ask for them |
| R-07 | EPIC-1-03, EPIC-1-05, EPIC-4-02, EPIC-4-03 | Severity criteria, including the ranking, assume High/Medium/Low | Confirm OQ-01 |
| T-07 | EPIC-1-01 | Largest story (5 REQs); kept whole so the first story is end to end | Accept, or ask me to split `raid list` out |
| R-10 | EPIC-1-05, EPIC-1-06 | Checked by a person running the command in Claude Code, not by pytest; expected items are my reading of the sample notes | Accept; compared with the answer key in stage 5 |
| R-11 | EPIC-2-02, EPIC-4-03 | Walkthrough size (10 items, 4 mine) and worst-case size (40 open items) are my numbers | Confirm or replace |
| R-13 | whole set | About 7,200 words across 26 files, over the 10-minute rule. Story numbers within an epic differ from build order | Nothing; read `docs/epics.md` first, its build-order table is authoritative |
| R-14 | EPIC-2-01, EPIC-2-02, OQ-04 | How the project manager reaches a single-user local file is unanswered | Answer OQ-04 before stage 3 |

Questions still open in `docs/requirements.md` that affect a story but not its readiness: OQ-02, OQ-07, OQ-13 to OQ-18. Each is named in the story it touches.

## Amendment after approval (2026-10-10, during stage 3)

Decisions DEC-10 to DEC-19 added eight criteria: one each to EPIC-1-01, EPIC-1-06, EPIC-2-02, EPIC-2-04, EPIC-3-03 and EPIC-3-04, and two to EPIC-2-03. REQ-042 was added and is covered by EPIC-1-06. There are now 42 requirements and 123 criteria. Coverage, order and criterion form were re-checked by script with no problems. Findings T-03, T-04, T-05, R-07 and R-14 are closed by ADR-005 and decisions DEC-13, DEC-17 and DEC-18.
