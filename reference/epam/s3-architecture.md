# Stage 3 — architecture and ADRs

> Trimmed excerpt of the EPAM AI Factory notes. Sections included:
> - epam-ai-factory-400_Architecture.md — Block 2
> - epam-ai-factory-400_Architecture.md — Block 3
> - epam-ai-factory-400_Architecture.md — Block 4

---

<!-- source: epam-ai-factory-400_Architecture.md -->
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

C4 L2 — Container View (what must be running for the system to work):

Notice: the L1 answers "who interacts with the system and what external systems does it depend on?" The L2 zooms in to answer "what must be running, where does state live, and how do components communicate?" Each level adds one zoom level — never both at once. Notice too the **job queue** between the Order API and the Fulfilment Worker, rather than a direct call. The API drops a job on the queue and returns to the customer at once, so a slow fulfilment step — shipping, inventory reconciliation, email — never blocks the order response, and a burst of orders queues up instead of overwhelming the worker.

er response, and a burst of orders queues up instead of overwhelming the worker.

**Part B — Integration Boundaries**

**What is this material?** A specification of where one system (or agent) ends and another begins — what it can access, what it cannot, and how it connects. Architects define these so that AI agents know their reach.

**The traditional way.** Integration knowledge lives in tribal memory: "Team B owns that service, ask them"; "the payment API has a weird timeout, check with Sarah." A new developer who needs to integrate spends days in Slack channels tracking down endpoints, auth methods, and constraints — and AI tools have zero access to any of it.

**The AI-native way.** Boundaries are written as explicit contracts in the repository. An AI agent can discover what tools and data are available, what security posture applies, and what it must not touch.

The standard for this is **MCP (Model Context Protocol)** (course Glossary — Learn portal or curriculum repo: ./modules/000-glossary.md#mcp-model-context-protocol) — think of it as "USB-C for AI tools." It defines how AI agents discover and use external tools and context; the boundaries themselves (read-only vs write, scope, rate limits) are set by how each server is built, not by the protocol:

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


<!-- source: epam-ai-factory-400_Architecture.md -->
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


<!-- source: epam-ai-factory-400_Architecture.md -->
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
