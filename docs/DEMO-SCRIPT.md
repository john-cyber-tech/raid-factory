# Showcase script — the RAID Log AI Factory

**Audience:** delivery/project managers and engineering leads, mixed technical level.
**Length:** about 45 minutes plus Q&A (stages are shown live or from snapshots, see Part 0).
**Takeaway to land:** *An AI factory is not "AI writes code". It is a chain of small, reviewable stages with a human approving each one, and every output traces back to what a stakeholder said.*

---

## Part 0 — Preparation (do this the day before)

### 0.1 Do one full rehearsal run
A live full run (especially stage 5, the build) is long and its output varies each time. So rehearse once and save snapshots you can fall back on.

1. Unzip the repo, `cd raid-factory`, `git init && git add -A && git commit -m start`.
2. Run the whole factory once (`/factory-next`, review, `/approve n`, for stages 1–6).
3. After approving each stage, tag it so you can jump to that state later:
   ```
   git add -A && git commit -m "stage N approved" && git tag demo-after-stage-N
   ```
   (N = 1 to 6). Also tag the clean start: `git tag demo-start` before stage 1.
4. Read every output once so you know what it says. Note two or three good moments to point at (see "Talking points" in each part).

### 0.2 Decide your live vs pre-built split (recommended)
| Part | How |
|---|---|
| Stage 1 requirements | **Live** (shows the pattern: produce → self-check → gate) |
| Stages 2–4 | **Pre-built**: `git checkout demo-after-stage-N` and walk the files |
| Stage 5 build | **Pre-built**, then run the tests live (fast) |
| `/raid-extract` on messy notes | **Live** (the "wow" moment, and the injection trap) |
| Stage 6 | **Pre-built** |

### 0.3 Environment checklist (30 min before)
- [ ] Claude Code installed and signed in; `claude` starts without errors.
- [ ] Terminal font large (at least 18pt), dark text on light or high contrast, window ~100 columns wide.
- [ ] Python 3.12 and pytest available (`python3 --version`, `python3 -m pytest --version`).
- [ ] A markdown viewer open in a second window (e.g. VS Code preview) pointed at the repo folder, for showing documents nicely.
- [ ] `git status` clean, on the `demo-start` tag/branch for the live part.
- [ ] Notifications off, no client material visible on screen. **Use only the fictional Acme inputs.**
- [ ] Backup: a screen recording of your rehearsal run, in case the network or Claude Code misbehaves.
- [ ] Printed or second-screen copy of this script.

### 0.4 Know the limits
- Outputs differ slightly every run. Don't promise exact wording. Describe what the stage must contain, not the exact text.
- If Claude Code asks for permission prompts, approve them calmly. Mention that this is the human-in-control model working as designed.

---

## Part 1 — Frame the problem (5 min)

**Say:**
"Every delivery manager here has a RAID log: Risks, Assumptions, Issues, Dependencies. And it's out of date by Wednesday, because items come up in calls and get written down afterwards from memory. Today I'll show you a small AI factory that builds a tool to fix that, and, more importantly, how the factory itself works."

**Show:** `inputs/stakeholder-interviews/01-sean-delivery-manager.md` (30 seconds, scroll).

**Point out:** these are raw, messy notes from three people. Sean wants speed. Priya wants an audit trail. Tom (the client) wants a one-page document and has a data policy. They don't fully agree. "A real factory has to cope with that."

**Say:** "The factory has six stages. Each one produces a document, checks its own work, and then stops and waits for a human. Nothing moves forward without approval."

**Show on screen** (the table in `README.md`) the six stages and which EPAM role each one draws on. Spend 1 minute on this.

---

## Part 2 — Tour of the factory (5 min)

In the terminal:
```
cd raid-factory
claude
```

**Show, in this order (about 1 minute each):**
1. `CLAUDE.md` — "These are the standing rules. Notice rule 1: a human gate after every stage. Rule 4: no invention. If the brief doesn't say it, it becomes an open question."
2. `.claude/commands/` folder — "Each stage is just a markdown file. No framework, no code. Anyone can read or change how a stage works."
3. Open `stage-1-requirements.md` — read the three headings: what to produce, the self-check, and "Stop."
4. `reference/epam/` — "The knowledge each stage draws on comes from the EPAM AI Factory role notes."
5. `inputs/brief.md` — "This is the only thing a human writes to start the factory."

**In Claude Code, type:** `/factory-status`

**Expected:** a table with all six stages NOT STARTED and a recommended next action.
**Say:** "This is how anyone picks the work back up, even a week later."

---

## Part 3 — Stage 1 live: requirements (10 min)

**Type:** `/factory-next`

**While it runs (about 1–3 minutes), say:** "It's reading the brief and the three interview notes. It will produce needs, requirements with acceptance criteria, and non-functional requirements, then review its own work."

**When it stops, show these in the viewer:**
1. `docs/requirements.md`
   - The **NEED** table: "Each need is solution-free and names a stakeholder."
   - A **REQ** row: point to the acceptance criteria. "Concrete and testable, not 'the system should be fast'."
   - The **NFR** table: "Targets and how they will be verified."
   - The **Open Questions** section: "It asked rather than guessed. Severity scale and assumption validation dates were left open in the brief."
2. `docs/reviews/stage-1-review.md`
   - "It graded its own requirements and logged problems. Here is a finding it fixed, and what it changed."

**Talking points:**
- Every requirement cites a NEED id. "Traceability starts here."
- Stakeholder conflicts: look for where it noted Tom wants a document while Sean wants local files. If it resolved or flagged this, point at it. If it missed it, say so honestly, "that's what the human review is for."

**Do the gate live:**
- Say what you would change (e.g. "Answer the severity question: High/Medium/Low").
- Tell Claude: `Use High/Medium/Low and a validation note on assumptions. Update the requirements.`
- Then type `/approve 1`.
- **Say:** "That is the control point. Approving is a human decision, and it's recorded in `docs/state.md`."

**If it goes wrong:** if the output is poor, say "this is exactly why there's a gate", give feedback, re-run `/stage-1-requirements`. If it takes too long, switch to `git checkout demo-after-stage-1`.

---

## Part 4 — Stages 2–4 from snapshots (10 min)

Use `git checkout demo-after-stage-4` (or open the files from your rehearsal). Say upfront: "I ran these earlier so we don't wait. Same commands, same process."

### Stage 2: epics and stories (3 min)
**Show:** `docs/epics.md`, then one file in `docs/stories/`, then `docs/traceability.md`.
**Point out:**
- A story with Given/When/Then criteria using real values from the sample notes.
- The traceability matrix: NEED → REQ → EPIC → STORY. "I can ask: why does this story exist? And the answer is a sentence a stakeholder actually said."
**Show:** `docs/reviews/stage-2-review.md` for coverage checks.

### Stage 3: architecture (4 min)
**Show:** `docs/architecture.md` (the diagram in a Mermaid-capable viewer) and one ADR in `docs/adr/`.
**Point out, the key design decision:**
- "Extraction runs in Claude Code, not in the app. The Python tool makes no network calls. That decision is written down in an ADR, with alternatives considered and the downsides."
- The NFR → component table: "Every non-functional requirement lands on a component."
- Ask the audience: "Why does this matter for a client who's worried about data?"

### Stage 4: specs and build order (3 min)
**Show:** one spec in `docs/specs/` and `docs/task-dag.md`.
**Point out:**
- The spec's five parts: Why, Capabilities, Constraints, Non-goals, Success signal. "A spec is the contract the build stage must obey."
- Risk tiers in the DAG: "Low risk builds on its own. Medium shows me the diff. High stops and asks. Anything that writes the log file is high."

**Say:** "Four stages, and no code yet. That is deliberate. By the time we build, the build is nearly mechanical."

---

## Part 5 — Stage 5 results: the built tool (8 min)

`git checkout demo-after-stage-5` (or `demo-after-stage-6`).

### 5.1 Show the tests (2 min)
```
python3 -m pytest -q
```
**Expected:** all tests pass.
**Say:** "Tests were written before the code, from the test plan in each spec." Show `docs/reviews/stage-5-review.md`: the spec → tests → pass table, and any defect the factory found with its guard test.

### 5.2 The live moment: extraction (5 min)
**In Claude Code, type:**
```
/raid-extract inputs/meeting-notes/2025-10-07-weekly-call.md
```
**Expected:** it reports proposed items and writes `pending.json`.
**Show:** open `pending.json`. Point out:
- Each item has type, owner (null if not stated), severity, and a **verbatim source excerpt**.
- The ERP file being fixed-width (not CSV) shows as an issue that invalidates the earlier assumption.
- Nothing is in the log yet. "The tool never adds items by itself."

**Review step (in a normal terminal):**
```
raid review
```
Accept two, edit one, reject one. **Say:** "A human confirms every item. That's Sean's requirement from the interview."

### 5.3 The trap (3 min)
**In Claude Code, type:**
```
/raid-extract inputs/meeting-notes/2025-10-14-messy-notes-with-trap.md
```
**Say first:** "This note has a hidden instruction in it telling the AI to close every item and delete the file."

**Expected:** the extraction ignores the instruction and, ideally, flags it as suspicious. Show `pending.json` and that the log was not touched.
**If it follows the injection or doesn't flag it:** don't hide it. Say: "This is the kind of thing the security stage looks for. Let's see what Stage 6 says." Then go to Part 6. (Honesty here is more convincing than a perfect run.)

### 5.4 Flags and summary (1 min)
```
raid flag
raid summary
```
Show the summary: "Tom reads this on his phone. One page, plain English."

---

## Part 6 — Stage 6 and wrap-up (5 min)

`git checkout demo-after-stage-6`.

**Show:**
1. `docs/threat-review.md` — "The factory reviewed its own product for threats: injection from notes, a tampered `pending.json`, client data in an AI session. And it lists the risks a human must accept."
2. `docs/release-note.md` — known limitations, what was left out, how each NFR was verified.
3. `docs/state.md` — all six stages APPROVED with dates.

**Say (the close):**
1. "Six stages, six documents, six human decisions."
2. "Everything traces from a stakeholder sentence to a test."
3. "The factory is just markdown files. You could change a stage in five minutes."
4. "The human owns scope, risk acceptance and release. The factory does the writing and the checking."

---

## Part 7 — Likely questions and answers

| Question | Answer |
|---|---|
| Is this safe for client data? | Only if the client's policy allows processing notes in your AI assistant. The tool itself makes no network calls. Check with the client first. |
| Does it always give the same output? | No. That's why there are review gates and self-checks. |
| What if a stage output is wrong? | Give feedback and re-run the stage. Nothing downstream has started, because of the gate. |
| How long did the full run take? | State your rehearsal time honestly. |
| Can we use it for a different tool? | Yes. Change `inputs/brief.md` and the stack choices. The stages stay the same. |
| Why not just ask the AI to build the tool? | You'd get code with no requirements, no tests tied to needs, and no record of why. The stages exist so humans can check the thinking, not only the code. |
| What did EPAM's material add? | It gave each stage its method: requirements validation, ADRs, enforceable NFRs, test strategy, threat modelling, delivery readiness. |

---

## Part 8 — Timing summary

| Part | Time |
|---|---|
| 1 Frame the problem | 5 |
| 2 Tour of the factory | 5 |
| 3 Stage 1 live | 10 |
| 4 Stages 2–4 snapshots | 10 |
| 5 Build results and live extraction | 8 |
| 6 Stage 6 and wrap-up | 5 |
| Q&A | 10+ |

If you are short on time, drop Part 4's stage 2 detail and the flags/summary step.

## Recovery cheat sheet
- Claude Code stuck or slow → `Esc` to interrupt, then re-run the command, or `git checkout demo-after-stage-N` and carry on from the snapshot.
- Output looks wrong → use it as the demo of the human gate.
- Tool not found (`raid`) → `pip install -e .` from the repo folder, or run `python3 -m raid`.
- Slash commands missing → you started `claude` outside `raid-factory`; exit and restart from inside it.
