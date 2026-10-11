# Stage 6 — security and delivery

> Trimmed excerpt of the EPAM AI Factory notes. Sections included:
> - epam-ai-factory-900_Security.md — Block 2
> - epam-ai-factory-900_Security.md — Block 3
> - epam-ai-factory-900_Security.md — Block 5
> - epam-ai-factory-900_Security.md — Human-owned decisions
> - epam-ai-factory-1000_Delivery.md — Block 4
> - epam-ai-factory-1000_Delivery.md — Block 5
> - epam-ai-factory-1000_Delivery.md — Block 6

---

<!-- source: epam-ai-factory-900_Security.md -->
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

📎**Engineering ↔️Security:** Engineering provides the implemented feature and test evidence. The delivery team maps the classical and AI-specific surface; the security partner reviews the ranked risks, required controls, and escalation decisions.

📎**Wide ↔️Deep connection:** Wide recognises and routes AI-specific risk. Deep owns STRIDE and DFD production, incident-level treatment, the lethal trifecta, OWASP Agentic Top 10, and specialist governance packs.

**Scoring risks**

This module uses a course-specific 5×5 model: score Likelihood and Impact from **1–5**. It is not the OWASP Risk Rating Methodology, which uses different factors and scales. Calibrate the course anchors and band names to the project’s risk method before using the result for sign-off.

Multiply them:

Severity = Likelihood × Impact

Read the result through four bands:

- **Low:** 1–4;

- **Medium:** 5–9;

- **High:** 10–14;

- **Critical:** 15–25.

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


<!-- source: epam-ai-factory-900_Security.md -->
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


<!-- source: epam-ai-factory-900_Security.md -->
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

A scanner can return more findings than a sprint can resolve. Prioritise by two dimensions:

- **severity** — how much damage can occur;

- **reachability** — whether an exploitable path exists in this code.

Fix high-severity, reachable findings first. Defer lower-value work with a recorded rationale.

An unranked backlog of 200 findings repeats the all-Medium-register failure. It hides the first action.

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


<!-- source: epam-ai-factory-900_Security.md -->
# Human-owned decisions — always

AI drafts in this module. Humans decide:

- **Residual-risk acceptance** — a named individual accepts residual risk with an expiry date and documented re-evaluation triggers; AI cannot sign off. Generic ownership is the single most-cited audit failure pattern in 2025–2026 SOC 2 reports.

- **Kill-switch decisions** — the human who can stop an agent at 03:00 must be named before the agent ships. An untested kill-switch is a hypothesis.

- **Autonomy tier classification** — classifying a Tier 3 system as Tier 2 to avoid governance overhead is a governance failure, not a design decision.

- **Governance charter approval** — a charter signed only by Security is incomplete. The requesting-side owner must also sign, accepting the autonomy tier and residual risks.

- **EU AI Act classification** — screen every in-scope production AI system by intended purpose and document whether Article 6 and a relevant Annex I or Annex III category apply. This is a legal determination that AI can assist but cannot make.

See the Deep Theory (**900-SECURITY:Deep:Theory**, curriculum repo: ./modules/900-security/900-deep-theory.md) — Autonomous Security Agents (D8) and AI Governance Building Blocks (D9) — for the full accountability discussion.


<!-- source: epam-ai-factory-1000_Delivery.md -->
## Block 4 — Where AI helps, and where the human owns the call

AI now assists every recurring delivery deliverable that has a template. What it does not do is make the call on the right-hand column below.

| **AI assists**                                                 | **Human-owned (non-negotiable)**                                           |
|----------------------------------------------------------------|----------------------------------------------------------------------------|
| Drafting status memos, meeting summaries, retro analysis       | Strategic decisions on team direction, client positioning, programme scope |
| Risk identification and dependency surfacing from project data | Resource and capacity decisions (who works on what, at what cost)          |
| Estimation drafts and historical-comparable lookups            | Escalation calls on cost, quality, governance, or client risk              |
| Backlog clustering, defect dedup, action tracking              | Performance-management conversations                                       |
| Onboarding-doc drafting, FAQ surfacing                         | Contract changes and client commitments                                    |
| Dashboard commentary, weekly readout assembly                  | Risk acceptance at portfolio level                                         |
| RFP drafting, proposal-section writing                         | Hiring, team composition, AI Champion designation                          |
| Anomaly detection in delivery and product metrics              | What a metric anomaly means for the client relationship                    |

The right-hand column is not where AI is blocked — it is where the manager owns the outcome and signs the call. AI drafts options, surfaces precedent, and summarises context on every item there; the decision still travels through the human, because the failure mode of getting one wrong is real harm to a person, a client, or a regulatory obligation. *"The agent recommended it"* is not a defence that survives a review. And as agents take on more of the left-column sub-tasks, they run on the rest of the team's specifications, acceptance criteria, and context documents. Vague inputs produce unreliable output that needs human rework; clear, version-controlled context produces output the next agent can build on instead of redo.


<!-- source: epam-ai-factory-1000_Delivery.md -->
## Block 5 — How the team is graded

Two models sit behind every maturity claim. The first is *what* gets scored: the four dimensions of the [AI-SDLC Maturity Framework](https://leap.epam.com/sp/ai-maturity-program/framework), each rated L1–L3. The L1→L3 bands below — including the \>80% daily-active-usage threshold — are the framework's, not numbers invented here. A maturity score is a *profile* across the four, scored at team level — not one number — and it is only honest when the artefacts behind each dimension exist.

| **Dimension**                | **What it measures**            | **L1 (At Risk)**                                        | **L2 (Baseline)**                                                                    | **L3 (Frontier)**                                                                  |
|------------------------------|---------------------------------|---------------------------------------------------------|--------------------------------------------------------------------------------------|------------------------------------------------------------------------------------|
| **AI Capabilities**          | how far AI runs the work        | assisted (deliverables made with AI help, results vary) | augmented (\>50% of core-role deliverables made and verified with AI)                | agentic (agents handle sub-tasks; new ways of working)                             |
| **Reusability**              | whether assets compound         | siloed (local prompts and scripts used by individuals)  | shared (prompts, rules, context, custom agents reused; onboarding materials updated) | codified (rules and custom agents maintained as code; automated improvement loops) |
| **AI Champions**             | who drives adoption on the team | sporadic (enthusiasts acting without a mandate)         | designated (at least one champion per team)                                          | embedded (all core roles represented; a champions network)                         |
| **Performance Tracking**     | whether adoption is measured    | partial (anecdotal evidence, no standard metrics)       | tracked (productivity metrics defined and measured consistently)                     | governed (AI cost tracked; reviews drive optimisations to output per total cost)   |
| **Daily Active Usage (DAU)** | how routine AI use is           | low (occasional use)                                    | majority (\>70% DAU)                                                                 | prevalent (\>80% DAU)                                                              |

Most projects should aim for L2. An assessment is not required at L1, but is required at L2 and L3 — the level a team claims has to be scored against the rubric with the artefacts behind it.

**Block 5 — How the team is graded**

Two models sit behind every maturity claim. The first is *what* gets scored: the four dimensions of the [AI-SDLC Maturity Framework](https://leap.epam.com/sp/ai-maturity-program/framework), each rated L1–L3. The L1→L3 bands below — including the \>80% daily-active-usage threshold — are the framework's, not numbers invented here. A maturity score is a *profile* across the four, scored at team level — not one number — and it is only honest when the artefacts behind each dimension exist.

| **Dimension**                | **What it measures**            | **L1 (At Risk)**                                        | **L2 (Baseline)**                                                                    | **L3 (Frontier)**                                                                  |
|------------------------------|---------------------------------|---------------------------------------------------------|--------------------------------------------------------------------------------------|------------------------------------------------------------------------------------|
| **AI Capabilities**          | how far AI runs the work        | assisted (deliverables made with AI help, results vary) | augmented (\>50% of core-role deliverables made and verified with AI)                | agentic (agents handle sub-tasks; new ways of working)                             |
| **Reusability**              | whether assets compound         | siloed (local prompts and scripts used by individuals)  | shared (prompts, rules, context, custom agents reused; onboarding materials updated) | codified (rules and custom agents maintained as code; automated improvement loops) |
| **AI Champions**             | who drives adoption on the team | sporadic (enthusiasts acting without a mandate)         | designated (at least one champion per team)                                          | embedded (all core roles represented; a champions network)                         |
| **Performance Tracking**     | whether adoption is measured    | partial (anecdotal evidence, no standard metrics)       | tracked (productivity metrics defined and measured consistently)                     | governed (AI cost tracked; reviews drive optimisations to output per total cost)   |
| **Daily Active Usage (DAU)** | how routine AI use is           | low (occasional use)                                    | majority (\>70% DAU)                                                                 | prevalent (\>80% DAU)                                                              |

Most projects should aim for L2. An assessment is not required at L1, but is required at L2 and L3 — the level a team claims has to be scored against the rubric with the artefacts behind it.


<!-- source: epam-ai-factory-1000_Delivery.md -->
## Block 6 — The two-way contract

L3 delivery runs both ways. The manager owes the team a maturity roadmap with named owners, adoption metrics with defined denominators, AI cost visible in the dashboard, clear escalation paths, and a named **executive sponsor** with written authority to unblock policy or budget. In return, the system needs evidence that lands in every role's own work, every sprint:

- **Carry-forwards in version control**, not personal drives — if the manager has to book time to recover context, the artefact does not exist yet.

- **Clear acceptance criteria** — testable and unambiguous; the agent that drafts the next sprint backlog relies on them.

- **Documented decisions** — a Decision Memory entry with alternatives and rationale, not "we agreed in a chat"; a scope choice cannot be defended to a sceptical stakeholder from a private conversation.

- **Honest maturity self-reports with evidence** — the framework's dimensions can only be scored if the artefacts exist; the work is the evidence.

- **Retros that produce artefacts** — a retro that ends with no written output does not compound; a bi-weekly cadence × ≥1 artefact is 26 reusable artefacts a year.

A manager cannot honestly claim L2 if no artefacts exist; a team that produces them makes the claim defensible. The contract is concrete per role:

| Your role      | What your work gives the delivery system                 | Lever it feeds         |
|----------------|----------------------------------------------------------|------------------------|
| PROD / BA      | testable acceptance criteria; documented scope decisions | Direction              |
| Design         | journey and usability requirements                       | Direction              |
| Architecture   | decision records with rationale and rejected options     | Direction / Conditions |
| Engineering    | version-controlled specs and context; PR evidence        | Conditions / Economics |
| QA             | test evidence, golden sets, coverage numbers             | Direction              |
| Data           | feature definitions; data-quality numbers                | Economics              |
| Infrastructure | gateway logs (the AI-costs source); runbooks             | Economics              |
| Security       | the scored risk register and evidence pack               | Direction              |

**Anti-Patterns**

- **The kick-off risk register.** Written in week one and never updated, with no cadence, owner, or probability score → risks surface as crises because nobody was watching. *Done right:* score probability × impact and review on a fixed cadence, with a named owner per risk.

- **RAG without a route back to green.** A red item carries a colour but no corrective action → the report records the problem and changes nothing. *Done right:* every red carries a named go-to-green action, an owner, and a date.

- **Maturity claims without artefact evidence.** "We're at L2" with nothing in version control → the claim collapses the moment a buyer asks for proof. *Done right:* cite the artefact behind each level.

- **One cadence for all stakeholders.** A single weekly email to everyone → the high-influence exec and the low-interest reviewer are both served badly. *Done right:* derive the cadence from the interest × influence map.

- **Contingency absorbed into margin.** Risk reserve and profit on one line → when a risk materialises both vanish together and neither was visible beforehand. *Done right:* keep contingency and margin as separate lines.

- **Decisions that live in chat.** Scope agreed verbally and never written down → the rationale is gone when the question resurfaces, and no record exists for anyone who was not in the room. *Done right:* capture a Decision Memory entry with alternatives and rationale.

**Outcomes**

By the end of Wide Theory you can:

1.  Name the three levers a DM/PM operates (Direction, Economics, Conditions) and the evidence each one requires.

2.  Describe the DM/PM's recurring activities and why they run every sprint rather than at project milestones.

3.  Identify the five things every role's work owes the delivery system (carry-forwards, clear acceptance criteria, documented decisions, honest maturity evidence, artefact-producing retros).

4.  Tell a measured L3 commitment from an asserted one, and name what a sceptical reviewer would attack first.
