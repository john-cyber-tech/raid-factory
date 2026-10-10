---
description: Approve a stage (argument = stage number)
argument-hint: <stage number 1-6>
---
Stage to approve: $ARGUMENTS

1. Read `docs/state.md` and check the stage is DRAFT. If not, say so and stop.
2. Read `docs/reviews/stage-$ARGUMENTS-review.md`. If it has unresolved BLOCKER findings, list them and stop unless I have explicitly said to approve anyway.
3. Set the stage to APPROVED with today's date in `docs/state.md`.
4. Tell me the next command to run.
