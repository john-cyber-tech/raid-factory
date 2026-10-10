# EPIC-5-03 — Items are never deleted

**Epic:** EPIC-5 Data safety and audit · **Covers:** REQ-019 · **Size:** S · **Build order:** 22 of 25
**Depends on:** EPIC-2-03, EPIC-3-04 · **Open questions:** none

**Story:** As a project manager, I want closed and merged items to stay in the log, so that the audit trail is complete.

## Acceptance criteria

1. Given the CLI's help output, then it lists no delete or remove command.
2. Given R-001 closed and a proposal merged into R-002, when I run `raid list`, then R-001 and R-002 are both shown.
3. Given the same log, then R-001 and R-002 each still have every history entry they had before.
