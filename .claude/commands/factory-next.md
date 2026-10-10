---
description: Run the next stage that is NOT STARTED, or tell me what needs approval
---
Read `docs/state.md`.
- If any stage is DRAFT, do not run anything: summarise its review file in `docs/reviews/` and tell me to review the artifacts and run `/approve <n>` or give feedback.
- Otherwise run the first NOT STARTED stage by following the matching file in `.claude/commands/` (stage-N-*.md) exactly.
- If all stages are APPROVED, say the factory run is complete and point to `docs/release-note.md`.
