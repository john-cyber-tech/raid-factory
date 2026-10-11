# Stage 6 review — security and delivery check

**Status:** DRAFT, awaiting the owner's approval · **Date:** 2026-10-11 · **Reviewed at commit:** `75860c3` on `main`
**Produced:** `docs/threat-review.md`, `docs/release-note.md`, `docs/traceability.md` (new section "Through SPEC → tests")
**Scope:** the 8 built specs only (SPEC-EPIC-1-01, 1-02, 1-03, 1-04, 5-01, 5-02, 5-04, 5-05), by the owner's instruction of 2026-10-11.
**Knowledge used:** `reference/epam/s6-release.md`: classical and AI-specific threats, Likelihood × Impact scoring, access scope and blast radius, bypass-case tests and the verification log, human-owned decisions. The optional skills and `/security-review` were not run.

**Open findings: 0 BLOCKER · 2 MAJOR · 3 MINOR.** No code was changed in this stage.

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
| Full test run | `python3 -m pytest -q`, 2026-10-11, Python 3.13.9: 329 passed, none failed, none skipped |
| No network calls in `src/` | Confirmed by reading every import, and by `test_suite_runs_with_sockets_blocked` and `test_no_network_imports_in_src`. The one URL is the `$schema` identifier in `pending.schema.json` |
| No keys in `src/` | Confirmed. No environment variable is read; `test_commands_work_without_api_keys` passes |
| Logging inspected | The `logging` module is not used. Output is the terminal and the three JSON files only |
| No secrets in the repo | `git grep -i` over tracked files for API key, secret, password, token, private key, AWS and GitHub token patterns: no match. No `.env`, key file, log, config or `pending.json` is tracked |
| Mitigations cite files and tests | Threat review section 2: 14 controls, each with its file and test names; section 7 gives the commands run |
| Bypass cases, not only clean input | Planted import, planted outside write, planted invisible character, 71 contract violations, altered history, dropped item, injected save failures. All in the suite |

## Findings

| # | Severity | Finding | Where |
|---|---|---|---|
| F-01 | MAJOR | `raid list` sends item fields from a hand-edited log to the terminal unchecked, including escape and text-direction characters. The `pending.json` path is protected; the log path is not | Threat review TH-02 |
| F-04 | MAJOR | The three data files are created readable by every user of the machine (mode 0644) | TH-05 |
| F-02 | MINOR | A log item with a missing field ends `raid list` in a Python error trace instead of the damaged-log message | TH-06 |
| F-03 | MINOR | A field changed by hand in the log, history untouched, is not noticed. A design question: nothing promises tamper evidence | TH-04 |
| F-05 | MINOR | `.gitignore` covers `raid-log.json` but not `pending.json` or `raid-config.json` (already in G-06) | TH-05 |

F-01, F-02 and F-03 were shown by a run in a scratch folder on 2026-10-11, not by a test in the suite. If they are to be fixed, each needs a guard test first.

## Not done

- No dependency scan and no static security scanner. `jsonschema` is pinned at 4.25.0; the four packages it requires are not pinned.
- No run on Python 3.12.
- No review of the extraction path, and none of the 15 out-of-scope specs.
- The stage 5 end-to-end test (validate → review → flag → summary) still does not exist.
- `docs/DEMO-SCRIPT.md` was not updated for the reduced scope.

## Residual risks the owner must accept, or send back

Risk acceptance and release are the owner's decision. Nothing here is accepted by me.

1. **Parked extraction risk.** Hidden instructions in notes, and client data in an AI session, are unaddressed because SPEC-EPIC-1-05 and 1-06 are not built. Nil exposure on `main`; real as soon as `wip/spec-1-05` is merged or a `pending.json` is made from real notes with an assistant. Condition I suggest: repeat this review before that merge, and do not ship 1-05 without 1-06.
2. **Data at rest (TH-05, Medium):** plain files, readable by other users of the machine, two of them not ignored by git.
3. **The log is not tamper-evident (TH-04, Medium):** the history is append-only against the tool only. G-07 and G-08 are open.
4. **Unchecked log content reaches the terminal (TH-02, Low):** F-01.
5. **Self-declared name (TH-08, Low):** by ADR-005.
6. **Loss or duplication at the edges (TH-03, Low):** G-03, stage 5 note N-04.
7. **Unpinned transitive dependencies and no scan (TH-07, Low).**
8. **The 13 open gaps** in threat review section 5.
9. **This is 8 of 25 specs.** The build cannot change, close or summarise items and has no extraction.
