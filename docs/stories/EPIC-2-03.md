# EPIC-2-03 — Status, and closing an item with a reason

**Epic:** EPIC-2 Log management · **Covers:** REQ-016, REQ-017, REQ-018 · **Size:** S · **Build order:** 14 of 25
**Depends on:** EPIC-2-02, EPIC-2-06 · **Open questions:** none

**Story:** As a project manager, I want each item to have a status and to give a reason when I close it, so that 'closed' in the log can be trusted.

## Acceptance criteria

1. Given a newly accepted item, then its status is Open.
2. Given open item R-001, when I update its status to Mitigating, then `raid list` shows Mitigating and one history entry records the change from Open.
3. Given R-001, when I set its status to `Done`, then it is refused with a message listing Open, Mitigating, Closed.
4. Given open item I-001, when I close it without a reason, then it is refused and its status is still Open.
5. Given open item I-001, when I close it on 2026-10-10 with the reason "Test environment restored by infra", then its status is Closed, and viewing I-001 shows closed date 2026-10-10 and that reason.
6. Given Closed item I-001, when I reopen it without a reason, then it is refused and its status is still Closed.
7. Given Closed item I-001, when I reopen it with the reason "Environment down again", then its status is Open and one history entry records the reopening and that reason.

## Notes

Reopening with a reason is decision DEC-15. The same three statuses apply to all four types (decision DEC-21).
