**Introduction**

**Not Started**

10 minutes

**Focus:** Equip every team to take an ambiguous problem to a defensible architecture — generate real options, choose one with evidence, draw the C4 pack, record the decisions, set measurable budgets, and stress-test the result — driving AI through the workflow and catching what it consistently gets wrong. For architects, it moves the craft from L2 (AI as a diagram generator) to L3 (AI-native architecture: agent-readable decisions, automation agents, and an AI-native architecture layer with fallbacks).

**Deep for:** Solution, Software, Technical, and Enterprise architects on AI-native delivery teams.

**Total time per learner:**

- Wide path: 50 min Theory + ~120 min kata series (8 × 15) + 60 min Final Kata ≈ 3.8h

- Deep path (own role): + 180 min Theory + ~150 min kata series (5 × 30) ≈ +5.5h (Final Kata is universal — done once)

The architect produces the materials the rest of the team — and its AI tools — consume every day: context, options, diagrams, decisions, contracts, and budgets. The L3 distinction for this role is twofold: **decisions become agent-readable constraints** (an ADR whose Agent-Readable Summary stops a coding agent from quietly reversing it), and **the architect ships automation** — impact-analysis, governance-conformance, handoff, and documentation agents that run the role's recurring work, plus an AI-native architecture layer designed with fallbacks. This module trains you to produce both — and to consume them well when an architect hands them to you.

**Objectives**

- **Learn to do:** take an ambiguous problem to a chosen architecture — generate options, choose one with evidence, draw the C4 pack, record decisions, set NFR budgets, and run a fresh-session pre-mortem (Wide); build the architecture-automation agents and design the AI-native architecture layer with fallbacks (Deep).

- **Skills (role):** framing inputs and generating conceptual options; trade-off-based decisions recorded as ADRs; structuring the solution (C4, integration contracts, pattern placement); NFR budgeting and adversarial review.

- **Skills (tooling):** Mermaid C4 + sequence diagrams, four-layer context doc, comparison matrix, ADR template, NFR budget table, fresh-session pre-mortem, agent-contract authoring (Deep).

- **Outcome:** a Meridian Architecture Pack (context, options, C4, integration contract, ADRs, patterns, NFR budgets, pre-mortem); the Deep path adds four architecture-automation agents and an AI-native architecture pack with fallbacks.

- **Tested by:** the Wide kata chain (K 4.W.1 → K 4.W.8) + the Final Kata (K 4.3); the Deep path adds the specialist kata series (K 4.D.1 → K 4.D.5).

**Role Context**

**1 — Role names and who they apply to**

This module covers anyone who owns the shape of the solution — how the system is structured, how its parts integrate, and which decisions are load-bearing. Common job titles:

- **Solution Architect** — end-to-end solution shape across systems and integrations.

- **Software Architect** — structure and patterns inside the application boundary.

- **Technical Architect** — technology selection, NFRs, and delivery-time technical guidance.

- **Enterprise Architect** — standards, governance, and cross-program coherence.

- Common synonyms across firms: Application Architect · Cloud Architect · Principal Engineer (architecture-leaning) · Tech Lead (on smaller teams).

If your title varies, the test is functional: do you decide how a system is structured — its boundaries, integrations, and the decisions that are expensive to reverse? If yes, the **Deep** track covers you. Everyone else takes the **Wide** track: you collaborate with an architect (or stand in for one) on AI-native work.

**2 — Role description and core duties**

The architect owns the space between *"here's what to build"* and *"here's how it's structured and why."* In observable verbs:

- **Mines** context — turns a prose brief into structured, agent-readable constraints across the business, product, engineering, and regulatory layers.

- **Generates** options — produces genuinely different ways to solve a problem before committing to one.

- **Decides** with evidence — scores options against constraints and records the choice as ADRs that survive contact with a fresh AI session.

- **Structures** the solution — C4 diagrams, dependency graphs, integration contracts.

- **Budgets** the non-functionals — measurable latency, cost, quality, reliability, and security & compliance targets owned by named containers.

- **Stress-tests** the design — adversarial pre-mortems before production runs the experiment for you.

- **Researches** prior art — studies how other EPAM teams solved similar problems and brings those patterns into the current engagement, querying the internal MCP servers now open to every employee instead of starting each problem from scratch.

What this role does *not* own: final ownership of the production code, the sprint backlog, or production sign-off. Those belong downstream in Engineering. On many teams the architect is also the most senior engineer on the project and is hands-on in the code every day — the carve-out is about where final accountability sits, not about staying out of the codebase.

**3 — Main processes**

Architecture work recurs across an EPAM delivery project as five activities (detailed in the Wide and Deep Theory):

- **Discovery** — context review, existing-system assessment, constraint and dependency identification, risk analysis.

- **Solution structure** — diagrams, boundaries, dependency and flow modelling, integration contracts.

- **Decisions** — option generation, trade-off analysis, ADRs, pattern selection.

- **Non-functional requirements** — performance, reliability, security, and cost quality attributes as budgets.

- **Governance, handoff & AI architecture** — standards, conformance, impact analysis, documentation from models, the AI-native architecture layer (specialist depth), and — where the architect holds admin access — provisioning and monitoring the team's AI tooling and infrastructure (who gets which tools, which model access, and at what scope).

**4 — Role in SDLC**

Architecture sits **downstream of Design (Module 300) and PROD/BA (Module 200)** and **upstream of Engineering (Module 500)**. It receives the redesigned journey, the agent-ready handoff, and the requirements; it produces the structure, decisions, and budgets the build runs against. The audience contract:

Your role

You send Architecture

You expect back

Design (M300)

Redesigned journey, CONTEXT.md, agent-ready handoff

A C4 pack + integration contracts that honour the experience

PROD/BA (M200)

Requirements, scope, success metrics

NFR budgets traceable to the requirements

Engineering (M500)

What's already built, the repo state

C4 + ADRs + NFR budgets + patterns an AI coding agent can build against

Quality (M600)

"Done" shape for the system

NFR budgets with test approaches that drive the test plan

The most common upstream failure: a solution arrives named in the brief, and Architecture skips the actual job — generating and choosing between options.

﻿

5 — How the role changed with AI (general)

AI collapsed the cost of producing architecture materials — a C4 diagram, a first-draft ADR, an NFR table, a pattern list are minutes of work now, not hours. It amplified the architect's reach: three options explored in the time one used to take, a fresh-session pre-mortem on demand. And it shifted the deliverable — a decision is no longer a PDF a human reads once, but an agent-readable constraint a coding agent reads on every invocation. The work that stays is the judgment: which problem, which option, which risk to accept.

﻿

6 — What changed at L2 (AI-assistant)

At L2 the architect still owns the architecture; AI is a copilot. Where AI assists: generating C4 and sequence diagrams from a description, drafting ADRs and NFR tables, listing candidate patterns, summarizing a brief into context. Stays human at L2: the option choice, the trust-boundary and PCI-scope decisions, the accept-vs-reject verdict on a trade-off, and saying no to a design that fails its budget. An architect who uses AI only to draw diagrams is operating at L2.

**7 — What changed at L3 (AI-native)**

At L3 the work restructures around agent-readable artefacts and automation. The role gains reach; it does not disappear. The concrete shifts:

- **Decisions as constraints.** ADRs carry an Agent-Readable Summary that stops a coding agent reversing the decision; governance becomes rule-file content, not a SharePoint PDF.

- **The architect ships agents.** Impact-analysis, governance-conformance, handoff, and documentation agents run the role's recurring work — the specialist authors the contracts, not the one-off reports.

- **The architect co-builds the AI Factory.** Beyond shipping their own role-agents, the architect helps the team stand up the project's AI Factory — the shared agentic delivery pipeline the whole team runs against — and owns the technical side of it: which platform capabilities to build, how the role-agents chain, and who provisions and monitors access to them. Seniority and a broad view of the client's architecture and ways of working are usually what put the architect in the best position to see how to stand it up.

- **An AI-native architecture layer.** When AI ships inside the product, the architect designs the component map, request flow, fallback/degradation, cost and rate-limit architecture, observability, and security — failure-mode design is first-class.

- **New artefacts the role produces:** the agent-readable Architecture Pack, the four architecture-automation agents, and a native-format Architecture role-agent.

The Wide path teaches you to *recognize and consume* these artefacts. The Deep path teaches you to *produce* them.

# Carry-Forward

Three artefacts leave this module: the Wide-series Architecture Pack, the Deep-series automation agents + AI-native architecture pack, and the Final-Kata role-agent.

**1 — Meridian Architecture Pack (Wide)**

- **Artefact name:** Architecture Pack.

- **Source:** Wide katas K 4.W.1 → K 4.W.8 — context, options, C4 + integration contract, ADRs, patterns, NFR budgets, pre-mortem.

- **Consuming stage(s):**

  - **Module 500 (Engineering)** — consumes the C4 + ADRs + patterns as the build contract, and the ADR Agent-Readable Summaries as coding-agent constraints.

  - **Module 600 (QA)** — consumes the NFR budgets (each with a test approach) to drive the test plan.

  - **Module 800 (Infrastructure & Operations)** — consumes the C4 containers, NFR budgets (availability, reliability, cost), and resilience patterns (Bulkhead, Circuit Breaker) to shape deployment topology, the AI gateway, and operational SLOs.

  - **Module 1111 (Final Assembly)** — the pack is part of the portfolio.

- **Format:** Markdown + Mermaid — meridian-arch-pack/ with 00-discovery-context.md, 00-options.md, 01-context.mmd, 02-containers.mmd, 03-flow-instore-cart.mmd, 03-deps.mmd, 03-integrations.md, 04-adr-001..003.md, 05-patterns.md, 06-nfrs.md, 07-adversarial.md.

**2 — Architecture Automation Agents + AI-Native Pack (Deep)**

- **Artefact name:** Architecture Agents, plus the Phase 3 AI-native architecture pack.

- **Source:** Deep katas K 4.D.1–4 (the four agents) and K 4.D.5 (the AI-system architecture).

- **Consuming stage(s):**

  - **Module 500 (Engineering)** — the governance-conformance and impact-analysis agents run against PRs; the AI-native pack grounds AI-feature implementation.

  - **Module 900 (Security)** — prospective consumer of the trust-boundary and security sections of the AI-native pack *(edge to wire when Security adopts 400 in its consumes_from)*.

  - **Module 1000 (Management)** — the impact-analysis agent feeds change-control reporting.

  - **Module 1111** — the agents join the agent roster.

- **Format:** Markdown agent contracts — meridian-arch-agents/arch-impact/, governance-check/, handoff-gen/, docs-gen/, and phase3-ai-arch/.

**3 — Architecture Role-Agent (Final Kata)**

- **Artefact name:** Architecture Role-Agent.

- **Source:** Final Kata K 4.3 (all learners; specialists add the depth-add sections).

- **Consuming stage(s):** **Modules 500–600** load .claude/skills/architecture/ or .claude/agents/architecture.md when no architect is on the team — read in place, not transformed. **Module 1111** lists it in the agent roster a joining teammate reads.

- **Format:** a runnable Claude Skill or sub-agent, ≤ 2 pages of body, with the human-owned architecture decisions inline as guardrails.

- **Engine guide target:** .ai-run/guides/architecture/architecture.md, under header \## NFR budgets, integration patterns, ADR shape (from Module 400 — Architecture). This is the authoritative chain mapping; the spec's chain:rules delimiter attributes mirror it; on disagreement this line wins.

- **Optional stand-in override (Deep only):** tech-lead-reviewer — Module 1111 decision-router gates spec.approved, plan.approved; escalation triggers map to its verdict.

# Wide Theory

**Why This Matters for You**

An architect's job is to turn what the team knows — constraints, system shape, decisions, quality targets — into **materials** the rest of the team can use: diagrams, decision records, requirements, context documents, integration contracts. In AI-native delivery those same materials become the input your AI tools read. Stuck in a slide deck, a wiki behind a login, or someone's head, they are invisible to a tool — and the tool produces garbage.

Here's the twist: architecture is what AI agents are *worst* at — it needs long-range coherence and reasoning about constraints nobody wrote down. Yet architecture artefacts are the most undersupplied, so that gap is where structuring context pays off most. The architect's defining move at L3 is to mine and structure that context so every *other* role's AI tools get more accurate.

This module walks the four materials in the order an architect hits them on any engagement: discovering what exists (4.1), structuring the solution (4.2), recording decisions (4.3), and setting measurable non-functional budgets (4.4). For each you get what it is, how teams build it traditionally, and how it changes once AI consumes it.

You do not need to become an architect. You need to recognise these materials, know what "good" looks like, and understand why your AI tools depend on them.

**Goal**

ERecognise the four architectural materials that feed AI-native delivery — discovery, solution structure (diagrams + boundaries), decision records, and NFR budgets — tell the traditional approach apart from the AI-native one for each, spot when a material is missing or broken, and tell an architect what you need and why.

**Time**

~45 min.

**Audience**

All learners — every role that consumes an architect's materials: consultants, PMs/BAs, designers, engineers, QA, data, infrastructure, security, delivery, and management. Architects can read this as a refresher; the specialist depth is in §1.2.

**Prerequisites**

Onboarding, Fundamentals, Consulting & SME, PM/BA, and Design completed. Helpful inputs to have on hand: the Meridian brief (Case A) and the redesigned journey plus agent-ready handoff carried forward from Design. Every term used here is defined on first use; no prior architecture background is assumed.

**Must Cover**

**Architecture produces the materials your AI tools consume — context, diagrams, decisions, budgets. If it's not in the repo in a structured format, it doesn't exist for an agent.**

Four foundational activities, in the order an architect hits them on any engagement:

- **Discovery (4.1)** — surfacing what the team "knows" but never wrote down into a four-layer context pack agents (and new joiners) can read.

- **Solution structure (4.2)** — diagrams-as-code (C4) and integration boundaries, with MCP as the contract that tells an agent its reach and Skills as the reusable procedures it loads.

- **Decisions / ADRs (4.3)** — recording what was decided and why as agent-readable constraints, not wiki pages nobody reopens.

- **NFR budgets (4.4)** — turning "should be fast" into numbers with an enforcement chain behind them.

**Key Messages / Ideas**

- **Discovery comes first, and "if it's not in the repo, it doesn't exist for agents."** Before any diagram or decision, the architect surfaces tribal knowledge into a structured context pack; the AI-native version of every material is version-controlled and lives in the repo where the downstream role-agent that needs it can read it.

- **Solution structure lives as diagrams-as-code, with boundaries as explicit contracts.** Mermaid/C4 in the repo (not PNGs in slides) lets agents parse and update it, and an MCP-style boundary contract tells an agent its reach so it can't go rogue through ignorance. A Skill packages the reusable *how-to* procedures alongside it — MCP for reach, a Skill for the procedure.

- **A decision record captures what, why, and what was rejected — with an Agent-Readable Summary.** The summary line is what turns a wiki page nobody reopens into a constraint an agent applies, so it stops re-proposing options the team already rejected.

- **An NFR is a number with an enforcement chain, not a wish.** "Should be fast" becomes "p95 \< 3 s," backed by a fitness function and a CI gate; cost and quality are the new budget families AI features add.

- **Pick the simplest shape that fits.** Most of a system is still plain code; an automation or a workflow usually beats an agent, and *multi*-agent is a smell to justify — and the shape you choose is itself an ADR.

**Structure (Per-topic context blocks)**

Each block elaborates one topic from the list above — the material, its traditional form, and how it shifts once AI consumes it.

<img src="media/image1.png" style="width:6.27987in;height:2.42104in" />

**Two jobs, one role.** Everything below is job one — the materials an architect produces on *any* project. A second job starts when the product itself ships AI features: designing the agent runtime, its boundaries, the knowledge layer it retrieves from, how its output is evaluated, and what it may cost. That is specialist architecture — Deep Theory (**400-ARCH:Deep:Theory**, curriculum repo: ./modules/400-arch/400-deep-theory.md) covers it; this Wide path stays on the materials every role needs to recognise.

## Block 1 — Discovery (4.1)

**What is this activity?** The architect's first job on any engagement: surface what the team "knows" but never wrote down, so AI agents (and new joiners) can consume it. Discovery produces a **context pack** (course Glossary — Learn portal or curriculum repo: ./modules/000-glossary.md#context-pack) — the structured set of constraints, dependencies, and assumptions every downstream tool needs before it can help.

**In this topic you will:**

- Name the two types of context (architecture vs engineering) and the four layers the context document is written in (business, product, engineering, regulatory).

- Explain why implicit constraints are the biggest risk to AI-assisted delivery.

- Recognise when a context pack is missing and know what to ask for.

- Identify which three stakeholder types to interview and what each provides.

- Identify which context layer your own role's AI tools depend on.

**The traditional way.** Tribal knowledge lives in people's heads. "We never deploy on Fridays." "The payment service has a 5-second timeout that can't be changed." "Team B owns that microservice and changes take 2 sprints." None of this is written anywhere an AI tool can find it.

**The AI-native way.** Implicit constraints are captured as structured text in the repository. An AI agent can read them before generating code, writing tests, or proposing designs.

**The AI-native way.** Implicit constraints are captured as structured text in the repository. An AI agent can read them before generating code, writing tests, or proposing designs.

| **Context type**         | **What it contains**                                                             | **Example**                                          |
|--------------------------|----------------------------------------------------------------------------------|------------------------------------------------------|
| **Architecture context** | Business constraints, team boundaries, deployment rules, regulatory requirements | "PCI data must not leave the payment trust boundary" |
| **Engineering context**  | Repository map, code patterns, dependency graphs, naming conventions, rule files | CLAUDE.md with "use PostgreSQL, never MongoDB"       |

**Two types, four layers.** The two context *types* above tell you *who consumes* the context — architects vs coding agents. When you sit down to write the document, you split it into four *layers* instead — the layers a brief speaks in. The architecture context becomes three: **business** (revenue, stakeholders, success measures), **product** (customer surfaces, channels, user moments), and **regulatory** (each named regulation and its architectural implication). The engineering context is the fourth, the **engineering** layer (repo map, stack, dependency graph). Those four — business / product / engineering / regulatory — are what you mine in K 4.W.1: the type split says who reads it, the layer split says how to structure it.

<img src="media/image2.png" style="width:6.60417in;height:2.17503in" />

**Who reads which layer.** Each layer feeds a *specific* downstream AI tool — the pack isn't read by "an agent" in the abstract, but by the agent standing in for a particular role:

| **Context layer**                            | **Feeds the AI tool used by**     | **So it can**                                                         |
|----------------------------------------------|-----------------------------------|-----------------------------------------------------------------------|
| Business + product                           | BA / PM, and QA                   | draft requirements, stories, and test plans that track the real goals |
| Engineering (repo map, patterns, rule files) | Engineers                         | build to the existing structure and conventions                       |
| Regulatory                                   | Security and compliance reviewers | check trust boundaries and where regulated data may flow              |

So the practical question for *you* is: **which layer does my role's AI tool depend on, and is it actually in the repo?** When a QA agent writes thin tests, the missing input is often the business and product context an architect never structured.

**Why you care.** Every time you ask an AI tool to generate code, propose a design, or draft a test, it makes implicit decisions from whatever context it can see. With no structured context pack, it:

- writes code using a library the team banned six months ago,

- proposes a deployment pattern that breaks a regulatory constraint nobody wrote down,

- builds a service that overlaps one Team B already owns.

**The quality test for any context artefact:** *"Could an AI agent ingest this artefact directly and produce measurably better output than without it?"* If the answer is no, the context is not structured enough.

**Who to interview.** Discovery runs in parallel with business and technical discovery tracks — not sequentially. Three stakeholder types feed the context pack:

| **Stakeholder**                                            | **What they provide**                                                                                                                                                               | **When to involve them**                                    |
|------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------|
| **Platform / enterprise architects**                       | Where this system sits in the organisation; general policies, security rules, data governance, decision-making process for changes                                                  | Start of discovery; revisit before finalising constraints   |
| **Domain / technical owners**                              | Deep knowledge of the specific platform or application; the people who can validate your understanding and challenge your improvement ideas before you take them to decision-makers | Core of discovery; best sounding-board for proposed changes |
| **Technical specialists** (analysts, engineers, modellers) | Specific topics — one service, one pipeline, one integration point                                                                                                                  | Ad-hoc, as questions arise                                  |

**Discovery outcomes.** A complete discovery produces:

1.  A **context pack** — current architecture in structured text (constraints, dependencies, boundaries, rule files).

2.  A **challenge list** — key bottlenecks, risks, and gaps identified against the business/technical objectives.

3.  An **architecture map** — diagram of current state, ideally as Mermaid in the repo (see Block 2).

Without the challenge list, the context pack is a description, not a diagnosis.

**Risk analysis starts at discovery.** The challenge list is where architecture risk analysis begins — not the pre-mortem (K 4.W.8), which stress-tests a design you've already drawn. A discovery-time risk is a structured entry: the risk, the architectural area it threatens, its likelihood, and its blast radius if it lands. For Meridian: *"SAP ECC serves inventory in batch, not real time (likelihood: high; blast radius: phantom-stock cancellations across click-and-collect)."* Surfaced before any diagram is drawn, these shape which options you generate; the pre-mortem later tests whether the option you chose survives them.

**Check your understanding**

1.  Name one implicit constraint on your current project that is not written anywhere a tool could read.

2.  Why does the architect mine context *before* drawing any diagrams?

3.  Which stakeholder type is the best person to validate a proposed improvement before it reaches decision-makers?

4.  A discovery pack has an architecture map and constraints but no challenge list. What is missing and why does it matter?

**Recap**

- Discovery produces three outputs: context pack (constraints + dependencies), challenge list (bottlenecks + risks vs objectives), architecture map (current state diagram).

- Discovery runs in parallel with business/technical tracks — not as a separate phase.

- Three stakeholder types: platform architects (policies, decisions), domain owners (deep knowledge, validation), technical specialists (ad-hoc topics).

- Architecture context = the business / product / regulatory layers; engineering context = the engineering layer (code/repo/dependency structure) — together the four-layer context document the katas build.

- If it's not in the repo in a structured format, it doesn't exist for AI agents.

- The quality test: would an AI agent produce measurably better output with this artefact?

- Each layer feeds a specific downstream role-agent — business + product → BA/QA, engineering → engineers, regulatory → security; ask which layer your own role's AI tool needs.

**Key terms:** Architecture Context Pack, engineering context, implicit constraint.

## Block 2 — Solution Structure (4.2)

**What is this material?** A visual and textual representation of how parts of a system relate — services, data flows, boundaries, dependencies, and integration points. Architects produce these so the team can reason about the system without reading all the code.

**In this topic you will:**

- Distinguish a diagram-in-a-slide from a diagram-as-code.

- Name why image-based diagrams are an unreliable source of truth for AI tools.

- Recognise Mermaid / D2 / PlantUML syntax at a glance.

- Distinguish "ask Team B" from a structured integration contract.

- Recognise MCP (Model Context Protocol) as the standard agents use to discover and use external tools and context — and where boundaries get expressed.

- Choose the simplest shape — standard service, automation, workflow, or agent — for an AI feature.

**Part A — System Diagrams**

**The traditional way.** Someone draws boxes and arrows in Visio, Lucidchart, or a PowerPoint slide; it lives in a shared drive or a wiki page. Within two weeks it is out of date, within two months nobody trusts it, and new team members who ask "is this still accurate?" get a shrug.

**The AI-native way.** The diagram is written as code — Mermaid, D2, or PlantUML — and lives in the repository next to the system it describes. An AI agent can:

- **Generate** an initial diagram by mining the codebase (reading imports, configs, deployment files).

- **Read** the diagram to understand system boundaries before generating code.

- **Update** the diagram when the system changes (a new service, a changed dependency).

<img src="media/image3.png" style="width:5.21875in;height:2.91667in" />

**Side-by-side:**

| **Aspect**       | **Traditional**                                                                     | **AI-native**                           |
|------------------|-------------------------------------------------------------------------------------|-----------------------------------------|
| Format           | PNG / PDF / Visio file                                                              | Mermaid / D2 / PlantUML (text)          |
| Lives in         | Wiki, slide deck, shared drive                                                      | Repository, next to the code            |
| Updated by       | A person who remembers                                                              | AI agent + human review                 |
| Consumable by AI | Unreliably — a vision model can read a screenshot but can't diff, edit, or trust it | Yes — agents parse, diff, and update it |
| Freshness        | Weeks to months stale                                                               | Refreshed on change                     |

**Why you care.** When you ask an AI tool "what services does this system have?" or "generate code for the payment flow," the tool needs to know the system shape. If the diagram is a PNG in last month's deck, the tool can't reliably read it. If it is Mermaid in the repo, the tool reads it directly.

**Worked example: Order Management System.** A neutral reference system — read it to see what a good C4 pair looks like. In the C4 katas you produce an equivalent pair on **Meridian** (Case A, the module's reference case): K 4.W.3 draws the L1 + L2, and K 4.W.4 adds the runtime sequence and dependency views.

C4 L1 — System Context (who uses the system and what external systems surround it):

<img src="media/image4.png" style="width:6.51042in;height:3.85677in" />

C4 L2 — Container View (what must be running for the system to work):

<img src="media/image5.png" style="width:6.0625in;height:2.34778in" />

Notice: the L1 answers "who interacts with the system and what external systems does it depend on?" The L2 zooms in to answer "what must be running, where does state live, and how do components communicate?" Each level adds one zoom level — never both at once. Notice too the **job queue** between the Order API and the Fulfilment Worker, rather than a direct call. The API drops a job on the queue and returns to the customer at once, so a slow fulfilment step — shipping, inventory reconciliation, email — never blocks the order response, and a burst of orders queues up instead of overwhelming the worker.

er response, and a burst of orders queues up instead of overwhelming the worker.

**Part B — Integration Boundaries**

**What is this material?** A specification of where one system (or agent) ends and another begins — what it can access, what it cannot, and how it connects. Architects define these so that AI agents know their reach.

**The traditional way.** Integration knowledge lives in tribal memory: "Team B owns that service, ask them"; "the payment API has a weird timeout, check with Sarah." A new developer who needs to integrate spends days in Slack channels tracking down endpoints, auth methods, and constraints — and AI tools have zero access to any of it.

**The AI-native way.** Boundaries are written as explicit contracts in the repository. An AI agent can discover what tools and data are available, what security posture applies, and what it must not touch.

The standard for this is **MCP (Model Context Protocol)** (course Glossary — Learn portal or curriculum repo: ./modules/000-glossary.md#mcp-model-context-protocol) — think of it as "USB-C for AI tools." It defines how AI agents discover and use external tools and context; the boundaries themselves (read-only vs write, scope, rate limits) are set by how each server is built, not by the protocol:

<img src="media/image6.png" style="width:3.55208in;height:2.95833in" />

**What a boundary contract specifies:**

| **Element**          | **Traditional (tribal)**   | **AI-native (contract)**                          |
|----------------------|----------------------------|---------------------------------------------------|
| What can be accessed | "Ask Sarah"                | Explicit tool list with parameters                |
| Security level       | "Be careful with that one" | Read-only / write / destructive — per tool        |
| Rate limits          | "Don't hammer it"          | 100 req/min, documented                           |
| What's off limits    | "Don't touch production"   | Scope boundary: "MUST NOT write to production DB" |
| Who owns it          | "Team B, I think"          | Named owner + escalation path                     |

**Why you care.** When an AI agent acts on your behalf — writing code, running tests, deploying — it needs to know what it can and cannot do. Without boundary contracts:

- An AI code-generation tool might try to call an API that requires special auth.

- An AI test tool might hit a production database instead of staging.

- An AI deployment tool might trigger a pipeline it shouldn't touch.

Boundaries prevent AI tools from "going rogue" — not through malice, but through ignorance.

**Part C — Reusable Procedures: Skills**

**What is this material?** A boundary contract tells an agent *what it can reach*. An **Agent Skill** (course Glossary — Learn portal or curriculum repo: ./modules/000-glossary.md#agent-skill) — a *Skill* for short — tells it *how to do a recurring task well*. Where an MCP server hands the agent a capability — read this database, trigger that pipeline — a Skill hands it a procedure: a reusable instruction pack the agent pulls in when a task matches it.

<img src="media/image7.png" style="width:6.59375in;height:2.61187in" />

In the emerging standard, a Skill is a folder with a SKILL.md file — a name, a one-line "use me when…" description the agent reads to decide whether the task fits, and a body of steps it loads only when needed. "How we review a pull request here," "how we write an ADR on this project," "our incident runbook" — each written once, then loaded by any agent that hits that task.

﻿

Traditional

AI-native

Where the procedure lives

a senior's head, or a wiki page nobody reopens

a SKILL.md in the repo, version-controlled

Reuse

re-explained per person, per task

written once, loaded by every agent that needs it

Who sanctions it

whoever answers first in Slack

the architect decides what is standard enough to be a shared Skill

Why you care. A Skill is shared infrastructure, not a personal snippet. When your team keeps re-explaining the same procedure to an AI tool, that procedure wants to be a Skill — and the architect decides what is standard enough to sanction as one, versus a one-off prompt you paste for a single task. The rule of thumb to recognise: MCP for capabilities and data; a Skill for procedures and instructions. (The Final Kata in this module has you package your own architecture role-agent as exactly this kind of Skill.) The full three-way choice — MCP server vs Skill vs prompt content — is specialist depth in Deep Theory.

Part D — Choosing the shape of an AI feature

Before any diagram, there is a prior decision: what shape should this feature even be? The AI era added options, and reaching for the fanciest one is the common mistake. Four shapes, simplest first:

Shape

What it is

Reach for it when

Standard service

plain deterministic code, no large language model (LLM)

the rules are known and fixed — still most of the system

Automation

one scripted LLM call in a fixed place

a single step needs language understanding (classify, extract, summarise)

Workflow

LLM steps chained in a fixed, named order

the path is known but several steps need judgement

Agent

the model chooses the steps at run time

the path genuinely cannot be known in advance

The rule of thumb: pick the simplest shape that fits, and treat reaching for an agent — or worse, for multi-agent — as a choice to justify, not a default. A workflow you can read top to bottom beats an agent you have to debug at 3 a.m. The shape itself is an architecture decision, so it earns an ADR (Block 3).

<img src="media/image8.png" style="width:6.25in;height:3.08066in" />

**Check your understanding**

1.  You find a system diagram in a PowerPoint from 3 months ago. What two problems does this create for AI tools?

2.  Name one diagramming-as-code format.

3.  In the OMS L2 diagram, what is the purpose of the SQS FIFO queue? Why is it not drawn as a direct call from Order API to Fulfilment Worker?

4.  Name one integration on your current project where the boundary knowledge lives in someone's head.

5.  What is the risk when an AI agent has no boundary information?

**Recap**

- Diagrams-as-code (Mermaid, D2, PlantUML) live in the repo and AI can read them.

- Image-based diagrams in slides or wikis are an unreliable source of truth — a vision model may read a screenshot, but agents can't diff, update, or trust it.

- The architect's job is to keep diagrams in a format both humans and agents can consume.

- C4 has 4 levels: L1 (people + external systems), L2 (containers), L3 (components), L4 (code). Use L1–L2 for all-learner communication; L3–L4 rarely.

- Integration boundaries define where one system ends and another begins.

- Traditional: tribal knowledge. AI-native: explicit contracts in the repo.

- MCP is the emerging standard for AI agents to discover available tools and their constraints.

- A Skill packages a reusable procedure (a SKILL.md the agent loads on demand) — MCP gives an agent its reach, a Skill gives it a repeatable *how-to*; the architect decides what is standard enough to be a shared Skill.

- An AI feature has a *shape* — standard service, automation, workflow, or agent. Pick the simplest that fits; an agent (and especially multi-agent) is a choice to justify, not a default.

**Key terms:** diagram-as-code, Mermaid, system diagram, C4 model, integration boundary, MCP, scope boundary, boundary contract, Agent Skill.

# Block 3 — Decisions / Architecture Decision Records (4.3)

Diagrams and decision records evolve together. The diagram shows the chosen shape; the ADR preserves why the team chose it, so people and agents can apply the reasoning later.

An **ADR (Architecture Decision Record)** (course Glossary — Learn portal or curriculum repo: ./modules/000-glossary.md#adr-architecture-decision-record) is a short document for one significant architecture decision.

It captures:

- what was decided;

- why it was decided;

- which alternatives were rejected;

- consequences.

The collection of all ADRs is the **Architecture Decision Log (ADL)**. It is the project decision audit trail.

In this topic you will learn to:

- name the core ADR sections;

- distinguish a wiki note from an agent-readable decision;

- explain why AI tools repeat rejected options;

- identify when a new ADR is needed.

**When to write an ADR**

Only architecturally significant choices need records. Write an ADR when the choice changes system shape or delivery behaviour.

Use an ADR when the decision:

- changes an external system property, such as API contract, data format, or authentication;

- affects a high-priority quality attribute, such as latency, cost, security, or availability;

- adds or removes a dependency;

- changes system structure, such as adding a service or splitting a module;

- accepts strategic technical debt;

- forces developers to change approach, tool, or process.

If none of these apply, a lightweight note is enough.

**Traditional decisions**

A common wiki paragraph says:

“We chose Kafka for performance.”

Two months later, a developer or AI agent picks RabbitMQ because it looks simpler. Three days of rework follow.

The decision existed. It was invisible at the moment of choice.

**AI-native decisions**

An AI-native decision lives as structured Markdown in the repo.

It follows a common ADR format used in this course and adds one course-specific extension:

**Agent-Readable Summary** — one or two sentences written so an AI tool can parse and apply the durable constraint.

This summary is a curriculum extension, rather than a required field in every industry ADR template.

**Traditional decision: wiki paragraph**

“After discussing options in the architecture meeting, we decided to go with Kafka for our event streaming needs because of its performance characteristics and our team's familiarity with the tool.”

**Agent-readable decision: ADR in repo**

The example includes both decision content and the lifecycle fields used by this course.

\# ADR-007: Use Kafka for all event streaming

\## Status

Accepted \<!-- Lifecycle: proposed → accepted → revoked; or proposed → rejected --\>

\## Owner

Architecture team

\## Source and Freshness

Approved architecture review and broker evaluation.

Last reviewed: \`YYYY-MM-DD\`

\## Review Trigger

Re-evaluate when the event-volume profile, replay requirement, platform strategy, or approved broker service changes.

\## Decision

We will use Apache Kafka for all event publishing and consumption.

\## Alternatives Considered

1\. RabbitMQ — rejected: it would add a second broker beside the approved Kafka platform without a requirement that justifies it

2\. AWS SQS — rejected: cloud-specific operation conflicts with the multi-cloud strategy

\## Consequences

\- Positive: proven at scale, team expertise exists

\- Negative: operational complexity, requires dedicated cluster management

\## Agent-Readable Summary

All event publishing uses Kafka. Do not introduce alternative message brokers.

New event-driven features use the approved shared Kafka service resolved through platform configuration.

<img src="media/image9.png" style="width:6.26806in;height:3.15278in" />

Why you care: an AI tool that generates code, specifications, or designs makes implicit technology choices. Without ADRs in context, it may keep proposing options the team already rejected.

Keep volatile details such as hostnames, ports, credentials, and current endpoints in service discovery or governed configuration. The ADR should hold the durable choice and the rule that points to that source.

**ADR status lifecycle**

This course's ADR template uses four status values.

- **Proposed** — under discussion.

- **Accepted** — committed; the team builds to it.

- **Rejected** — considered and declined; keep it so future teams know why.

- **Revoked** — accepted earlier, then replaced by a newer decision.

The immutability rule applies to the decision content:

Once accepted, do not rewrite the decision or its rationale. If the decision changes, write a new ADR that supersedes the old one. The old ADR's status metadata may then change to Revoked, with a link to its successor.

<img src="media/image10.png" style="width:6.26806in;height:2.68542in" />

**Pattern decisions**

ADRs also capture pattern choices.

A pattern decision says which design pattern fits this context and why. Then an AI tool generating code in that area can follow the pattern instead of inventing its own structure.

K 4.W.6 gives you nine candidate patterns. The table below is a **recognition reference for Wide learners**. It helps you understand a recommendation; it is not a substitute for architecture judgment.

In the kata, you place each pattern on the architecture or reject it, then record the reasoning.

| **Pattern**                                     | **What it is**                                                                             | **When it fits**                                                                  |
|-------------------------------------------------|--------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------|
| Strangler Fig                                   | Move traffic from a legacy system to its replacement incrementally                         | A phased migration with a controlled cutover                                      |
| Outbox                                          | Write the event to a DB table in the same transaction as the state change, then publish it | Reliable event publishing without distributed transactions                        |
| Saga                                            | Run a multi-step business transaction as local steps with compensations                    | Cross-service workflows that cannot share one DB transaction                      |
| Bulkhead                                        | Isolate resources so one failure cannot sink the rest                                      | Keeping one tenant, region, or dependency from starving others                    |
| Circuit Breaker                                 | Stop calling a failing dependency and fail fast until it recovers                          | External calls that time out or cascade                                           |
| BFF (Backend for Frontend)                      | A tailored API layer per client surface                                                    | Web, mobile, and POS surfaces with different shapes                               |
| Pipe & Filter                                   | Chain independent, testable processing stages                                              | Request pipelines, including LLM call chains, that need per-stage instrumentation |
| Event Sourcing                                  | Persist state as an append-only log of events                                              | Audit trails and replay for high-stakes decisions                                 |
| CQRS (Command Query Responsibility Segregation) | Separate the read model from the write model                                               | Read-heavy workloads where reads and writes scale differently                     |

How these patterns mutate for AI-native systems is covered in Deep Theory §4.7.9 (**400-ARCH:Deep:Theory**, curriculum repo:

./modules/400-arch/400-deep-theory.md).

**Ask for:** the relevant ADR or ADL entry with owner, source and freshness, status, review trigger, decision, rejected alternatives, consequences, and the course's Agent-Readable Summary.

**Check your understanding**

1.  Your team chose PostgreSQL over MongoDB six months ago. Where should that decision live?

2.  What is the difference between a decision record and meeting notes?

3.  Name three events that should trigger a new ADR and two lightweight choices that should not.

4.  A senior developer wants to rewrite ADR-012 because context changed. What is the correct approach?

**Recap**

- A decision record captures what, why, and what was rejected.

- The ADL is the project's decision audit trail.

- In AI-native delivery, ADRs live in the repo as structured Markdown.

- ADR status follows two paths in this course: proposed → accepted → revoked, or proposed → rejected.

- Accepted ADRs are superseded by newer ADRs. They are not rewritten.

- The Agent-Readable Summary is the course-specific extension that turns documentation into a concise agent constraint.

- Pattern decisions belong in ADRs too.

**Key terms:** ADR, ADL, Agent-Readable Summary, decision record, design pattern.

# Block 4 — Non-Functional Requirements / enforceable NFRs (4.4)

Quality constraints begin in discovery and shape solution options and ADRs. This block appears after ADRs only as a learning sequence. It shows how to turn those early constraints into enforceable NFRs that tell Engineering what to build, QA what to prove, and Operations what to watch.

An NFR is a **Non-Functional Requirement** (course Glossary — Learn portal or curriculum repo: ./modules/000-glossary.md#nfr). It describes a quality property or invariant rather than a feature behaviour.

Each NFR entry in a governed set has six fields. Four describe its content:

1.  **Metric or invariant** — what property is measured or must always hold.

2.  **Target** — the threshold, range, or categorical rule.

3.  **Conditions** — workload, region, data set, model version, failure state, or test environment under which the target applies.

4.  **Enforcement** — automated check and its consequence, such as a continuous integration (CI) gate, runtime alert, degrade rule, or stop rule.

Add two lifecycle fields to that entry: **owner** and **review trigger**. The governed NFR set adds three shared metadata fields when all entries use the same values: **source**, **freshness**, and **status**. This gives one consistent completeness rule: six fields per NFR entry, plus three metadata fields for the governed set.

An **NFR budget** is the quantitative target or ceiling inside that model. Latency and cost often use budgets. Security may use an invariant such as “0 cardholder-data stores or flows exist outside the documented cardholder data environment.”

In this topic you will learn to:

- name five NFR families: latency, cost, quality, reliability, security & compliance;

- distinguish a wish, a target, and a complete enforceable NFR;

- explain why AI makes cost and quality first-class operating constraints;

- describe the enforcement and review chain.

**Traditional NFRs**

Teams often say:

- “Performance should be fine.”

- “Keep spend under control.”

- “The answer should be good.”

- “It must be compliant.”

Those are wishes. They give Engineering too little to build and QA too little to test.

Six weeks into production, a feature may respond in 28 seconds at the 99th percentile (p99). The target, workload, and enforcement were all missing.

An AI feature may cost a few dollars per request in the demo. At production volume, the monthly bill surprises everyone.

**Enforceable NFRs**

The rows below show the four content fields. Read across each row: property, target, conditions, then enforcement. Add the owner and review trigger from the lifecycle section above; record source, freshness, and status for the governed set.

| **Family**                | **Metric or invariant**                                       | **Target**                                                                                                                                                                                                                        | **Conditions**                                                                                          | **Enforcement**                                                          |
|---------------------------|---------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------|
| **Latency**               | 95th-percentile (p95) end-to-end response time                | p95 \< 3 s user-facing; p95 \< 30 s background                                                                                                                                                                                    | named region, representative peak load, production model and tool chain                                 | pull-request load test + runtime alert                                   |
| **Cost**                  | cost per request and daily spend                              | \< \$0.05 / request; \< \$500 / day                                                                                                                                                                                               | stated model prices, token range, tool calls, and traffic volume                                        | usage telemetry + budget alert + stop or degrade rule                    |
| **Quality**               | versioned eval score and hallucination rate                   | \> 85% on eval rubric; \< 5% hallucination rate                                                                                                                                                                                   | named eval set, sample size, model version, prompt version                                              | eval run in CI or release gate                                           |
| **Reliability**           | uptime, error rate, fallback recovery time                    | 99.5% uptime; \< 2% error rate; fallback within 5 s                                                                                                                                                                               | defined traffic window and dependency-failure scenarios                                                 | service-level objective (SLO) monitoring + fault test + incident trigger |
| **Security & compliance** | SCA-or-exemption coverage; cardholder-data boundary invariant | 100% of in-scope electronic payments either complete SCA or record a permitted exemption; 0 cardholder data (CHD) or sensitive authentication data (SAD) stores or flows outside the documented cardholder data environment (CDE) | transactions classified under current PSD2 rules; data flows assessed against the current PCI DSS scope | SCA/exemption audit + automated data-flow checks + release gate          |

<img src="media/image11.png" style="width:5.50723in;height:5.34055in" />

<img src="media/image12.png" style="width:5.50723in;height:5.27805in" />

These are illustrative course targets, not universal production or legal requirements. Each project must set its own values and validate regulatory scope with the responsible compliance owner.

Cost and quality already exist in software architecture. AI changes their operating importance.

- **Cost becomes granular and variable.** Model, token, retrieval, and tool choices change unit cost per request.

- **Quality becomes statistical.** The team evaluates a sample against a versioned rubric instead of assuming identical output on every run.

Security and compliance often use invariants rather than budgets. “0 CHD or SAD stores or flows exist outside the documented CDE” is enforceable when the scope and check are named. A separate privacy invariant should govern personally identifiable information (PII). “Handle data safely” remains a wish.

The specialist treatment of trust boundaries, PII flow, and controls is in Deep Theory §4.7.10 (**400-ARCH:Deep:Theory**, curriculum repo: ./modules/400-arch/400-deep-theory.md).

**The enforcement and review chain**

A complete NFR entry becomes operational over time only when the team records all six per-entry fields and maintains source, freshness, and status for the governed set.

Metric or invariant + target + conditions → automated check (fitness function) + consequence → owner → review trigger when the source, workload, model, or architecture changes

A **fitness function** (course Glossary — Learn portal or curriculum repo: ./modules/000-glossary.md#fitness-function) is an automated check that tests whether an architecture property still holds.

Complete latency example:

Metric: p95 end-to-end latency. Target: \< 3 s. Conditions: 200 concurrent users, EU region, production model and tool chain. Enforcement: pull-request load test and runtime alert. Owner: Platform team. Review trigger: model, region, or request path changes. NFR-set metadata: source evidence, last_reviewed, and status are maintained once for the governed set.

<img src="media/image13.png" style="width:6.26806in;height:1.82153in" />

Why you care: if you build or test an AI feature, you need the target, conditions, and check. A number alone can pass in a toy environment and fail in production.

**Ask for:** an NFR statement with metric or invariant, target, conditions, and enforcement; per-NFR owner and review trigger; and collection-level source, freshness, and status.

**Check your understanding**

1.  Rewrite “the chatbot should be fast” as an operational NFR with all six per-entry fields, then name the source, freshness signal, and status for its governed set.

2.  Why are cost and quality existing architecture concerns that become more operationally visible in AI features?

3.  Which part is missing from p95 \< 3 s if the workload and region are unspecified?

4.  Give one security invariant and the automated check that enforces it.

5.  Write one cost or quality NFR with its conditions and enforcement.

**Recap**

- A complete NFR entry has six fields: metric or invariant, target, conditions, enforcement, owner, and review trigger.

- Its governed set also records source, freshness, and status.

- Five families matter: latency, cost, quality, reliability, security & compliance.

- Cost becomes per-request and variable; quality becomes statistical and eval-driven.

- Security and compliance often use invariants rather than numeric budgets.

- The full chain is definition → check and consequence → owner → review trigger.

- A target without conditions or enforcement is still incomplete.

**Key terms:** NFR, invariant, NFR budget, latency budget, cost ceiling, quality threshold, compliance invariant, fitness function.

**Implementation example — EPAM Technology Copilot**

The team produces the five core materials through the four activities above. On EPAM engagements, Technology Copilot is one implementation path for mining source context and drafting the outputs listed below.

[**EPAM Technology Copilot**](https://epa.ms/copilot) is an EPAM tool that supports this workflow. Treat it as an implementation example, rather than the architecture method itself.

It takes engagement inputs such as:

- requests for proposal (RFPs);

- requirements;

- call transcripts;

- existing architecture docs;

- engineering docs;

- URLs.

- These inputs become four linked context sets:

| **Context it builds** | **What is in it**                                                                                                                                      | **Roles that consume it**                                       |
|-----------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------|
| **Business**          | business drivers, goals, key performance indicators (KPIs), in-scope capabilities                                                                      | Architects, Delivery Managers, QA Architects, Business Analysts |
| **Product**           | functional and non-functional requirements                                                                                                             | Architects, Business Analysts, QA Engineers, Software Engineers |
| **Architecture**      | quality attributes, metrics, ADRs, solution strategy, diagrams in supported domain-specific languages (DSLs), role-specific governance recommendations | Architects, QA, System, DevOps, and Security Engineers          |
| **Engineering**       | an agentic team bundle wired to the other three contexts for spec-driven development                                                                   | Software Engineers                                              |

Here, an **agentic team bundle** means the packaged agent configuration and instructions that connect coding agents to the Business, Product, and Architecture sets. Its exact contents may vary by product version.

This is a product-output taxonomy, not the four-layer writing taxonomy from Discovery. Do not map the names one-to-one: the course layers organise discovery input, while the Technology Copilot sets organise generated outputs.

- Business + Product support Discovery.

- The product's Architecture set covers solution structure, decisions, and NFR inputs; it is not the same term as the course's architecture context.

- Engineering gives coding agents the build context.

- Regulatory constraints still need to be captured during Discovery and carried into the relevant diagrams, decisions, and enforceable NFRs.

It works in both directions:

- **AS-IS** — current system;

- **TO-BE** — target architecture.

<img src="media/image14.png" style="width:6.26806in;height:2.82153in" />

The linked product materials also describe architecture-document assessment, Rapid EngX Assessment, and presales support.

**How the context reaches your tools**

Technology Copilot uses a shared workspace where the team co-works.

The mined context and generated outcomes are exposed through an **MCP server** (course Glossary — Learn portal or curriculum repo: ./modules/000-glossary.md#mcp-server). The server is the access mechanism. The separate boundary contract must still define authorised roles, tool permissions, data scope, rate limits, owner, and escalation path.

This makes Technology Copilot more than a document generator.

- A BA pulls Business and Product contexts into CodeMie, or another MCP-aware tool.

- QA, System, DevOps, and Security engineers read the product's Architecture set the same way.

- Software and System engineers load the Engineering bundle in the integrated development environment (IDE) for spec-driven development against the linked context sets.

- Any authorised role with ingestion permission can re-mine context by adding documents or URLs.

The shared context gets more complete as the engagement goes on.

<img src="media/image15.png" style="width:6.26806in;height:2.76319in" />

Why you care: this is one implementation path for drafting the context, diagrams, decisions, and NFR inputs named in its output table. The boundary contract that governs MCP access remains a separate architecture material.

The tool drafts. The architect reviews, corrects, and decides:

- which option;

- which trust boundary;

- which budget;

- which decision summary.

Judgment stays human-owned.

**Key terms:** EPAM Technology Copilot, AS-IS / TO-BE architecture, agentic team bundle.

**Anti-patterns**

Use these as review prompts.

A weak architecture material leaves a visible trace. Match the trace to the missing material, then ask for the precise fix.

<img src="media/image16.png" style="width:5.96558in;height:5.44472in" />

**Outcomes**

After this Wide Theory, you can:

- explain why constraint discovery starts before solution choices and then continues iteratively;

- name two context types: architecture and engineering;

- name four context layers: business, product, engineering, regulatory;

- name four architecture activities and their five core materials: context pack, diagrams, boundary contracts, ADRs, and enforceable NFRs;

- distinguish the traditional and AI-native version of each material;

- explain why slide diagrams, inaccessible decisions, and tribal boundary knowledge are weak AI inputs;

- explain that MCP exposes tools, resources, and prompts while a boundary contract governs their use;

- distinguish protocol-delivered MCP features from portable Skills that package reusable guidance and supporting files;

- write an operational NFR with six per-entry fields and maintain source, freshness, and status for its governed set;

- tell an architect what material you need, in what format, and why;

- identify which context layer your own role's AI tool should consume;

- identify the owner, freshness signal, status, and review trigger for an architecture material;

- name four AI feature shapes: standard service, automation, workflow, agent;

- choose the simplest shape that fits;

- recognise that AI-in-product architecture is specialist work covered in Deep Theory.

<img src="media/image17.png" style="width:6.26806in;height:2.96736in" />
