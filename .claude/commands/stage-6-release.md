---
description: Stage 6 — security review, release note, handover
---
# Stage 6 — Security and delivery check
Precondition: stage 5 APPROVED. Set stage 6 to DRAFT when done.

**Knowledge:** `reference/epam/s6-release.md` (threats and risk, design review, security testing, human-owned decisions, delivery).

## Produce
1. `docs/threat-review.md`: short threat model for this tool — data flows (notes → Claude Code session → pending.json → log file), threats (prompt injection via notes content, malformed or tampered pending.json, client data handled in an AI session, log corruption, sensitive data in logs), mitigations present in code (cite files/tests), residual risks, and items needing a human security decision. Check the code actually does what it claims: confirm no network calls or keys in `src/`, and inspect logging.
2. `docs/release-note.md`: what v1 does, how to install and run (including how to use `/raid-extract`), known limitations, what was deliberately left out, how each NFR was verified, and suggested v2 items.
3. `docs/traceability.md` updated through SPEC → tests.

## Self-check → `docs/reviews/stage-6-review.md`
Run the full tests one more time. Confirm no secrets in repo (`git grep -i` for key patterns). List residual risks the human must accept.

Stop. Summarise and ask me to run `/approve 6`. Risk acceptance and release are my decision, not yours.
