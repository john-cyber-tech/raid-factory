# Release note — RAID Log Manager 0.1.0, partial build (Stage 6)

**Status:** DRAFT for the owner · **Date:** 2026-10-11 · **Commit:** `75860c3` on `main`
**Upstream:** `docs/specs/`, `docs/task-dag.md`, `docs/reviews/stage-5-review.md`, `docs/threat-review.md`

**8 of the 25 specs are built.** This is not the full tool described in the brief. By the owner's decision of 2026-10-11 the build stopped after SPEC-EPIC-1-01, 1-02, 1-03, 1-04, 5-01, 5-02, 5-04 and 5-05. This note describes only those. Release is the owner's decision.

## What this build does

Two commands, run from a project folder:

| Command | What it does | Specs |
|---|---|---|
| `raid review` | Checks the whole of `pending.json` and refuses it if any proposal is invalid, listing every problem and changing nothing. Otherwise shows each proposal with its source excerpt and source date and waits for accept, edit or reject. An accepted proposal becomes an item with the next ID for its type (`R-001`, `A-001`, `I-001`, `D-001`). Edits follow the same field rules as the file check; the excerpt and the date of the notes cannot be edited. An item is never stored without the date of the notes. Each decided proposal leaves `pending.json` at once | SPEC-EPIC-1-01, 1-02, 1-03, 1-04 |
| `raid list` | Prints every item: ID, type, title, owner, severity, due date, status | SPEC-EPIC-1-01 |

Behind both:

- The log is saved by write-then-replace, so a crash leaves the old file or the new one; a save that would drop an item is refused; a damaged log stops the command and is never overwritten (SPEC-EPIC-5-01).
- Every item carries an append-only history: who accepted it and when, and which fields were edited before the accept (SPEC-EPIC-5-02).
- The user's name is asked once, on the first accept, and kept in `raid-config.json` (SPEC-EPIC-5-05).
- No network call, no API key, nothing written outside the project folder (SPEC-EPIC-5-04).

## Install and run

Python 3.12 or later.

    pip install -e .
    pip install -e ".[test]" && pytest     # 329 tests

Then, in a project folder holding a `pending.json`: `raid review`, then `raid list`. The README section "Using the tool" has the detail. An example file is `tests/fixtures/pending/valid_three.json`.

There is no extraction command in this build. `pending.json` has to be written by hand or copied from a fixture.

## How the built NFRs were verified

Suite run on 2026-10-11, Python 3.13.9: 329 passed, none failed, none skipped.

| NFR | Verified by | Result |
|---|---|---|
| NFR-002 crash leaves the log whole | `tests/test_spec_epic_5_01.py`: a failure injected at each step of a save | Passed |
| NFR-003 accepted items are never lost | `tests/test_spec_epic_5_01.py`: 27 command sequences, an interrupted review, the save guard | Passed, with the limit in G-03(a) below |
| NFR-004 no network, no key | `tests/test_boundaries.py`: suite run with sockets blocked; import check of `src/`; commands run with no key set. Imports also read by hand at stage 6 | Passed |
| NFR-006 data stays in local files | `tests/test_boundaries.py`: no write outside the project folder | Passed, within the limits of stage 5 notes N-06 and N-08 |
| NFR-007 history is append-only | `tests/test_spec_epic_5_02.py` | Passed for the two ways an item can change today (accept, and the store's update routine, which no command reaches yet). G-08 is open |
| NFR-010 Python 3.12 or later, tests need no Claude session | Suite run on Python 3.13.9 from fixture files. 3.12 by the declared minimum version only; **not run on 3.12** | Passed on 3.13. Each of the 13 requirements the built specs cover is cited in at least one test file |

**Not verified, because the specs that carry them are not built:** NFR-005 notes as data, never instructions (SPEC-EPIC-1-06); NFR-008 weekly update under 5 minutes (SPEC-EPIC-2-02), so the timed walkthrough was not done; NFR-009 summary within 400 words (SPEC-EPIC-4-03). NFR-001 performance has no target (OQ-11).

## Not in this build

**Deferred (2 specs):** SPEC-EPIC-1-05 `/raid-extract` writes proposals from a notes file, and SPEC-EPIC-1-06 extraction ignores instructions hidden in notes. Work on 1-05 is parked on branch `wip/spec-1-05`; it needs six manual runs by the owner. 1-06 was not started.

**Out of scope for this run (15 specs, not started):**

| Area | Specs |
|---|---|
| Working with items | SPEC-EPIC-2-01 list only my items · 2-02 update an item · 2-03 status, and closing with a reason · 2-04 add an item by hand · 2-05 check note and waiting-on party · 2-06 view one item in full · 2-07 mark an item as needing a decision |
| Flags and duplicates | SPEC-EPIC-3-01 unowned and overdue · 3-02 stale · 3-03 likely duplicates during review · 3-04 merge a proposal into an item |
| Weekly summary | SPEC-EPIC-4-01, 4-02, 4-03 |
| Data safety | SPEC-EPIC-5-03 items are never deleted |

Also not built: the save-guard step G-08, and the end-to-end test the stage 5 command asks for.

## Known limits of what is built

From `docs/threat-review.md` (findings F-01 to F-05) and the open gaps in `docs/reviews/stage-5-review.md`:

- An item cannot be changed, closed or viewed in full once accepted; only listed.
- `raid list` prints what is in the log as stored. A log edited by hand is not checked field by field: odd characters reach the terminal (F-01), a missing field ends in an error trace (F-02), and a changed field is not noticed (F-03). The history is not tamper-evident.
- The three files are plain text, readable by other users of the same machine (F-04). `.gitignore` covers `raid-log.json` only (F-05, G-06).
- If the log is saved but `pending.json` cannot then be trimmed, the proposal is shown again and a second accept makes a second item (G-03a). A failed disk write shows a Python error trace (G-03b).
- The name in the history is whatever was typed; it is not verified. A damaged `raid-config.json` is replaced without a message (G-06).
- History times have no time zone (G-07).
- The 80-character title limit counts code points, so some accented or emoji titles count longer than they look (G-10).
- All messages go to standard output (G-04). An empty owner or due date shows as `-`, and an empty log shows the header only (G-01, G-02); no test pins these.
- A log written before SPEC-EPIC-5-02 is refused as damaged; there is no migration (stage 5 note N-10).
- Open and undecided: G-08, G-11, G-13; and G-12, G-16, G-17, which belong to the parked extraction path.

## Suggested next steps

Suggestions only; scope is the owner's call.

1. Decide the five findings in `docs/threat-review.md`.
2. Do the six manual runs for SPEC-EPIC-1-05, then build SPEC-EPIC-1-06 before merging either, and repeat the threat review for the extraction path.
3. Build G-08, then SPEC-EPIC-2-06 and 2-02, following `docs/task-dag.md`.
