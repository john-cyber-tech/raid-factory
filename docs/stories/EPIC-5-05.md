# EPIC-5-05 — Ask for my name once and remember it

**Epic:** EPIC-5 Data safety and audit · **Covers:** REQ-035 · **Size:** S · **Build order:** 4 of 25
**Depends on:** EPIC-1-01 · **Open questions:** none

**Story:** As a delivery manager, I want to give my name once, so that every change I make is recorded under it without a login.

## Acceptance criteria

1. Given no stored name, when I run a command that changes the log, then I am asked for my name once, and "Sean Murphy" is saved to a local configuration file.
2. Given the stored name "Sean Murphy", when I run another command that changes the log, then I am not asked again.
3. Given no stored name, when I run `raid list`, then I am not asked for a name.
4. Given no stored name, when I am asked and enter nothing, then the command stops with a message and the log is unchanged.

## Notes

Decision DEC-02. Where the configuration file lives (per project or per user) is for stage 3.
