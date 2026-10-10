# EPIC-2-05 — Check note on assumptions, waiting-on party on dependencies

**Epic:** EPIC-2 Log management · **Covers:** REQ-021, REQ-022 · **Size:** S · **Build order:** 15 of 25
**Depends on:** EPIC-1-03, EPIC-2-02, EPIC-2-06 · **Open questions:** none

**Story:** As a delivery manager, I want every assumption to say how we will check it and every dependency to say who we are waiting on, so that they do not sit in the log forever.

## Acceptance criteria

1. Given the Assumption proposal "Legacy ERP export will be available in CSV", when I accept it with the note "Confirm format with the ERP vendor", then viewing A-001 shows that note.
2. Given the Dependency proposal "Acme finance year-end close", when I accept it with waiting-on "Acme finance team", then viewing D-001 shows that party.
3. Given A-001, when I update its check note, then the new note is stored and one history entry is added.
4. Given an Assumption proposal, when I accept it and give no check note, then it is not accepted and is still awaiting my decision.
5. Given an Assumption proposal, when I accept it with a note and the validation date 2026-10-20, then viewing A-001 shows 2026-10-20; given I skip the date, then A-001 is accepted with no validation date.

## Notes

The check note is mandatory and the validation date optional, by decision DEC-21.
