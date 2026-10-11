# Stage 2 — epics and stories (also read Block 3 of s1-requirements.md)

> Trimmed excerpt of the EPAM AI Factory notes. Sections included:
> - epam-ai-factory-200_ProductMgmt_and_BA.md — Block 5

---

<!-- source: epam-ai-factory-200_ProductMgmt_and_BA.md -->
# Block 5 — The build-and-validate interface

PROD/BA work doesn't stop at the spec — you sit on the other side of every build handoff, and the Wide audience (QA, engineers, management) *receives* these artefacts:

- **Definition of Ready (DoR)** — a story that fails the gate (no falsifiable AC, no named user role, unsized, no eval rubric for an AI feature) goes back to refinement, not into the sprint.

- **UAT-script review** — PROD/BA checks the User Acceptance Tests cover every AC, error path, and NFR, not only the happy path.

- **Defect triage** — defects are scored by business impact (severity × reach × strategic fit) and called release-blocker / ship-with-known-issue / defer; QA owns the fix, PROD/BA owns the priority.

- **Release readiness & communication** — a numeric go/no-go, plus a comms pack: delivery leads get scope + open risks, business stakeholders get the behaviour change + benefit + dates, and every line of the release note traces back to a story that actually shipped.
