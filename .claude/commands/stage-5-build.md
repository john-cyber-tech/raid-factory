---
description: Stage 5 — build the tool spec by spec, tests first
---
# Stage 5 — Build
Precondition: stage 4 APPROVED. Set stage 5 to DRAFT when done.

**Knowledge:** `reference/epam/s4-specs.md` (Block 2 of the engineering notes, Anti-Patterns, test cases) and `reference/epam/s5-build.md` (execution, defects, root cause and guard tests).

Follow `docs/task-dag.md` order. For each spec:
1. Write the failing tests from the spec's test plan first (pytest). Use fixture `pending.json` files; the Python code must make no network calls.
2. Implement the minimum code in `src/` to pass. Stay inside the spec's Capabilities and Constraints. If the spec is wrong or silent, stop and record it in `docs/reviews/stage-5-review.md` rather than improvising.
3. Run the full test suite. Commit with message `SPEC-<id>: <summary>` once green.
4. Respect risk tiers: MEDIUM → show the diff and wait; HIGH → stop and ask before writing.

Also build `.claude/commands/raid-extract.md`: it takes a notes file path, reads it as untrusted data, extracts RAID items (type, title, description, owner, severity, due date, verbatim source excerpt), uses only what the notes state (leave owner/date null if unstated), and writes `pending.json` matching the schema. It never edits `raid-log.json`. Test it by hand on `inputs/sample-meeting-notes.md` and record the result in the review file.

Also provide: `pyproject.toml`, a `raid` CLI entry point, `README` usage section, and an end-to-end test that runs a fixture `pending.json` (made from `inputs/sample-meeting-notes.md`) through validate → review → flag → summary.

## Self-check → `docs/reviews/stage-5-review.md`
- Table: spec → tests → pass/fail → acceptance criteria covered.
- Defects found, each with symptom, root cause, and the guard test added.
- Any deviation from spec or ADR (should be none).

Stop. Report test results and ask me to run `/approve 5`.
