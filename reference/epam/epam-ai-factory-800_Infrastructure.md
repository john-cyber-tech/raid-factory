# Introduction

10 minutes

**Focus:** Run and support the applications that live on your cloud platform. Infrastructure & Operations owns the substrate every released app runs on — cloud environments, containers, CI/CD, the gateway, observability — and the post-release work that keeps it healthy: incident and request management, L1–L3 support, hypercare after a launch, and the operational-improvement loop that turns each incident into a fix. AI shows up two ways here: as one more workload you host and govern — through **EPAM DIAL**, which controls model access, caps cost, and reports usage — and as agents that help you run ops, triaging incidents, auditing infrastructure-as-code, attributing cost, and drafting runbooks. L3 is operating and supporting the platform with those agents while humans write the specs, evals, and guardrails that keep them honest. **Deep for:** DevOps engineers, SREs, platform engineers, build/release engineers, support engineers. **Total time:**

- Wide path: 50 min Theory + ~90 min kata series + 60 min Final Kata ≈ 3.3h (plus 120 min Wide Practical for portfolio carry-forward)

- Deep path (own role): + 240 min Theory + ~180 min kata series ≈ +7h (Final Kata is universal — done once)

**Objectives**

- **Learn to do:** stand up and operate an application on a cloud platform — produce a deployment manifest and a CI/CD workflow (each audited in a fresh session), diagnose a production incident and draft its runbook, estimate the monthly cloud + AI (DIAL-capped) cost, and place the team on the EPAM maturity ladder (Wide); ship six runnable ops-agent specs (autoscaler, DIAL cost-guardian, observability-synthesis, SLO-advisor, incident-and-support commander, patch-and-release) with kill-switches, bounds, and falsifiable evals (Deep).

- **Skills (role):** deploy, run, and ship changes to an app on cloud infrastructure through an audited CI/CD pipeline; diagnose and support a released app across the L1–L3 tiers; attribute and cap cost across cloud and AI (the latter at the gateway); score a team on the EPAM maturity ladder.

- **Skills (tooling):** agentic dev tools (Claude Code / Cursor / Copilot, CodeMie); IaC scanners (Checkov / Trivy / kube-score); the AI gateway (EPAM DIAL / LiteLLM); autoscaling (KEDA); observability (Grafana / OpenTelemetry) (Deep).

- **Outcome:** a Cloud Operations & Support Pack (Wide); the six ops-agent specs (Deep); an Ops role-agent spec (Final Kata).

- **Tested by:** the Wide kata chain K 8.W.1–6 + the Final Kata K 8.3; the Deep path adds K 8.D.1–6.

# Role Context

**1 — Role names and who they apply to**

This module covers anyone who owns the cloud platform that released applications run on, and anyone who keeps those applications healthy after launch. Common job titles:

- **DevOps engineer** — owns the build/deploy pipeline and the cloud substrate beneath it.

- **Site Reliability Engineer (SRE)** — owns runtime reliability, SLOs, incident response, and the toil ceiling.

- **Platform engineer** — owns the internal developer platform: paved roads, golden paths, the shared gateway, and the artefact registry.

- **Build/release engineer** — owns the CI/CD topology, the release bundle, and the promotion gates.

- **Support engineer** — owns post-release support: incident and request handling across the L1–L3 tiers, hypercare, and the support knowledge base.

Common synonyms: Cloud Engineer · Production Engineer · Reliability Engineer · Infrastructure Engineer · Release Manager · DevSecOps Engineer · Internal Platform Lead · Service Desk Engineer · Application Support Analyst. If your title varies, the test is functional: do you own the *substrate* (clusters, pipelines, gateway, observability, IaC modules, runbooks) that other teams' code runs on, or do you keep a released app running and answer for it when it breaks? If yes, this module covers you.

**Support tiers (L1 / L1.5 / L2 / L3).** Post-release support is organised in tiers, and they recur across this module. **L1** is the first line — takes the ticket, follows the playbook, resolves the known cases. **L1.5** is enriched first line — runs deeper diagnostics scripts before escalating. **L2** owns application-level investigation — reads logs, reproduces the issue, applies a documented fix. **L3** is the engineering tier — the people who change the code or the platform when no playbook covers the problem. *(Do not confuse these support tiers with the L1/L2/L3 maturity levels the EPAM AI SDLC ladder uses — same letters, different axis.)*

A note on *AIOps*. The term is sometimes confused with *"DevOps for AI."* It isn't. **AIOps** is an industry term for *AI applied to IT Operations* — anomaly detection, root-cause analysis, event correlation, predictive capacity, automated remediation. Some of those patterns appear later in this module, but the module is not *about* AIOps as a category. It is about running and supporting cloud-hosted applications at L3 using agents as a first-class tool. If your team uses a commercial AIOps platform (PagerDuty AIOps, BigPanda, Moogsoft), treat it as one of several agent surfaces — not as the framing of your job.

**2 — Role description and core duties**

The platform/ops specialist owns the cloud platform and the released app on it, end-to-end. In observable verbs:

- **Provisions** the substrate (compute, network, storage, identity, secrets) and the higher-level platforms on top (Kubernetes, CI/CD, the gateway, the observability stack).

- **Authors and reviews** Infrastructure-as-Code, pipeline definitions, dashboard configs, and runbooks — *increasingly via agents whose work the platform engineer specs, reviews, and gates*.

- **Operates** the platform: capacity, scaling, on-call response, incident command, postmortems, the burn-rate ladder.

- **Supports the released app** — handles incidents and requests across the L1–L3 tiers, runs hypercare after a launch, keeps the support knowledge base current, and feeds each incident back into an operational-improvement backlog.

- **Attributes and bounds cost** across teams, features, and request classes — cloud spend and AI spend alike, enforcing AI budgets.

- **Ships agents that do ops work** — autoscaling advisors, cost guardians, observability synthesisers, SLO advisors, incident-and-support commanders, patch+release agents — with kill-switches, audit trails, and falsifiable evals.

What this role does *not* own at L3: writing the application code, deciding whether an AI feature's *behaviour* is acceptable (Product and the building roles), threat-modelling the platform from a security perspective (the Security module), or owning the cost narrative for management (the Delivery & Project Management module). The platform produces the artefacts those downstream roles consume.

**3 — Main processes**

The recurring workflows this role runs:

- **Environment & platform setup** — provisioning clusters, namespaces, node pools, gateways; authoring Helm charts, K8s manifests, Terraform modules, Dockerfiles; reviewing the same when agents draft them.

- **Pipeline authoring and review** — GitHub Actions / GitLab CI workflow drafting, gate definition (test, security scan, bundle check), supply-chain controls.

- **Capacity & cost management** — sizing for steady-state and burst, attribution by team/feature/request class, soft/hard-limit enforcement — cloud cost on the bill and AI cost at the DIAL gateway.

- **Observability & incident response** — the three classical pillars (metrics, logs, traces); SLOs and burn-rate alerts; on-call rotation; runbook authoring; postmortems.

- **Post-release support** — incident and request management across the L1–L3 tiers, hypercare immediately after a launch, support handover from delivery to operations, and keeping user guides and support playbooks current.

- **Operational improvement** — turning each incident into a reliability-backlog item, identifying automation opportunities, and reporting service-management metrics.

- **Release & lifecycle** — build-artefact and config-bundle assembly, promotion gates, deprecation, rollback.

- **Agent platform operations** — running the platform's own AI agents (autoscaler, DIAL cost guardian, observability synthesiser, incident-and-support commander, patch+release) and the evals/guardrails that keep them safe.

- **Toil reduction** — every quarter, picking three repetitive operations and either eliminating them or wrapping them in a small skill/agent the team can invoke on demand.

**4 — Role in SDLC**

In the pre-AI SDLC, infrastructure & operations sat at the *end* of the pipeline — *deploy*, *run*, *page when broken*. The role received built artefacts from Engineering, deployment requests from Release Management, and incident escalations from QA or Support. It handed off SLO reports and post-incident reviews to Management.

In the AI-augmented SDLC, the role's surface area shifts in two directions. *Earlier* — because IaC, pipelines, and dashboards are now drafted by agents inside the same loop as application code, the platform team reviews and gates agent output continuously, not at deploy alone. *Later* — because the heaviest part of the job lives after release: incident and request handling across the support tiers, hypercare on a fresh launch, cost attribution, and the operational-improvement loop that turns each incident into a backlog item. Where the app embeds an AI feature, the platform also watches its cost and behaviour through the gateway — one more workload to govern, not a separate discipline.

**5 — How the role changed with AI (general)**

AI changed three things about platform/ops work simultaneously. **Agents now draft the artefacts.** Helm charts, Terraform modules, GitHub Actions workflows, runbooks, dashboards, postmortem skeletons — all are drafted by agents in PRs that look like any other change. **Agents now do the diagnosis.** In-cluster diagnostic agents (k8sgpt, HolmesGPT, vendor copilots like Datadog Bits AI SRE) can correlate alerts, summarise logs, and rank hypotheses faster than a human at 02:00. **Agents now run continuously inside the platform.** Autoscaling decisions, cost guardrails, log summarisation, conversational infrastructure ("talk to your infrastructure") — these are agent surfaces the platform team operates, not features the platform team consumes from elsewhere.

What disappeared: the assumption that *plausible-looking output is safe output*. What's amplified: the value of policy-as-code, fresh-session adversarial review, kill-switches, and audit trails. What's automated: the first three minutes of triage, the first draft of every runbook, the impact analysis on every IaC PR.

**6 — What changed at L2 (AI-assistant)**

At L2, the platform engineer still owns every artefact end-to-end; AI is a copilot. The agent drafts the Terraform, but the human reads every line, runs terraform plan, gates apply behind a code review. The agent suggests a kubectl next step during an incident, but the human decides whether to execute it. The agent summarises a postmortem, but the human signs the published version.

Concrete L2 tasks where AI assists:

- Drafting Helm charts, K8s manifests, Terraform modules, Dockerfiles from a brief.

- Reviewing IaC for misconfigurations and missing labels.

- Generating PromQL queries, Grafana dashboard JSON, alerting rules from a description.

- Summarising a long incident timeline into a postmortem first draft.

- Proposing the next kubectl describe / kubectl logs command during triage.

- Estimating per-month cost from an IaC diff.

What stays human at L2: every terraform apply, every gateway policy change, every SLO redefinition, every rollback decision, every alert that pages on-call.

**7 — What changed at L3 (AI-native)**

At L3, the work is restructured around agents. The platform engineer becomes the *agent specifier* and *agent reviewer* for the operations surface. The agents themselves do the routine work:

- An **autoscaling-decision agent** reads load signals (queue depth, CPU/memory, request latency, and — for an AI workload — token throughput), proposes scaling actions, and applies them within bounds the engineer set.

- A **DIAL cost-guardian agent** attributes AI spend per team and feature at the gateway, enforces soft/hard limits, and pages the budget owner before the invoice arrives.

- An **observability-synthesis agent** correlates metrics, logs, and traces across signals — and surfaces a regression quietly before it becomes an outage.

- An **SLO advisor agent** drafts SLI/SLO tables, burn-rate ladders, and alert rules from the service spec.

- An **incident-and-support commander agent** is the first responder: read-only, ranks hypotheses, drafts a runbook and an L1–L3 support note, hands off to a human when confidence drops below threshold.

- A **patch+release agent** reads release notes, greps call sites, drafts the migration PR, assembles the release bundle (build artefact + config + changelog), and writes the release note under a grounding contract.

The human role at L3 is to:

- **Specify** each agent — its system prompt, its tools, its inputs and outputs, its guardrails, its evals.

- **Review** what the agents draft. A rubber-stamp on agent output recreates every failure mode the platform exists to prevent.

- **Govern** the agent fleet — kill-switches, audit trails, scoped service accounts, fresh-session adversarial review, drift detection on the agents' own decisions.

- **Decide** the things the agents must not — what gets a hard rollback, when to declare an incident, when an SLO needs re-negotiating, when to deprecate a model in production.

The platform engineer at L3 ships *agents* as a primary deliverable, not Terraform alone.

# Carry-Forward

Two artefacts leave this module: the operations work (Wide pack + Deep agent specs) and the Ops role-agent.

**1 — Cloud Operations & Support Pack (+ ops-agent specs)**

- **Artefact name:** Cloud Operations & Support Pack (Wide), plus the six ops-agent specs (Deep).

- **Source:** the Wide series (artefacts/800-wide/01-stack-map.md → 06-readiness-brief.md — a cloud stack/ownership map, a deployment manifest with a fresh-session audit, a CI/CD workflow with a supply-chain audit, an incident diagnosis with a drafted runbook, a monthly cloud + AI cost estimate, and a readiness-and-support readout) for all learners; extended by the Deep series into six ops-agent specs (autoscaler, DIAL cost-guardian, observability-synthesis, SLO-advisor, incident-and-support commander, patch-and-release, each with kill-switch and bounds) for specialists. Produced on the learner's chosen Reference Case (their live engagement, else Case A or Case B), used consistently across every kata.

- **Consuming stage(s):**

  - **Security** — threat-models the Operations & Support Pack and the ops-agent specs; the pack's deployment manifest, CI controls, and gateway configuration feed the threat model and the audit trail.

  - **Delivery & Project Management** — the pack's cost estimate and readiness readout roll up into delivery dashboards and FinOps reporting; the maturity scorecard feeds the adoption plan.

  - **Final Assembly Line** — the ops-agent specs are how the multi-role agentic workflow runs in practice — the gateway, the monitors, and the agents that operate and support them.

- **Format:** A version-controlled directory: the Wide pack (artefacts/800-wide/06-readiness-brief.md and the 01–05 artefacts behind it) and the Deep ops-agent specs.

**2 — Ops Role-Agent Spec**

- **Artefact name:** Role-Agent Spec.

- **Source:** Final Kata K 8.3 (all learners; specialists add the depth-add sections).

- **Consuming stage(s):** **the downstream roles (Security, Delivery & Project Management)** load .claude/skills/ops/ or .claude/agents/ops.md when no platform engineer is on the team — read in place for operational context, not transformed. **Final Assembly Line** lists it in the agent roster a joining teammate reads.

- **Format:** a runnable Claude Skill or sub-agent, ≤ 2 pages of body, with the guardrails (human-owned decisions) inline.

- **Engine guide target:** .ai-run/guides/quality-gates.md, under header \## Runner/env configuration + ops bounds (from Module 800 — Infrastructure & Operations). This is the authoritative chain mapping; the spec's \<!-- chain:rules:start guide=… topic=… --\> delimiter attributes mirror it, and on any disagreement this line wins.

- **Optional stand-in override (Deep only):** none.

#### Wide Theory

**Not Started**

50 minutes

**Why This Matters for You**

Two teams ship the same application to the cloud in the same week — a customer-facing web service, a few containers behind a load balancer, a database, and one AI call for a "summarise this for me" button. Same code, same cloud account, same demo that made the room clap. What happens next is decided not by the code but by whether anyone *operates and supports* it after launch.

Thirty days later they are in very different rooms.

Team A treated "it deploys" as done. With no on-call rotation, the first production incident surfaced on Twitter, from a customer, not an alert. With no runbook, the one engineer who knew the deploy steps spent a Saturday rebuilding them from memory. With no rollback path, a bad release stayed live for three hours while someone hot-fixed forward. And with no cap on the AI call, a loop in a new feature quietly ran the model bill to **\$18,000** before the monthly invoice revealed it. Every dashboard stayed green the whole time — they were answering "is the server up?", and it was.

Team B treated launch as the *start* of the work. They shipped through a pipeline that could roll back in one click. They put the service on-call with a runbook for the top five failures, and a support flow that took a customer ticket from a first-line agent to an engineer only when it actually needed code. They routed the AI call through the company gateway with a hard cost cap, so spend was a number they chose, not one they discovered. When a dependency slowed down on day two, the alert fired before the customer did, the first-line agent followed the playbook, and the issue closed without paging anyone at 2 a.m.

The difference was not the cloud provider or the framework. It was whether anyone **ran and supported** the application after it shipped.

That is the job of Infrastructure & Operations: get the app onto the cloud floor, keep it running and cheap, and support it — diagnose, fix, and improve — after the applause stops. You are almost certainly not going to *become* that person. This 50 minutes gives you the vocabulary and the questions to do meaningful operations thinking on an application your team runs — to read where it lives, judge what it costs and how it is supported, and place your team on the maturity ladder — **without taking a specialist's word for any of it**.

**﻿  
**

**Goal**

After this Wide Theory you can read the cloud platform an application runs on, describe how it gets deployed and rolled back, estimate what it costs to operate (cloud plus any AI calls), name how it is supported after release across the L1–L3 tiers, and score your team against the EPAM AI SDLC Maturity ladder.

﻿

**Time**

~50 min.

﻿

**Audience**

Everyone. No infrastructure background assumed.

﻿

**Prerequisites**

Foundations (010, 020). Helpful but not required: any module where you have seen software specified, built, or released (200, 400, 500).

**﻿  
**

**Must Cover**

**An application isn't finished when it ships — that's when its cost, its risk, and its support burden begin.** Operations is the discipline of getting it onto the cloud, keeping it cheap and recoverable, and supporting it after launch.

The one question to keep after you forget everything else, asked of any application your team runs:

*Where does it run, what does it cost, what stops it when it breaks, and who supports it after release?*

**This section covers:**

- **What Infrastructure & Operations owns** — the cloud substrate an app runs on, and the after-release support that keeps it alive.

- **Getting a released app onto the floor** — containers, the deployment manifest, the CI/CD pipeline, and the one-click rollback.

- **What it costs to run** — cloud rent plus metered AI calls, and cost as a capped signal at the gateway.

- **What stops it when it fails** — the seven runtime guardrails and the observability that catches a failure before a customer does.

- **Supporting it after release** — incident and request management across the L1–L3 tiers, hypercare, and the operational-improvement loop.

- **Where your team stands** — the EPAM AI SDLC Maturity ladder through the operations lens.

**Terms used in this section**

A non-specialist meets these words the moment they talk to a platform or support team. One line each — enough to read the rest, not to operate.

<img src="media/image1.png" style="width:5.64612in;height:5.81974in" />

**Key Messages / Ideas**

- An application isn't finished when it ships — shipping is where its cost, its risk, and its support burden begin. Operations gets it onto the cloud, keeps it cheap and recoverable, and supports it after launch.

- "It works on my machine" and "it is deployed, monitored, and rollback-able" are different claims; the pipeline and the rollback path are what make a release safe and reversible.

- Cloud cost is rent plus an AI meter; one gateway turns the AI part from a per-invoice surprise into a per-request signal you can cap and attribute.

- A green "is it up?" dashboard misses cost runaway and silent wrongness; the gateway adds the per-request cost and response signals the classical three lack.

- Post-release support runs in tiers (L1–L3); the cheap teams catch problems early, feed the operational-improvement loop, and let agents handle the known cases.

- The maturity ladder rewards governed cost tracking, agentic ops and support, and codified runbooks — not the ability to deploy a container.

**Structure (Per-topic context blocks)**

The six topics below build the read in order — what the role owns, how an app gets deployed, what it costs, what stops it failing, how it is supported after release, and where the team stands on the maturity ladder.

# Block 1 — What Infrastructure & Operations owns

**Mental model: the cloud floor, and who keeps it open.** Every other role in this course produces something — a spec, a design, code, a dataset. Operations owns the *floor* it all runs on: the cloud machines, the assembly line that ships changes, the front door for AI calls, the instruments on the wall — and the support desk that answers when the running app misbehaves. When a BA's user story becomes running software a customer touches, it is running on this floor, and someone is on call for it.

Across the SDLC the role sits at deploy-and-after: it receives built artefacts from Engineering and owns everything after — running them, paying for them, and answering the phone when they break. The recurring work: **provision** the floor (cloud compute, the cluster, the gateway), **ship** changes through the pipeline, **operate** what is running (capacity, scaling, on-call), **support** the released app across the tiers, **attribute and cap cost**, and **keep the instruments honest** so a failure is seen before a customer sees it.

<img src="media/image2.png" style="width:6.26806in;height:2.36458in" />

**Why you care.** When you promise a stakeholder an app "ships next sprint," the floor is what decides whether that promise survives contact with production — and the running cost, the failure surface, and the support load that promise creates are owned here, not in your spec.

**Where you still own the call.** What the app is *for*, and whether its behaviour is acceptable, stays with you and Product. Operations keeps it alive and supported; it does not decide it was worth building.

🏛️**EPAM perspective.** When the app calls an AI model, the front door in this picture is **DIAL** — EPAM's open-source, vendor-agnostic AI gateway. Every model call routes through it, so cost attribution, per-team limits, and the prompt-and-response audit trail live on one governed surface instead of scattered across direct API keys. It turns "what did this feature cost?" from a month-end surprise into a live number, and "who is allowed to call which model?" from an honour system into policy. EPAM staff use it at [chat.lab.epam.com](https://chat.lab.epam.com/).

🔍**Check your thinking.** For an app your team ships, name one thing on the floor you depend on but do not own. (If you can't, that is the gap to close this week.)

# Block 2 — Getting a released app onto the floor

**Mental model: an assembly line, not a hand-carry.** At L0 someone copies files onto a server and restarts it by hand. Every step that an operations team adds turns that hand-carry into a repeatable assembly line — so the same change ships the same way every time, and an unsafe one is caught before it reaches a customer.

Four things turn code into a running, recoverable service:

- **A container** packages the app with everything it needs, so it runs the same on a laptop, in CI, and in production. No more "works on my machine."

- **A deployment manifest** (a Kubernetes/Helm file or a Terraform module) declares *what* should be running — how many copies, how much memory, which secrets, which health check — as code in version control, not clicks in a console.

- **A CI/CD pipeline** carries each commit through build → test → security scan → deploy, with gates that fail the change rather than the customer. The supply-chain controls (signed images, pinned dependencies, provenance) live here.

- **A rollback path** puts the last known-good version back in one step. A team without one fixes forward under pressure at the worst possible time.

<img src="media/image3.png" style="width:6.26806in;height:2.075in" />

A non-specialist does not author the manifest. You need to recognise that "it works on my machine" and "it is deployed, monitored, and rollback-able" are different claims — and to ask which one is true before you promise a date.

**Where you still own the call.** *When* to release — the go/no-go against business risk — is a Product and Delivery decision. Operations builds the line that makes the release safe and reversible; it does not decide the calendar.

🔍**Check your thinking.** For the last thing your team shipped: could it be rolled back in one step, or would a bad release have to be fixed forward? (If you don't know, that is the readiness question to ask.)

# Block 3 — What it costs to run

**Mental model: rent plus a taxi meter.** Cloud cost has two shapes. Most of it is **rent** — compute, storage, and network you pay for by the hour whether busy or idle, roughly flat. The AI part is a **meter** — you pay per **token** in and per token out, on every single call, so it scales with usage. A non-specialist who can separate these two reads a cost surprise correctly: a flat overspend is usually rightsizing; a spiking one is usually the meter.

You can roughly estimate a running cost from a few numbers:

- **Cloud rent** — the count and size of always-on resources (compute instances or pods, the database, storage, the load balancer) times their hourly price. This is the steady-state floor.

- **AI calls per month** — driven by traffic and how often the feature fires — times the **tokens per call** (system prompt + user input + anything retrieved + the answer) times the **price per million tokens** from the provider's published list. Retrieval is the sneaky multiplier: four documents stuffed into a prompt can dwarf the user's actual question.

- **Multipliers** — retries, autoscaling headroom, and traffic spikes.

Worked example: a service on a small cluster might cost ~\$1,500/month in cloud rent — predictable. Add an AI summarise-button at ~1,200 tokens/call × 3,000,000 calls/month × \$2.50 per million ≈ **\$9,000** in AI alone, and now the meter dominates the bill. Numbers that *feel* small hide here because each call costs a fraction of a cent — until you multiply by the traffic.

**The gateway turns AI cost from a surprise into a signal.** When every model call routes through one gateway (i.e. DIAL), spend is attributed to a team and a feature *as it happens*, and a cap can refuse a call that would breach the budget instead of letting the meter run. A \$18,000 month-end surprise becomes a daily line you watch and a limit you set — and the usage analytics tell you which feature, and which team, is spending it.

<img src="media/image4.png" style="width:6.26806in;height:2.41944in" />

# Block 4 — What stops it when it fails

**Mental model: a circuit breaker in your house.** You do not prevent every electrical fault; you install a breaker that trips before a fault burns the house down. A running service — and any agent or AI call inside it — needs the same bounded, automatic safety, because an unbounded retry against a slow dependency will hammer it forever and spend real money doing it.

The seven guardrails a platform team puts around a service or an AI call. You do not configure these — you check they exist:

<img src="media/image5.png" style="width:5.6739in;height:3.10433in" />

The kill-switch is the one every non-specialist should ask about by name. "Someone manually kills the pod" is a runbook step, not a kill-switch.

<img src="media/image6.png" style="width:6.26806in;height:2.99236in" />

**The green dashboard misses what matters.** A platform watches three classical signals: **metrics** (numbers over time), **logs** (what happened), **traces** (the path of one request). All three can be green while the thing customers care about is broken — the server is up, but the feature returns nonsense, or the bill is tripling, or a 3%-of-sessions defect is hurting people who never file a ticket. Two failures hide behind a healthy uptime number especially well: **cost runaway** (nothing is "down" except the budget) and **silent wrongness** (the answer arrives, fast and confidently, and is wrong). When the app calls an AI model, the gateway adds the signal the classical three lack — **per-request cost and the model's actual responses** — so "is it right?" and "what does it cost?" become answerable, not guessed.

**Where you still own the call.** What the fallback *says* to the user, and what threshold should trip the kill-switch, are Product and domain calls — operations builds the switch, you decide when it should fire.

🔍**Check your thinking.** Of the seven guardrails, which one ends a "retrying a slow dependency forever" incident fastest? (The circuit breaker stops the hammering; the retry cap and time budget bound a single run.)

# Block 5 — Supporting it after release

**Mental model: a triage desk, not a fire brigade.** A released app generates a steady stream of incidents (something broke) and requests (someone needs something). Handling each one by paging an engineer does not scale and burns out the team. Post-release support is the discipline of catching that stream at the right tier and only escalating what genuinely needs code.

The support tiers, from cheapest to most expensive to involve:

- **L1 — first line.** Takes the ticket, follows the playbook, resolves the known cases (password resets, known errors with known fixes). Most volume ends here.

- **L1.5 — enriched first line.** Runs deeper diagnostic scripts and checks before escalating, so L2 only sees what truly needs investigation.

- **L2 — application support.** Reads logs, reproduces the issue, applies a documented fix or configuration change. Owns the known-error database.

- **L3 — engineering.** The people who change the code or the platform when no playbook covers the problem. The most expensive tier — you want as little reaching it as possible.

<img src="media/image7.png" style="width:6.26806in;height:2.64514in" />

Two practices make support more than a complaints queue:

- **Hypercare** — a short, intense window of heightened support right after a launch or major release, when the team watches closely, responds fast, and feeds what they learn straight into runbooks. It is how a risky launch lands without a 2 a.m. surprise.

- **The operational-improvement loop** — every recurring incident becomes a backlog item (a fix, an automation, a new playbook, a better alert) so the same problem does not pay full price twice. A team that closes tickets but never feeds this loop will answer the same question forever.

This is exactly where AI agents earn their place at L3: an agent drafts the support note from the ticket and the logs, proposes the L1 playbook entry, and ranks the likely causes — so the human spends their time on the genuinely new problem, not the fortieth instance of a known one. The same versioned-asset shift the maturity ladder calls **Codified** applies here: when runbooks, playbooks, and known-error entries live in version control instead of one senior engineer's head, anyone — and any agent — can read and reuse them.

**Where you still own the call.** What counts as an acceptable customer experience, and which incidents are severe enough to halt a release, are Product and Delivery calls. Operations runs the desk; it does not set the business's tolerance.

🔍**Check your thinking.** For your app's most common support ticket, which tier should resolve it — and which tier resolves it today? (The gap between those two is your support-cost problem.)

# Block 6 — Where your team stands: the maturity ladder

The EPAM AI SDLC Maturity framework scores a team on five dimensions, each from L1 to L3. Operations is the role that makes the top of two of them real:

<img src="media/image8.png" style="width:5.65307in;height:3.44462in" />

<img src="media/image9.png" style="width:6.26806in;height:2.7625in" />

A real cloud deploy moves a team on **none** of these — the framework measures AI *adoption*, not whether you can click a console or stand up a cluster. What moves the needle is the cost tracking, the agentic ops and support, and the codified runbooks. That is why, for a non-specialist, the useful skill is not deploying infrastructure; it is reading an app's cost, risk, and support posture and placing the team honestly on this ladder.

**The reader sees themselves.** Whatever your role, you take one question to the platform or support team:

<img src="media/image10.png" style="width:5.52112in;height:2.21539in" />

# Anti-Patterns

- **Deploy-done** — *Wrongdoing:* treating "it deploys" as shipped. *Cost:* no on-call, no runbook, no rollback — the first incident is found by a customer. *Done right:* answer the readiness questions — how it deploys and rolls back, who's on call, what's monitored, who supports it — before launch.

- **Green-dashboard trust** — *Wrongdoing:* reading 200 OK and uptime as "the app is healthy." *Cost:* the bill triples or the feature returns nonsense and no alert fires. *Done right:* ask for the cost and response signals — through the gateway for AI calls — on top of the classical three.

- **Cost-by-invoice** — *Wrongdoing:* discovering an app's AI cost when the bill arrives. *Cost:* a month of unbounded spend and no one accountable. *Done right:* estimate before launch; route model calls through the gateway so cost is a live, capped, attributed signal.

- **Page-the-engineer-for-everything** — *Wrongdoing:* sending every ticket straight to L3. *Cost:* burnout, slow resolution, and the same question answered forever. *Done right:* tier the support, write the L1 playbook, and feed each recurring incident into the operational-improvement loop.

- **Deploy-equals-mature** — *Wrongdoing:* believing standing up cloud infra raises the team's maturity score. *Cost:* effort spent on the wrong dimension. *Done right:* invest in cost tracking, agentic ops and support, and codified runbooks — what the ladder actually measures.

# Outcomes

After this Wide Theory you can:

- Read the cloud platform an application runs on and name which parts the operations team owns.

- Describe how a release reaches production and gets rolled back, and tell "works on my machine" from "deployed, monitored, recoverable."

- Estimate an app's monthly running cost — cloud rent plus metered AI calls — and explain where a cap belongs.

- Name how an app is supported after release across the L1–L3 tiers, and what the operational-improvement loop is for.

- Score a team against the five dimensions of the EPAM AI SDLC Maturity framework and name the operations gap.

<img src="media/image11.png" style="width:6.26806in;height:2.47986in" />

# Required Materials

- The cloud-floor mental model and the deploy assembly line (container → deployment manifest → CI/CD pipeline → one-click rollback) — the wide theory file.

- The support tiers (L1 · L1.5 · L2 · L3) and the post-release support loop (incident & request management · hypercare · operational improvement) — the wide and deep theory files.

- The seven runtime bounds vocabulary (time budget · cost cap · retry cap · checkpointing · fallback · circuit breaker · kill-switch).

- The three classical observability signals (metrics · logs · traces), plus the per-request cost and response signals the gateway adds for an AI workload.

- **EPAM AI DIAL** — the open-source, vendor-agnostic AI gateway: access control, per-team cost caps, and usage analytics for LLMs and agents ([dialx.ai](https://dialx.ai/); EPAM staff at [chat.lab.epam.com](https://chat.lab.epam.com/)). Built on in Wide Kata 8.W.5 (cost) and Deep Kata 8.D.2 (cost-guardian).

- The **EPAM AI SDLC Maturity framework** — the five dimensions (AI Capabilities · Reusability · AI Champions · Performance Tracking · Daily Active Users) scored L1–L3 — on [EPAM LEAP](https://leap.epam.com/sp/ai-maturity-program/framework). Assessed in the readiness brief (Wide Kata 8.W.6).

- The running-cost estimation method (Wide Kata 8.W.5) — cloud rent plus tokens/call × calls/month × published per-million price.

- The four-artefact release bundle definition (model snapshot + prompt version + retrieval index version + eval-suite version) — for the Deep release-lifecycle topic.

- The Honest README template — what an artefact *does*, *doesn't*, and *would need* to harden.

# Internal Knowledge

- Your team's allow-list of agentic dev tools (Claude Code, Cursor, GitHub Copilot, EPAM DIAL — whichever your project has approved). EPAM DIAL is the EPAM-owned general-AI gateway used as the first AI option for gateway routing, cost attribution, and observability work in this module's katas; confirm allow-list status against your data-class matrix before pasting any non-public material.

- The data-classification rule for AI surfaces — per EPAM's *Acceptable use of AI at EPAM* guidelines, DIAL is approved for public and generally-available-confidential EPAM data; strictly confidential data and PII require approval, and client data requires the MSA/SOW to permit AI plus formal client approval.

- Reference IaC seed repos for the running case (the mrg-platform and mrg-infra-seed repos) — used in the **Deep** kata series. The Wide series needs no repo, cloud account, or container runtime; it runs on your AI surface plus a text editor.

🏛️**EPAM perspective.** [EPAM DIAL](https://chat.lab.epam.com/) is EPAM's open-source, vendor-agnostic AI gateway (EPAM staff sign in at chat.lab.epam.com); it is the first-choice AI surface for the gateway-routing, cost-cap, and observability katas in this module, and the place your model-tier routing and audit trail can live.

# External References (Optional)

- [Google SRE Book / Workbook](https://sre.google/books/) — canonical SLO, error-budget, alerting-on-SLOs material.

- [DORA Four Keys](https://dora.dev/) — delivery health metrics.

- [OpenGitOps](https://opengitops.dev/) — the four GitOps principles.

- [The Twelve-Factor App](https://12factor.net/) — the baseline for an app that runs cleanly on a cloud platform.

- [Google SRE — Managing Incidents](https://sre.google/sre-book/managing-incidents/) — incident, request, and post-release support practice (the L1–L3 escalation, runbooks, hypercare).

- [DIAL documentation](https://docs.dialx.ai/) — the EPAM open-source AI gateway: access control, cost limits, usage analytics, and provider routing.

- [OpenTelemetry](https://opentelemetry.io/docs/) — the metrics/logs/traces instrumentation contract (incl. the [GenAI semantic conventions](https://opentelemetry.io/docs/specs/semconv/gen-ai/) for an AI workload).

- [LiteLLM](https://docs.litellm.ai/), [KEDA](https://keda.sh/), [Grafana](https://grafana.com/docs/) — the OSS surfaces the **Deep** kata series exercises (a local gateway stand-in, autoscaling, dashboards).

- [OpenAI pricing](https://openai.com/api/pricing) · [Anthropic pricing](https://claude.com/pricing) — published price lists for the Wide cost kata (8.W.5). Free, no account.

- [Podman](https://podman.io/) — open-source, commercial-use-free container engine (the Docker Desktop alternative, which is paid at EPAM's size); used only in the optional Wide "see it run" appendix.

- [Google Cloud Shell](https://docs.cloud.google.com/shell/docs), [GitHub Codespaces](https://github.com/features/codespaces) — no-account, no-credit-card, ephemeral sandboxes for that optional appendix.

# Reference Cases and task menu

**Pick one subject and stay on it across every kata and the Final Kata** — the carry-forward chain only works if your artefacts compound on the same project. **First choice is always your own current project.** Otherwise pick a standard reference case — **Case A (Meridian Retail Group / MRG)** or **Case B (Kepler Insurance)**. The katas are written to run on whichever you pick; the worked examples throughout this module use Case A (MRG) as the illustration, so substitute your own service names if you are on your project or Case B.

- **Case A — Omnichannel Commerce Platform for a Global Retailer (Meridian Retail Group / MRG).** *The illustration this module's worked examples use.* A 22-country headless commerce build (commercetools, Apollo GraphQL, EKS, Kafka, Next.js, React Native) with a strangler-fig rollout against a legacy SAP ERP and six regional CRMs. The katas use the MRG cart-api / recommendation-api / support.ticket-summary services. Best when your project resembles a high-traffic, multi-region, customer-facing platform with a mix of services and AI features at checkout, search, and support.

- **Case B — Cloud-to-Cloud Migration of 50 Legacy Applications.** *Acceptable alternative for regulated-migration-shaped projects.* A regulated-industry migration with claims-processing SLOs, SOX-audit trail requirements, compliance governance, and observability gaps post-cutover — a fit for ops/SRE work on a heterogeneous estate: capacity planning under SLA pressure, IaC across many services, and agent-assisted patching.

Full case details (scenario, stakeholders, scope, constraints, sample inputs): reference-cases.md.

**Role-specific task menu**

When a kata asks you to "name a real, recurring task," pick from this menu — these are tasks the Infrastructure & Operations role would actually handle on each case.

**Case A — recurring tasks for this role:**

- Author the Helm chart and cart-api Kubernetes manifests for one Phase 1 microservice, with cost-attribution labels.

- Draft the GitHub Actions workflow that builds, scans, and signs the cart-api image, then promotes it to staging.

- Configure the EPAM DIAL / LiteLLM gateway for the AI recommendations feature (model tier per squad, soft/hard cost caps, usage analytics, audit trail).

- Wire the three observability signals (metrics, logs, traces) for cart-api into the platform Grafana, with one SLO burn-rate alert.

- Define the L1–L3 support tiers and the first-line playbook for the top two cart-api ticket types, and set the hypercare window for the next release.

- Stand up the autoscaling-decision agent for the recommendation-api against load signals (queue depth, latency, token throughput).

- Run a tabletop drill on the *latency spike* runbook with the incident-and-support commander agent as first responder, ending in an L1 support note.

**Case B — recurring tasks for this role:**

- Inventory the IaC across 50 legacy apps and produce the migration prioritisation matrix (an agent reads the seed repos and proposes the order).

- Draft and review the per-app Terraform plan for cutover, with moved blocks and a clean plan diff.

- Define the SLO + burn-rate ladder for the claims-processing service post-cutover.

- Stand up the cost-guardian agent across the 50-app estate with per-team attribution.

- Stand up the patch+release agent that reads release notes, greps call sites, and drafts the migration PR for breaking dependency bumps.

- Run a tabletop drill on the *post-cutover observability gap* runbook with the observability-synthesis agent acting as first responder.

# Wide kata series (all learners)

**Not Started**

3 minutes

Six katas, ~15 min each, ~90 min total. None requires a cloud account, a credit card, Docker, or kubectl — only the AI surface you already have (EPAM DIAL / CodeMie / your one agentic dev tool), a published price list, and a text editor. You read one cloud-hosted app like an operator: map where it runs, generate and audit its deployment manifest and pipeline, diagnose an incident and write its runbook, cost it for a month, and assemble a one-page readiness brief the security and delivery teams downstream can act on.

*﻿  
*

*Goal:* produce a **Cloud Operations & Support Pack** for one service your team runs — a cloud stack/ownership map, a deployment manifest with a fresh-session audit, a CI/CD workflow with a supply-chain audit, an incident diagnosis with a drafted runbook, a monthly cloud + AI cost estimate, and a one-page readiness-and-support readout.

*﻿  
*

*Persona:* non-role-learner — a reader with no platform or operations role, who has shipped or specified software and used an AI tool, but has never read an app from the operations side.

*﻿  
*

*Superpower moment:* "I can take any app my team runs and say where it lives, how it deploys and rolls back, what it costs, how it fails, and how it's supported after release — and write the one-page brief that proves it's ready."

*﻿  
*

*Reference case:* **Pick one and stay on it across all six katas.**

- **Your own project** (best, highest-signal) — one service your team runs and supports. Use this whenever you can; an NDA that blocks committing artefacts to a shared repo is the only reason to fall back.

- ﻿[**Case A — Meridian Retail Group**](https://eu.git.epam.com/airun-mission-26-ai-factory/curriculum/-/blob/main/modules/001-reference-cases.md) — cart-api, a checkout service that calls an AI "summarise my cart" step. This is the worked illustration the six katas below run on.

- ﻿[**Case B — Kepler Insurance**](https://eu.git.epam.com/airun-mission-26-ai-factory/curriculum/-/blob/main/modules/001-reference-cases.md) — a migrating app from the Azure cutover portfolio, e.g. the **Claims API** or a **Policy Admin** service.

The artefacts compound into one pack, so switching subject mid-series breaks the chain. The worked inputs below use cart-api as the illustration; **if you picked Case B or your own project, read "cart-api" as your chosen service** (the Claims API, a Policy Admin app, or your own) and substitute its real shape throughout — its replicas, dependencies, and whether it has an AI step.

*﻿  
*

*Artefact folder:* artefacts/800-wide/ — every kata writes one file here. Each kata after the first names a dependency_fallback sample you can paste if you joined the series late.

# Optional appendix — see one container run (no account, ~15 min)

This is **optional** and not graded. It exists only to remove the mystery from "the cloud": you run a real container and open its live URL, with no cloud account, no credit card, and automatic teardown.

- **Tool:** [Google Cloud Shell](https://docs.cloud.google.com/shell/docs) — a Google account, no billing, no card; a container engine (Docker Engine) is pre-installed. To use Podman instead: sudo apt-get install -y podman. Fallback: [GitHub Codespaces](https://github.com/features/codespaces).

- **Why Podman matters on your own machine:** Docker *Desktop* needs a paid licence at EPAM's size; **Podman** is open-source and free for commercial use — the house default. (The pre-installed Docker *Engine* here is the free CLI, so this one-off is fine either way.)

- **Steps:** (1) open Cloud Shell; (2) run a hello-world web container on port 8080 (docker run -p 8080:80 … or podman run …); (3) click **Web Preview → port 8080** and open the live URL; (4) close the tab — the sandbox tears itself down on timeout.

- **The point:** a deployed container is a process on a machine behind a URL — nothing more. Running it once retires "the cloud" as a mystery; it does not change your maturity score (adoption does, not provisioning).

**What you walk out with**

By the end of the six katas, artefacts/800-wide/ holds the **Cloud Operations & Support Pack** for your chosen service: a cloud stack/ownership map (01), a deployment manifest with a fresh-session audit (02), a CI/CD workflow with a supply-chain audit (03), an incident diagnosis with a drafted runbook (04), a monthly cloud + AI cost estimate with a cap (05), and the one-page readiness-and-support brief (06). None of it needed a cloud account, Docker, or kubectl — only your AI surface, a price list, and the discipline to ask what a green dashboard cannot tell you. This pack carries forward into the Security module (which threat-models it) and the Delivery & Project Management module (which reports on its cost and readiness).
