# In a nutshell

Two engineers run the same task with the same AI. One leaves a trail anyone can follow; the other ships a pull request that says "AI helped write this" and nothing more. That gap is the whole point of this track: **AI-assisted work is trustworthy only when someone outside the author's head can reconstruct what was checked, by whom, against what.** Engineering is where the spec becomes running code — it comes after Consulting, Product, Design, and Architecture. The Wide path is for every non-engineering role: you learn to recognise reliable AI-assisted engineering and ask for the evidence when it's missing, not to write the code yourself.

# Role Context

- **Who it's for.** All learners who do not specialise in Engineering: consultants, PMs/BAs, designers, architects, QA, data, infrastructure, security, delivery, and management.

- **What the role does.** Builds the layered context bundle, writes a spec before coding, directs the AI to implement, generates independent tests, reviews the diff, enforces quality in CI, and ships a PR that links all of it together.

- **Where it sits.** Downstream of Architecture and Design, upstream of Quality. Engineering receives the spec package, the prototype, and the architecture pack; it hands back working code plus the evidence that QA, Security, and Infrastructure act on.

- **The common failure.** Engineering gets a ticket with no spec, builds against the ticket, and ships code that answers a different question from the one the team asked.

- **L2 → L3 shift.** The L2 engineer uses AI and accepts the output when tests turn green; the L3 engineer treats the workflow as a system that produces auditable evidence — context, spec, independent tests, review, and a PR anyone can reconstruct.

# Why this matters for you

You may never write production code. But your team will ship code that AI helped produce, and you will be asked to act on it — schedule it, sell it, secure it, deploy it, test it, or design around it. This hour gives you the vocabulary to join those conversations and the questions to ask when the evidence behind a change is thin, without taking the engineer's word for everything. The same skills let you read the codebase yourself: with an approved tool you can ask "what statuses can an order have?" instead of waiting for an engineer to find out.

<img src="media/image1.png" style="width:6.26806in;height:2.68403in" />

# Topic recap

The track runs in six short blocks — here's each in brief.

- **Local setup and guardrails (Block 1).** How an AI-assisted environment is set up before any AI helps: the repo (the team's code under version control), the rule file the AI reads every session, and the three context layers — hot (always loaded), warm (loaded by task), cold (loaded for history). Two guardrails frame it: use only approved tools, and start read-only when you're exploring. Warm context does the most work and is the layer that quietly goes stale.

- **AI-assisted development (Block 2).** The careful loop, in order: requirement → plan and context → code → independent tests → review → evidence. Two ideas carry it — context (what the AI can read before it starts) matters more than clever prompting, and you write a short brief before building so you have something to check the output against. Match the model tier to the task; the most capable model isn't always the right one.

- **How a change moves, and where controls run (Block 3).** A change travels as a commit on a branch, proposed in a pull request — and the PR is where the evidence of an AI-assisted change lives. Hooks run on one engineer's laptop and break when the tool changes; CI required checks run on the shared server and apply to every change, so they are the real enforcement. The evidence a PR carries scales with risk: a rename needs nothing extra, an auth or billing change needs a full provenance note.

- **Independent verification (Block 4).** A test has to be independent from the code it checks: tests written in the same session as the implementation share its blind spots and pass for the wrong reason, while tests built from the requirement in a fresh session fail when the code misses the spec. Four lenses help you read any AI-assisted change — behaviour preservation, hidden assumptions, drift from spec or architecture, and confirmation without evidence — and none needs you to read code.

- **Coding agents (Block 5).** Agents now run from a terminal and can read a repo, write code, and open PRs on their own. The first question is whether a human watched: supervised work is spot-checked, async work must be reconstructed from the evidence it leaves. A skill packages a repeatable procedure once so the agent runs it on demand; an MCP connection gives the agent live data — the codebase, a database, a ticket — instead of a pasted copy.

- **Talk to your code (Block 6).** The capability you take away: ask your own codebase grounded questions with an approved, read-only tool instead of waiting for an engineer. A trustworthy answer has a shape — scope the files, ask specifically, request file:line sources, and ask what couldn't be verified. An answer with no sources and no named gaps is a hypothesis to check, not a finding. Never paste secrets or client code into an unapproved tool.

<img src="media/image2.png" style="width:6.26806in;height:1.175in" />

Key terms

<img src="media/image3.png" style="width:5.91697in;height:3.77103in" />

# Key takeaways

1.  "Show me the context the AI had loaded" tells you more than "show me the prompt" — what the AI can read, not how the request is phrased, shapes the output.

2.  Independent tests come from the requirement in a separate session; tests written beside the code only confirm what the code already does.

3.  A hook on one laptop isn't enforcement — if a control matters, it lives in a server-side CI required check that blocks merge.

4.  Match the evidence you ask for to what the change can break: nothing extra on a rename, a full provenance note on auth, billing, or data.

5.  You can ask your own codebase questions — but trust the answer only when it cites file:line sources and names what it couldn't verify.

**Course Repo: <https://epa.ms/ai-run-26-curriculum-repo>**

# Wide Theory

1 hour

**Focus:** Equip the whole team to recognise reliable AI-assisted engineering evidence — context layers, spec discipline, independent tests, and provenance — and equip engineers to produce it: a layered context bundle, spec-driven delivery loop, seven-lens code review, CI-enforced quality gates, and a PR that every downstream role can audit without asking the engineer to reconstruct the session.

**Deep for:** Software Engineers, Backend Developers, Frontend Developers, Full-Stack Developers, Platform Engineers.

**Total time per learner:**

- Wide path: 60 min Theory + 135 min Katas (9 × 15) + 60 min Final Kata ≈ 4h15

- Deep path (own role): + 265 min Theory + 330 min Katas (11 × 30, core path) ≈ +10h (Final Kata is universal — done once)

Every role on an AI-native team ends up acting on code that AI helped write — you schedule it, sell it, secure it, test it, deploy it, or build the next feature on top of it. To do that well you don't need to write the code, but you do need to recognise what reliable AI-assisted engineering looks like and ask for the evidence when it's missing. That is what the Wide path teaches every team member, whatever your role.

For the engineer, the shift goes deeper. The engineer is where the spec becomes running code. The L2 engineer uses AI tools and accepts output when tests turn green. The L3 engineer treats the AI workflow as a system: a layered context bundle the agent reads before every session, a spec that is the contract before any code is written, tests generated in a separate session that has never seen the implementation, and a PR that carries enough evidence for QA, Security, and the next engineer to reconstruct what happened and why. The Deep path gives engineers the ten disciplines to produce that evidence.

**Objectives**

- **Learn to do:** direct an AI coding agent through a complete feature delivery on a sandbox repo — context setup, spec, supervised implementation, independent tests, a CI-gated PR, a reviewed refactor, and a by-hand-vs-agent comparison (Wide); produce the full ten-discipline evidence chain and a CI-enforced quality gate for a real feature on your own stack (Deep)

- **Skills (role):** context engineering (hot/warm/cold layered bundle); spec-driven delivery (greenfield spec and brownfield delta with supervised agent direction); independent verification (independent test generation, seven-lens and adversarial review); CI gate authorship and PR provenance

- **Skills (tooling):** Claude Code CLI, Cursor, CLAUDE.md / AGENTS.md rule files, /model tier switching, subagent dispatch, Skill authoring and packaging, GitHub PRs & branch protection, GitHub Actions CI, pytest and ruff (Wide)

- **Outcome:** CLAUDE.md + layered context bundle + working CLI + independent tests + CI workflow + refactor notes + repo Q&A + by-hand-vs-agent comparison (Wide); feature spec or delta + context bundle + session log + independent tests + seven-lens review + adversarial findings + CI gate + PR provenance block (Deep); engineering role-agent spec (Final Kata)

- **Tested by:** K 5.W.1–9 (Wide kata series) + K 5.3 (Final Kata); the Deep path adds K 5.D.1–13

# 0 — Role Context

**How to read this section.** Two audiences share it. If Engineering is your role, this is your own role description — read it as the L3 standard you produce against. If you take this module Wide — PROD/BA, design, architecture, QA, data, infrastructure, security, delivery, or management — read it to understand the role you collaborate with and the evidence reliable AI-assisted engineering should hand you. You are not expected to do the engineering; you are expected to recognise it.

**0.1 — Role names and who they apply to**

This module is for everyone on a delivery team. If you write, modify, or ship code as a primary work product, the Deep path is yours — it teaches you to produce the engineering evidence. Everyone else — PROD/BA, design, architecture, QA, data, infrastructure, security, delivery, or management — takes the Wide path and learns to recognise that evidence and ask for it when it is missing. Common engineering job titles (Deep):

- **Software Engineer** — writes and maintains application code across the stack; owns implementation quality and the engineering evidence that supports review.

- **Backend Developer** — owns server-side logic, APIs, data access, and service integrations.

- **Frontend Developer** — owns the client-side layer: UI components, browser interactions, and frontend performance.

- **Full-Stack Developer** — owns both layers and often coordinates the handoff between them.

- Common synonyms across firms: Application Engineer · Platform Engineer · Developer · Senior Engineer · Software Developer · Principal Engineer · Staff Engineer.

If your title varies, the test is functional. Do you spend material time writing, reviewing, or shipping code on a team that uses AI tools? If yes, this module covers you Deep — the Deep path teaches you to produce the evidence. If instead you act on code that AI helped produce without owning the implementation — you schedule it, sell it, secure it, test it, deploy it, or build on it — the Wide path covers you, and teaches you to recognise that evidence and ask for it when it is missing. On an AI-native team, every engineer — regardless of seniority or specialisation — has to understand what reliable AI-assisted work looks like so they can produce it and recognise it in review; every other role has to recognise it well enough to act on it.

**0.2 — Role description and core duties**

The engineer owns the surface between *"here is the spec and design"* and *"here is working, shippable code with evidence that it does what the spec required."* In observable verbs:

- **Builds and maintains** the layered context bundle — the hot rule file, the warm reference files, the cold archive — so every AI session starts from the team's actual conventions, not a cold guess from training data.

- **Specifies** before implementing: writes a greenfield spec with **acceptance criteria** (course Glossary — Learn portal or curriculum repo: ./modules/000-glossary.md#acceptance-criteria), **NFRs** (course Glossary — Learn portal or curriculum repo: ./modules/000-glossary.md#nfr), and edge cases, or a brownfield delta with explicit ADDED / MODIFIED / REMOVED accounting.

- **Implements** in supervised or async mode, capturing rejected alternatives and discovered constraints in a session log.

- **Generates independent tests** in a context that has not seen the implementation, from the spec alone, so the test surface does not share the implementation's blind spots.

- **Reviews** AI-generated code with seven structured lenses plus at least one adversarial pass before opening a pull request.

- **Enforces** quality at the CI layer — server-side required checks that survive tool changes, not only local hooks.

- **Ships** PRs with a provenance block that links the spec, the tests, the review, and the session log so any downstream role can audit the chain without asking the engineer to reconstruct it.

- **Packages** repeatable workflows as portable Skills so the next engineer — or the next agent — can follow the same procedure without reinventing it.

What this role does *not* own: product scope (PROD/BA owns the spec; engineering implements it), the architecture record (Architects own the ADRs; engineers implement within them), QA sign-off (QA runs the eval harness against the production signal), and deployment scheduling.

**0.3 — Main processes**

The ten disciplines that structure engineering work at L3 (each maps to a section of Deep Theory):

- **Layered context engineering** — building, versioning, and refreshing the hot/warm/cold context bundle as repo reality changes (5.1).

- **Agents-as-code harnesses** — rule files, Skills, MCP servers, slash-commands, hooks, and CI required checks, each at the right scope (5.2).

- **Spec-driven development** — four-phase greenfield flow (spec → plan → tasks → implementation) and brownfield delta flow (ADDED / MODIFIED / REMOVED) with living spec discipline (5.3).

- **AI code review** — business requirements review before implementation, seven-lens review of the generated diff, and adversarial pre-mortem and edge-case-hunter passes (5.4).

- **Modernization and reverse engineering** — reading existing code, producing a delta-spec, and applying the brownfield flow to keep the REMOVED section honest (5.5).

- **Test data synthesis and independent test generation** — representative test data at the right model tier; tests generated in a context that has never seen the implementation (5.6).

- **Build, integration, and CI enforcement** — server-side required checks that survive tool changes, and the line between what belongs in a hook and what belongs in CI (5.7).

- **Database engineering discipline** — the irreversibility boundary for schema migrations and the validation protocol before any DDL runs against non-test data (5.8).

- **Application knowledge and log mining** — using the agent to answer questions about the codebase for roles that cannot read code directly (5.9).

- **Maintenance, supervision, provenance, and replay packets** — session observability, PR provenance blocks, and the replay packet that makes a failing agent run reproducible (5.10).

**0.4 — Role in SDLC**

Engineering sits **downstream of Architecture and Design** and **upstream of Quality**. The central audience contract:

<img src="media/image4.png" style="width:6.02809in;height:3.96548in" />

The most common upstream failure: Engineering receives a ticket without a spec, implements against the ticket, and produces code that answers a different question from the one the product team asked.

**0.5 — How the role changed with AI (general)**

Two shifts, at high level:

- **Shift 1 — AI accelerates the implementation work itself.** Code generation, refactoring, modernization, documentation, test scaffolding. This applies on every project — greenfield, brownfield, and maintenance alike. The engineer's day moves from typing code to directing the agent, loading context, and reviewing the output for gaps the agent cannot catch.

- **Shift 2 — when the agent produces the code, the engineer owns the evidence.** A change the engineer typed carries implicit provenance — the engineer's knowledge was in the code. A change the agent generated has no provenance unless the engineer builds it explicitly: spec, context, session log, review, and a PR that links all of them.

What collapsed: mechanical code authoring, boilerplate generation, first-pass test scaffolding, search-and-replace refactors. What amplified: context curation, spec quality requirements, review depth, CI gate authorship. What survived and got more valuable: judgement — what the spec actually requires, which part of the diff needs more scrutiny, and when to reject the agent's first instinct.

**0.6 — What changed at L2 (AI-assistant)**

At L2 the human still owns the implementation; AI is a copilot. Where AI assists:

- Autocomplete and code completion inside the IDE.

- Generating boilerplate, scaffolding, and test stubs from the current file context.

- Explaining unfamiliar code sections and suggesting refactors.

- Drafting first-pass implementations from a ticket description.

Stays human at L2 (the lines that do not move): **architectural decisions**, **security-sensitive code paths**, **the merge button**, and **"is this implementation correct for this specific requirement?"** A developer who uses AI only for autocomplete, explanation, and first-pass generation is operating at L2.

**0.7 — What changed at L3 (AI-native)**

At L3 the workflow restructures around a layered context system, a spec-first discipline, and a provenance chain. The role's scope expands; it does not disappear. The concrete shifts:

- **Context bundle as repo infrastructure.** The hot rule file, the warm reference files, and the cold archive are versioned alongside the code. Updates are triggered by the same events that trigger **ADR** (course Glossary — Learn portal or curriculum repo: ./modules/000-glossary.md#adr-architecture-decision-record) changes — not by periodic memory.

- **Spec before session.** Every non-trivial feature starts with a written spec that the agent implements against. The spec is the single source of truth the review checks against. When the spec changes, the PR carries the change.

- **Independent test generation.** Tests are produced in a session that has not seen the implementation — a structurally different starting point from "the same agent writes the code and the tests." The gap between what the tests cover and what the spec requires is the engineer's review responsibility.

- **Seven-lens review as a structured practice.** Code review is not "does this look right?" — it is seven passes, each looking for a different class of AI-generated gap (behaviour preservation, hidden assumptions, spec drift, test independence, edge cases, security surface, over-engineering).

- **CI required checks as the enforcement floor.** Controls that matter go server-side. A hook that runs on one engineer's workstation is not enforcement; a required check that blocks merge is.

- **PR provenance as the evidence package.** A PR that says "AI assisted" is not documented. A PR that links the spec, the session log, the independent tests, the seven-lens review, and the adversarial findings is the evidence package any downstream role needs to act on the change with confidence.

The Wide path teaches you to *recognise and evaluate* this evidence. The Deep path teaches you to *produce* it.

# 1 — Theory

<img src="media/image5.png" style="width:4.54885in;height:1.66675in" />

# 2 — Materials and Links 

Tool references (Claude Code CLI, AGENTS.md spec, GitHub Actions, pytest, ruff), internal knowledge links, optional external references, and the reference-case task menu (learner-project — the log-summariser sandbox for Wide, your own-stack repo for Deep).

# 3 — Practice

**How this connects to what you built.** In the Consulting, Product, Design, and Architecture modules you took one subject — your own project, or a reference case (Meridian or Kepler) — from an opportunity through a spec, a clickable prototype, and an architecture pack. Engineering is where those become running code: the Wide series builds a small, runnable tool you can tie back to that platform, and the Deep series implements a real feature on your own stack, seeded by the Architecture Context Pack you carried forward. Keep the same subject you carried upstream; the connection is an overlay on the practice, never a hard dependency.

**Practice rule for every kata and the Final Kata in this module:** the Wide series runs on the log-summariser CLI sandbox — all context, data, and code is AI-generated on your laptop; synthetic logs only, no real customer data, no production deployments. If you have a real backlog item that fits in ~15 min of AI-assisted work, use that instead. The Deep series runs on a real repo from your own work — or on the sandbox the Wide series produces, if you have nothing else. Stay on one repo for the full Deep series; switching mid-series breaks the carry-forward chain.

**3.1 — Wide Katas**

K 5.W.1 → K 5.W.9 (nine katas, ~135 min total; the Engineering onboarding block runs to nine 15-minute katas so the by-hand → by-agent capstone survives without overloading a single kata). **Superpower moment.** You shipped a small program end-to-end without writing code by hand — first as a supervised loop, then as an agent replay — and you can name specifically where the AI saved time and where it went wrong. Chains into a working sandbox repo with CLAUDE.md, spec.md, src/, tests/, CI workflow, refactor notes, repo Q&A, and the load-bearing by-hand-vs-agent.md capstone artefact.

**3.2 — Deep Katas**

K 5.D.1 → K 5.D.13 (core path: K 5.D.1–11, 11 katas; advanced extension: K 5.D.12–13). Specialist outcome: *a feature evidence chain — context bundle + spec or delta + plan + session log + independent tests + seven-lens review + adversarial findings + CI gate + PR provenance block — that any downstream role can audit cold.*

**Scope of the Deep series.** Thirteen katas compose in five phases: infrastructure (context bundle, portable Skill, CI gate), specification (greenfield spec or brownfield delta, then task decomposition), implementation (supervised session + session log), verification (seven-lens review + adversarial pre-mortem and edge-case-hunter), and delivery (PR provenance block). Katas K 5.D.12–13 are an advanced extension covering architectural debate and replay-packet authoring.

**3.3 — Final Kata**

K 5.3 — specify a runnable Engineering role-agent / Skill in a native format another teammate can load and use.

# 4 — Carry-Forward

Two artefacts leave this module for consumption downstream.

**4.1 — Feature Evidence Chain**

- **Artefact name:** Feature Evidence Chain.

- **Source:** Deep kata series K 5.D.1–11 — context bundle + spec or delta + plan + tasks + session log + independent tests + seven-lens review + adversarial findings + CI gate + PR provenance block. Produced on a real repo (or the log-summariser sandbox from the Wide series if no real project is available).

- **Consuming stage(s):**

- **Quality** — consumes the independent test artefacts (spec, tests, pass/fail record) and the seven-lens review findings to drive QA verification; uses the CI gate configuration from K 5.D.3 in the QA eval harness.

- **Security** — consumes the security-lens findings from the seven-lens review and the PR provenance block to trace security-sensitive decisions.

- **Infrastructure & Operations** — consumes the operational impact notes from the business requirements review and the run-operational requirements in the PR.

- **Final Assembly Line** — the Feature Evidence Chain is what Engineering's subagent produces in the end-to-end delivery scenario.

- **Format:** Markdown in the repo — specs/\<feature-id\>/ (spec, audit, plan, tasks) or changes/\<change-id\>/ (delta, plan, tasks); sessions/\<task-id\>/session-log.md; independent tests in the repo's own test convention; reviews/\<pr-or-task-id\>/review.md; PR body (provenance block); .github/workflows/\<gate\>.yml (CI gate).

**4.2 — Engineering Role-Agent Spec**

- **Artefact name:** Engineering Role-Agent Spec.

- **Source:** Final Kata K 5.3 (all learners; specialists add the depth sections covering the full ten-discipline harness).

- **Consuming stage(s):** **the downstream role modules (Quality through Delivery & Project Management)** load .claude/skills/engineering/ or .claude/agents/engineering.md when no engineer is on the team — read in place for implementation context, not transformed. **Final Assembly Line** lists it in the agent roster a joining teammate reads.

- **Format:** a runnable Claude Skill or sub-agent, ≤ 2 pages of body, with the human-owned decisions (architecture approvals, merge button, security overrides, exception decisions on verification gates) inline as guardrails.

- **Engine guide target:** .ai-run/guides/standards/code-quality.md, under header \## Code-quality standards + verification evidence (from Module 500 — Engineering). This is the authoritative chain mapping; the spec's \<!-- chain:rules:start guide=… topic=… --\> delimiter attributes mirror it, and on any disagreement this line wins.

- **Optional stand-in override (Deep only):** code-reviewer — gates code-review.final, code-review.check; the spec's escalation triggers map to its verdict.

**Why This Matters for You**

Two engineers use about the same amount of AI for the same task. Both produce working code. Only one leaves evidence that another person can follow.

**The shortcut.** An engineer gives AI a vague request. The tests turn green, so the engineer opens a pull request. The description says, "AI helped write this."

The request is missing. The AI's context is missing. The test origin and human changes are missing. Two weeks later, a problem appears. The team cannot reconstruct how it entered the code.

**The workflow.** Another engineer begins with the requirement and project context. AI drafts the implementation. A separate session writes tests from the requirement.

The engineer checks the result against the spec. She records manual changes and open gaps. The pull request gives QA, Security, Infrastructure, and future engineers a trail they can audit.

The difference becomes visible across five dimensions:

<img src="media/image6.png" style="width:5.90308in;height:3.0696in" />

<img src="media/image7.png" style="width:6.26806in;height:2.39444in" />

Your role may stay outside production code. Your team will still ship code that AI helped produce. You may schedule, sell, secure, deploy, test, or design around it.

This Wide Theory gives you the vocabulary and questions to act without taking an engineer's word for everything. You can challenge thin evidence before it becomes a delivery promise or production risk.

It also gives you a capability many non-engineers leave unused: asking the codebase grounded questions through an approved AI tool. The repository stops being a black box reserved for Engineering.

That changes everyday handoffs. QA can trace a test to its requirement. Security can inspect how a sensitive path was produced. Delivery can separate reported progress from verified progress.

Repository self-service removes another delay. A PM can inspect status rules. A designer can confirm the frontend stack. Infrastructure can locate service dependencies.

Instead of waiting for someone to answer, "What statuses can an order have?", you can begin the investigation yourself. A useful answer cites its sources and exposes its gaps. Block 6 teaches that move safely.

**Goal**

Learn to recognise reliable AI-assisted engineering. Ask for missing evidence. Use approved tools to investigate a codebase without becoming its engineer.

**Time**

~60 min: ~45 min for the core theory and ~15 min for Block 6 practice.

**Audience**

This path is for consultants, PMs/BAs, designers, architects, QA, data, infrastructure, security, delivery, and management.

Engineers can use it as a refresher. Engineering depth lives in Deep Theory.

**Prerequisites**

Complete Onboarding, Fundamentals, Consulting & SME, Product Management & BA, Design & Experience, and Architecture.

Keep these upstream materials available:

- opportunity brief from Consulting & SME;

- **Spec Package** (course Glossary — Learn portal or curriculum repo: ./modules/000-glossary.md#spec-package);

- prototype, CONTEXT.md, and SPEC.md from Design & Experience;

- **Architecture Context Pack** (course Glossary — Learn portal or curriculum repo: ./modules/000-glossary.md#context-pack) with ADRs and enforceable NFRs.

These materials define intent and constraints. Engineering turns them into code and evidence.

**Must Cover**

**AI-assisted work is trustworthy only when someone else can reconstruct what was checked, by whom, and against what.**

The path starts with shared language. It then follows an AI-assisted change from setup to source-backed investigation.

- **Shared vocabulary** — PR, repo, spec, CI, ADR, context, rule file, model tier, and provenance.

- **Local setup and guardrails** — repository, rule file, context layers, approved tools, and read-only access (Block 1).

- **AI-assisted development** — the mini-cycle, context before prompting, planning before building, and model tiers (Block 2).

- **How a change moves and where controls run** — commits, branches, PRs, hooks, CI, and risk-based provenance (Block 3).

- **Independent verification** — fresh-session tests and four review lenses for any role (Block 4).

- **Coding agents** — supervised and async work, Agent Skills, and MCP connections (Block 5).

- **Talk to your code** — safe, grounded repository questions with source-backed answers (Block 6).

The blocks use the terms below repeatedly. Learn their plain meaning before following the workflow.

<img src="media/image8.png" style="width:5.84058in;height:6.2781in" />

**Key Messages / Ideas**

Seven messages connect the theory. Each answers one review question you can use outside Engineering.

1.  **Trustworthy AI work is reconstructable.** Ask what was checked, by whom, and against what.

2.  **Context is infrastructure.** Ask what the AI could read before it started.

3.  **Plan before building and match the model to the task.** Ask which written intent guided the output. Check whether the model tier fits the task's risk, cost, and complexity.

4.  **Hooks help; CI enforces; provenance scales with risk.** Ask whether important controls block every shared-server change. Match the evidence to the change's blast radius.

5.  **Verification needs independent context.** Ask whether tests came from the requirement or the implementation session.

6.  **Agent mode changes review depth; Skills and MCP shape capability.** Ask whether a human watched the work. Check which procedure and live access the agent used.

7.  **Grounded answers cite sources.** Ask for files, lines, conflicts, confidence, and unverified gaps.

**Structure (Per-topic context blocks)**

# Block 1 — Local Setup and Foundational Knowledge

Reliable output starts before the first prompt. The repository, rule file, context layers, and access controls shape what the AI can do safely.

**The repository and the assistant**

A *repository* stores code and related files under version control. Its history shows how the code changed. Engineering investigations often begin there.

An *AI coding assistant* can read, explain, edit, and test repository code. Its answer depends on the files and instructions it can access.

Reliable output also needs a current, relevant, and approved source.

**The rule file**

A *rule file* gives an AI tool persistent project instructions. It names the project, conventions, boundaries, and paths to deeper context.

Common names include:

- CLAUDE.md for Claude Code;

- .cursorrules or project rules for Cursor;

- .github/copilot-instructions.md for GitHub Copilot;

- AGENTS.md for several agent tools.

The filename varies. The job stays the same: give each session a short, maintained starting point.

A current rule file grounds the AI in project reality. A stale file sends the AI toward old patterns. A missing file makes each session depend on pasted context and model training.

Use the rule file as a project index. Point to deeper sources when the task needs them. This keeps the always-loaded layer focused and reduces conflicting instructions.

Maintenance matters as much as creation. Update the file when a convention, toolchain, or system boundary changes. A named owner and review trigger make that update more reliable than memory.

**The three context layers**

AI tools have limited context windows. Engineering therefore loads project knowledge in layers.

A **context layer** is a group of information loaded at a defined moment. See **Context Layer** (course Glossary — Learn portal or curriculum repo: ./modules/000-glossary.md#context-layer).

<img src="media/image9.png" style="width:6.26806in;height:2.49444in" />

<img src="media/image10.png" style="width:6.00725in;height:1.81954in" />

Warm context usually carries the repository's working shape. It does the most task-specific work. This also makes warm-context drift expensive.

Hot context should stay short. Hundreds of competing instructions force the AI to guess which rule applies.

A rule file with several hundred lines is a warning sign. Move task-specific detail into warm context and link to it.

Consider a team that migrates from REST to GraphQL. Its warm stack document still says REST. Three sprints later, AI keeps generating REST clients.

Every output needs human correction. A twenty-minute context refresh would have prevented that repeated cost.

The three layers solve different problems. Hot context gives every session a safe starting point. Warm context gives one task enough technical depth. Cold context preserves history without crowding current work.

Loading everything at once defeats the model. The session becomes slower, more expensive, and harder to direct. Load the smallest current set that can support the task.

**Approved tools only**

**Use approved tools for project work.** Approval should cover data handling, logging, access, retention, and contractual boundaries.

Public tools may sit outside those controls. Ask Security or your project owner when approval is uncertain.

Approval applies to both the tool and the connection. An approved assistant connected to an unapproved data source still crosses a boundary. Check which repositories, trackers, and databases the setup may access.

**Read-only by default**

Begin repository investigation with read-only access. The tool may read files, while edit, shell, database, and external-service actions stay disabled.

Escalate access only when the role, task, and environment require it. This keeps a learning question from becoming a system change.

Read-only is a starting posture. Source code can still contain confidential logic or embedded secrets. Use the same data-classification rules that apply to human access.

# Block 2 — Application Development and AI Assistance

The environment provides safe context. The delivery loop then turns written intent into code, independent tests, review, and evidence.

**The mini-cycle**

The L3 engineering mini-cycle has six ordered steps:

requirement → plan / context → code → independent tests → review → evidence

1.  **Requirement** — write what the work must achieve before implementation starts.

2.  **Plan and context** — choose an approach and load the relevant project sources.

3.  **Code** — AI drafts the implementation while the engineer supervises or reviews.

4.  **Independent tests** — a separate session writes tests from the requirement.

5.  **Review** — challenge scope, assumptions, behaviour, security, and evidence.

6.  **Evidence** — package the change so another role can audit it cold.

<img src="media/image11.png" style="width:6.26806in;height:1.12917in" />

Focus on spotting missing steps rather than memorising the loop. A gap early in the loop weakens every later claim.

**The bottleneck moved**

AI reduced the effort needed to produce working-looking code. Review effort remains.

The slow questions now require judgement:

- Does the implementation match the requirement?

- Did AI invent an interface contract?

- Are the tests genuinely independent?

- Can another team safely pick up the result?

The engineer's work shifts from typing toward intent, supervision, and evidence review. Generation became cheaper. Trust still has to be earned.

This shift changes planning conversations. A fast first draft can make a task look nearly complete. Review, integration, security, and evidence work may still remain.

Review the state of the evidence alongside the state of the code. "Generated" and "ready for merge" describe different workflow points.

**Context matters more than prompting**

*Prompt engineering* improves the wording of one request. *Context engineering* controls the sources and instructions available before the request.

A clever prompt cannot supply missing architecture decisions or current conventions. It also disappears when the team changes tools.

Maintained context survives across tasks and tools. A good prompt against stale context still produces stale output.

Context engineering also decides what stays outside the session. Irrelevant files create noise. Sensitive sources may exceed the tool's approved boundary. Historical records may conflict with current rules.

The engineer should be able to name the selected sources and explain why they fit the task. That explanation becomes part of the review trail.

For review, ask:

What context did the AI have loaded?

That question reveals more than a polished prompt transcript.

**Plan before building**

Write a short brief before asking AI to build. A paragraph or focused list is enough for Wide-level review.

The brief should answer:

- What should this component do?

- Who uses it?

- Which decisions should it support?

- Which boundaries must it respect?

- What sits outside scope?

AI fills gaps with plausible guesses. Written intent makes those guesses visible and gives review a comparison point.

The plan adds another checkpoint. It turns the brief into an approach before code makes the approach expensive to change. Reviewers can challenge scope, dependencies, and architectural fit at this cheaper stage.

Watch for a spec that emerged from the code. Acceptance criteria written after implementation often describe current behaviour. They may fail to represent the original intent.

This creates a circular proof: the code defines the tests, then the tests confirm the code. The original business need disappears from the chain.

The terms connect in order. The requirement states the need. The spec makes that need implementable. Acceptance criteria define observable pass conditions.

**The model spectrum**

Model names change, but most providers offer several capability and cost tiers. The task should determine the tier.

<img src="media/image12.png" style="width:5.90308in;height:1.61119in" />

Claude Code commonly presents Haiku, Sonnet, and Opus families. GitHub Copilot may change or partly abstract its underlying models. Cursor lets engineers select provider models by task.

Names can change while the tiering idea survives.

The most capable model is not always the best choice. A stronger model adds little value to routine boilerplate.

A risky refactor deserves stronger reasoning. Compare the same output across two or three capability levels. Judge every result against the same pre-written quality criteria.

The cheaper tier may already satisfy the need.

The comparison only works when "good" is defined first. Otherwise the most polished answer wins, even when it misses the requirement.

Model choice also affects provenance. Record the tier or model when it materially changes cost, risk, or reproducibility. Routine drafting rarely needs a full model history.

# Block 3 — Code Modification and Insights

The mini-cycle produces a change. Git and CI then make that change reviewable, enforceable, and traceable.

**How a change moves**

A *commit* is a saved snapshot with a message. A *branch* isolates a line of work from the main codebase.

A *pull request* proposes merging that branch. It shows the diff, carries review discussion, and links automated checks.

For a Wide learner, the PR is the main audit surface. This is where AI-assisted evidence either appears or goes missing.

The branch keeps unfinished work away from the main codebase. Commits divide that work into reviewable snapshots. The PR then connects those snapshots to discussion and controls.

These records answer different questions. Commits show how the implementation moved. The PR shows why the team accepted it.

**Hooks and CI**

A *hook* runs on an engineer's workstation. It can block a dangerous shell command or format an edited file.

A *CI required check* runs on a shared server. Every pull request triggers it, regardless of local tool or workstation.

The boundary is direct:

**Hooks help locally. CI required checks enforce for the team.**

If a process says, "our hooks prevent dangerous patterns," ask one more question:

Does a server-side required check block the same pattern?

A workstation control can disappear after a tool, version, machine, or environment change. A required check blocks merge for every contributor.

Hooks still have value. They provide fast feedback before the engineer pushes a change. Their speed improves flow, while CI supplies the shared enforcement floor.

Use both when the control benefits from early feedback and universal enforcement. Keep the server-side check authoritative when results disagree.

<img src="media/image13.png" style="width:6.26806in;height:2.38542in" />

**Reading CI output**

You can read a CI result without fixing its code. First identify the category and consequence.

<img src="media/image14.png" style="width:6.00725in;height:1.96538in" />

Both security findings and formatting findings can block merge. Only one may require incident-level investigation. Read the signal before asking for a delivery date.

The check name starts the diagnosis. Open its detail, locate the failed step, and identify the affected surface. Ask Engineering or Security when the consequence remains unclear.

A green CI run has a narrow meaning. The configured checks passed for that commit. It cannot prove that those checks cover every requirement or hidden risk.

**What an AI-assisted PR should carry**

AI context and decisions stay outside commit history unless the engineer records them. The PR must carry enough evidence for the change's risk.

At minimum, ask:

- Which context and rule files did the AI use?

- Which requirement did it implement?

- Did tests come from the implementation session or a separate one?

- Where did the engineer override the AI?

- Which gaps remain incomplete, uncertain, or unverified?

The **PR provenance block** (course Glossary — Learn portal or curriculum repo: ./modules/000-glossary.md#pr-provenance-block) records this trail.

Evidence should grow with blast radius. This is *provenance proportional to risk*.

Blast radius means the damage a faulty change could cause. Authentication can expose accounts. Billing can charge incorrectly. Data migrations can alter many records at once.

Higher blast radius needs stronger reconstruction. Reviewers should see the original intent, AI context, independent checks, human decisions, and unresolved risk.

<img src="media/image15.png" style="width:5.91697in;height:1.75704in" />

A team once ships an async feature with passing tests. The PR only says, "AI assisted with implementation."

Two months later, Security finds unsafe input validation. The team needs to know whether AI introduced the pattern. Missing provenance stretches the investigation to one week.

A two-paragraph PR note would have answered the question in five minutes.

**Your part in the change**

A non-engineering role shapes quality before, during, and after implementation. You can act at three points without reading code.

**Before build:** hand Engineering written intent, acceptance criteria, relevant context, and the approval owner.

**During review:** trace the PR to the requirement. Check context, test independence, human overrides, and open uncertainty.

**At escalation:** involve Engineering when context is missing or tests share the implementation session. Escalate high-risk authentication, billing, and data changes when evidence is thin.

Your role still owns its part of the evidence. Product owns the requirement. Design owns experience constraints. Architecture owns recorded boundaries. Security owns its risk decision.

Engineering should link those inputs rather than silently reinterpret them. A missing upstream decision should return to its owner.

# Block 4 — Simple Modernisation with AI

AI can modernise code quickly. The review must prove that required behaviour survived the rewrite.

**Why independent tests matter**

A test should begin from the requirement, independently from the implementation it checks.

When one session writes both code and tests, both share its assumptions. The tests may confirm the code's behaviour instead of the intended behaviour.

Imagine one person writing a crossword and then solving it immediately. They already know every answer. The puzzle cannot test their reasoning.

Independent verification breaks that loop. A separate session receives the requirement and public interface, while the implementation stays outside its context.

Separate sessions create structural independence. Correctness still needs review. The test session can misunderstand the requirement. The engineer must compare coverage with acceptance criteria and known edge cases.

The key advantage is different information. The test writer sees intent and public behaviour. Internal implementation choices stay outside its assumed truth.

<img src="media/image16.png" style="width:6.26806in;height:2.48333in" />

Consider a payment-validation function. AI writes the function and tests together. The function accepts negative amounts.

The tests only check that a positive amount creates a payment. Everything passes. Two weeks later, a refund sends −\$100 through the faulty path.

A fresh-session test begins from the requirement. It asks what should happen when an amount is negative. That test catches the bug on day one.

The contrast is sharp. Same-session tests ask whether the implementation behaves consistently with itself. Independent tests ask whether it satisfies an external contract.

You can apply this boundary without reading the tests:

**Independent tests come from the requirement in a fresh context, not from the session that wrote the implementation.**

**Four review lenses**

Independent tests cover one part of review. Four lenses help any role challenge the wider evidence.

<img src="media/image17.png" style="width:5.81974in;height:2.4029in" />

The last lens has a mechanical check: trace each claim to a specific artefact. An untraceable summary is decorative.

The lenses expose different failure classes. Behaviour review protects existing users. Assumption review finds invented rules. Drift review protects scope and architecture. Evidence review checks the claims themselves.

One pass cannot replace the others. A change may preserve behaviour while violating an ADR. It may follow the spec while relying on an unsafe silent default.

**Which lens your role uses first**

Every role can use all four lenses. Your responsibilities usually determine the first question.

<img src="media/image18.png" style="width:5.96558in;height:3.13211in" />

Evidence may appear in a PR, ticket, release note, QA handoff, architecture review, chat summary, or status report. The same question applies:

What was checked, by whom, and against what?

Use the answer to choose the next action. Strong evidence can move the handoff forward. Thin evidence should trigger a focused request instead of a general demand for more documentation.

# Block 5 — Working Without an IDE: Coding Agents

AI assistants now work beyond IDE plugins. *AI coding assistant* is the broad tool category. A *coding agent* can act through several steps toward an outcome.

Agents can read repositories, edit code, run checks, and open pull requests.

Their operating mode and access determine the review burden.

**Supervised and async work**

Two modes require different evidence:

<img src="media/image19.png" style="width:5.75724in;height:1.17367in" />

In supervised work, the engineer redirects the agent while it acts. Errors can surface early.

In async work, the engineer receives a completed PR, draft, or file. Review begins cold. The output must therefore carry more evidence.

Tool names reveal little about this distinction. The same product may support an interactive terminal session and a background task. Review the operating mode, permissions, and evidence rather than the brand.

Ask first:

Was a human watching the work happen?

The less the engineer watched, the more the PR must carry. Expect context, requirement, checks, agent decisions, and unreviewed areas.

Async work can increase throughput. It also moves judgement from the moment of action to the review of a finished result. That delay makes omissions harder to notice.

For high-blast-radius work, teams may keep execution supervised or add an explicit human gate. The mode should follow risk, reversibility, and observability.

A team uses an async agent to refactor a data-access layer. Tests pass, and the PR says, "refactored per spec."

Three weeks later, a migration exposes a removed retry mechanism. That mechanism handled transient connection failures. The requirement omitted this existing behaviour, so the generated tests missed it.

Supervision could have caught the deletion as it happened. An adversarial review could also ask which existing behaviour changed beyond the requirement.

**Agent Skills package repeatable work**

An **Agent Skill** packages a reusable procedure. The team defines the steps once and invokes them by name.

Different tools call this a skill, slash command, custom command, or workflow. The portable concept is a precise procedure with a repeatable output.

This is a practical capability threshold for non-engineers. If you keep asking for the same review, report, or data check, package the procedure once. A few careful minutes can replace repeated prompting across future tasks.

Skills suit work with a stable sequence and a checkable result. Examples include a review checklist, a data-quality report, or a standard repository investigation.

The value comes from consistency rather than novelty. Each invocation starts from the same steps, threshold, and output shape. That makes the result easier to compare and review.

The human still owns the procedure's boundaries. A packaged mistake repeats more consistently, so the team should version and review important skills.

"Analyse this data for problems" is a broad prompt. It leaves the meaning of "problem" open.

A stronger skill says:

Check every numeric column against expected bounds. List each outlier with its row identifier. Flag any column where more than 5% of values are outliers.

The second instruction defines scope, output, and a threshold. That shape makes repeated use more consistent.

The threshold also creates a reviewable decision. Another person can challenge 5%, change it, or test whether the skill applied it correctly.

**MCP connects agents to live systems**

A Skill tells an agent *what procedure to follow*. MCP gives the tool live capabilities and data it may use.

An approved **MCP server** (course Glossary — Learn portal or curriculum repo: ./modules/000-glossary.md#mcp-server) can expose a codebase, development database, or ticket tracker.

For example, an agent may read a Jira ticket and the relevant code. It can then propose a grounded fix without manual copy-and-paste.

Live access improves freshness. Authority still depends on governance. A ticket may conflict with an accepted ADR. Code may lag behind an approved migration plan.

The agent should report those conflicts. The responsible human decides which source governs the task.

MCP access needs the Block 1 boundaries. Use approved connections, least privilege, and read-only access for investigation.

A boundary contract should define who may call the connection, which data it exposes, and which actions it permits. The MCP server transports the capability; governance controls its use.

<img src="media/image20.png" style="width:6.26806in;height:3.21111in" />

# Block 6 — Talk to Your Code

**Short on time?** Spend 15 minutes here. Read the safety frame and prompt shape. Then choose one role example.

This block gives every non-specialist a practical capability. An approved AI tool can act like a fast project colleague who cites the evidence behind each answer.

You can inspect product rules, setup steps, technology choices, dependencies, and architecture without waiting for a general code walkthrough. You still validate the answer before acting on it.

Read-only access limits action. Current repository or MCP sources reduce stale-copy risk. The prompt shape makes the answer auditable.

**Safety frame**

Two boundaries matter most when the tool reads real project material.

- **Approved tools and read-only first.** Escalate permissions only for an authorised task.

- **Treat answers as fast investigation.** Validate source-backed findings before making high-impact decisions.

⚠️**Never paste sensitive material into an unapproved tool.** This includes secrets, credentials, API keys, production data, client-confidential code, and personally identifiable information (PII).

Input safety depends on approved handling, regardless of answer quality. Data may be retained or logged beyond your control.

Even approved tools can miss files, merge similar components, or overlook configuration outside the repository. Ask for sources, confidence, conflicts, and gaps.

An answer may arrive in under a minute and still be wrong. Speed reduces investigation time; sources establish whether the answer deserves trust.

The repository may describe only part of the running system. Deployment configuration, managed services, feature flags, and live data can sit elsewhere. A useful answer names those blind spots.

"I could not find this in the files I read" is a useful result. It exposes the boundary of the investigation.

**The minimum prompt shape**

A grounded repository question has four parts. Each part makes the answer easier to check.

1.  **Scope the source.** Name the files or folders to inspect.

2.  **Ask one specific question.** State the fact or relationship you need.

3.  **Request sources.** Ask for file:line references for every claim.

4.  **Request honest gaps.** Ask what remains unverified or conflicting.

<img src="media/image21.png" style="width:6.26806in;height:1.37847in" />

Done this way, the answer separates evidence from inference.

Keep the first attempt narrow. One entity, rule, service, or setup path is enough. A broad question encourages a broad summary that is difficult to verify.

Use this copy-ready template:

Read only these sources: \[files or folders\].

Answer this question: \[one specific question\].

For every claim, cite the supporting file:line. Separate direct evidence from inference.

Return the result as \[table, checklist, runbook, or short explanation\].

Add a final section named **Gaps and conflicts**. List missing evidence, conflicting sources, assumptions, and anything you could not verify.

**Cross-role examples**

The examples below share one structure. Each scopes sources, asks for evidence, and invites uncertainty.

**Order states and transitions** — PROD/BA, Design, QA

Read the repository rule file, relevant files under docs/context/, and every definition or handler for the Order entity.

List every status an Order can have. Then list every valid transition between statuses, including the condition or event that triggers it.

Return two tables: **Statuses** and **Transitions**. Cite file:line evidence for every row. Mark confidence per item. Add **Gaps and conflicts** for incomplete, duplicated, or contradictory rules.

A useful answer contains a sourced status table and transition list. Missing references mean the answer still needs validation.

Check whether transitions live in one state machine or across several handlers. Conflicting paths may expose a real product or maintenance problem.

**Run the repository locally** — any new joiner, Design, BA

Read README.md, CONTRIBUTING.md, package.json, Makefile, docker-compose.yml, and environment templates where present.

Give me a step-by-step local setup runbook with exact commands in execution order. Include prerequisites, required environment variables, required services, database setup, and the command that starts the application.

For each service, explain how it starts and how I can confirm it is ready. Flag likely failure points and their visible symptoms. Cite each instruction to file:line evidence. End with **Unverified steps**.

The answer is a draft runbook. Running the commands remains the verification step. It may also expose a stale README.

Record where the run fails. The failure can reveal a missing service, undocumented environment variable, or version mismatch.

**Identify the frontend stack** — Design, PM

Read package.json, the frontend README, docs/context/stack.md, and relevant build configuration.

Identify the frontend framework and version, language, build tool, styling system, state-management approach, routing approach, test framework, and UI component library.

List major dependencies under active migration or replacement. Return a table with **Area**, **Technology**, **Version**, **Evidence**, and **Confidence**. Cite the relevant file:line for every row. Flag conflicting or missing version evidence.

**Identify external services** — Infrastructure, Security, PM

Read compose files, environment templates, dependency manifests, and top-level configuration. Search for every external service the application expects.

List databases, caches, queues, search indexes, object stores, identity providers, and third-party APIs. Include the declared version where available.

Return a table with **Service**, **Purpose**, **Required or optional**, **Where configured**, **Local startup path**, and **Evidence**. Cite file:line for each dependency. Flag services referenced in code but missing from local setup, plus any files that disagree.

Conflicting configuration is itself a finding. It can explain failed onboarding and deployment.

Ask which source is authoritative before turning the list into an infrastructure plan. A declared service may be optional, retired, or environment-specific.

**Describe the high-level architecture** — Architecture, Security, PM

Read the architecture document, ADR archive, top-level README, service manifests, and repository layout.

Describe the system's main components, each component's responsibility, communication paths, data stores, and external boundaries. Distinguish direct evidence from inferred structure.

Return a component table and a short request or event flow. List accepted, open, and superseded architectural decisions with source references. Cite file:line for every claim. End with **Unverified areas and conflicting evidence**.

**Locate a business rule** — PROD/BA

Find every implementation, validation, configuration entry, test, and documentation reference for this rule: \[describe the rule\].

Explain where the rule begins, which components apply it, and how the pieces compose at runtime. Distinguish the stated business intent from the current implementation.

Return a table with **Location**, **Role in the rule**, **Observed behaviour**, and **Evidence**. Cite file:line for every row. Flag duplicate implementations, missing tests, and any code that conflicts with the rule as described. Leave the final product decision to the responsible human.

Two contradictory implementations are useful evidence. Bring that finding back to Engineering for resolution.

Avoid asking the tool to choose which rule is correct. Product or Engineering owns that decision, depending on whether intent or implementation is unclear.

**Read answers critically**

A useful repository answer has three signals:

- **Sources** — file or file:line references support each claim.

- **Honest gaps** — the answer names what its sources could not establish.

- **Conflicts stay visible** — the tool reports disagreement instead of smoothing it over.

A fluent answer without these signals is a hypothesis. Validate it before acting.

Validation can stay lightweight. Open the cited lines, compare conflicting files, or ask the owning engineer one focused question. The tool reduces investigation time while accountable judgement stays human.

# Anti-Patterns

These patterns break the evidence chain at different points. The cost column shows why each deserves review attention.

<img src="media/image22.png" style="width:5.96558in;height:6.10448in" />

**Outcomes**

By the end of Wide Theory, you can:

- explain the purpose and staleness risk of hot, warm, and cold context;

- recognise a current rule file and ask who maintains it;

- explain why written intent should precede implementation;

- choose a model tier based on task risk, cost, and complexity;

- distinguish an Agent Skill's procedure from MCP-provided capabilities and data;

- distinguish local hooks from server-side CI required checks;

- apply behaviour, assumptions, drift, and evidence review lenses;

- explain why independent tests begin from the requirement in a fresh session;

- calibrate review depth for supervised and async agent work;

- match PR provenance depth to the change's blast radius;

- ask safe, source-backed repository questions with approved read-only tools;

- recognise useful answers through sources, honest gaps, and visible conflicts;

- enforce the hard boundary against sensitive data in unapproved tools.

<img src="media/image23.png" style="width:6.26806in;height:3.03542in" />

# Assessment Questions \[Optional\]

**Awaiting Action**

5 minutes

What should be done

\*

**Knowledge Check (3 retrieval-practice questions)**

1.  **(Wide Theory)** Name the three context layers and the primary staleness risk for each. Then describe two of the four cross-role review lenses from Block 4 (behaviour preservation, hidden assumptions, spec/ADR drift, confirmation without evidence) and explain what class of AI-generated code failure each one is designed to catch.

2.  **(Deep Theory)** Explain the difference between a spec-driven greenfield flow and a brownfield delta flow. Name the one section of a brownfield delta that automated generators consistently miss, and give one concrete example of an entry that belongs there. Then explain why a hook is not a substitute for a CI required check.

3.  **(Katas / Final Kata)** Walk the five-phase arc of the Deep kata series (infrastructure → specification → implementation → verification → delivery). For each phase, name the artefact it produces. Then name two decisions that the engineer must make personally in any agent-assisted delivery, regardless of what the agent proposes — and explain why those decisions cannot be delegated.

**Self-Reflection (2–3 comparison prompts against the L3 standard)**

1.  Open your team's current rule file (CLAUDE.md, AGENTS.md, .cursorrules, or equivalent). Pick one factual claim about the stack or conventions. Verify it against the actual codebase now — does the code match what the rule file says? If not, you have found context drift. What would the discipline look like to keep that claim current: periodic review, or coupling the update to the engineering events that change repo reality?

2.  On your last AI-assisted change, where were the tests written — in the same session that produced the implementation, or in a separate session with access only to the spec and the public interface? If the same session: what class of assumptions do those tests share with the implementation, and what would an independent test catch that the current test cannot?

3.  **(Specialist)** Honest check on your last agent-assisted PR: could a colleague on the opposite shift triage a production incident caused by that PR — or reconstruct the key implementation decisions — from the PR body alone, without pinging you? If not, what is the lightest-weight addition that would make the next PR self-documenting? Name the specific field of the provenance block that is missing.

﻿

**Type your answers into the "Answer" block:**

**Answer**

\*

# Required Materials

**Templates the module uses (copy-paste skeletons, all defined inline in the katas):**

- **Layered context bundle** — hot rule file (CLAUDE.md / AGENTS.md, ≤ 80 lines), warm docs/context/stack.md, cold context/cold/gap-log.md. (K 5.W.1, K 5.D.1.)

- **Feature spec** — Goal · Inputs · Outputs · Normalisation · Grouping · Aggregation · Edge cases · CLI · Out of scope, plus an NFR budget in numbers. (K 5.W.2, K 5.D.4.)

- **Brownfield delta** — preserved-behaviour sentence · ADDED · MODIFIED · REMOVED · REMOVED audit · risk note. (K 5.D.5.)

- **Plan + tasks** — one component per section with named seams; 4–8 tasks, each Input · Output · Done. (K 5.D.6.)

- **Session log** — task spec · context loaded · ordered action log · rejected alternatives · verification gates · outcome. (K 5.D.7.)

- **Seven-lens review + adversarial pass** — one section per lens with file:line findings and severities, adversarial section appended, verdict on top. (K 5.D.9, K 5.D.10.)

- **PR provenance block** — tool/model · context loaded · verification gates · human decisions · known limitations · session duration · SDD approach, plus linked evidence. (K 5.D.11.)

- **Replay packet** — sensitivity header · task/prompt · context snapshot · model metadata · ordered action log · output · triage note. (K 5.D.13.)

- **Role-agent definition** — Claude Skill or Claude Code sub-agent carrying the seven required fields with guardrails inline. (K 5.3.)

**Tools for AI-native engineering work** — pick one per row. EPAM teams confirm allow-list status against the internal data-class matrix before pasting non-public material; external learners pick whichever vendor in each row they can access. EPAM tools marked \*.

<img src="media/image24.png" style="width:5.98642in;height:5.11137in" />

# Internal Knowledge (EPAM-specific)

- **CodeMie Claude** (codemie-claude) — the EPAM-provisioned build of Claude Code; request access via support.epam.com. Reads the same rule files and slash commands as the public claude CLI.

- EPAM AI-tool allow-list (data-class matrix) — *"what can I paste where"* before any non-public material enters a tool.

- The Engineering Development Registry taxonomy — the ten Deep Theory sub-sections map to it (5.1–5.10).

- The Architecture Context Pack from the Architecture module — optional upstream input for the context bundle (K 5.D.1) and the spec NFR budget (K 5.D.4).

# External References (Optional) — self-study shelf

Pick depth, not breadth. Read at least one per cluster relevant to your work.

**Context, rule files, and Skills**

- [AGENTS.md specification](https://agents.md/) — tool-agnostic rule-file format.

- [Anthropic — Equipping agents with Skills](https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills).

- [Anthropic — Effective context engineering for AI agents](https://www.anthropic.com/research/effective-context-engineering-for-ai-agents).

- [Claude Code — memory and CLAUDE.md](https://code.claude.com/docs/en/memory).

**Spec-driven development**

- [GitHub Spec-Kit](https://github.com/github/spec-kit).

- [OpenSpec](https://github.com/Fission-AI/OpenSpec) — openspec CLI with /opsx: brownfield delta commands.

**Review, verification, and independence**

- [Anthropic — Towards understanding sycophancy](https://www.anthropic.com/research/towards-understanding-sycophancy-in-language-models) — why independent verification matters.

- [Anthropic — Building effective agents](https://www.anthropic.com/research/building-effective-agents) — supervised vs async framing.

**CI and observability**

- [GitHub Actions — required status checks](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/defining-the-mergeability-of-pull-requests/about-protected-branches).

- [Langfuse](https://langfuse.com/), [Braintrust](https://braintrust.dev/), [Arize Phoenix](https://phoenix.arize.com/), [LangSmith](https://www.langchain.com/langsmith-platform) — trace replay.

**Agent / Skill build**

- [Anthropic — Agent Skills](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview).

- [Claude Code — Subagents](https://code.claude.com/docs/en/sub-agents).

# Reference Cases and task menu

Practice runs against real project material. **First choice is always your own current project / repo.** This module is learner-project-based: the Wide series builds a self-contained **log-summariser CLI sandbox** (synthetic logs only, AI-generated on your laptop); the Deep series runs on **one real repo from your own work** — or on the sandbox the Wide series produced if you have nothing else. If you would rather work a fixed external brief, Case A (Meridian Retail Group) or Case B (Kepler Insurance) from [reference-cases.md](https://eu.git.epam.com/airun-mission-26-ai-factory/curriculum/-/blob/main/modules/001-reference-cases.md) both work — pick one and stay on it across every kata. (Case C is the Data module only.)

When a kata says *"use a real, recurring task,"* pick from this menu — tasks the Engineering role would actually own:

- **Bootstrap the context bundle** for a repo: generate the hot rule file, verify one warm claim against the code, record three honest cold gaps. (K 5.D.1.)

- **Convert a re-used prompt into a portable Skill** plus its repo-rule fragment, load-tested for zero repo-fact leakage. (K 5.D.2.)

- **Ship one server-side CI required check** (test-file deletion guard, provenance-field check, secret scan, migration-changelog check, or lint/typecheck), verified against a failing and a passing diff. (K 5.D.3.)

- **Spec a feature and drive the implementation from it**, then stress-test the spec with a fresh-session audit. (K 5.W.2, K 5.D.4.)

- **Produce a brownfield delta** with honest ADDED / MODIFIED / REMOVED accounting and a risk note on the highest-risk preserved behaviour. (K 5.D.5.)

- **Generate independent tests from the spec alone** in an isolated session, then run a seven-lens review and an adversarial pre-mortem on the diff. (K 5.D.8, K 5.D.9, K 5.D.10.)

- **Assemble a PR provenance block** that links the spec, session log, tests, and review so a stranger can merge with confidence. (K 5.D.11.)

#### Wide kata series (all learners)

**Not Started**

3 minutes

***Goal:*** Ship a tiny log-summariser command-line interface through the AI-assisted engineering loop: context setup, spec, implementation, independent tests, CI, refactor review, async agent task, code Q&A, and by-agent replay comparison.

***Persona:*** non-role-learner. Someone who has shipped software and used an AI tool, but has not yet watched an AI coding agent work through a repo with evidence.

***Superpower moment:*** You shipped a small program end-to-end without writing code by hand - first as a supervised loop, then as an agent replay - and you hold by-hand-vs-agent.md, a concrete comparison that says where the agent saved time, where it missed context, and which evidence a reviewer should ask for.

***Reference case:*** learner-project. The default is a private sandbox repo, logsum-sandbox — a tiny command-line interface (CLI) that reads synthetic events.csv logs (timestamp, level, service, message) and writes a counted summary. You can tie it back to whatever subject you carried through the upstream modules — your own project, Meridian (Case A), or Kepler (Case B): name the service column after that system's services (Meridian's checkout-service / cart-api, Kepler's Claims API, or your own) so the tool reads as part of the platform you specced, designed, and architected. The CLI is identical either way; the connection is an optional overlay. Use a real backlog item instead only if it fits a 15-minute kata and holds no production or customer data. Stay on one repo across all nine katas.

***Artefact folder (curriculum repo):*** ./modules/500-eng/artefacts/500-wide/ — you can find output examples there. Each kata after the first declares consumes_from: and has a fallback under \_fallbacks/.

***How to read every kata in this block.*** Each title starts with a verb — read it as a command. The output mechanic varies across the nine (a rule/config file, Markdown notes, Python code, a CI workflow, a comparison table) so you practise a range of formats, not only prose. One kata (K 5.W.4) requires a **fresh AI session** to write the tests — do not test code in the same session that produced it. Each kata is hard-capped at ~15 minutes.

*Default tool.* Use CodeMie Claude on EPAM engagements, or Claude Code / Cursor / GitHub Copilot / Codex with equivalent repo-read and file-write capability. The raw terminal commands are shown so you can read what the agent is doing; you may ask the agent to run them and show output before you approve.

*Safety boundary.* Use synthetic logs only. Do not paste production logs, names, emails, tokens, or customer records into the sandbox or an AI session.

**Katas are offered for inspiration, not direct reuse in production setup.** If not adjusted and grounded in your context, they may produce unpredictable and unverified results.
