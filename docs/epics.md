# RAID Log Manager — Epics (Stage 2)

**Status:** DRAFT (awaiting review) · **Date:** 2026-10-10 · **Upstream:** `docs/requirements.md` (approved 2026-10-10)

Five epics, 25 stories. Amended 2026-10-10 with decisions DEC-01 to DEC-22 (`docs/requirements.md` section 4). Epics are listed in delivery order; the exact story order is in the last section. Stories are in `docs/stories/`.

## EPIC-1 — Extraction and review

**Goal:** Notes become proposals in `pending.json`, and only proposals the manager accepts in `raid review` enter the log.

**Covers:** NFR-005, NFR-010, REQ-001, REQ-002, REQ-003, REQ-004, REQ-005, REQ-006, REQ-007, REQ-008, REQ-009, REQ-010, REQ-011, REQ-012, REQ-014, REQ-039, REQ-040, REQ-041, REQ-042

**Sequence rationale:** First. EPIC-1-01 is the end-to-end thin slice (fixture proposals → review → log → list) that every other story builds on. The `/raid-extract` command itself (EPIC-1-05, EPIC-1-06) comes after the schema is settled, because the CLI is built and tested from fixture files.

| Story | Title | Size | Covers | Open questions |
|---|---|---|---|---|
| EPIC-1-01 | Review fixture proposals into the log and list them (thin slice) | M | REQ-007, REQ-008, REQ-010, REQ-011, REQ-014, NFR-010 | — |
| EPIC-1-02 | Reject invalid extraction output | S | REQ-005, REQ-006, REQ-041 | — |
| EPIC-1-03 | Edit a proposal before accepting it | S | REQ-009, REQ-041 | — |
| EPIC-1-04 | Keep the source excerpt and date with every item | S | REQ-012, REQ-040 | — |
| EPIC-1-05 | `/raid-extract` writes proposals from a notes file | M | REQ-001, REQ-002, REQ-003, REQ-004, REQ-039 | — |
| EPIC-1-06 | Extraction ignores instructions hidden in notes | S | REQ-042, NFR-005 | — |

## EPIC-5 — Data safety and audit

**Goal:** The log survives crashes, never loses or deletes an item, keeps a history of every change, and stays on the local machine.

**Covers:** NFR-002, NFR-003, NFR-004, NFR-006, NFR-007, REQ-019, REQ-020, REQ-035

**Sequence rationale:** Second, and interleaved. Atomic writes (EPIC-5-01), the no-network guard (EPIC-5-04), the user name (EPIC-5-05) and history (EPIC-5-02) go in straight after the thin slice, so every later story records its changes from the start and none has to be reworked to add history.

| Story | Title | Size | Covers | Open questions |
|---|---|---|---|---|
| EPIC-5-01 | Log writes are atomic and never lose accepted items | S | NFR-002, NFR-003 | — |
| EPIC-5-04 | The tool stays local: no network, no API key | S | NFR-004, NFR-006 | — |
| EPIC-5-05 | Ask for my name once and remember it | S | REQ-035 | — |
| EPIC-5-02 | Every change to an item is recorded in an append-only history | M | REQ-020, NFR-007 | — |
| EPIC-5-03 | Items are never deleted | S | REQ-019 | — |

## EPIC-2 — Log management

**Goal:** People can see their own items, update them, close them with a reason, add items by hand, and record the type-specific details for assumptions and dependencies.

**Covers:** NFR-008, REQ-011, REQ-013, REQ-015, REQ-016, REQ-017, REQ-018, REQ-021, REQ-022, REQ-034, REQ-036, REQ-041

**Sequence rationale:** Third. Needs items in the log (EPIC-1) and history (EPIC-5-02) so every update is recorded from the first day it exists.

| Story | Title | Size | Covers | Open questions |
|---|---|---|---|---|
| EPIC-2-06 | View one item in full | S | REQ-034 | — |
| EPIC-2-02 | Update an item | S | REQ-011, REQ-016, REQ-041, NFR-008 | — |
| EPIC-2-01 | List only my items | S | REQ-015 | — |
| EPIC-2-03 | Status, and closing an item with a reason | S | REQ-016, REQ-017, REQ-018 | — |
| EPIC-2-05 | Check note on assumptions, waiting-on party on dependencies | S | REQ-021, REQ-022 | — |
| EPIC-2-04 | Add an item by hand | S | REQ-013, REQ-041 | — |
| EPIC-2-07 | Mark an item as needing a decision | S | REQ-036 | — |

## EPIC-3 — Flags and duplicates

**Goal:** Unowned, overdue and stale items are made obvious, and a repeated item is merged instead of recorded twice.

**Covers:** REQ-023, REQ-024, REQ-025, REQ-026, REQ-027

**Sequence rationale:** Fourth. Flags need owner, due date, status and last-changed data from EPIC-2 and EPIC-5. Duplicate detection plugs into the review flow from EPIC-1.

| Story | Title | Size | Covers | Open questions |
|---|---|---|---|---|
| EPIC-3-01 | Flag unowned and overdue items | S | REQ-025, REQ-026 | — |
| EPIC-3-02 | Flag stale items | S | REQ-027 | — |
| EPIC-3-03 | Show likely duplicates during review | M | REQ-023 | — |
| EPIC-3-04 | Merge a proposal into an existing item | M | REQ-024 | — |

## EPIC-4 — Weekly summary

**Goal:** One command produces a short markdown RAID summary the delivery manager can send to the sponsor.

**Covers:** NFR-009, REQ-028, REQ-029, REQ-030, REQ-031, REQ-032, REQ-033, REQ-037, REQ-038

**Sequence rationale:** Last. It only reads the log, and reuses the overdue rule (EPIC-3), status (EPIC-2), waiting-on (EPIC-2) and creation dates (EPIC-5).

| Story | Title | Size | Covers | Open questions |
|---|---|---|---|---|
| EPIC-4-01 | Generate the weekly summary with new and overdue items | M | REQ-028, REQ-029, REQ-030 | — |
| EPIC-4-02 | Summary shows top risks, what is blocked by whom, and decisions needed | S | REQ-031, REQ-032, REQ-037 | — |
| EPIC-4-03 | Summary shows owners and never exceeds 400 words | M | REQ-033, REQ-038, NFR-009 | — |

## Build order

Each story depends only on stories above it.

| # | Story | Depends on |
|---|---|---|
| 1 | EPIC-1-01 Review fixture proposals into the log and list them (thin slice) | — |
| 2 | EPIC-5-01 Log writes are atomic and never lose accepted items | EPIC-1-01 |
| 3 | EPIC-5-04 The tool stays local: no network, no API key | EPIC-1-01 |
| 4 | EPIC-5-05 Ask for my name once and remember it | EPIC-1-01 |
| 5 | EPIC-5-02 Every change to an item is recorded in an append-only history | EPIC-1-01, EPIC-5-01, EPIC-5-05 |
| 6 | EPIC-1-02 Reject invalid extraction output | EPIC-1-01 |
| 7 | EPIC-1-03 Edit a proposal before accepting it | EPIC-1-01, EPIC-1-02 |
| 8 | EPIC-1-04 Keep the source excerpt and date with every item | EPIC-1-01 |
| 9 | EPIC-1-05 `/raid-extract` writes proposals from a notes file | EPIC-1-02, EPIC-1-04 |
| 10 | EPIC-1-06 Extraction ignores instructions hidden in notes | EPIC-1-05 |
| 11 | EPIC-2-06 View one item in full | EPIC-1-04, EPIC-5-02 |
| 12 | EPIC-2-02 Update an item | EPIC-5-02 |
| 13 | EPIC-2-01 List only my items | EPIC-1-01 |
| 14 | EPIC-2-03 Status, and closing an item with a reason | EPIC-2-02, EPIC-2-06 |
| 15 | EPIC-2-05 Check note on assumptions, waiting-on party on dependencies | EPIC-1-03, EPIC-2-02, EPIC-2-06 |
| 16 | EPIC-2-04 Add an item by hand | EPIC-1-04, EPIC-5-02, EPIC-2-06 |
| 17 | EPIC-2-07 Mark an item as needing a decision | EPIC-2-02, EPIC-2-06 |
| 18 | EPIC-3-01 Flag unowned and overdue items | EPIC-2-03 |
| 19 | EPIC-3-02 Flag stale items | EPIC-3-01, EPIC-5-02 |
| 20 | EPIC-3-03 Show likely duplicates during review | EPIC-1-03 |
| 21 | EPIC-3-04 Merge a proposal into an existing item | EPIC-3-03, EPIC-5-02, EPIC-2-03 |
| 22 | EPIC-5-03 Items are never deleted | EPIC-2-03, EPIC-3-04 |
| 23 | EPIC-4-01 Generate the weekly summary with new and overdue items | EPIC-3-01, EPIC-5-02 |
| 24 | EPIC-4-02 Summary shows top risks, what is blocked by whom, and decisions needed | EPIC-4-01, EPIC-2-05, EPIC-2-07 |
| 25 | EPIC-4-03 Summary shows owners and never exceeds 400 words | EPIC-4-02 |

## Not mapped

| ID | Why |
|---|---|
| NFR-001 | Performance: "none identified" in stage 1, so there is nothing to build or test until OQ-11 is answered |

## Questions raised in stage 2 (answered)

These continue the numbering in `docs/requirements.md` section 4. All three defaults were accepted on 2026-10-10 (decision DEC-07) and are applied in the stories.

| ID | Question | Accepted answer | Affects |
|---|---|---|---|
| OQ-21 | When notes repeat an item already raised in the same notes (sample notes line 8 repeats line 4), should extraction propose it once or twice? | Once, with the fuller statement as the excerpt | EPIC-1-05 |
| OQ-22 | Should an owner filter match part of a name ("Priya" finding "Priya Nair")? Notes use first names | Exact match, ignoring case | EPIC-2-01 |
| OQ-23 | Notes give dates without a year ("25 Oct"). Which year does extraction use? | The year of the notes date; left empty if that is unknown | EPIC-1-05 |
