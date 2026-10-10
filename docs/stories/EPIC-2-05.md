# EPIC-2-05 — Check note on assumptions, waiting-on party on dependencies

**Epic:** EPIC-2 Log management · **Covers:** REQ-021, REQ-022 · **Size:** S · **Build order:** 15 of 25
**Depends on:** EPIC-1-03, EPIC-2-02, EPIC-2-06 · **Open questions:** OQ-02

**Story:** As a delivery manager, I want every assumption to say how we will check it and every dependency to say who we are waiting on, so that they do not sit in the log forever.

## Acceptance criteria

1. Given the Assumption proposal "Legacy ERP export will be available in CSV", when I accept it with the note "Confirm format with the ERP vendor", then viewing A-001 shows that note.
2. Given the Dependency proposal "Acme finance year-end close", when I accept it with waiting-on "Acme finance team", then viewing D-001 shows that party.
3. Given A-001, when I update its check note, then the new note is stored and one history entry is added.

## Notes

Whether the check note is mandatory (and whether a validation date exists) is OQ-02; no criterion enforces it until answered.
