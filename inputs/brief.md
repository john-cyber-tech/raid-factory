# Project brief: RAID Log Manager

## Problem
Project and delivery managers at client sites capture risks, assumptions, issues and dependencies
in scattered meeting notes and emails. Items get lost, have no owner, and go stale.

## Users
- **Delivery manager (primary):** pastes notes, reviews extracted items, maintains the log, sends a weekly summary.
- **Project manager / team lead:** reads the log, updates their own items.
- **Client sponsor (read-only):** receives the weekly RAID summary.

## Goals (v1)
1. Extract RAID items from meeting notes/emails using a Claude Code command (`/raid-extract <notes file>`), which writes proposals (type, title, description, owner, severity, due date, source excerpt) to `pending.json`.
2. The CLI validates `pending.json` against a schema, then the manager accepts, edits or rejects each proposal (`raid review`) before it enters the log.
3. One RAID log per project, stored locally, with stable IDs (R-001, A-001, I-001, D-001).
4. Detect likely duplicates of existing items and offer to merge.
5. Flag items that are unowned, overdue, or not updated in 14 days.
6. Generate a weekly RAID summary (markdown) suitable for sending to a client.

## Non-goals (v1)
Jira/Teams/email integrations, logins/multi-user, multi-project dashboards, web UI, notifications.

## Constraints and quality targets
- Extraction must never auto-add: proposals land in `pending.json` only; a human confirms every item through `raid review`.
- Every log entry keeps its source excerpt and date (auditability).
- Malformed or schema-invalid extraction output is rejected with a clear message and never touches the log.
- Log file must survive a crash mid-write (atomic writes) and never lose accepted items.
- The Python tool makes no network calls and needs no API key. Extraction happens only inside the user's Claude Code session; the user is responsible for confirming the client allows notes to be processed there.
- Notes files are treated as untrusted input: text inside them must never be followed as instructions by the extraction command.

## Stack (change here if you disagree)
- Interface: command-line tool (`raid add|review|list|flag|summary`)
- Language: Python 3.12, pytest
- Storage: JSON file per project (`raid-log.json`)
- Extraction: a Claude Code slash command shipped with the tool (`.claude/commands/raid-extract.md`) that writes `pending.json`. The Python CLI only validates, reviews and stores; tests use fixture `pending.json` files.

## Open questions
- Severity scale: High/Medium/Low, or probability x impact?
- Should "Assumptions" have a validation date?
