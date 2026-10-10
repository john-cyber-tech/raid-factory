# EPIC-5-01 — Log writes are atomic and never lose accepted items

**Epic:** EPIC-5 Data safety and audit · **Covers:** NFR-002, NFR-003 · **Size:** S · **Build order:** 2 of 25
**Depends on:** EPIC-1-01 · **Open questions:** none

**Story:** As a delivery manager, I want the log to survive a crash in the middle of a save, so that I never lose items I have already accepted.

## Acceptance criteria

1. Given a log holding R-001 and R-002, when a write that adds R-003 fails after the new content is written but before it replaces the log, then the log file parses as valid JSON and holds exactly R-001 and R-002.
2. Given the same failure injected at each step of the write, when the log is read afterwards, then in every case it equals either the complete before state or the complete after state.
3. Given a review of three proposals, when I accept the first and the review is interrupted before the second decision, then R-001 is in the log on the next run.
4. Given any sequence of the CLI commands built so far, when the sequence finishes, then every item ID that was in the log before is still in it.

## Notes

Criterion 3 rests on assumption A-6 (each accept is saved immediately).
