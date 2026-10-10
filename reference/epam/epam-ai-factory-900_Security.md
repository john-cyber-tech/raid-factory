**In a nutshell**

Two teams ship the same feature. One decided early which data crosses which boundary, which service can call which API, and who owns the leftover risk; the other discovered all three during an incident. This Wide track teaches the first habit: **security gets decided at design time or discovered in an incident — on every solution your team ships, with or without a model in it.** It sits late in the program, after Engineering, QA, Data, and Infrastructure. It's for every role, because on most features the security work happens before any specialist is in the room. You learn to model a system, score its risks, and evidence one mitigation — not to replace a security specialist, but to know when to call one.

**Role Context**

- **Who it's for.** Everyone — on most features the security work happens before any specialist is in the room (engineers, PMs, architects, QA, data, infra).

- **What the role does.** The security owner models the system and inventories its assets, enumerates threats (classical and AI-specific), scores them, designs preventive/detective/responsive controls, verifies they work, and governs access scope and kill-switches.

- **Where it sits.** Late in the SDLC, downstream of Architecture, Engineering, and Infrastructure. It receives the architect's trust boundaries and the team's solution, and hands back a threat model, a scored risk register, and an evidence pack the delivery and governance functions act on.

- **What they don't own.** The architect draws the trust boundaries and the data-flow diagram; you read them and bring the access-scope and blast-radius lens — you don't draw the boundaries yourself.

- **The L2 → L3 shift.** The L2 owner writes the threat model and evidence pack by hand with AI drafting the first pass; the L3 owner restructures it as a system — the model regenerates from the architecture on every change, checks run as a CI gate, guardrails are declared as code, and a scoped agent triages findings, while the human specifies the agent, defines what "pass" means, and accepts the residual risk.

**Why this matters for you**

Security decisions are made in every sprint, by every role, on every solution — which data crosses which boundary, which service can call which API, whether a control closes a gap or only describes it. If you can model a system, score its risks, and evidence one mitigation, you make those decisions deliberately instead of discovering them in an incident. You won't replace a security specialist, but you will know when a risk is big enough to escalate to one.

<img src="media/image1.png" style="width:6.26806in;height:2.64653in" />

**Topic recap**

The track runs in seven short blocks — here's each in brief.

- **Security Planning (Block 1).** Every secure solution ships with three artefacts: a threat model (the map of how it can be attacked), a scored risk register (threats ranked so you know which to fix first), and an evidence pack (proof the top risk has a control, a named owner, and a passing test). Three first principles frame every decision — the CIA triad (confidentiality, integrity, availability — name which one a control protects), least privilege (give a component only the access its job needs), and defense in depth (layer controls so each catches what the last missed). These are delivery-team documents the security team reviews, not security-team documents.

- **Threats & Risk (Block 2).** Threats split into two buckets: classical ones every system has had for decades (injection, leaked secrets, denial of service), caught by scanners and design review, and AI-specific ones a model adds, which a classical scanner won't see. For the AI bucket you run the OWASP LLM Top 10 checklist rather than inventing threats from a blank page, mapping each to a CIA property and the asset it targets. Then score every threat on Likelihood × Impact (1–5 each, a 1–25 product) so a flat "all-Medium" register can't hide which risk to fix first.

- **Reviewing the Design (Block 3).** The architect draws the trust boundaries and data-flow diagram; you read them and bring two questions. Access scope: does each component hold only the access its job needs, and is every external input and AI-retrieved document treated as untrusted — even one from your own SharePoint? Blast radius: written as a count ("up to 1,200 client engagements exposed," not "many users") so the mitigation is sized to the exposure.

- **Secure Engineering Support (Block 4).** Every critical risk needs three control classes — preventive (stops the attack), detective (notices it), and responsive (contains the damage); one class alone isn't defense in depth. Match the control class to the threat's CIA property: a confidentiality control does nothing for an integrity threat. Whatever risk remains is the residual risk, which needs a five-field contract — statement, named owner, expiry date, re-evaluation triggers, and an approver — or it's a deferred decision with no owner.

- **Security Testing (Block 5).** A control that's described but not tested is theater, so you test the bypass case — feed it the attack input (the PII string, the injected payload) and confirm it's blocked, not the happy path. Scanners (Semgrep, Snyk, gitleaks) flag more than any sprint can fix, so triage by severity × reachability and fix the high-and-reachable first. The verification log — control name, exact test command, pasted output, date — is the artefact; "tested manually" is an audit finding.

- **Governance & Compliance (Block 6).** Anything leaving your boundary routes through an approved gateway, not a consumer endpoint with no audit trail, no deletion, and no data-processing agreement. A usage policy names allowed uses, disallowed uses, and a named escalation owner for borderline cases; a license scan flags GPL/AGPL before it ships. EU AI Act classification starts from intended purpose and the conditions in Article 6 and the relevant annex; a qualified human signs that determination.

- **Security Operations (Block 7).** Any component that takes irreversible actions (sends, writes, pays) needs a kill switch with three properties: a named owner reachable at 03:00, out-of-band operation, and a risk-based test cadence. When an incident lands, work the four-step loop in order — contain, investigate, remediate, postmortem (blameless). Project-calibrated block/error, cost, and latency alerts catch attacks before the outage.

<img src="media/image2.png" style="width:6.26806in;height:1.21389in" />

# Key terms

<img src="media/image3.png" style="width:5.84058in;height:3.72936in" />

**Key takeaways**

1.  The three artefacts — threat model, scored risk register, evidence pack — are delivery-team documents your team produces; the security team reviews them, it doesn't write them for you.

2.  Run the OWASP LLM Top 10 as a prioritised checklist on any feature with a model; review uncategorised findings instead of treating the list as exhaustive.

3.  Match the control to the property the threat puts at risk — a confidentiality control does nothing for an integrity threat — and never ship one control class alone.

4.  "Tested manually" is an audit finding; evidence is a named test command, the bypass input, and the pasted output that proves the gap is closed.

5.  Every irreversible action needs a named, out-of-band kill switch tested on the project’s defined cadence, and every accepted risk needs a named owner with an expiry date.

**Course Repo: <https://epa.ms/ai-run-26-curriculum-repo>**

# Wide Theory

55 minutes

***Focus**: From ad-hoc PR comments to a machine-readable threat model, scored risk register, and evidence pack that ships alongside any solution your team builds — security of any feature first, with AI-feature security and the specialist depth in the Deep track.*

***Deep for:** security engineers, security champions, tech leads responsible for security and AI governance.*

*Total time per learner:*

- *Wide path: 45 min Theory + 75 min kata series + 60 min Final Kata ≈ 3h*

- *Deep path (own role): + 180 min Theory + 210 min, 7-kata Deep series ≈ +6.5h*

*(Per-role times are firm; the program-wide ~40h total is under recomputation.)*

Security decisions are made in every sprint, by every role, on every solution — not only the ones with AI in them. Which data crosses which boundary. Which service can call which API. Whether a control actually closes the gap or only describes closing it. This module gives you the vocabulary and the practice chain to make those decisions deliberately on any solution your team builds — from telling an AI-specific threat from a classical one and running the **OWASP LLM Top 10** (course Glossary — Learn portal or curriculum repo: ./modules/000-glossary.md#owasp-llm-top-10) checklist, through a scored risk register, a mitigation design, and the evidence pack an auditor reads two minutes before deciding whether to issue a finding. The superpower you walk away with: *"I built a risk-based plan, mitigated one critical risk end-to-end, and specified the assistant that does the first half of this work for the next solution."* AI features carry an extra threat class on top of this baseline; the Deep track covers it — naming the threat class itself (D1) and building the specialist governance pack.

**Objectives**

- **Learn to do:** Build and deliver a complete threat model → risk register → mitigation → evidence pack for any solution or feature your team ships.

- **Skills (role):** Tell AI-specific threats from classical ones and run the OWASP LLM Top 10 checklist; score, mitigate, and accept one critical risk with a residual-risk contract; compile a SOC-2-ready evidence pack.

- **Skills (tooling):** OWASP LLM Top 10 and risk-rating references; static/secret scanners (Semgrep, gitleaks); control implementation + verification.

- **Outcome:** Five chained artefacts (00-assets.md through 04-evidence.md) plus a project-grounded threat-modeling role-agent (a Claude Skill or sub-agent under .claude/). Deep adds a production-grade AI-security / governance pack (00-decomposition.md → 08-charter.md) and an agentic vulnerability-analysis report.

- **Tested by:** The K 9.W.1 → K 9.W.5 chain and the Final Kata (K 9.3); Deep is tested by the K 9.D.1 → K 9.D.7 governance + vuln-analysis pack.

No security background is required for the Wide path. The Wide katas run on a solution you pick — your own project, a **Reference Cases** (Learn portal or curriculum repo: ./modules/001-reference-cases.md), or one of the generic solution archetypes in the Wide menu — so nobody stalls on choosing a system.

# 0 — Role Context

**0.1 — Role names and who they apply to**

This module's Deep path is written for the people who own security decisions on an AI delivery team. Titles vary by client and account; if any of these is yours, this is your module:

- **Security Engineer / Application Security (AppSec) Engineer** — builds and verifies controls in the product.

- **Security Champion** — an engineer, tech lead, or architect who carries security ownership inside a delivery team without a dedicated security headcount.

- **DevSecOps Engineer** — wires security gates into the pipeline.

- **Security Architect / AI Governance Lead** — owns trust boundaries, autonomy-tier classification, and the governance charter.

- **GRC / Compliance Analyst** — owns the audit trail, evidence, and framework alignment (SOC 2, ISO 27001, GDPR, EU AI Act).

The Wide path is for everyone else — engineers, PMs, architects, QA, data, infra — because on most AI features the security work happens before any of these specialists is in the room.

**0.2 — Role description and core duties**

The security owner on a delivery team:

- **Models** the system as a data-flow diagram with explicit trust boundaries, and inventories its assets by sensitivity.

- **Enumerates** threats against each element (STRIDE), and — where the solution includes a model — maps the AI-specific subset to the OWASP LLM and Agentic Top 10.

- **Scores** each threat on Likelihood × Impact and names the top critical risk and its blast radius.

- **Designs** preventive / detective / responsive control triples and writes the residual-risk acceptance contract.

- **Verifies** that a shipped control closes the gap, and compiles the auditor-readable evidence pack.

- **Governs** access scope, kill-switch ownership, framework alignment, and — for production AI systems — autonomy-tier classification.

**0.3 — Main processes**

- **Threat modeling** — DFD → trust boundaries → STRIDE → scored register, refreshed when the architecture changes.

- **Secure design review** — reviewing an architecture for trust-boundary placement, access control, and data protection before build.

- **Security testing** — SAST/DAST triage, dependency and secret scanning, and — for features with a model — red-teaming prompts and evals in CI.

- **Governance and sign-off** — system-register entry, residual-risk acceptance, charter approval, and autonomy-tier decisions for AI systems.

- **Incident support** — kill-switch activation, NIST IR phases, post-incident evidence.

**0.4 — Role in SDLC**

Pre-AI, security sat near the end of the pipeline: a pen-test before release, a checklist at a design gate, a SAST scan in CI. Upstream inputs were architecture diagrams and requirements; downstream hand-offs were findings tickets and a sign-off. The interface to delivery was mostly a gate — pass or block — rather than a design partnership. The recurring failure mode was finding a structural risk too late to fix cheaply.

**0.5 — How the role changed with AI (general)**

AI changed how the security work itself gets done, on every solution — not only the ones with a model in them: a model drafts the DFD, runs the first STRIDE pass, proposes controls, and generates eval cases, turning hours of blank-page work into minutes of review. The judgment (is this threat real, is this control sufficient, who accepts the residual risk) stays human. AI features then add a threat class of their own — which data enters a prompt, which tools an agent may call, whether a control closes a gap or only describes it — pulling part of the security surface to design time; that surface is the subject of the Deep track.

**0.6 — What changed at L2 (AI-assistant)**

The human owns the security artefact; AI copilots the drafting. You prompt a model to generate a first-pass DFD, a STRIDE enumeration, or a control design, then review and correct it. The threat model is a document a person writes with AI help; the evidence pack is assembled and checked by hand before an audit. AI speeds the first draft; nothing it produces ships without a human reading every line.

**0.7 — What changed at L3 (AI-native)**

As the work becomes more automated, it is restructured around agents and policy-as-code: the threat model is regenerated from the architecture on every change; security checks run as a gate in CI; guardrails and access scopes are declared as code, not prose; and a scoped security agent triages findings within a fixed boundary. The human's work shifts to specifying the agent, defining what "pass" means, setting the guardrails and kill-switch, and accepting residual risk. The new artefacts — agent specs, eval rubrics, guardrail context packs, and a governance charter — are what this module's Deep katas produce.

File map

<img src="media/image4.png" style="width:5.86141in;height:3.50018in" />

# Theory contents

**Wide Theory — for all roles**

<img src="media/image5.png" style="width:6.04198in;height:6.40311in" />

Deep Theory — for specialists

<img src="media/image6.png" style="width:5.69474in;height:6.36144in" />

# Wide katas overview 

All five katas run on one solution chosen at K 9.W.1 — your own project, a Reference Case, or a generic solution archetype from the Wide menu — carried through all five without switching.

*Goal:* produce a complete threat-model-to-evidence chain for one solution.

*Superpower moment:* "I built a risk-based plan and mitigated one critical risk end-to-end."

<img src="media/image7.png" style="width:6.00031in;height:2.83348in" />

# Deep katas overview 

All seven katas use the StarAssist v2 running case (L3 agentic JIRA assistant with People Central write access) — commit to one system before K 9.D.1 and carry it through all seven without switching. (The five published AI reference archetypes in the module Materials (**900-SECURITY:Materials**, curriculum repo: ./modules/900-security/900-materials-links.md) are alternates if StarAssist doesn't fit your project.)

*Specialist outcome:* a complete AI-security pack — use-case decomposition, AI-feature threat model, eval rubric + guardrail context pack, AI governance charter, and an agentic vulnerability-analysis report — production-grade enough to gate a Tier 3 AI system.

<img src="media/image8.png" style="width:6.06281in;height:3.94465in" />

# Human-owned decisions — always

AI drafts in this module. Humans decide:

- **Residual-risk acceptance** — a named individual accepts residual risk with an expiry date and documented re-evaluation triggers; AI cannot sign off. Generic ownership is the single most-cited audit failure pattern in 2025–2026 SOC 2 reports.

- **Kill-switch decisions** — the human who can stop an agent at 03:00 must be named before the agent ships. An untested kill-switch is a hypothesis.

- **Autonomy tier classification** — classifying a Tier 3 system as Tier 2 to avoid governance overhead is a governance failure, not a design decision.

- **Governance charter approval** — a charter signed only by Security is incomplete. The requesting-side owner must also sign, accepting the autonomy tier and residual risks.

- **EU AI Act classification** — screen every in-scope production AI system by intended purpose and document whether Article 6 and a relevant Annex I or Annex III category apply. This is a legal determination that AI can assist but cannot make.

See the Deep Theory (**900-SECURITY:Deep:Theory**, curriculum repo: ./modules/900-security/900-deep-theory.md) — Autonomous Security Agents (D8) and AI Governance Building Blocks (D9) — for the full accountability discussion.

# 4 — Carry-Forward

This module **consumes from** the Product Management & BA, Engineering, and Infrastructure & Operations modules — the agentic vulnerability analysis (K 9.D.7) runs over the Engineering **Feature Evidence Chain** (the implementation and its test evidence), and the threat model secures the feature and the infrastructure defined upstream — and **carries forward to** the Delivery & Project Management and Assembly Line modules. The full per-artefact edges, fallbacks, and the Deep governance-pack chain live in the module Materials (**900-SECURITY:Materials**, curriculum repo: ./modules/900-security/900-materials-links.md), Carry-Forward Catalog.

**4.1 — Evidence pack and governance pack**

| **Artefact**                                                          | **Produced in**  | **Consumed by**                                                                                    |
|-----------------------------------------------------------------------|------------------|----------------------------------------------------------------------------------------------------|
| 04-evidence.md — working control + auditor-readable **evidence pack** | K 9.W.5 (Wide)   | **Delivery & Project Management** (risk register, status reporting); **Assembly Line** (portfolio) |
| Deep governance pack (00-decomposition.md → 08-charter.md)            | K 9.D.1–6 (Deep) | **Delivery & Project Management** (AI-readiness gate); **Assembly Line** (Security subagent)       |

The Wide kata chain (00-assets.md → 01-threats.md → 02-risks.xlsx → 03-mitigation.md → 04-evidence.md) is internal to this module; only 04-evidence.md leaves the Wide path.

**4.2 — Threat-Modeling Assistant Role-Agent Spec**

- **Artefact name:** Role-Agent Spec.

- **Source:** Final Kata K 9.3 (all learners; specialists add the depth-add sections — V1–V15 enumeration, autonomy-tier branching, eval-of-evals).

- **Consuming stage(s):** **Assembly Line** (primary — lists it in the agent roster a joining teammate reads, and loads .claude/skills/security/ or .claude/agents/security.md when no Security partner is on the team); informs **Delivery & Project Management** status reporting via the K 9.W.5 evidence-pack chain.

- **Format:** a runnable Claude Skill or sub-agent, ≤ 2 pages of body, with the guardrails (human-owned decisions) inline; the 8-platform compatibility matrix is bundled as REFERENCE.md (reference material, not a spec field).

- **Engine guide target:** .ai-run/guides/security/security-practices.md, under header \## Threat model + security verification cases (from Module 900 — Security). This is the authoritative chain mapping; the spec's \<!-- chain:rules:start guide=… topic=… --\> delimiter attributes mirror it, and on any disagreement this line wins.

- **Optional stand-in override (Deep only):** tech-lead-reviewer overlay — Module 1111's decision-router uses it at gate feature.verification; the spec's escalation triggers map to its decision / confidence / risk_flags verdict.

This Deep Theory is for the security owner on an AI delivery team. It takes the Wide threat-model-to-evidence loop and rebuilds it at specialist depth: the threat class a model adds to any feature, the AI Factory threat surface, AI-augmented **STRIDE** (course Glossary — Learn portal or curriculum repo: ./modules/000-glossary.md#stride), layered controls, **policy-as-code** (course Glossary — Learn portal or curriculum repo: ./modules/000-glossary.md#policy-as-code) and security evals, supply-chain security, agentic guardrails, autonomous security agents, governance building blocks, and the Security Champion model. The body has three layers: execution patterns, self-running controls, and governed autonomy. Each layer names what AI can automate and what remains a human decision.

# Why This Matters for You

On most delivery teams, no dedicated security engineer is in the room when the decisions that matter get made. The Wide path assumes that is your situation: with AI support, you perform the first-pass security work that the delivery team owns.

You model the solution, produce the three artefacts a security partner expects, and recognise when a risk needs a specialist.

The team decides which data crosses each boundary. It decides which service can call an API. It also decides whether a control closes a gap or only describes one.

Those choices happen on every solution. A model adds threats, but it does not create the need for security.

If you can map a solution, rank its risks, and evidence one mitigation, you improve the decision before an incident.

**Security gets decided at design time or discovered in an incident.**

The Wide path gives every role that baseline. Blocks 1–7 cover the shared delivery practice. The Deep track covers specialist AI-security governance and engineering.

**Goal**

After this Wide Theory, you can trace one solution from threat model through ranked risk and control evidence, distinguish AI-specific from classical findings, and escalate security or legal decisions to a named owner.

**Time**

~55 min for guided reading and reflection. Applying all seven checks to a real solution may take longer.

**Audience**

Everyone. No security background is required.

The Wide reader learns to read, challenge, and hand off security evidence. The security specialist still owns specialist design, legal interpretation, and formal sign-off.

**Prerequisites**

The Onboarding and Fundamentals modules, including the AI fundamentals.

**Must Cover**

**A secure solution carries three linked artefacts: a threat model, a scored risk register, and evidence that the required controls for the top risk work.**

The seven blocks follow one risk from design to operation:

- **Security planning** — define scope, requirements, applicable regimes, and acceptance criteria through three delivery-team artefacts.

- **Threats and risk** — separate classical and AI-specific threats, apply the OWASP checklist, and rank the result on a 1–25 scale.

- **Reviewing the design** — read trust boundaries, challenge access scope, and express blast radius as a count.

- **Secure engineering support** — match threat classes to preventive, detective, and responsive controls, then contract the residual risk.

- **Security testing** — exercise the bypass case, triage scanner findings by severity and reachability, and record reproducible evidence.

- **Governance and compliance** — govern outbound data, licences, AI usage, intake, and the applicable EU AI Act obligations.

- **Security operations** — prepare a tested kill switch, a four-step incident loop, and three project-calibrated production alerts.

**Key Messages / Ideas**

1.  **Security starts with three artefacts.** The threat model sets scope, the risk register ranks work, and the evidence pack proves the required controls were tested.

2.  **AI adds a threat bucket.** Use the OWASP LLM Top 10, then map each finding to a CIA property and asset.

3.  **Blast radius is a count.** Size the exposure before you size the mitigation.

4.  **Controls must match threats.** Confidentiality, integrity, availability, and excessive agency need different control patterns.

5.  **A record containing only “tested manually” is not evidence.** Record the procedure or command, attack input, output, date, and implementation reference.

6.  **Data leaving the boundary needs an approved route.** Model calls use the approved AI gateway; new third-party components go through intake review. Do not assume that an unapproved consumer endpoint provides the required audit, deletion, access-policy, or contractual controls.

7.  **Irreversible action needs a tested stop.** Name the kill-switch owner, keep the control out-of-band, and test it on the project’s defined cadence. An untested stop is a hypothesis.

**Structure (Per-topic context blocks)**

Each block starts with a mental model. It then names the evidence, decision boundary, and next hand-off.

Terms used in this section

<img src="media/image9.png" style="width:5.73641in;height:7.96569in" />

# Block 1 — Security Planning

Security work starts while the design can still change cheaply. The first task is to turn broad concern into three reviewable artefacts.

**Security decisions happen at design time, rather than at pull-request review.**

A late review asks expensive questions:

- Which data crosses this boundary?

- Can this service delete a record?

- Can the component call the billing API?

- Who reviews output before a customer sees it?

- What evidence must pass before release?

A secure solution answers those questions through three artefacts:

1.  **Threat model** — sets the scope and shows credible attack paths early.

2.  **Scored risk register** — ranks threats by likelihood and impact.

3.  **Evidence pack** — proves the top risk has the required controls, accountable owners, and passing tests.

These are delivery-team documents. The security partner reviews them; the delivery team produces and maintains them.

Together, they answer four review questions:

<img src="media/image10.png" style="width:5.6114in;height:1.7987in" />

<img src="media/image11.png" style="width:6.26806in;height:2.59653in" />

📎**Upstream roles → Security:** Product/BA supplies requirements and behaviour boundaries. Engineering supplies implementation and test evidence. Infrastructure & Operations supplies gateway, deployment, monitoring, and support evidence. The architect supplies the DFD and trust boundaries.

Three principles guide every decision.

**CIA triad**

Every security threat damages one or more properties:

- **Confidentiality** — only authorised people and systems can see the data.

- **Integrity** — data and behaviour remain accurate and untampered.

- **Availability** — the system remains usable when needed.

Name the property before choosing the control. Encryption can protect confidentiality. Encryption alone does not prove payload integrity; use authenticated encryption, a message authentication code, or a signature when integrity must also be verified.

**Least privilege**

Give a component exactly the access its task requires.

A reporting service needs read access to order history. It does not need customer-table write access. An invoice job needs email access. It does not need an administrator role.

The same rule scopes an AI agent. A knowledge assistant does not need CRM write access.

**Defence in depth**

Assume every control can fail. Layer the response.

If the input filter misses an attack, the output filter may catch it. If both miss, an audit alert may detect it. A kill switch then contains the damage.

Each layer expects the previous layer to fail.

<img src="media/image12.png" style="width:6.26806in;height:2.60347in" />

**AI does the first pass.** Throughout this module, AI drafts the work and you review it. Point a model at your feature, and it can draft the threat checklist, propose controls, and draft test cases. A coding agent can also review a repository, using a tool such as Claude Code’s /security-review. The judgement stays with you: which threats are real, which control is sufficient, and who accepts the residual risk. AI accelerates blank-page work; it does not make the decisions.

As a team’s automation matures, this extends into regenerated threat models, continuous-integration security gates, policy-as-code, and scoped triage agents. Humans still define “pass”, set guardrails, name the kill switch, and accept residual risk.

**🔍Check your thinking**

Choose one solution your team shipped during the last 90 days. Carry it through all seven blocks.

- Which CIA property matters most, and which control protects it?

- Which component holds more access than its task requires, and what would you scope it down to?

- If the first input filter fails, which layer acts next? If no second layer exists, that is a defence-in-depth gap.

- Who owns the residual risk today?

An unnamed residual-risk owner is your first finding.

# Block 2 — Threats & Risk

The threat model shows the attack surface. The risk register turns that surface into ranked work.

A model adds threats, while classical threats remain. Run both checks.

**Classical and AI-specific threats**

The architect draws the DFD and trust boundaries. You read that design and sort threats into two buckets.

**Classical threats** affect systems with or without a model:

- injection;

- broken access control;

- leaked secrets;

- denial of service.

Design review and scanners cover many findings in this bucket. A Wide learner recognises and routes them.

**A useful first pass for AI-specific threats** starts with three common properties:

1.  **Natural-language input.** Free text can carry instructions that compete with intended behaviour.

2.  **Retrieved content becomes instructions.** A document remains untrusted, including one from internal SharePoint.

3.  **Agents take irreversible actions.** They send email, write records, or call billing APIs without per-step approval.

Name which properties are present before running the AI checklist.

<img src="media/image13.png" style="width:6.26806in;height:3.35833in" />

**The OWASP LLM Top 10**

Use the OWASP LLM Top 10 as a prioritised AI checklist, not as a complete threat taxonomy. Cross-check the feature against all ten categories, then keep any additional AI, agentic, or classical findings from the rest of the threat-modeling pass.

Place every finding deliberately:

- a prompt-injection path belongs in the AI pass;

- a leaked key beside a model remains a classical finding;

- an open database remains a classical finding.

A finding outside the ten remains unclassified until you review it. It may be another AI or agentic risk, or it may belong in the classical pass.

Map each threat to:

1.  its OWASP category, another named AI taxonomy, or its classical category;

2.  the primary CIA property or properties it threatens;

3.  the asset it targets.

That mapping informs the control choice in Block 4. It does not select a control by itself: the attack path, asset, and project context still matter.

<img src="media/image14.png" style="width:6.26806in;height:4.33403in" />

📎**Engineering ↔️Security:** Engineering provides the implemented feature and test evidence. The delivery team maps the classical and AI-specific surface; the security partner reviews the ranked risks, required controls, and escalation decisions.

📎**Wide ↔️Deep connection:** Wide recognises and routes AI-specific risk. Deep owns STRIDE and DFD production, incident-level treatment, the lethal trifecta, OWASP Agentic Top 10, and specialist governance packs.

**Scoring risks**

This module uses a course-specific 5×5 model: score Likelihood and Impact from **1–5**. It is not the OWASP Risk Rating Methodology, which uses different factors and scales. Calibrate the course anchors and band names to the project’s risk method before using the result for sign-off.

<img src="media/image15.png" style="width:5.96558in;height:1.43757in" />

Multiply them:

Severity = Likelihood × Impact

Read the result through four bands:

- **Low:** 1–4;

- **Medium:** 5–9;

- **High:** 10–14;

- **Critical:** 15–25.

<img src="media/image16.png" style="width:6.26806in;height:3.34097in" />

Because severity is a product, one extreme caps the result:

| 5 × 1 = 5: Medium 1 × 5 = 5: Medium |
|-------------------------------------|

One extreme rating alone never reaches Critical. **Score both axes honestly.**

Challenge every 3 × 3 score against the same evidence anchors: required access, exploit availability, exposed records or actions, and recovery cost. Do not force a distribution. If many rows still remain 3 × 3, record the uncertainty and ask the security or product owner to calibrate the anchors; a flat register without evidence still hides the order of work.

**🔍Check your thinking**

For your chosen solution:

- name one classical and one AI-specific threat;

- map the AI threat to its OWASP category, CIA property, and asset;

- score both on Likelihood × Impact;

- choose which one you would fix first.

If your AI threat reads “the model could be attacked”, it is a category, not a threat. Name the OWASP entry and the asset.

# Block 3 — Reviewing the Design

The architect owns the design map. The Wide security reviewer brings two lenses: access scope and blast radius.

**Read the boundaries; challenge the consequences.**

**Access scope**

Ask whether each component has exactly the access its job needs.

- A build runner needs no production database credentials.

- A document-reading agent needs no CRM write access.

- Every external input remains untrusted.

- Every AI-retrieved document remains untrusted, including internal content.

**Blast radius**

Ask what happens if the highest risk succeeds:

- Which data can leak?

- Which actions can fire?

- How many users, records, systems, or engagements are exposed?

**Blast radius is a count, rather than an adjective.**

Weak:

Many users could be affected.

Useful:

All 1,200 delivery managers have SharePoint access, with one client engagement per manager. Up to 1,200 client engagements could be exposed.

The count informs the mitigation decision, but does not make it alone. A \$50K mitigation may fit a 1,200-engagement exposure and may exceed the proportionate response for a 5-person internal tool; data sensitivity, potential loss, recovery cost, and project risk appetite still decide.

**AI and human decisions**

AI can draft threat enumeration, scoring suggestions, and control options. Three calls require a named human.

<img src="media/image17.png" style="width:6.26806in;height:3.46389in" />

*AI drafts threat enumeration, risk scoring, and control suggestions. A named human owns risk acceptance, kill-switch operation, and the compliance determination.*

Human-owned calls:

- **Residual-risk acceptance** — with an owner, expiry, and re-evaluation triggers.

- **Kill-switch operation** — by a named person, rather than a generic on-call group.

- **Compliance determination** — including EU AI Act classification by a qualified person.

📎**Architecture ↔️Security:** Architecture owns trust-boundary placement and the DFD. Security turns those boundaries into access-scope findings, blast-radius counts, and escalation decisions.

**🔍Check your thinking**

For the same solution:

- Is every external and retrieved input treated as untrusted?

- What is the blast radius as a count?

- Which component can lose an unnecessary permission?

“Internal” describes location. It does not prove trust.

# Block 4 — Secure Engineering Support

Risk scoring selects the problem. Control design changes the likelihood, impact, or containment path.

Every Critical risk needs prevention, detection, and response.

**Three control classes**

<img src="media/image18.png" style="width:5.84058in;height:1.8751in" />

One class is insufficient. Prevention can miss a novel attack. Detection without response produces a record of uncontrolled damage.

**Match control to threat**

A control must protect the property the threat puts at risk.

The table gives primary starting patterns, not exclusive mappings. One concrete threat can affect several CIA properties and may need controls from more than one row.

<img src="media/image19.png" style="width:5.90308in;height:2.95849in" />

The feature flag is a kill switch only when its control path and permissions remain available independently of the component being stopped.

**Not your stack?** You do not have to build every control. For a non-specialist, the skill is recognising which property a proposed control closes. That is enough to test whether the mitigation matches the threat and escalate when no control addresses it.

**Residual-risk contract**

Controls reduce risk. They rarely erase it.

After the required controls are deployed and tested, re-score Likelihood and Impact against the same anchors and record the result in the risk register. The remaining possibility is residual risk. Acceptance requires five fields:

1.  **Risk statement** — cause, event, and consequence.

2.  **Named owner** — one person and role.

3.  **Expiry date** — the reassessment date.

4.  **Re-evaluation triggers** — events that force earlier review.

5.  **Approver** — the person authorised to accept the risk for the client.

Set the expiry from the project’s risk-acceptance policy. If no policy exists, 30 days is this course’s default for High residual risk; ask an authorised owner to confirm or replace it.

Possible early triggers include:

- a published attack against the threat class;

- a model-provider version change;

- a new tool added to the agent.

“Engineering” cannot accept client risk. K. Yoon, Engineering Lead, Meridian checkout service can own the action. An authorised client-side approver still accepts the residual risk.

<img src="media/image20.png" style="width:6.26806in;height:3.3125in" />

**An acceptance missing one field is a deferred decision with no owner.**

**🔍Check your thinking**

For the top risk:

- design one preventive, one detective, and one responsive control;

- name the threat property each control protects;

- name an individual owner and due date for each control; if no project deadline exists, use a date within 30 days as the course default;

- write all five residual-risk fields.

“Risk is now acceptable” records a feeling. The contract records accountability.

# Block 5 — Security Testing

Control design is a claim. A bypass-case test supplies the evidence.

**A control that is described but untested is theatre.**

**Test the attack**

Feed the control the thing it must stop:

- the PII string;

- the injected payload;

- the credential pattern;

- the cross-resource request.

Then confirm the expected block, detection, or containment.

A clean input proves the happy path. It does not prove the security control.

The bypass-case evidence contains:

- exact test command;

- malicious or prohibited input;

- output showing the block or detection;

- implementation reference.

**Tools for the first pass**

The first-pass tools below cover SAST, dependency scanning, and secrets scanning. SAST inspects code before it runs. DAST probes the running application, but configuring an unfamiliar DAST scanner remains a QA or security-specialist task.

The Wide learner checks whether the required static and dynamic evidence exists, then triages or routes the findings.

<img src="media/image21.png" style="width:5.73641in;height:2.69458in" />

A scanner can return more findings than a sprint can resolve. Prioritise by two dimensions:

- **severity** — how much damage can occur;

- **reachability** — whether an exploitable path exists in this code.

Fix high-severity, reachable findings first. Defer lower-value work with a recorded rationale.

An unranked backlog of 200 findings repeats the all-Medium-register failure. It hides the first action.

<img src="media/image22.png" style="width:6.26806in;height:4.36389in" />

**Verification log**

The log proves the test ran. Record:

1.  control name;

2.  implementation file path or commit SHA;

3.  exact test command;

4.  relevant output lines;

5.  test date.

“Tested manually” as the entire record is an audit finding. A reproducible manual test can be evidence when the log includes the exact procedure or command, attack input, result, implementation reference, and date.

A coding agent can run a repository security review. Claude Code provides /security-review. EPAM learners can reach it through the codemie-claude command-line interface.

📎**QA ↔️Security:** QA contributes bypass inputs, evaluation evidence, and production-signal expectations. Security maps them to a threat, control, and auditor-readable verification line.

**🔍Check your thinking**

Choose one control you can test this week:

- Which bypass input must it block?

- Which command runs the test?

- Which output line proves the result?

- Where will the proof live?

If an auditor cannot reproduce the test, the evidence is incomplete.

# Block 6 — Governance & Compliance

Technical controls govern behaviour. Compliance evidence proves that the controls, owners, and approved routes exist.

The Wide learner identifies the applicable question and escalates it. Qualified owners make legal and regulatory determinations.

**IP and data leakage**

A common failure starts outside the architecture diagram. Someone pastes client code, confidential requirements, or customer records into an unapproved service.

That unapproved consumer endpoint may provide:

- no deletion mechanism;

- no audit trail;

- no DPA;

- no project-approved access policy.

Route data leaving the project boundary through an approved channel.

For model calls, use the approved AI gateway. DIAL is one vendor-agnostic gateway with authentication, logging, and policy enforcement. A project may use another approved route.

If no gateway exists, implement equivalent authentication, logging, policy enforcement, deletion, and contractual controls before production.

<img src="media/image23.png" style="width:6.26806in;height:3.23403in" />

**Usage policy**

A useful policy contains:

1.  **Allowed uses** — with two worked examples.

2.  **Disallowed uses** — what must not enter the model under any circumstances, with two worked examples.

3.  **Escalation path** — one named role and the project-defined response time for a borderline case. If the project has not defined one, use one business day as the course default and have the owner confirm it.

A policy without an escalation owner describes ambition. It does not govern an edge case.

**Meridian Retail Group** — **Reference Cases**, Case A (Learn portal or curriculum repo: ./modules/001-reference-cases.md#case-a--omnichannel-commerce-platform-for-a-global-retailer): allow status summaries and draft client communications. Keep customer PII, payment data, and contract content outside the model.

**Kepler Insurance** — **Reference Cases**, Case B (Learn portal or curriculum repo: ./modules/001-reference-cases.md#case-b--cloud-to-cloud-migration-of-50-legacy-applications): allow plans from sanitised architecture diagrams. Keep claims, policyholder, and SOX-relevant financial data outside the model.

**Licence scanning**

“Open source” does not settle compliance.

Scan these dependencies before the first staging deployment:

- libraries and SDKs;

- container base images;

- model SDKs;

- vector-database clients.

Snyk and FOSSA can scan dependency trees for licence risk. Flag GPL, AGPL, and non-commercial-use terms before release.

GPL code may require releasing modifications under GPL. Some model licences restrict commercial use. Do not infer the obligation from the licence name alone: a qualified owner checks how the dependency is used, modified, combined, and conveyed.

**EU AI Act tiers**

Use the four broad risk buckets below for orientation. Formal classification starts from the system’s intended purpose, function, and modalities. A system is High risk only when it meets the conditions in Article 6 and the relevant Annex I or Annex III category; a qualified legal owner makes that determination.

<img src="media/image24.png" style="width:5.90308in;height:3.43768in" />

<img src="media/image25.png" style="width:6.26806in;height:3.55278in" />

Many enterprise features fall into the Transparency or Minimal/no-risk buckets. Treat that as orientation, not classification evidence.

For example, recruitment ranking or credit-worthiness assessment requires qualified review against the relevant Annex III category. Do not infer the classification from the words “internal tool” or from the most severe function in isolation; document the intended purpose and assess each regulated use under current guidance.

AI can prepare classification evidence. A qualified human signs the determination.

**Intake before production**

Every new third-party component enters through the account intake route:

- SaaS integration;

- library;

- model;

- Model Context Protocol (MCP) tool;

- agent framework.

A personal API key or unreviewed dependency bypasses the incident-response playbook, ownership, and escalation. Mature programmes place intake and approved platforms, such as DIAL and CodeMie, under formal governance.

📎**Infrastructure & Operations ↔️Security:** Operations provides gateway, deployment, alert, and kill-switch evidence. Security checks whether those controls match the risk and approved intake route.

**🔍Check your thinking**

For the same solution:

- document the intended purpose, screen each regulated use against the four buckets, and route the formal classification to a qualified owner;

- identify the approved gateway and intake route; if either is bypassed, name the missing controls;

- name one prohibited input;

- name the escalation owner for a borderline case.

An ownerless escalation path cannot resolve the decision.

# Block 7 — Security Operations

Controls need an operational response. Prepare the stop mechanism, incident sequence, and alerts before production.

**Plan the 03:00 action while the team is awake.**

**Kill switches**

Any component taking irreversible action needs a kill switch. This includes a batch job, deploy script, or AI agent that sends, writes, or pays.

A production-ready kill switch has three properties:

1.  **Named owner.** Record first name, last name, and role in the runbook. The person is reachable at 03:00.

2.  **Out-of-band operation.** The stop path works independently of the component being stopped.

3.  **Risk-based test cadence.** Run it in staging on the cadence defined by the project’s risk policy and after material changes. If no cadence exists, quarterly is this course’s default for a production component taking irreversible action; record the owner’s decision, date, and outcome.

The runbook also names a backup or rotation path so the control does not depend on one person being continuously available. The accountable owner remains explicit.

A message sent to the failing component is not out-of-band. It assumes that component still works.

The Replit/SaaStr incident from July 2025 shows the structural gap. An autonomous agent dropped a production database during a code freeze it could not honour. The reported environment lacked production separation and an enforceable stop path.

A tested kill switch exists to close that gap.

**Incident response**

Run four steps in order:

1.  **Contain.** Stop damage immediately. Revoke credentials, disable the feature, or quarantine data.

2.  **Investigate.** Identify the exploited threat, timeline, affected data, and failed controls.

3.  **Remediate and recover.** Strengthen or replace the specific failed control, restore clean data and service, and validate the return to operation. “Add more monitoring” does not remediate that control.

4.  **Postmortem.** Record the timeline, remediation, and prevention without blaming individuals.

Speed precedes understanding during containment. Understanding drives the later steps.

<img src="media/image26.png" style="width:6.26806in;height:1.66875in" />

The four steps are delivery-team shorthand. NIST SP 800-61 Rev.3, published in April 2025, integrates incident-response considerations across all six NIST CSF 2.0 Functions:

| Preparation and improvement: Govern, Identify, Protect Incident handling: Detect, Respond, Recover |
|----------------------------------------------------------------------------------------------------|

These Functions are not a strict six-step sequence. Rev.3 supersedes Rev.2 and replaces its older four-phase model with a CSF 2.0-based lifecycle. The security partner owns the formal mapping.

**Monitoring thresholds**

Configure three project-calibrated alerts before production:

<img src="media/image27.png" style="width:5.79891in;height:2.45846in" />

For AI features, include input-classifier and output-filter block rates.

Resource-abuse attacks often appear first as cost. In its 2024 LLMjacking research, Sysdig modelled a worst-case AWS Bedrock cost of more than \$46K/day; this was an estimate, not a reported victim bill.

Each threshold can often be implemented with one dashboard query and one alert rule, without a specialist security platform. Without useful alerting, the outage may become the first signal.

📎**Security → Delivery:** Delivery & Project Management receives the top risk, residual-risk owner, readiness evidence, and unresolved decisions (**900-SECURITY:Carry-Forward**). Assembly Line loads the evidence pack and Security role-agent into the final delivery system (**900-SECURITY:Final-Kata**).

**🔍Check your thinking**

For the same solution:

- name the kill-switch owner and last-tested date;

- name which alert is configured today and choose the first missing alert;

- name the first containment action;

- name who performs that action tonight.

**An untested kill switch is a hypothesis, not a control.**

# Anti-Patterns

<img src="media/image28.png" style="width:6.00725in;height:4.45856in" />

# Outcomes

By the end of Wide Theory, you can:

- classify and rank solution threats with evidence-based likelihood, impact, and blast-radius reasoning;

- match the top risk to preventive, detective, and responsive controls and record residual-risk ownership;

- specify a bypass-case test and preserve reproducible control evidence;

- route governance, legal, gateway, kill-switch, and incident decisions to the qualified owner.

<img src="media/image29.png" style="width:6.26806in;height:3.76319in" />

# Sources

📎[NIST SP 800-61 Rev.3 (April 2025) — Incident Response Recommendations and Considerations for Cybersecurity Risk Management: A CSF 2.0 Community Profile](https://csrc.nist.gov/pubs/sp/800/61/r3/final)

📎[OWASP Threat Modeling Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Threat_Modeling_Cheat_Sheet.html)

📎[OWASP Top 10 for LLM and GenAI Applications — 2025 risks and mitigations](https://genai.owasp.org/llm-top-10/)

📎[OWASP Risk Rating Methodology — related methodology; the course 5×5 matrix is a separate customised model](https://owasp.org/www-community/OWASP_Risk_Rating_Methodology)

📎[European Commission — Navigating the AI Act](https://digital-strategy.ec.europa.eu/en/faqs/navigating-ai-act)

📎[Regulation (EU) 2024/1689 — AI Act legal text](https://eur-lex.europa.eu/eli/reg/2024/1689/)

📎[European Commission — Article 50 transparency guidelines, July 2026](https://digital-strategy.ec.europa.eu/en/library/guidelines-transparency-obligations-providers-and-deployers-ai-systems)

📎Replit — response and safeguards after the SaaStr database incident

📎Sysdig — LLMjacking research and the modelled \$46K/day cost

📎[ZAP documentation — dynamic scanning of authorised web applications and APIs](https://www.zaproxy.org/docs/)

# AI solution archetypes (Deep path)

These five AI systems are the subjects the **Deep** track threat-models (the Deep reference pack S1/S2/S3 draws on three of them; the StarAssist v2 running case in 900-deep-katas.md is the default). They are **not** the Wide subject — the Wide series uses the generic menu above. The full archetype descriptions live here.

⚠️**No subscriptions required.** You threat-model these systems on paper or in Mermaid — you do not deploy them. The architectural specifics (Azure OpenAI, AWS Bedrock, Anthropic Claude, specific MCP tools) exist only so your DFD and STRIDE pass land on realistic trust boundaries. **No cloud provider account, AI provider subscription, or paid platform is required to complete any kata.** Free / OSS / free-tier alternatives for hands-on work are listed in K 9.W.5 path \#1.

**1. Internal RAG Assistant — internal RAG chatbot**

- **Purpose** — delivery managers query project documentation and create / update project-tracker tickets.

- **Architecture** — Azure OpenAI on the current OpenAI frontier model (GPT-4o or successor), RAG over SharePoint document library, two MCP tools (project tracker: read + write), HITL on schedule / budget / resource changes, autonomous on read queries.

- **Audience** — internal company staff only; no client data in scope.

- **Data classes touched** — internal documents, project metadata, employee identifiers.

- **Compliance flags** — internal data handling policies; EU AI Act Limited Risk; Article 50 transparency disclosure to internal users.

- **Best fit for** — BA / PM / Eng; most teams have a comparable internal-tool deployment on their plate.

- **Reference architecture lineage** — Microsoft Foundry / Azure OpenAI baseline RAG chatbot.

**2. Customer Support Bot — customer-facing support chatbot**

- **Purpose** — customers of a SaaS product ask product questions, file support tickets, request refunds under a per-transaction cap.

- **Architecture** — Anthropic Claude on AWS Bedrock; AgentCore Runtime with session isolation; AgentCore Gateway over internal APIs; AgentCore Policy (Cedar) enforcing refund caps OUTSIDE the model.

- **Audience** — external customers.

- **Data classes touched** — customer account data, order history, payment metadata (no raw PAN).

- **Compliance flags** — GDPR Article 22 (automated decisions on refunds); PCI DSS (no raw cards); EU AI Act Limited Risk + Article 50 disclosure.

- **Best fit for** — Eng / Arch; external trust boundary plus monetary-action authorization.

- **Reference architecture lineage** — Amazon Bedrock AgentCore customer-support demo.

**3. Coding Agent — coding agent**

- 

Purpose — developers delegate code review and draft-PR generation; agent runs in a sandboxed CI runner.

Architecture — GitHub Copilot coding agent or Claude Code; ephemeral GitHub Actions VM; firewall-restricted internet (allowlist of package registries + CAs); write access only to copilot/\* branches; mandatory human review for merge.

Audience — internal developers.

Data classes touched — source code (potentially confidential), CI secrets (must be isolated), PR descriptions, commit history.

Compliance flags — SOC 2 CC6 / CC7 / CC8 (access, monitoring, change management); ISO 27001 A.8.28 (secure coding).

Best fit for — Eng / Arch; agent + sandboxing + repo ACLs.

Reference architecture lineage — GitHub Copilot coding agent (docs.github.com); Claude Code permission model (code.claude.com).

﻿

4\. Document Triage Pipeline — document classification batch pipeline

Purpose — classify incoming contracts, extract structured fields, route to legal review queues.

Architecture — S3 ingest → EventBridge → Step Functions → Textract OCR → Bedrock Prompt Flow (Claude or Nova) for classification → schema-driven extraction → DynamoDB; Amazon A2I human-in-the-loop on confidence \< 85%.

Audience — internal legal + operations users.

Data classes touched — contract text (commercial-confidential plus special-category personal data possible), party identifiers, financial terms.

Compliance flags — GDPR Article 22 (automated routing decisions); ISO/IEC 42001 Annex A.5 + A.7; EU AI Act potentially High Risk under Annex III(4) if used for HR contracts.

Best fit for — Data / Infra / QA; batch architecture, PII handling, confidence routing.

Reference architecture lineage — AWS GenAI IDP Accelerator v0.5.0.

﻿

5\. Voice-to-Task Assistant — voice meeting assistant

Purpose — transcribe meetings, generate summaries and action items, push tasks to project tooling.

Architecture — browser extension audio capture → Amazon Transcribe streaming ASR → Anthropic Claude on Bedrock for summarization → Bedrock Agents → project-tool API.

Audience — internal meeting participants (consent required from all participants).

Data classes touched — meeting audio, transcripts (potentially confidential discussions), action-item assignees.

Compliance flags — GDPR Article 22 if action items auto-trigger HR or performance management; US two-party consent states (CA / FL / PA / IL); EU AI Act Limited Risk + Article 50 disclosure; Article 5 prohibition if used for emotion recognition in workplace.

Best fit for — Data / BA; audio → text → action chain, multimodal trust boundary.

Reference architecture lineage — AWS Live Meeting Assistant sample (aws-samples/amazon-transcribe-live-meeting-assistant), repackaged as "Voice-to-Task Assistant" for this module to keep the menu name vendor-neutral.

# Security Intake Form — sample artifact

The intake form below is provided as a sample artifact for K 9.W.1 → K 9.W.5 work. It is not a Security-team-owned form on its own — it is what a delivery team produces and Security receives. Real intake forms inside the company may differ in format; use your account's current security-intake standard for the canonical version.

SECURITY INTAKE FORM

────────────────────────────────────────────────────

Feature name and scope:

\[One sentence: what the feature does and who uses it\]

Data classification:

\[ \] Client PII

\[ \] Confidential client data

\[ \] Internal data

\[ \] Public data only

Describe data accessed:

\[What does the feature read, write, or process?\]

AI components:

Model: \[name + hosting: self-hosted / cloud-managed / third-party API\]

Fine-tuning: \[ \] Yes \[ \] No

RAG: \[ \] Yes — source: \[\_\_\_\] \[ \] No

MCP tools: \[ \] Yes — list: \[\_\_\_\] \[ \] No

Other agents: \[ \] Yes — describe: \[\_\_\_\] \[ \] No

Autonomy level:

\[ \] HITL always

\[ \] HITL on exceptions only — describe triggers: \[\_\_\_\]

\[ \] Fully autonomous

Blast radius (if this feature were compromised):

Data that could leak: \[\_\_\_\]

Actions that could trigger: \[\_\_\_\]

Who would be affected: \[\_\_\_\]

Compliance requirements:

\[ \] GDPR \[ \] SOC 2 \[ \] ISO 27001 \[ \] EU AI Act high-risk (Annex III)

\[ \] Client-specific: \[\_\_\_\] \[ \] None

Requesting team: \[team name\]

Target release date: \[date\]

────────────────────────────────────────────────────

<img src="media/image30.png" style="width:6.00031in;height:5.63223in" />

The intake form aligns to Block 2 (data classification per LLM02), Block 2 (trust-boundary detail), Block 3 (lethal-trifecta blast radius), and Block 6 (compliance flagging). A well-filled intake gets a Security decision in hours; an incomplete intake ("we are building an AI assistant") delays everything.

# Carry-Forward Catalog

This module's Wide path produces these artifacts:

<img src="media/image31.png" style="width:5.86141in;height:3.19461in" />

# Further Reading by Category

These categories are out of scope for the Wide path but expected on an L3-mature enterprise roadmap. Pointers only — depth lives in the Deep path or in vendor-specific procurement.

**AI Access Control & Governance Platforms**

- **Knostic** — RAG / identity-aware access control

- **Securiti AI** — data + AI governance

- **Credal**, **Portal26**, **Cranium** — adjacent governance tooling

**ML Supply-Chain Integrity (extended)**

- **in-toto** — supply-chain attestations standard ([link](https://in-toto.io/))

- **OpenSSF Model Transparency** — end-to-end model SBOM signing

- **GUAC** (Graph for Understanding Artifact Composition, OpenSSF)

- **OSV-Scanner** (Google, OSV.dev integration)

**Differential Privacy Toolchains**

- **OpenDP** (Harvard) — [link](https://opendp.org/)

- **Google Differential Privacy** library

- **Opacus** (Meta, PyTorch-native DP)

- **TensorFlow Privacy**

**Federated Learning Frameworks**

- **PySyft** (OpenMined)

- **Flower** ([link](https://flower.ai/))

- **NVIDIA FLARE**

- **FedML**

**AI Policy / Compliance Tooling Vendors**

- **Credo AI**, **Holistic AI**, **Saidot**, **FairNow**, **Vera** — governance platforms that map AI systems to NIST AI RMF / ISO 42001 / EU AI Act controls

**Commercial AI Red-Team / Adversarial-ML Platforms**

- **Lakera Guard** / **Lakera Red** — commercial prompt-injection defense

- **HiddenLayer** — ML detection and response

- **Mindgard** — AI red-team as a service

- **CalypsoAI** — runtime LLM moderation

- **Robust Intelligence** (now Cisco) — AI validation

- **Palo Alto Networks Prisma AIRS** — successor of Protect AI portfolio
