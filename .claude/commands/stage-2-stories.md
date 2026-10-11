---
description: Stage 2 — group requirements into epics and write INVEST stories
---
# Stage 2 — Epics and stories
Precondition: stage 1 APPROVED. Set stage 2 to DRAFT when done.

**Knowledge:** `reference/epam/s1-requirements.md` (Block 3 only) and `reference/epam/s2-stories.md`. Optional skills: `requirements-to-epics`, `epic-to-story-decomposer`, `epics-vs-requirements-checker`, `story-checker`.

## Produce
1. `docs/epics.md`: 3–5 epics (expect: extraction & review, log management, flags & duplicates, weekly summary, data safety/audit). Each has goal, REQ/NFR ids covered, sequence rationale.
2. `docs/stories/<EPIC-ID>-<nn>.md`: one file per story. Each: story ("As a… I want… so that…"), parent EPIC id, REQ/NFR ids, acceptance criteria in Given/When/Then with concrete values, size (S/M; split anything bigger), dependencies. Use `inputs/sample-meeting-notes.md` to make criteria concrete (e.g. which items the extractor should find).
3. `docs/traceability.md`: matrix NEED → REQ → EPIC → STORY.

## Self-check → `docs/reviews/stage-2-review.md`
- Coverage: every REQ and NFR maps to ≥1 epic and story. No orphan epics/stories.
- INVEST per story; acceptance criteria testable and not a restatement of the title.
- Order: stories can be built in a sensible sequence; the first story delivers an end-to-end thin slice.
List findings as BLOCKER / MAJOR / MINOR, fix BLOCKER/MAJOR, record changes.

Stop. Summarise and ask me to run `/approve 2`.
