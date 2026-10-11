# Threat review — RAID Log Manager 0.1.0 (Stage 6)

**Status:** DRAFT for the owner · **Date:** 2026-10-11 · **Reviewed at commit:** `75860c3` on `main`
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

**Checked by hand for this review, 2026-10-11:**

- Imports in `src/raid/`: `argparse`, `copy`, `json`, `os`, `re`, `sys`, `unicodedata`, `datetime`, `pathlib`, `jsonschema` and the package's own modules. No `socket`, `urllib`, `http`, `requests`, `subprocess`, `os.system`, `eval`, `exec` or `pickle`. No environment variable is read. The one URL in `src/` is the `$schema` identifier in `pending.schema.json`; the suite passes with sockets blocked.
- Logging: the `logging` module is not used. The tool writes nothing but its three JSON files and what it prints to the terminal. No telemetry.
- Secrets: `git grep` over tracked files for key, token, password and private-key patterns found nothing. No `.env`, key file, `raid-log.json`, `raid-config.json` or `pending.json` is tracked.

## 3. Threats to the built tool

| # | Threat | Class · property · asset | Controls | Residual | L×I |
|---|---|---|---|---|---|
| TH-01 | A malformed or tampered `pending.json` puts bad data in the log or on the screen | Classical: input validation · Integrity · the log, the terminal | C-01 to C-06 | A well-formed but false proposal is stopped only by the person reading it. Zero-width and direction-mark characters U+200B, U+200E, U+200F and U+FEFF are not in the refused set (the refused list is in G-11) | 2×2 = 4 Low |
| TH-02 | A hand-edited or tampered `raid-log.json` prints terminal escape or text-direction characters through `raid list` | Classical: output encoding · Integrity · the terminal | None. C-02 and C-03 protect only the `pending.json` path | **Finding F-01** | 2×2 = 4 Low |
| TH-03 | A crash or disk fault loses or corrupts the log | Classical: data loss · Availability, Integrity · the log | C-07 to C-10 | No folder sync after the replace, so the very last save may not survive a power loss (stage 5 note N-04). A failed disk write ends in a Python error trace, not a plain message (G-03b). An accept can be repeated after a failed trim of `pending.json` and make a second item (G-03a) | 1×3 = 3 Low |
| TH-04 | Someone with access to the folder changes items or history by editing `raid-log.json` | Classical: tampering, access control · Integrity · the audit history | C-09 catches only a structurally damaged file | **Finding F-03.** The history is append-only against the tool, not against a text editor. It is not tamper-evident | 2×3 = 6 Medium |
| TH-05 | Client or project data in the three JSON files is read by another user of the machine, or committed to a repository | Classical: data exposure · Confidentiality · notes excerpts, names | `raid-log.json` is in this repo's `.gitignore` | **Findings F-04, F-05.** Plain text, files created readable by every user of the machine, and `pending.json` and `raid-config.json` are not ignored by git (G-06) | 3×3 = 9 Medium |
| TH-06 | Sensitive data leaks through logs or error output | Classical: data exposure · Confidentiality · excerpts | No logging; C-03 | Source excerpts are shown on the review screen by design. A Python error trace (F-02, G-03b) shows file paths and a field name, not field values | 1×2 = 2 Low |
| TH-07 | The tool or a dependency sends data out, or a dependency is compromised | Classical: exfiltration, supply chain · Confidentiality · all data | C-11 to C-13 | `jsonschema` is pinned at 4.25.0; the packages it pulls in are not pinned. **No dependency scan was run** for this review. The socket block does not cover the one test that starts a child process, and a write to an absolute path outside the watched folder would not be seen (stage 5 notes N-06, N-08) | 1×4 = 4 Low |
| TH-08 | An item's history names the wrong person | Classical: spoofing · Integrity · the audit history | None, by decision: the name is self-declared (ADR-005) | Anyone can type any name; a damaged `raid-config.json` is replaced without a word (G-06) | 2×2 = 4 Low |

## 4. Findings from this review

Nothing was changed in the code. Each needs the owner's call.

| # | Finding | Evidence | My suggestion |
|---|---|---|---|
| F-01 | `raid list` prints item fields from the log as stored. Field values are not checked when a log is loaded, only its structure | Scratch run, 2026-10-11: a log whose title held an escape sequence and U+202E listed with exit 0 and the characters sent to the terminal | Pass printed fields through the same replacement the validator uses, or check field values at load |
| F-02 | An item in the log with a key missing (for example no `title`) ends `raid list` in a Python `KeyError` trace, exit 1, nothing written | Same scratch run | Treat it as a damaged log (C-09) with the plain message |
| F-03 | A hand edit of an item's fields or status, with the history left alone, loads and lists as normal | Same scratch run: title and status changed by hand, exit 0 | Decide whether tamper evidence is wanted at all. ADR-006 and NFR-007 promise only that no command alters history |
| F-04 | The three files are created with mode 0644: readable by every user on a shared machine | `src/raid/atomic.py` line 10; `ls -l` in the scratch folder | Create them 0600, or state the limit |
| F-05 | `.gitignore` covers `raid-log.json` only | `.gitignore`; already in G-06 | Add `pending.json` and `raid-config.json`, and say so in the README for project folders kept in git |

## 5. Open spec gaps, by ID

All are open in `docs/reviews/stage-5-review.md`. "Security" says whether the gap bears on a threat above.

| Gap | What is open | Security |
|---|---|---|
| G-01 | How an empty owner or due date is shown (`-` today, not pinned by a test) | None |
| G-02 | What `raid list` prints for an empty log (header only today) | None |
| G-03 | (a) a repeated accept after a failed trim makes a second item; (b) a failed disk write shows an error trace | TH-03 |
| G-04 | Whether messages go to standard output or standard error (all to output today) | None |
| G-06 | A damaged `raid-config.json` is silently replaced; `.gitignore` misses two files | TH-05, TH-08, F-05 |
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

On `main` the exposure is nil in practice, because there is no extraction command. It becomes real when `wip/spec-1-05` is merged, or when anyone makes a `pending.json` from real notes with an assistant outside this tool. Then C-01 to C-06 still stand between a bad proposal and the log, but nothing here limits what the session itself does. SPEC-EPIC-1-05 should not ship without SPEC-EPIC-1-06, and this review must be repeated for that path.

## 7. Verification log

Run on 2026-10-11, Python 3.13.9, commit `75860c3`, from the repo root.

| Control | Command | Result |
|---|---|---|
| All | `python3 -m pytest -q` | 329 passed, none failed, none skipped |
| C-11 to C-14 | `python3 -m pytest -q tests/test_boundaries.py` | 29 passed |
| C-11, C-13, C-14 bypass cases (planted import, planted write, invisible character) | `python3 -m pytest -q tests/test_boundaries.py -k 'planted or invisible'` | 24 passed |
| C-01, C-02 | `python3 -m pytest -q tests/test_spec_epic_1_02.py` | 124 passed |
| C-03 | `python3 -m pytest -q tests/test_spec_epic_1_02.py -k bad_values_are_not_echoed_raw` | 7 passed |
| C-05 | `python3 -m pytest -q tests/test_spec_epic_1_03.py -k 'cannot_be_edited or same_rules'` | 9 passed |
| C-06 | `python3 -m pytest -q tests/test_spec_epic_1_04.py -k 'future or cannot_be_emptied'` | 11 passed |
| C-07 to C-09 | `python3 -m pytest -q tests/test_spec_epic_5_01.py` | 46 passed |
| C-08 | `python3 -m pytest -q tests/test_spec_epic_5_02.py -k 'save_guard or never_change'` | 2 passed |

Not run: a dependency scan, a static security scanner, any test on Python 3.12, any test of the extraction path.

## 8. Decisions for the owner

Risk acceptance and release are the owner's, with a name, an expiry and a trigger to look again. I have not accepted anything.

1. Accept or fix F-01 to F-05, and with them TH-04 and TH-05, the two Medium rows.
2. Accept the parked extraction risk in section 6 as stated, on the condition that it is reviewed again before `wip/spec-1-05` is merged.
3. OQ-08: client approval for notes in an AI session. Not needed for what is on `main`; needed before extraction is used on real notes.
4. Whether a dependency scan is required before this build is given to anyone.
5. Whether the open gaps in section 5 are accepted for this build.
