# Stage 6 review — security and delivery check

**Status:** DRAFT, second pass, awaiting the owner's approval · **Date:** 2026-10-11 · **First reviewed at commit:** `75860c3`; fix and re-verification at `94dcfb1` on `main`
**Produced:** `docs/threat-review.md`, `docs/release-note.md`, `docs/traceability.md` (new section "Through SPEC → tests")
**Scope:** the 8 built specs only (SPEC-EPIC-1-01, 1-02, 1-03, 1-04, 5-01, 5-02, 5-04, 5-05), by the owner's instruction of 2026-10-11.
**Knowledge used:** `reference/epam/s6-release.md`: classical and AI-specific threats, Likelihood × Impact scoring, access scope and blast radius, bypass-case tests and the verification log, human-owned decisions. The optional skills and `/security-review` were not run.

**Open findings: 0 BLOCKER · 0 MAJOR · 0 MINOR.** First pass: 2 MAJOR, 3 MINOR. The owner sent four back, fixed in `94dcfb1`, and accepted one (F-03) as a documented design limit.

## Where the owner's instruction was followed instead of the stage 6 command text

| # | The command says | What was done instead | Why |
|---|---|---|---|
| S-1 | Threat model data flow: notes → Claude Code session → `pending.json` → log file | The reviewed flow starts at `pending.json`. The notes and session step is section 6 of the threat review, "known, parked risk" | SPEC-EPIC-1-05 and 1-06 are deferred; there is no extraction command on `main` |
| S-2 | Threats to cover include prompt injection via notes content and client data handled in an AI session, with mitigations present in code | Both are listed as parked and unassessed, with no mitigation claimed. The untested prompt on `wip/spec-1-05` is not counted as a control | Same. Nothing built or tested addresses them |
| S-3 | Release note: "what v1 does" | The note is titled "0.1.0, partial build" and opens with "8 of the 25 specs are built". It does not call the build v1 | Owner's instruction: state 8 of 25 and claim nothing from the other specs |
| S-4 | Release note: how to install and run, "including how to use `/raid-extract`" | No `/raid-extract` usage. The note says there is no extraction command and that `pending.json` is written by hand or copied from a fixture | Not built |
| S-5 | Release note: "how each NFR was verified" | Verification is given for the 6 NFRs the built specs carry (NFR-002, 003, 004, 006, 007, 010). NFR-005, 008 and 009 are listed as not verified because not built; NFR-001 has no target | Not built. The NFR-008 timed walkthrough and the NFR-009 read-through, both due at stage 6, were not done |
| S-6 | Release note: "suggested v2 items" | "Suggested next steps": the remaining work, not a second version | There is no finished v1 to follow |
| S-7 | Traceability "updated through SPEC → tests" | Done for the 8 built specs. The other 17 are listed with the requirements they leave without a test | Not built |

The owner also asked for each open gap to be listed by ID (threat review section 5, 13 gaps) and for the built controls to be listed (section 2, C-01 to C-14).

## Checks the stage asks for

| Check | Result |
|---|---|
| Full test run | `python3 -m pytest -q -rs`, 2026-10-11, Python 3.13.9, at `94dcfb1`: 454 passed, none failed, none skipped (first pass: 329; the fix added 125) |
| No network calls in `src/` | Confirmed by reading every import, and by `test_suite_runs_with_sockets_blocked` and `test_no_network_imports_in_src`. The one URL is the `$schema` identifier in `pending.schema.json` |
| No keys in `src/` | Confirmed. No environment variable is read; `test_commands_work_without_api_keys` passes |
| Logging inspected | The `logging` module is not used. Output is the terminal and the three JSON files only |
| No secrets in the repo | `git grep -i` over tracked files for API key, secret, password, token, private key, AWS and GitHub token patterns: no match on the first pass; on the second, one match, the threat review's own sentence about this search. No `.env`, key file, log, config or `pending.json` is tracked |
| Mitigations cite files and tests | Threat review section 2: 18 controls, each with its file and test names; section 7 gives the commands, all run again after the fix |
| Bypass cases, not only clean input | Planted import, planted outside write, planted invisible character, 71 contract violations, altered history, dropped item, injected save failures. All in the suite |

## Findings and the owner's decisions (2026-10-11)

| # | Severity | Finding | Decision | State |
|---|---|---|---|---|
| F-01 | MAJOR | `raid list` sent item fields from a hand-edited log to the terminal unchecked | Sent back | **Closed in `94dcfb1`.** `raid list` and the review screen mask with the existing field rules; an item ID quoted in a message is masked too |
| F-02 | MINOR | A log item with a missing field ended `raid list` in a Python error trace | Sent back | **Closed in `94dcfb1`.** Damaged-log message, exit 1, nothing written |
| F-04 | MAJOR | The three data files were created readable by every user (mode 0644) | Sent back | **Closed in `94dcfb1`.** Mode 0600, with two tests of the mode |
| F-05 | MINOR | `.gitignore` covered `raid-log.json` only | Fix | **Closed in `94dcfb1`**, with a README line for project folders kept in git |
| F-03 | MINOR | A field changed by hand in the log, history untouched, is not noticed | Accepted as a documented design limit | Stated in the threat review (TH-04) and the release note |

**Tests first, failing run shown.** `tests/test_threat_review_findings.py` was written before any code changed. Run then: 125 collected, **124 failed, 1 passed**, no collection error. The failures by test: 54 `raid list` masking, 48 + 2 review screen masking, 1 masked ID in a message, 7 missing field, 9 field that is not text, 2 file mode, 1 `.gitignore`; each on its own assertion (the raw character present, the masked text or the damaged-log message absent, the mode not 0600). The one that passed, `test_empty_owner_and_due_date_are_still_a_valid_log`, pins behaviour that must not change. After the code: 125 passed, whole suite 454 passed.

**Things in the fix that go past the letter of the instruction, for the owner to confirm:**

- F-02 also refuses a field that is present but not text (a number, a list), because it ended in the same error trace. Only owner and due date may be empty.
- F-01 also masks an item ID quoted in a damaged-log or refused-save message.
- F-04: the file is set to 0600 just before it replaces the old one, so a wider existing file or leftover temporary file becomes private at the next save. A file the tool does not write again keeps its mode; the name file is written once only.
- F-05: the three ignore lines are anchored to the repo root, so fixture files named `pending.json` under `tests/` (used on `wip/spec-1-05`) are not ignored.
- Masking uses the rules' set of characters, as instructed. Zero-width characters and two direction marks are outside that set and are still printed (threat review TH-01, TH-02; G-11).
- While writing the tests I made the mistake defect D-01 describes (literal invisible characters in a test file). Its guard test failed and I replaced them with escapes before committing.

**Other decisions the owner gave:**

- The parked extraction risk is accepted on three conditions: the review is repeated before `wip/spec-1-05` merges; SPEC-EPIC-1-05 does not ship without SPEC-EPIC-1-06; G-16 is settled first. No expiry date was given.
- The 13 open gaps are accepted for this build.
- **Release condition:** a dependency scan, starting with pinning the transitive packages, before anyone else gets the build. **Not done. The build is not releasable to others until it is.**

## Not done

- No dependency scan and no static security scanner. `jsonschema` is pinned at 4.25.0; the four packages it requires are not pinned. The owner made this a release condition.
- No run on Python 3.12.
- No review of the extraction path, and none of the 15 out-of-scope specs.
- The stage 5 end-to-end test (validate → review → flag → summary) still does not exist.
- The mode test has not been run on Windows.

Done on the second pass: `docs/DEMO-SCRIPT.md` is rewritten for the 8-spec scope (Parts 5 to 7: review and list from a fixture, refused input, no extraction, flags or summary), and the release note states the Python version the tests ran on.

## Residual risks after the second pass

Release is the owner's decision. Items 1, 3 and 8 carry the owner's acceptance of 2026-10-11; the rest are stated for the approval.

1. **Parked extraction risk.** Accepted on the three conditions above. Nil exposure on `main`.
2. **Data at rest (TH-05, Medium):** the files are private to the user but plain text.
3. **The log is not tamper-evident (TH-04, Medium):** accepted as F-03. G-07 and G-08 are open.
4. **Zero-width characters are neither refused nor masked (TH-01, TH-02, Low).**
5. **Self-declared name (TH-08, Low):** by ADR-005.
6. **Loss or duplication at the edges (TH-03, Low):** G-03, stage 5 note N-04.
7. **Unpinned transitive dependencies and no scan (TH-07, Low):** the release condition, not yet met.
8. **The 13 open gaps** in threat review section 5: accepted.
9. **This is 8 of 25 specs.** The build cannot change, close or summarise items and has no extraction.
