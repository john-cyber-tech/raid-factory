# Threat review — RAID Log Manager 0.1.0 (Stage 6)

**Status:** DRAFT for the owner, second pass · **Date:** 2026-10-11 · **First reviewed at commit:** `75860c3`; findings F-01, F-02, F-04 and F-05 fixed in `94dcfb1` and re-verified there, on `main`
**Upstream:** `docs/architecture.md`, ADR-001 to ADR-006, `docs/specs/` (the 8 built specs), `docs/reviews/stage-5-review.md`
**Scope (owner's instruction, 2026-10-11):** only what is built on `main`: SPEC-EPIC-1-01, 1-02, 1-03, 1-04, 5-01, 5-02, 5-04, 5-05. The extraction path (SPEC-EPIC-1-05, 1-06) is parked and is listed in section 6 as a known risk, not reviewed as built. The 15 out-of-scope specs are not reviewed.

Scores are Likelihood × Impact, each 1 to 5 (Low 1–4, Medium 5–9, High 10–14, Critical 15–25). They are my draft, with the controls in place; the owner calibrates and decides.

## 1. What is on `main`, and its data flow

```
pending.json (written by hand or copied from a fixture)
   → raid review: validator (whole file) → one screen per proposal → a/e/r by a person
   → raid-log.json (store, atomic save, save guard)        raid-config.json (the user's name)
   → raid list: prints the log to the terminal
```

Everything is a local file in the project folder. There is no model call, no network, no service, no account. **Trust boundaries:** (1) `pending.json` is untrusted input, whoever wrote it; (2) the terminal the tool prints to; (3) the project folder itself: anyone who can write there can change all three files.

**AI-specific properties present on `main`:** none. The Python tool reads no natural language as instructions, retrieves nothing and takes no action without a person's keystroke. All three properties arrive with the parked extraction command (section 6).

**Blast radius:** one project folder per run: one `raid-log.json`. The tool never reads or writes outside it (tested). How many projects and people that means in use is not stated in the brief.

## 2. Built controls

| # | Control | Where | Evidence (test) |
|---|---|---|---|
| C-01 | The whole of `pending.json` is checked before any proposal is shown; one bad proposal refuses the file; the bad file is left as it is | `src/raid/validator.py`, `src/raid/schemas/pending.schema.json`, `review.py` | `test_one_bad_proposal_rejects_all`, `test_contract_violations_are_rejected` (71 cases) |
| C-02 | Control characters and text-direction controls are refused in every text field; a key written twice refuses the file; unknown keys are refused | schema, `validator.py` (`_Object`) | `test_control_characters_are_rejected`, `test_contract_violations_are_rejected` |
| C-03 | A refused value is never printed raw: at most 40 characters, control and invisible formatting characters shown as `?` | `validator.py` (`_safe`) | `test_bad_values_are_not_echoed_raw` (7 cases) |
| C-04 | Nothing reaches the log without a person's explicit accept, one proposal at a time, with the source excerpt on screen | `review.py` | `test_review_shows_excerpt_and_waits`, `test_review_accept_reject_accept` |
| C-05 | Edits during review go through the same field rules as the contract; the source excerpt and source date cannot be edited | `rules.py`, `review.py` | `test_rules_match_the_contract`, `test_excerpt_cannot_be_edited`, `test_source_date_cannot_be_edited`, `test_store_updates_use_the_same_rules` |
| C-06 | No item without a source excerpt and a real source date; a date after today is refused at accept | `rules.py`, `store.py`, `review.py` | `test_store_requires_a_source_to_add_an_item`, `test_carried_future_source_date_never_reaches_the_log` |
| C-07 | Saves are write-temporary, sync, replace: a crash leaves the old or the new file | `src/raid/atomic.py` | `test_failure_at_each_step_is_all_or_nothing`, `test_failure_before_replace_keeps_old_log` |
| C-08 | Save guard: a save that would drop an item, or alter or drop a history entry, is refused | `store.py` (`_save`) | `test_save_guard_refuses_dropped_item`, `test_save_guard_refuses_altered_history`, `test_no_id_lost_across_command_sequences` |
| C-09 | A damaged log stops every command and is never overwritten | `store.py` (`_read`, `_problem`) | `test_damaged_log_is_never_overwritten`, `test_item_without_history_is_a_damaged_log`, `test_counter_behind_existing_id_is_damaged` |
| C-10 | A change and its history entry are one write; history is append-only through the store | `store.py` | `test_change_and_its_history_are_one_write`, `test_existing_entries_never_change` |
| C-11 | No network: sockets are blocked for the whole suite; `src/` imports no network or process module | `tests/conftest.py`, `tests/boundary_check.py` | `test_suite_runs_with_sockets_blocked`, `test_no_network_imports_in_src`, `test_import_check_catches_a_planted_import` (22 planted cases) |
| C-12 | No key needed; the only declared dependency is `jsonschema`, pinned | `pyproject.toml` | `test_commands_work_without_api_keys`, `test_only_declared_dependency_is_jsonschema` |
| C-13 | Nothing is written outside the project folder | all writes go through `atomic.py` | `test_no_writes_outside_project_folder`, `test_outside_watch_catches_a_planted_write` |
| C-14 | No invisible characters in the source or docs (guard for defect D-01) | — | `test_no_invisible_characters_in_source` |
| C-15 | What `raid list` and the review screen print is masked with the field rules: a control or text-direction character shows as `?`. An item ID quoted in a damaged-log or refused-save message is masked too. Added in `94dcfb1` for F-01 | `rules.py` (`mask`, `mask_long_text`), `cli.py`, `review.py`, `store.py` | `test_list_masks_control_and_direction_characters` (54 cases), `test_review_screen_masks_one_line_fields` (48), `test_review_screen_masks_long_text_but_keeps_line_breaks`, `test_damaged_log_message_masks_the_item_id` |
| C-16 | A log item with a field missing, or holding something other than text, is a damaged log: plain message, exit 1, nothing written. Only owner and due date may be empty. Added in `94dcfb1` for F-02 | `store.py` (`_problem`) | `test_log_item_with_a_missing_field_is_a_damaged_log` (7), `test_log_item_with_a_field_that_is_not_text_is_a_damaged_log` (9) |
| C-17 | The three data files are written readable by their owner only (mode 0600), also over a wider file or a wider leftover temporary file. Added in `94dcfb1` for F-04 | `atomic.py` | `test_data_files_are_created_private`, `test_wider_file_and_leftover_temp_become_private_on_next_save` |
| C-18 | This repo's `.gitignore` covers all three data files. Added in `94dcfb1` for F-05 | `.gitignore` | `test_gitignore_keeps_the_data_files_out_of_this_repo` |

**Checked by hand for this review, 2026-10-11:**

- Imports in `src/raid/`: `argparse`, `copy`, `json`, `os`, `re`, `sys`, `unicodedata`, `datetime`, `pathlib`, `jsonschema` and the package's own modules. No `socket`, `urllib`, `http`, `requests`, `subprocess`, `os.system`, `eval`, `exec` or `pickle`. No environment variable is read. The one URL in `src/` is the `$schema` identifier in `pending.schema.json`; the suite passes with sockets blocked.
- Logging: the `logging` module is not used. The tool writes nothing but its three JSON files and what it prints to the terminal. No telemetry.
- Secrets: `git grep` over tracked files for key, token, password and private-key patterns found nothing. No `.env`, key file, `raid-log.json`, `raid-config.json` or `pending.json` is tracked.

## 3. Threats to the built tool

| # | Threat | Class · property · asset | Controls | Residual | L×I |
|---|---|---|---|---|---|
| TH-01 | A malformed or tampered `pending.json` puts bad data in the log or on the screen | Classical: input validation · Integrity · the log, the terminal | C-01 to C-06 | A well-formed but false proposal is stopped only by the person reading it. Some invisible characters are not in the refused set; they are named in section 3a (the refused list is in G-11) | 2×2 = 4 Low |
| TH-02 | A hand-edited or tampered `raid-log.json` prints terminal escape or text-direction characters through `raid list` | Classical: output encoding · Integrity · the terminal | C-15, C-16 | F-01 closed. The masked set is the rules' set, so the characters named in section 3a are still printed | 1×2 = 2 Low |
| TH-03 | A crash or disk fault loses or corrupts the log | Classical: data loss · Availability, Integrity · the log | C-07 to C-10 | No folder sync after the replace, so the very last save may not survive a power loss (stage 5 note N-04). A failed disk write ends in a Python error trace, not a plain message (G-03b). An accept can be repeated after a failed trim of `pending.json` and make a second item (G-03a) | 1×3 = 3 Low |
| TH-04 | Someone with access to the folder changes items or history by editing `raid-log.json` | Classical: tampering, access control · Integrity · the audit history | C-09 and C-16 catch only a damaged file | **Finding F-03, accepted by the owner on 2026-10-11 as a documented design limit.** The history is append-only against the tool, not against a text editor. It is not tamper-evident | 2×3 = 6 Medium |
| TH-05 | Client or project data in the three JSON files is read by another user of the machine, or committed to a repository | Classical: data exposure · Confidentiality · notes excerpts, names | C-17, C-18 | F-04 and F-05 closed. The files are still plain text, not encrypted. A file written by an earlier build keeps its mode until the tool next writes it, and the name file is written once only. A project folder kept in another git repository needs its own ignore lines (README) | 2×3 = 6 Medium |
| TH-06 | Sensitive data leaks through logs or error output | Classical: data exposure · Confidentiality · excerpts | No logging; C-03 | Source excerpts are shown on the review screen by design. F-02 closed. A failed disk write still ends in a Python error trace (G-03b), which shows file paths, not field values | 1×2 = 2 Low |
| TH-07 | The tool or a dependency sends data out, or a dependency is compromised | Classical: exfiltration, supply chain · Confidentiality · all data | C-11 to C-13 | `jsonschema` is pinned at 4.25.0; the packages it pulls in are not pinned. **No dependency scan was run** for this review. The socket block does not cover the one test that starts a child process, and a write to an absolute path outside the watched folder would not be seen (stage 5 notes N-06, N-08) | 1×4 = 4 Low |
| TH-08 | An item's history names the wrong person | Classical: spoofing · Integrity · the audit history | None, by decision: the name is self-declared (ADR-005) | Anyone can type any name; a damaged `raid-config.json` is replaced without a word (G-06) | 2×2 = 4 Low |

## 3a. Characters left unmasked and unrefused

The rules refuse, and the output masks, U+0000 to U+001F, U+007F to U+009F, U+2028, U+2029, U+202A to U+202E and U+2066 to U+2069. Checked by running `rules.mask` over every code point on 2026-10-11 (Python 3.13.9, Unicode 15.1.0): 161 invisible formatting characters (Unicode category Cf) pass through unchanged, in `pending.json` and on the screen. An earlier draft of this review named four of them; this is the full list.

| Group | Characters |
|---|---|
| Zero-width (5) | U+200B zero width space · U+200C zero width non-joiner · U+200D zero width joiner · U+2060 word joiner · U+FEFF zero width no-break space (byte order mark) |
| Direction marks (2) | U+200E left-to-right mark · U+200F right-to-left mark |
| A third direction mark (1) | U+061C Arabic letter mark |
| Other invisible or formatting characters below U+3000 (23) | U+00AD soft hyphen · U+0600 to U+0605, U+06DD, U+070F, U+0890, U+0891, U+08E2 (Arabic and Syriac number and abbreviation marks) · U+180E Mongolian vowel separator · U+2061 to U+2064 (invisible mathematical operators) · U+206A to U+206F (deprecated shaping and swapping controls) |
| Higher ranges (130) | U+FFF9 to U+FFFB (interlinear annotation) · U+110BD, U+110CD · U+13430 to U+1343F · U+1BCA0 to U+1BCA3 · U+1D173 to U+1D17A · U+E0001 and U+E0020 to U+E007F (tag characters, 97, which can carry hidden text) |

What they can do: none moves the cursor or changes colour as an escape sequence does. They can hide a difference between two titles that look the same, shift how a line reads, or carry text a person cannot see. The embedding, override and isolate controls that reorder a whole line are refused and masked. Zero-width joiners are also part of ordinary text in some scripts and in joined emoji, so refusing them all is a decision for the owner under G-11, not a fix made here.

## 4. Findings from this review

The owner decided all five on 2026-10-11. F-01, F-02, F-04 and F-05 were fixed together, tests first, in commit `94dcfb1`. Before the code changed, the new file `tests/test_threat_review_findings.py` ran as 125 collected, 124 failed, 1 passed, each failure on its own assertion; the one that passed (`test_empty_owner_and_due_date_are_still_a_valid_log`) checks behaviour that must not change. After the fix: 125 passed, whole suite 454 passed.

| # | Finding | Evidence | State |
|---|---|---|---|
| F-01 | `raid list` prints item fields from the log as stored. Field values are not checked when a log is loaded, only its structure | Scratch run, 2026-10-11: a log whose title held an escape sequence and U+202E listed with exit 0 and the characters sent to the terminal | **Closed in `94dcfb1`** (C-15). Scratch run repeated: the escape and U+202E show as `?` |
| F-02 | An item in the log with a key missing (for example no `title`) ends `raid list` in a Python `KeyError` trace, exit 1, nothing written | Same scratch run | **Closed in `94dcfb1`** (C-16). Scratch run repeated: "raid-log.json is not a valid log: R-001 has no title. The file was not changed.", exit 1. A field that is not text is refused the same way; that part is my addition, because it ended in the same error trace |
| F-03 | A hand edit of an item's fields or status, with the history left alone, loads and lists as normal | Same scratch run: title and status changed by hand, exit 0 | **Accepted by the owner, 2026-10-11, as a documented design limit.** ADR-006 and NFR-007 promise only that no command alters history. Stated in the release note |
| F-04 | The three files are created with mode 0644: readable by every user on a shared machine | `src/raid/atomic.py` line 10; `ls -l` in the scratch folder | **Closed in `94dcfb1`** (C-17) |
| F-05 | `.gitignore` covers `raid-log.json` only | `.gitignore`; already in G-06 | **Closed in `94dcfb1`** (C-18), with a line in the README for project folders kept in git |

## 5. Open spec gaps, by ID

All are open in `docs/reviews/stage-5-review.md`. "Security" says whether the gap bears on a threat above. **The owner accepted all 13 for this build on 2026-10-11.** They stay open.

| Gap | What is open | Security |
|---|---|---|
| G-01 | How an empty owner or due date is shown (`-` today, not pinned by a test) | None |
| G-02 | What `raid list` prints for an empty log (header only today) | None |
| G-03 | (a) a repeated accept after a failed trim makes a second item; (b) a failed disk write shows an error trace | TH-03 |
| G-04 | Whether messages go to standard output or standard error (all to output today) | None |
| G-06 | A damaged `raid-config.json` is silently replaced. The `.gitignore` part was fixed in `94dcfb1` | TH-08 |
| G-07 | History timestamps carry no time zone | TH-04: weakens the history as evidence across machines or a clock change |
| G-08 | The save guard does not refuse a field change that has no history entry. Not built. No command can make such a save today | TH-04. Must be built before SPEC-EPIC-2-02 |
| G-10 | The 80-character title limit counts code points, not displayed characters | None |
| G-11 | The list of refused control characters is the owner's decisions plus one addition of mine, not from the contract text | TH-01 |
| G-12 | Line endings in a word-for-word excerpt: decided, but the two parts that carry it out are on `wip/spec-1-05` only | Parked path, section 6 |
| G-13 | Four details of editing a proposal that the spec does not state | TH-01: decides what a reviewer can and cannot change |
| G-16 | Whether Claude Code honours `Write(pending.json)` in a command's front matter is unconfirmed; `Read` cannot be tied to one file | Parked path, section 6 |
| G-17 | `/raid-extract` would overwrite undecided proposals in `pending.json` | Parked path, section 6 |

## 6. Known, parked risk: the extraction path (SPEC-EPIC-1-05, SPEC-EPIC-1-06)

**Not built, not on `main`, not reviewed here as a control.** The prompt, its output check, tests and manual check steps are on branch `wip/spec-1-05` (commit `bf0eab3`); the owner's six manual runs have not been done. SPEC-EPIC-1-06 was not started.

When that path exists, the flow gains a step in front: notes file → Claude Code session → `pending.json`. That step carries the threats the stage 6 command names and this review cannot assess:

| Threat | Class | State today |
|---|---|---|
| Instructions hidden in notes make the session write another file, run a command or open the log (REQ-042, NFR-005) | AI: prompt injection (OWASP LLM01), excessive agency (LLM06) · Integrity | No control built or tested. The fenced notes block, the `allowed-tools` limit and its tests, the two trap fixtures and the manual trap checks are all SPEC-EPIC-1-06. G-16 is unconfirmed |
| Client data in notes is handled in an AI session | AI: sensitive information disclosure (LLM02) · Confidentiality | Outside the Python tool. Needs the owner's sign-off on client approval (OQ-08) before real notes are used |
| Extraction replaces undecided proposals | Classical: data loss · Availability | G-17, open |

**Accepted by the owner on 2026-10-11, on three conditions:** (1) this review is repeated before `wip/spec-1-05` is merged; (2) SPEC-EPIC-1-05 does not ship without SPEC-EPIC-1-06; (3) G-16 is settled first. No expiry date was given.

On `main` the exposure is nil in practice, because there is no extraction command. It becomes real when `wip/spec-1-05` is merged, or when anyone makes a `pending.json` from real notes with an assistant outside this tool. Then C-01 to C-06 still stand between a bad proposal and the log, but nothing here limits what the session itself does. 

## 7. Verification log

Run on 2026-10-11, Python 3.13.9, commit `94dcfb1`, from the repo root. Every command from the first pass was run again after the fix.

| Control | Command | Result |
|---|---|---|
| All | `python3 -m pytest -q -rs` | 454 passed, none failed, none skipped (329 before the fix, plus 125 new) |
| C-11 to C-14 | `python3 -m pytest -q tests/test_boundaries.py` | 29 passed |
| C-11, C-13, C-14 bypass cases (planted import, planted write, invisible character) | `python3 -m pytest -q tests/test_boundaries.py -k 'planted or invisible'` | 24 passed |
| C-01, C-02 | `python3 -m pytest -q tests/test_spec_epic_1_02.py` | 124 passed |
| C-03 | `python3 -m pytest -q tests/test_spec_epic_1_02.py -k bad_values_are_not_echoed_raw` | 7 passed |
| C-05 | `python3 -m pytest -q tests/test_spec_epic_1_03.py -k 'cannot_be_edited or same_rules'` | 9 passed |
| C-06 | `python3 -m pytest -q tests/test_spec_epic_1_04.py -k 'future or cannot_be_emptied'` | 11 passed |
| C-07 to C-09 | `python3 -m pytest -q tests/test_spec_epic_5_01.py` | 46 passed |
| C-08 | `python3 -m pytest -q tests/test_spec_epic_5_02.py -k 'save_guard or never_change'` | 2 passed |
| C-15 to C-18 | `python3 -m pytest -q tests/test_threat_review_findings.py` | 125 passed |
| C-15 (escape, bell, C1 control, direction override, isolate, line separator, line break, tab) | `python3 -m pytest -q tests/test_threat_review_findings.py -k masks` | 105 passed |
| C-16, and the masked ID | `python3 -m pytest -q tests/test_threat_review_findings.py -k damaged_log` | 17 passed |
| C-17 | `python3 -m pytest -q tests/test_threat_review_findings.py -k private` | 2 passed |
| C-18 | `python3 -m pytest -q tests/test_threat_review_findings.py -k gitignore` | 1 passed |

The guard C-14 caught a mistake of mine during the fix: the first version of the new test file held literal invisible characters, the same slip as defect D-01. They were replaced with escapes before the commit.

Also repeated at `94dcfb1`: the search of `src/` for network, process, environment and logging use (no match) and the secrets search (one match, this document's own sentence about the search).

Not run: a dependency scan, a static security scanner, any test on Python 3.12, any test of the extraction path. The mode test assumes a POSIX file system; it has not been run on Windows.

## 8. Decisions

**Made by the owner on 2026-10-11:**

1. F-01, F-02, F-04 and F-05 sent back and fixed (`94dcfb1`). F-03 accepted as a documented design limit.
2. The parked extraction risk accepted on the three conditions in section 6.
3. The 13 open gaps in section 5 accepted for this build.
4. **Release condition, not yet met:** a dependency scan, starting with pinning the packages `jsonschema` pulls in (`attrs`, `jsonschema-specifications`, `referencing`, `rpds-py`), before anyone else gets the build.

**Still the owner's to make:**

1. Release, once condition 4 is met.
2. The two Medium rows that remain after the fix, TH-04 (covered by the F-03 decision) and TH-05 (plain-text files).
3. OQ-08: client approval for notes in an AI session. Not needed for what is on `main`; needed before extraction is used on real notes.
