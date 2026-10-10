---
description: Stage 1 — turn the brief into testable requirements and NFRs
---
# Stage 1 — Requirements
Precondition: `inputs/brief.md` exists. Also read every file in `inputs/stakeholder-interviews/` (raw notes: extract needs from them, note conflicts between stakeholders, and do not read `inputs/meeting-notes/` or `inputs/expected/` at this stage). Set stage 1 to DRAFT in `docs/state.md` when done.

**Knowledge:** skim `reference/epam/200_ProductMgmt_and_BA.md` (Blocks 3 and 6) and `reference/epam/600_Quality.md` (Block 2: requirements validation and acceptance criteria). If the `requirements-writer` / `nfr-elicitor` skills are available, use them.

## Produce `docs/requirements.md`
1. **Stakeholders and needs:** table of NEED-01… (solution-free statements: who, need, why).
2. **Functional requirements:** table REQ-001… with: statement ("The system shall…"), priority (MoSCoW), source NEED id, acceptance criteria (testable, with concrete values).
3. **Non-functional requirements:** NFR-001… for performance, reliability/data safety, security and privacy, auditability, usability, maintainability. Each has a measurable target and how it will be verified. Mark categories with no constraint as "none identified" explicitly.
4. **Assumptions and Open Questions:** anything not in the brief. Do NOT invent answers; propose a default and flag it.
5. **Out of scope:** copied from the brief.

## Self-check → `docs/reviews/stage-1-review.md`
Score each requirement: unambiguous, testable, atomic, traceable to a NEED, no duplicates. List findings as BLOCKER / MAJOR / MINOR with the ID and a suggested fix. Fix MAJOR and BLOCKER findings in the document, then re-check and record what changed.

Stop. Summarise (≤10 lines): counts of needs/REQs/NFRs, open questions I must answer, remaining findings. Ask me to review and run `/approve 1`.
