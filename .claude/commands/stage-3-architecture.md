---
description: Stage 3 — high-level architecture and ADRs
---
# Stage 3 — Architecture
Precondition: stage 2 APPROVED. Set stage 3 to DRAFT when done.

**Knowledge:** `reference/epam/400_Architecture.md` (Blocks 2–4: solution structure, ADRs, enforceable NFRs). Optional skills: `solution-architecture-writer`, `adr-writer`, `architecture-vs-requirements-checker`.

## Produce
1. `docs/architecture.md`: components (responsibility, interface, data owned), a Mermaid diagram, data flow for "paste notes → review → log → summary", NFR→component mapping table, and the stack from the brief. Keep it HLD only (no class diagrams). Expect roughly: `/raid-extract` Claude Code command (outside the Python app), pending.json contract + schema validator, CLI, Review flow, Log store (atomic JSON), Dedup, Flagger, Summary generator.
2. `docs/adr/ADR-00n-*.md`: one per real fork. Minimum: (a) storage format and atomic-write strategy, (b) the extraction boundary: the Claude Code command writes `pending.json`, the CLI validates it against a JSON schema and rejects malformed or injected content; compare with alternatives such as headless `claude -p` from the CLI or an API call, (c) duplicate detection approach (rule-based vs model-assisted). Each ADR lists ≥2 genuine alternatives, trade-offs, decision, consequences including downsides, and the REQ/NFR ids that drove it.

## Self-check → `docs/reviews/stage-3-review.md`
Every NFR is mapped to a component with a plausible mechanism and a way to verify it (e.g. what happens if `pending.json` is malformed, partially written, or contains instructions copied from the notes?). Every REQ lands on a component. List findings, fix BLOCKER/MAJOR.

Stop. Summarise and ask me to run `/approve 3`.
