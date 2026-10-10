# EPIC-2-02 — Update an item

**Epic:** EPIC-2 Log management · **Covers:** REQ-011, REQ-016, REQ-041, NFR-008 · **Size:** S · **Build order:** 12 of 25
**Depends on:** EPIC-5-02 · **Open questions:** none

**Story:** As a project manager, I want to update my items in a few seconds each, so that keeping the log current costs me under five minutes a week.

## Acceptance criteria

1. Given R-001 with due date 2026-10-16, when I update its due date to 2026-10-23, then `raid list` shows 2026-10-23 for R-001 and its ID is unchanged.
2. Given R-001, when I update its title, description, owner and severity in turn, then each new value is stored in the log file, title, owner and severity are shown by `raid list`, and each change adds exactly one history entry.
3. Given a log with no R-099, when I update R-099, then the exit code is non-zero, the message says R-099 does not exist, and the log is unchanged.
4. Given R-001, when I set its due date to `2026-13-40`, then it is refused and the stored date is unchanged.
5. Given R-001, when I try to change its type to Issue, then it is refused with a message saying a type cannot change after acceptance, and R-001 is unchanged.
6. Given R-001, when I set its title to one of 81 characters, then it is refused with a message stating the 80-character limit and the stored title is unchanged.
7. Given a log with 10 items of which 4 are mine, when I list my items and update all 4 in a timed walkthrough, then it takes under 5 minutes.

## Notes

Criterion 7 is the NFR-008 check, done by a person at the stage 6 demo (assumption A-7); the 10 and 4 are a walkthrough size I chose, confirm. v1 is single-user (decision DEC-13), so the project manager updates items on the machine that holds the log. The type rule is DEC-15.
