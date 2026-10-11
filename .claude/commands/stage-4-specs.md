---
description: Stage 4 — engineering specs per story plus build order
---
# Stage 4 — Engineering specs and task order
Precondition: stage 3 APPROVED. Set stage 4 to DRAFT when done.

**Knowledge:** `reference/epam/s4-specs.md` (engineering blocks, anti-patterns, test strategy, test cases, test data). Optional skills: `engineering-spec-writer`, `task-dag-builder`, `build-readiness-checker`.

## Produce
1. `docs/specs/SPEC-<story-id>.md` for every story, with: **Why** (story + REQ ids), **Capabilities** (what it must do, with file/module names from the architecture), **Constraints** (each cites an ADR/NFR id), **Non-goals**, **Success signal** (observable, testable), **Test plan** (named test cases incl. edge cases and failure paths; test data), **Definition of done**.
2. `docs/task-dag.md`: build order, which tasks can parallelise, dependencies, and a risk tier per task (LOW = auto-proceed with tests green; MEDIUM = show me the diff; HIGH = stop for my approval, e.g. anything touching file writes/atomicity or the extraction command prompt).

## Self-check → `docs/reviews/stage-4-review.md`
Each spec has a testable success signal; every Constraint cites an upstream id; no cycles in the DAG; no unresolved Open Questions in LOW tier tasks; one spec covers the `/raid-extract` command and the pending.json schema; tests cover each acceptance criterion. Fix BLOCKER/MAJOR.

Stop. Summarise and ask me to run `/approve 4`.
