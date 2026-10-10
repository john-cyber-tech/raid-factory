# EPIC-1-01 — Review fixture proposals into the log and list them (thin slice)

**Epic:** EPIC-1 Extraction and review · **Covers:** REQ-007, REQ-008, REQ-010, REQ-011, REQ-014, NFR-010 · **Size:** M · **Build order:** 1 of 25
**Depends on:** nothing · **Open questions:** none

**Story:** As a delivery manager, I want to accept or reject each proposed item and then see the accepted ones in my project's log, so that nothing enters the log without my decision.

## Acceptance criteria

1. Given an empty project folder and a fixture `pending.json` with three proposals taken from `inputs/sample-meeting-notes.md` (P1 Risk "Client security review may delay cutover", P2 Issue "Test environment down", P3 Dependency "Acme finance year-end close"), when I run `raid review` and answer accept, reject, accept, then the log holds exactly two items: R-001 with P1's title and D-001 with P3's title.
2. Given the same run, when each proposal is shown, then its source excerpt is displayed and the review does not move to the next proposal until I answer accept or reject.
3. Given the run in criterion 1, when it finishes, then `pending.json` holds no proposals and the rejected P2 is recorded nowhere.
4. Given the log from criterion 1, when I run `raid list`, then two rows are shown, each with ID, type, title, owner, severity, due date and status.
5. Given a log holding R-001, when a later review accepts another Risk, then its ID is R-002 and R-001 is unchanged.
6. Given two project folders A and B, when I accept an item in A, then B's log file is byte-identical to before.
7. Given a project folder with no `pending.json`, when I run `raid review`, then a message says there is nothing to review and the log is unchanged.
8. Given Python 3.12 or later with no Claude Code session, when pytest runs, then this story's tests pass using fixture files only, and each test names the REQ it checks.

## Notes

First story to build: it delivers the whole path from proposals to a listed log item. Removing decided proposals and not recording rejections is decision DEC-10. NFR-010's "every REQ has a test citing its ID" applies to every later story as part of done.
