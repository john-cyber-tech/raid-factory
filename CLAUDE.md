# RAID Log Manager — AI Factory

This repo is a small AI factory. It turns a project brief into a working RAID Log Manager
(Risks, Assumptions, Issues, Dependencies) by running six stages in Claude Code.
Each stage is a slash command in `.claude/commands/`. Stage knowledge comes from the EPAM
AI Factory notes in `reference/epam/` (read only the sections a stage names).

## Operating rules
1. **Human gate after every stage.** Never start stage N+1 until `docs/state.md` shows stage N as `APPROVED`.
2. **Each stage = produce → self-check → report.** Write artifacts, run the stage's checklist, write findings to `docs/reviews/stage-N-review.md`, then stop and ask for approval.
3. **Traceability.** Every artifact carries IDs and cites its upstream IDs: NEED/REQ → EPIC → STORY → SPEC → code/tests. Nothing without a parent.
4. **No invention.** If the brief doesn't say it, put it under "Open Questions" rather than guessing. Do not fill gaps silently.
5. **Small steps, tests first** in stage 5. One spec at a time; commit after each green spec.
6. **Human owns the call** on scope, risk acceptance, security sign-off and release.
7. Use plain markdown. Keep each artifact short enough to review in 10 minutes.

## Layout
- `inputs/brief.md` — the project brief (source of truth). `inputs/sample-meeting-notes.md` — test data.
- `docs/` — stage outputs. `docs/state.md` — stage status and approvals.
- `src/`, `tests/` — the built tool (Python 3.12 or later, pytest). No network calls, no API key.
- `reference/epam/` — EPAM AI Factory role notes (100–1000).

## Product design note
Extraction is done by a Claude Code command (`/raid-extract`) that the factory builds as part of the product, not by app code. The Python CLI validates and stores. Keep that boundary.

## Commands
`/factory-status` · `/stage-1-requirements` · `/stage-2-stories` · `/stage-3-architecture` ·
`/stage-4-specs` · `/stage-5-build` · `/stage-6-release` · `/approve <n>` · `/factory-next`
