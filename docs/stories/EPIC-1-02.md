# EPIC-1-02 — Reject invalid extraction output

**Epic:** EPIC-1 Extraction and review · **Covers:** REQ-005, REQ-006, REQ-041 · **Size:** S · **Build order:** 6 of 25
**Depends on:** EPIC-1-01 · **Open questions:** none

**Story:** As a delivery manager, I want a broken `pending.json` refused with a clear message, so that bad extraction output can never reach my log.

## Acceptance criteria

1. Given a `pending.json` that is not valid JSON, when I run `raid review`, then the exit code is non-zero, the message names the file and the parse error, and the log is byte-identical to before.
2. Given a `pending.json` with one proposal missing `title`, when I run `raid review`, then the exit code is non-zero and the message names `title` and which proposal lacks it.
3. Given a `pending.json` with one proposal of type `Question`, when I run `raid review`, then the exit code is non-zero and the message names `type` and the four allowed values.
4. Given a `pending.json` whose first proposal is valid and second is invalid, when I run `raid review`, then no proposal is shown for a decision, not even the first.
5. Given a `pending.json` with one proposal whose title is 81 characters, when I run `raid review`, then the exit code is non-zero and the message names `title` and the 80-character limit; given a title of exactly 80 characters, then the file passes validation.

## Notes

Whole-file rejection is assumption A-2. The title limit is decision DEC-09; rejecting the whole file for one long title is my reading of it, confirm.
