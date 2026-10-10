# In a nutshell

A regional sales manager asks which product line to push next quarter. The answer comes from one of two places: someone's gut feeling, or a dashboard showing last quarter's margin, return rate, and regional demand — same question, completely different quality of answer. This is the one track in the course where you look at data delivery from the inside, after Engineering and Quality: how raw activity becomes a number a decision-maker can trust. The durable anchor: **a data product is a trustworthy answer you can act on and trace back to its source — not the pipeline that produced it; AI drafts the pipeline fast, but a human still owns what the numbers mean.** The Wide path is for every role: you build one small synthetic pipeline with AI so you can commission, read, and challenge a governed data product without learning production platform design.

# Role Context

- **Who it's for.** All learners, including teams that have no dedicated data specialist and must cover the data role with AI. Specialists — data engineers, analytics engineers, ML engineers, and data scientists — can read this as a refresher; the depth is in the Deep Theory section.

- **What the role does.** Profiles and models the data, writes a spec before building, builds the bronze → silver → gold pipeline, designs schemas and publishes a contract, runs quality rules that fire before bad data reaches a decision, documents lineage from source to number, and serves the metric downstream roles consume.

- **Where it sits.** At the intersection of every other role — it receives business questions and source schemas from upstream, and delivers versioned datasets, metrics, contracts, and lineage that downstream roles act on. When a data delivery arrives, your job is to recognise a governed product and ask for the lineage, contract, and quality guarantees when they're missing.

- **The L2 → L3 shift.** The L2 engineer uses AI to draft a cleaning query and accepts it when it runs; the L3 engineer treats the pipeline as a governed product — a spec the agent builds against, a contract published to consumers, quality rules that fire on bad data, and lineage that traces every number back to its source.

- **What they don't own.** The business meaning of a metric (PROD/BA owns what "revenue" means), data classification and retention as legal calls (compliance owns the judgement), and the platform cost budget (Architecture owns the constraint). The data role implements and enforces these; it does not decide them.

# Why this matters for you

Every organisation makes decisions, and the only question is whether they run on evidence or on instinct. You may never design a production pipeline, but your team will ship metrics, dashboards, and datasets that AI helped produce. The Wide katas let you build a small synthetic pipeline so you can inspect the evidence behind those outputs. This 45-minute theory gives you the vocabulary to commission a data product, the structure to spot when a pipeline is a liability rather than an asset, and the review prompt to separate evidence, inference, and missing proof. If your team has no data specialist, it is the floor of working knowledge you need to cover the role yourself with AI.

<img src="media/image1.png" style="width:6.26806in;height:2.61111in" />

# Topic recap

The track runs in seven short blocks — here's each in brief.

- **Why data projects exist (Block 1).** A data team delivers an *answer* a business person can act on — a dashboard, a metric, an API — not a database or a pipeline; the infrastructure is the means, not the goal. The factory analogy frames it: raw data is ungraded timber, cleaned data is graded lumber, metrics and reports are the finished chairs. Every project answers one of two questions — "what happened?" (descriptive) or "what should we do?" (prescriptive) — and knowing which shapes every design choice.

- **From raw data to business insight (Block 2).** Raw data becomes trustworthy business output through the medallion pipeline — bronze (raw as-received, an audit log), silver (cleaned, standardised, point-in-time-trustworthy), gold (business-ready metrics and aggregates consumers read). Three layers beat one because each boundary is an audit point and a failure boundary: a wrong gold number is diagnosed by checking silver, then bronze. A single-layer pipeline gives you one mystery blob to sort through.

- **Data platforms and the organisational landscape (Block 3).** Most organisational data lives on a shared platform — Databricks, Snowflake, Microsoft Fabric — where the medallion runs and which every role both produces to and consumes from. Knowing what data exists, who owns it, and what quality it carries is the precondition for sourcing any feature or designing a report another team can reuse. These platforms increasingly host AI capabilities too — embeddings, model endpoints, BI query interfaces — so ask what's already provisioned before standing up separate infrastructure.

- **Data products vs. data pipelines (Block 4).** A pipeline moves data from A to B and is forgotten; a data product is served with guarantees and a named owner. Six components make the difference — owner, contract, lineage, SLA, quality monitors, and a deprecation policy. A pipeline without them works on launch day and becomes a liability by month six, when it breaks silently with no owner and no alert; the product keeps its freshness, ownership, and accountability.

- **The EPAM ADLC (Block 5).** Data delivery has its own eight-phase lifecycle — Learn, Plan, Validate, Build, Verify, Deploy, Operate, Observe — distinct from software delivery because data grows continuously and a bug can corrupt decisions retroactively. The phases iterate rather than run in a straight line: a quality issue found in Operate sends you back to Verify, a changed requirement back to Learn. AI accelerates every phase, but a named human approves each phase transition.

- **AI in data work (Block 6).** AI drafts well — cleaning and aggregation SQL, schema DDL, quality checks from column profiles, dashboard scaffolding, documentation — compressing the time from requirement to working code. Six decisions stay human: business-rule interpretation, data classification, schema commitments, source-of-truth designation, access control, and retention. The engineer's value shifts from "writing SQL" to "knowing when AI's SQL is wrong and why."

- **The collaboration model (Block 7).** The data team works at the intersection of every role: it needs business questions and metric definitions from PROD/BA, source schemas from Engineering, test datasets and quality bars from QA, and platform constraints from Architecture — and hands back versioned datasets, metric definitions, lineage, contracts, and readable documentation. The handoff that breaks most often is data shipped without lineage; before accepting any delivery, ask to see the trail from source to table.

<img src="media/image2.png" style="width:6.26806in;height:1.21667in" />

# Key terms

<img src="media/image3.png" style="width:6.00725in;height:3.85436in" />

# Key takeaways

1.  A data deliverable is an answer someone can act on, not a raw table dump — commission a named metric or dashboard with a stated business question, so the output is usable the day it arrives.

2.  Trust is built in layers: three medallion boundaries give you three places to diagnose a wrong number; a single-layer pipeline gives you one mystery blob.

3.  Six components separate a product from a pipeline — owner, contract, lineage, SLA, quality monitors, deprecation policy. Without them, a pipeline works on day one and becomes a liability by month six.

4.  AI drafts the SQL fast, but six decisions stay human — what a business rule means, which data is PII, whether a schema change breaks consumers, which source is authoritative, who gets access, and how long data is kept.

5.  Demand lineage before accepting any delivery: "Can you show me the lineage from source to this table?" If the answer is "it's complicated," the lineage is undocumented and you have inherited the liability.

6.  Review the supplied product spec, metric definition, schema, lineage, quality results, and monitor configuration as evidence. Label unsupported conclusions as inference or missing evidence, and leave governed decisions with named human owners.

**Course Repo: <https://epa.ms/ai-run-26-curriculum-repo>**

# Wide Theory

45 minutes

**Focus:** Equip the whole team to read a data product — its lineage, contracts, metric definitions, and quality guarantees — and equip data specialists to build one AI-native: a governed bronze → silver → gold pipeline with quality gates, an Open Data Contract Standard (ODCS) contract, lineage, and a served metric, handed off so any downstream role can trust the numbers without re-deriving them.

**Deep for:** Data Engineers, Analytics Engineers, Machine Learning (ML) Engineers, Data Scientists, Business Intelligence (BI) Developers.

**Total time per learner:**

- Wide path: 45 min Theory + ~105 min katas (7 × 15 min) + 60 min Final Kata ≈ 3.5h

- Deep path (own role): + 180 min Theory + 210 min katas (7 × 30 min) ≈ +6.5h (Final Kata is universal — done once)

Most modules in this course treat data as something your role consumes — a dashboard you read, a metric you trust, a dataset you query. This module is the exception: it shows how a data product is built from the inside, and how the work changes when AI drafts the SQL, schemas, and quality checks. The L2 data engineer uses AI to draft a cleaning query and accepts it when it runs; the L3 data engineer treats the pipeline as a governed product — a spec the agent builds against, a contract published to consumers, quality rules that fire before bad data reaches a decision, and lineage that lets anyone trace a number back to its source. The carry-forward artefact is that product: a working pipeline and served metric the Infrastructure & Operations module deploys, the Delivery & Project Management module reports against, and the Final Assembly Line assembles into the end-to-end portfolio.

**Objectives**

- **Learn to do:** build a bronze → silver → gold pipeline with data-quality checks and a served business metric, then redo it by handing the pattern to a coding agent on a fresh dataset and comparing the two runs (Wide); produce a governed data product — source-to-target mapping (STTM) and product requirements document (PRD), an Open Data Contract Standard (ODCS) contract, ingestion, Slowly Changing Dimension Type 2 (SCD Type 2) transformation, end-to-end data quality with auto-ticketing, lineage, and a schema-change runbook (Deep)

- **Skills (role):** data cleaning, transformation, and aggregation to business metrics; data-quality rule design; data modelling, schema, and contracts; lineage and governance

- **Skills (tooling):** DuckDB in Jupyter/Colab, SQL transformations, a served metric (Streamlit or FastAPI), Open Data Contract Standard (ODCS) contracts, Mermaid lineage diagrams, and directing a coding agent on a new dataset

- **Outcome:** a working pipeline + served metric + by-hand-vs-agent comparison (Wide); a governed data product with contracts and lineage + a schema-change runbook (Deep); a Data role-agent spec (Final Kata)

- **Tested by:** K 7.W.1–7 (Wide kata series) + K 7.3 (Final Kata); the Deep path adds K 7.D.1–7

# 0 — Role Context

**How to read this section.** Two audiences share it. If Data is your role, this is your own role description — read it as the L3 standard you produce against. If you take this module Wide — PROD/BA, design, architecture, engineering, QA, infrastructure, security, delivery, or management — read it to understand the role you collaborate with and the evidence a trustworthy data product should hand you. You build one small synthetic pipeline with AI to see the evidence at each layer; you are not expected to design a production pipeline. Your target is to recognise a governed data product and ask for lineage, contracts, and quality guarantees when they are missing.

This section is anchored to the EPAM ADLC (Analytics Development Life Cycle) — the data-delivery lifecycle framework that structures how EPAM runs data projects from discovery to operation. The phase names and the discipline areas below come from it; the Materials and Links file points to the source.

**0.1 — Role names and who they apply to**

This module is for everyone on a delivery team, but only the data specialists take it Deep. If your primary work product is data — pipelines, models, metrics, contracts, or reports — the Deep path is yours, and it teaches you to build the governed product. Everyone else takes the Wide path and learns to read that product and ask for it when it is missing. Common data job titles (Deep):

- **Data Engineer** — builds and maintains ingestion, transformation, and serving pipelines; owns the schema, the quality gates, and the lineage.

- **Analytics Engineer** — owns the transformation layer between raw sources and business-facing tables; defines metrics, grain, and the silver → gold logic.

- **ML Engineer** — owns feature pipelines and the data contracts that feed models; treats training and serving data as a versioned product.

- **Data Scientist** — owns exploratory analysis, model logic, and the data assumptions a model depends on.

- **BI Developer** — owns the semantic model, measures, and the reports business users consume.

- Common synonyms across firms: Data Platform Engineer · ETL Developer · Database Engineer · Analytics Developer · Data Modeller · Pipeline Engineer.

If your title varies, the test is functional. Do you spend material time moving, modelling, cleaning, or serving data as a primary work product on a team that uses AI tools? If yes, this module covers you Deep. If instead you consume data products — you read the dashboard, sell against the metric, test the pipeline's outputs, or build a feature on top of the served data — the Wide path covers you, and teaches you to recognise a governed data product and ask for the lineage, contract, and quality guarantees when they are missing.

**0.2 — Role description and core duties**

The data specialist owns the surface between *"here are the raw sources and the business question"* and *"here is a versioned, documented, quality-checked data product, with lineage tracing every number back to its source."* In observable verbs:

- **Profiles and models** the data — runs exploratory analysis, then specifies conceptual, logical, and physical models before any pipeline code is written.

- **Specifies** the data product before building: writes the STTM (source-to-target mapping), KPI and metric definitions with formula and grain, access controls, and retention policy.

- **Builds** the pipeline across the medallion layers — ingestion with validation at ingress, bronze → silver cleaning, silver → gold business metrics — drafting SQL and scaffolding with AI and verifying the row-count math by hand.

- **Designs** schemas and publishes contracts — naming standards, schema versioning, additive-vs-breaking change classification, and an ODCS (Open Data Contract Standard) contract consumers can depend on.

- **Designs and runs** data-quality rules across the six dimensions (accuracy, completeness, consistency, uniqueness, timeliness, validity), with end-to-end monitoring and auto-ticketing on failure.

- **Documents** lineage and governs change — a source-to-target lineage graph, metadata published to the catalog, and a schema-change runbook with impact analysis and consumer notification.

- **Serves** the metric — a dashboard or API endpoint exposing live gold-layer numbers that business users and downstream roles consume.

What this role does *not* own: the business definition of a metric (PROD/BA owns what "revenue" means; the data engineer implements it), data classification and retention as legal calls (compliance owns the judgement; the engineer enforces it), and the platform cost budget (Architecture owns the constraint; the engineer builds within it).

**0.3 — Main processes**

The data specialist's work runs along the eight EPAM ADLC phases, applied to the medallion data discipline:

- **Learn** — investigate the business domain, identify data sources, profile available data, and surface unknown challenges. AI helps by drafting source questionnaires and running data profiling.

- **Plan** — define objectives, success metrics, governance rules, and stakeholder alignment. AI helps by drafting KPI definitions and intake briefs; the human signs off on every metric formula and data classification decision.

- **Validate** — evaluate data readiness, quality, and architecture fit before any build work. AI helps by generating readiness reports; humans confirm the data is trustworthy enough to build on.

- **Build** — implement ingestion, transformation, and serving across bronze → silver → gold. AI generates SQL, cleaning code, and pipeline scaffolding.

- **Verify** — test correctness, performance, and safety using automated DQ checks and metric validation against known-good samples. AI drafts test cases; the human confirms business-rule correctness.

- **Deploy** — promote validated artifacts to production via CI/CD pipelines with version control and model registries.

- **Operate** — monitor freshness, handle failures, process schema changes from sources, and govern runtime behaviours.

- **Observe** — analyse behaviour and drift, surface new insights, and feed findings back into the next Learn phase.

The ADLC is not linear, and the phases are not all strictly ordered — Plan and Validate in particular often run in parallel, and EPAM sequences them in either order depending on whether scoping or data-readiness leads. The loop also runs backwards: a quality issue found in Operate sends you back to Verify; a changed business requirement sends you back to Learn. The discipline areas these phases cut across — data modelling, schema and contracts, ingestion, transformation (including SCD Type 2), scheduling and orchestration, data quality, reporting and conversational BI, and lineage and governance — each map to a sub-section of Deep Theory.

**0.4 — Role in SDLC**

The data team sits **at the intersection of every other role** — it consumes business questions and source schemas from upstream, and delivers versioned datasets, metrics, and contracts that downstream roles act on. Pre-AI, the failure that breaks this position most often is data shipped without lineage: when a metric changes unexpectedly, the consuming team has no way to trace the cause. The cross-role audience contract:

<img src="media/image4.png" style="width:5.92392in;height:2.88209in" />

The lineage handoff is the test for every other role: before accepting a data delivery, ask "Can you show me the lineage from source to this table?" If the answer is "it's complicated," the lineage is undocumented and you have inherited a liability.

**0.5 — How the role changed with AI (general)**

AI does not replace data engineering. It compresses the time from requirement to working code, and shifts the engineer's job from writing boilerplate to reviewing, correcting, and governing what AI produces. AI drafts well: SQL for cleaning, aggregation, and joins; schema DDL from a plain-language description; data-quality checks from column profiles; dashboard scaffolding from a metric list; pipeline boilerplate; and documentation from code.

What collapsed: mechanical SQL authoring, schema boilerplate, first-pass DQ checks, and documentation drafting. What amplified: spec quality, business-rule verification, contract discipline, and lineage rigour. What survived and got more valuable: judgement — knowing when AI's SQL is wrong and why, deciding which anomaly is a data-quality issue versus a real business event, and classifying a schema change as breaking or additive.

**0.6 — What changed at L2 (AI-assistant)**

At L2 the human still owns the work; AI is a copilot. Where AI assists:

- Drafting cleaning, aggregation, and join SQL from a column profile pasted into the chat.

- Generating schema DDL and STTM table rows from a plain-language description.

- Scaffolding data-quality checks and dashboard layouts from a metric list.

- Drafting documentation — STTM tables, lineage notes, end-user docs — from existing pipeline code.

Stays human at L2 (the lines that do not move): **what a business rule actually means**, **which data is PII or regulated**, **whether a schema change is breaking or additive**, and **which source is the source of truth**. A data engineer who uses AI only to draft SQL and accepts it when it runs is operating at L2. The team typically maintains a versioned AI prompt library so the drafting is consistent across every engineer.

**0.7 — What changed at L3 (AI-native)**

At L3 the workflow restructures around specification files, contracts, and an automated governance loop. The role gains reach; it does not disappear. The concrete shifts:

- **Spec before pipeline.** Each phase transition is triggered by a spec file — completing design-spec.md triggers a CI job where agents generate schema DDL, STTM tables, and DQ-rule skeletons. The human approves each transition, not the generation work itself.

- **Contract as published artefact.** A schema shipped to consumers is a contract. The ODCS contract is versioned alongside the pipeline; breaking it triggers the schema-change runbook before any consumer is affected.

- **DQ rules generated from the contract, enforcement mode chosen per use case.** The data contract is the machine-readable DQ specification: an agent generates check code from it, so the rules and the checks stay in sync as the contract evolves. Whether a failing check *blocks the load* (gate mode) or *marks the row* (annotation mode) is a business decision that belongs in the contract — both patterns are valid, and the right choice depends on how downstream consumers use the data. When a check fires, an agent drafts the ticket with rule name, expected vs actual values, affected row count, and downstream blast radius.

- **Lineage as generated infrastructure.** Lineage is auto-generated from pipeline code on every CI run and published to the catalog. When a source schema changes, an agent detects affected downstream datasets, drafts an impact analysis, and prepares consumer notifications — with human approval before they are sent.

- **The metric as a served product.** Gold-layer numbers are exposed through a dashboard or API endpoint that downstream roles consume directly, not a one-off export.

The Wide path uses one small synthetic pipeline to teach you to *recognise and evaluate* a governed data product. The Deep path teaches you to *design, build, and operate* one for production.

# 1 — Theory

<img src="media/image5.png" style="width:6.08365in;height:1.40285in" />

# 2 — Materials and Links 

Tool references (DuckDB, Jupyter/Colab, Streamlit, FastAPI, Mermaid, the Data Contract CLI for ODCS, SQLFluff), the EPAM anchors for this module (the EPAM ADLC, EPAM DIAL, and EPAM), internal knowledge links, optional external references, and the reference-case task menu (Case C — Customer 360 on Databricks, Nordstar Materials — the designated data case; the Wide katas run on a synthetic dataset for zero-setup practice).

# 3 — Practice

**Practice rule for every kata and the Final Kata in this module:** the Wide series runs on a small synthetic retail dataset generated on your laptop — no setup, no real customer data, no production deployment. The Deep series applies the same patterns to the designated data case, **Case C — Customer 360 on Databricks (Nordstar Materials)**, or to your own project data; stay on one dataset for the full Deep series, since switching mid-series breaks the carry-forward chain.

**3.1 — Wide kata series (all learners)**

K 7.W.1 → K 7.W.7 (seven katas, ~105 min total, 15-min cap each). **Superpower moment.** You set up a data workspace, generated a realistic dataset, cleaned it, computed business metrics, added quality checks, and built a dashboard — all with AI — then handed the whole pipeline pattern to a coding agent that rebuilt it on a fresh dataset, and you can name exactly where the agent saved time and where it went wrong. Chains into a working AI-built pipeline and served metric — notebook, cleaned parquet, gold-metric tables, DQ checks, dashboard, and the by-hand-vs-agent comparison.

**3.2 — Deep kata series (role specialists only)**

K 7.D.1 → K 7.D.7 (seven katas, ~210 min total, 30-min cap each). Specialist outcome: *a governed data product — STTM/PRD, an ODCS contract, ingestion with error handling, an SCD Type 2 transformation verified idempotent, end-to-end data quality with auto-ticketing, lineage, and a schema-change runbook — that any downstream consumer can depend on and trace.*

**3.3 — Final Kata**

K 7.3 — specify a runnable Data role-agent / Skill in a native format another teammate can load and use when no data specialist is on the team, with the human-owned decisions (business-rule interpretation, data classification, source-of-truth designation, retention) inline as guardrails.

# 4 — Carry-Forward

Three artefacts leave this module for consumption downstream.

**4.1 — AI-Built Data Pipeline & Served Metric**

- **Artefact name:** AI-Built Data Pipeline & Served Metric.

- **Source:** Wide kata series K 7.W.1–7 — workspace, synthetic dataset, bronze → silver cleaning, silver → gold metrics, DQ checks, served dashboard, and the by-hand-vs-agent comparison. Produced on the synthetic retail dataset (or a real dataset that fits the 15-min-per-kata cap).

- **Consuming stage(s):**

- **Infrastructure & Operations module** — deploys the served metric and schedules the pipeline run, using the notebook and DQ checks as the deployable unit.

- **Delivery & Project Management module** — reports against the served gold metric as a delivery signal, treating it as the source of truth for the number it tracks.

- **Final Assembly Line** — the pipeline and served metric are the Data subagent in the end-to-end delivery scenario.

- **Format:** a Jupyter notebook plus parquet outputs and a Markdown comparison, under artefacts/700-wide/ (fallbacks under artefacts/700-wide/\_fallbacks/).

**4.2 — Governed Data Product Pack**

- **Artefact name:** Governed Data Product Pack.

- **Source:** Deep kata series K 7.D.1–7 — STTM/PRD, an ODCS contract, ingestion with error handling, SCD Type 2 transformation, end-to-end DQ with auto-ticketing, lineage, and a schema-change runbook. Produced on Case C (or your own project data).

- **Consuming stage(s):**

- **Infrastructure & Operations module** — consumes the ODCS contract, DQ rules, and schema-change runbook to operate and monitor the product in production.

- **Delivery & Project Management module** — consumes the data-product spec and lineage to plan against data dependencies and report delivery risk.

- **Final Assembly Line** — the Governed Data Product Pack is the specialist Data deliverable in the end-to-end portfolio.

- **Format:** Markdown plus YAML — STTM, runbook, lineage, and end-user docs as Markdown; the ODCS contract and catalog metadata as YAML — under artefacts/700-deep/ (fallbacks under artefacts/700-deep/\_fallbacks/).

**4.3 — Data Role-Agent Spec**

- **Artefact name:** Data Role-Agent Spec.

- **Source:** Final Kata K 7.3 (all learners; specialists add the depth sections covering the full data-product pack).

- **Consuming stage(s):** **the downstream role modules** load the Data role-agent when no data specialist is on the team — read in place for data context, not transformed. **Final Assembly Line** lists it in the agent roster a joining teammate reads.

- **Format:** a runnable Claude Skill or sub-agent under .claude/, with the human-owned decisions (business-rule interpretation, data classification, source-of-truth designation, retention) inline as guardrails.

- **Engine guide target:** .ai-run/guides/data/database-patterns.md, under header \## Data contracts + lineage rules (from Module 700 — Data). This is the authoritative chain mapping; the spec's \<!-- chain:rules:start guide=… topic=… --\> delimiter attributes mirror it, and on any disagreement this line wins.

- **Optional stand-in override (Deep only):** none.

# Why This Matters for You

A regional sales manager asks which product line to push next quarter.

One answer comes from instinct. Another comes from margin, return rate, and regional demand. The question stays the same. The quality of the decision changes.

Data projects turn the activity a business already creates into evidence people can use. Orders, support tickets, and abandoned clicks become metrics, dashboards, and APIs. Those outputs shape pricing, staffing, inventory, and product decisions.

This module is the only place in the course where every learner views data delivery from the inside. Elsewhere, your role mostly consumes data platforms and data products. Here, you learn how to commission, build, read, and challenge them.

Your team may lack a data specialist. AI can then cover much of the drafting work. You still need enough judgement to:

- frame the business question;

- recognise a trustworthy pipeline;

- challenge a metric definition;

- demand quality evidence and lineage;

- keep governed decisions with their accountable human owners.

The practical gain is simple: you can turn “we need some data” into a traceable answer. You can also spot a polished dashboard built on weak foundations.

**Goal**

After this Wide Theory, you can commission, read, and challenge a data product, recognise when a pipeline has become a liability, and keep metric meaning with accountable humans while AI drafts the machinery.

**Time**

~45 min.

**Audience**

All learners, including teams that cover the data role with AI.

Data engineers, analytics engineers, machine learning engineers, and data scientists can use this as a refresher. Specialist depth lives in Deep Theory.

# Prerequisites

Complete Onboarding and Fundamentals first.

Bring two inputs from earlier modules:

- from Product Management and Business Analysis, business questions expressed as metric definitions;

- from Quality, acceptance criteria and a working definition of “good enough”.

The Wide path requires zero platform setup. Its katas use a small synthetic dataset on any laptop.

# Must Cover

**A data product is a trustworthy answer someone can act on and trace back to its source — not the pipeline that produced it. AI drafts the pipeline fast; a human still owns what the numbers mean.**

The first five topics build in order: why data work exists, how raw data becomes a trustworthy metric, where that data lives at organisational scale, what separates a product from a pipeline, and the lifecycle that names the whole arc. The last two explain how AI changes the work and how the data team collaborates with every other role.

- **Why data projects exist** — turn raw activity into a dashboard, metric, or API that changes a real decision.

- **The medallion pipeline** — use bronze, silver, and gold as separate trust layers, audit points, and failure boundaries.

- **Data platforms and the organisational landscape** — locate shared data, its owner, its quality guarantees, and existing AI capabilities before building another stack.

- **Data products versus pipelines** — add ownership, contracts, lineage, service levels, monitoring, and retirement rules so the output remains useful after launch.

- **The Analytics Development Life Cycle (ADLC)** — connect eight iterative phases from discovery through operation and observation.

- **AI in data work** — move effort from mechanical generation into specification, review, governance, and verification.

- **The collaboration model** — exchange precise inputs and outputs with every role, then demand source-to-table lineage at handoff.

# Terms Used

<img src="media/image6.png" style="width:6.02809in;height:6.20865in" />

# Key Messages / Ideas

1.  **A data deliverable is an answer, not infrastructure.** The dashboard, metric, or API is the product. The database and pipeline support it.

2.  **Trust is built in layers.** Bronze, silver, and gold create three audit points and three failure boundaries. One layer creates one mystery blob.

3.  **The platform is the organisational meeting point.** Know what data exists, who owns it, and which guarantees travel with it.

4.  **A pipeline moves data; a product keeps a promise.** Owner, contract, lineage, SLA, monitors, and deprecation policy keep it useful at month six.

5.  **Data delivery has its own lifecycle.** Learn, Plan, Validate, Build, Verify, Deploy, Operate, and Observe form an iterative loop.

6.  **Correct SQL can implement the wrong rule.** Review the approved meaning, classification, schema commitments, source-of-truth, access, and retention before accepting generated work.

7.  **Lineage is the handoff to demand.** If nobody can trace a number to its source, the team inherited a liability.

# Structure (Per-topic context blocks)

Each block starts with the mental model and then gives the precise practice. Most task-focused blocks also show the L2-to-L3 shift.

**L2** means a person prompts AI for each task and assembles the output.

**L3** means an agent works from versioned specifications, opens a change for review, and passes explicit gates. A human approves governed decisions and phase transitions.

The move from L2 to L3 is what going AI-native means for this work.

# Block 1 — Why Data Projects Exist

**The thread:** a business question defines the answer. The answer determines the data and transformations worth building.

**The factory analogy**

Think about data as a manufacturer thinks about raw material.

Raw timber reaches a sawmill ungraded and inconsistent. The sawmill turns it into graded lumber. A furniture maker then turns that lumber into finished chairs.

Raw data is the timber. Cleaned and validated data is the lumber. Metrics and reports are the chairs.

Each step adds predictability, trust, and usability.

<img src="media/image7.png" style="width:6.26806in;height:1.2125in" />

**What a data team delivers**

A data team delivers something a person or system can act on:

- a dashboard the CEO trusts;

- a metric that feeds a pricing model;

- an API that powers recommendations.

A database or pipeline alone is unfinished work. **If the output cannot change a decision, the project has delivered machinery instead of value.**

Data work usually answers one of two questions:

1.  **What happened?** Descriptive analytics covers sales by region, defect rate by shift, or churn by cohort.

2.  **What should we do?** Prescriptive analytics covers customers to contact, inventory to reorder, or models to deploy.

Most projects begin with the first question and move towards the second. The chosen question shapes every later design decision.

EPAM runs analytics platforms for retailers, data warehouses for banks, and real-time pipelines for logistics providers. The ADLC in Block 5 is one of the delivery methodologies used to organise this work at scale.

**How the method changes**

<img src="media/image8.png" style="width:6.26806in;height:2.45972in" />

**L2 method of work:** A shared prompt library covers source questionnaires, column profiling, and exploratory analysis. An engineer pastes a raw table profile into AI. AI drafts a column inventory, null-rate summary, and candidate quality rules. A first pass that took half a day can take under 15 minutes.

**L3 method of work:** An agent reads problem-spec.md, which contains the business question and source list. It profiles the first sample, generates source questionnaires, and drafts an STTM skeleton in a pull request. The engineer reviews the evidence and approves the specification.

# Block 2 — From Raw Data to Business Insight

**The thread:** raw data preserves what arrived. Cleaning makes it dependable. Business modelling turns it into an answer.

Data rarely travels straight from an application database to a chart. Each transformation should add trust or business meaning.

The common three-layer pattern is the medallion architecture.

**Bronze — raw as received**

Bronze keeps the source exactly as it arrived.

If amount arrives as text, bronze keeps it as text. If a source sends duplicate rows, bronze keeps them too. This layer is the audit log: it shows what arrived and when.

**Silver — cleaned and standardised**

Silver removes noise and applies stable technical rules.

Typical work includes:

- removing invalid rows such as negative prices;

- deduplicating order IDs;

- casting columns to the right types;

- standardising dates and applying business naming conventions.

Silver supports trustworthy point-in-time queries. It cleans up noise without changing business logic; business aggregation belongs in gold.

**Gold — business-ready output**

Gold joins and aggregates silver data into the exact form consumers need.

A table such as daily_sales_by_category belongs in gold. Dashboards, reports, APIs, and models read from this layer.

<img src="media/image9.png" style="width:6.26806in;height:1.46181in" />

**Why three layers beat one**

Each boundary creates an audit point and a failure boundary.

When a gold metric looks wrong:

1.  inspect silver to see whether cleaning changed the value;

2.  inspect bronze to see whether the source sent bad data;

3.  compare the gold formula with the approved metric definition.

**Three layers give you places to diagnose. One layer gives you one mystery blob.**

📎**ADLC connection:** Build creates bronze, silver, and gold. Verify runs data-quality checks and confirms gold formulas against known-good samples. Deploy then serves the validated output.

**L2 method of work:** Versioned scaffolds define data definition language (DDL), folders, and naming. A prompt generates bronze landing, silver cleaning, and gold aggregation for DuckDB, Spark, BigQuery, or Synapse. A person reviews each layer.

**L3 method of work:** An agent reads source-spec.yaml. It generates bronze DDL, silver SQL with casts and deduplication, and gold aggregation SQL in one pull request. SQLFluff, a SQL linter, checks naming in continuous integration. A human reviews the business rules before merge.

**Human-owned call:** approve cleaning policy and metric formula. Running SQL proves execution, rather than business correctness.

# Block 3 — Data Platforms and the Organisational Landscape

**The thread:** applications create activity records. A shared platform governs and serves those records across organisational boundaries.

Every order, support ticket, and click belongs first to an application. Engineering owns that operational system. Organisational analytics needs a wider surface: the data platform.

A **data platform** collects, stores, governs, transforms, and serves data across the organisation.

Common platforms include:

- Databricks;

- Snowflake;

- Microsoft Fabric;

- Google BigQuery;

- Amazon Redshift.

They centralise data that would otherwise remain scattered across application databases. The medallion pattern usually runs on top of this shared platform.

<img src="media/image10.png" style="width:6.26806in;height:2.38958in" />

**Why every role should care**

Applications both produce data for the platform and consume data from it.

A recommendation feature may read historical purchases from gold. A clickstream service may write events to bronze. A report may depend on a shared semantic model maintained by another team.

Before choosing a source, ask:

- What data already exists?

- Who owns it?

- What quality guarantee does it carry?

- Which contract controls access and change?

- Which consumers already depend on it?

These answers prevent duplicate datasets and conflicting metrics.

**AI capabilities already on the platform**

Modern platforms may already provide:

- model registries, which track approved model versions;

- embedding stores and vector search, which retrieve related content by meaning;

- model inference endpoints, which run a model behind an API;

- large language model (LLM)-powered business-intelligence interfaces, which answer questions over governed data;

- machine learning (ML)-driven quality monitoring, which flags unusual data patterns;

- orchestration for agent workflows, which schedules and coordinates agent steps.

Ask the data team what is already provisioned before creating separate infrastructure.

📎**Engineering ↔️Data connection:** Engineering applications produce records for the data platform and consume governed outputs from it. Architecture decides platform and layer ownership. ADLC Plan records governance and access; Operate enforces them. The boundary becomes a documented decision rather than tribal knowledge.

**Block 4 — Data Products versus Data Pipelines**

**The thread:** a pipeline moves records today. A data product keeps the output useful, explainable, and supported over time.

Many teams build pipelines. Fewer build products. The difference appears after launch.

**Pipeline thinking**

“We moved data from A to B. Done.”

Then the source schema changes. Nobody knows which consumers break. The data goes stale without an alert. A 3am failure has no clear owner.

**Product thinking**

“We serve data with guarantees, and we own it.”

The gold table daily_sales_by_category can be a data product. It refreshes on a known cadence. A named person owns it. A monitor fires when it breaks its contract.

A spreadsheet export is different. It starts ageing as soon as someone saves it. Three teams can soon quote three different revenue figures.

**A pipeline moves data. A product keeps a promise.**

<img src="media/image11.png" style="width:6.26806in;height:2.88611in" />

**Six components of a data product**

The components work together. Ownership gives the promise an accountable person. Contracts and lineage explain the promise. Monitoring and retirement rules keep it true over time.

<img src="media/image12.png" style="width:5.97947in;height:3.25711in" />

<img src="media/image13.png" style="width:6.26806in;height:1.99167in" />

A pipeline without these components can work on day one and become a liability by month six.

📎**ADLC connection:** EPAM treats the data product as the unit of delivery. The six components therefore belong in ADLC Plan artefacts, rather than optional documentation.

**L2 method of work:** A shared Markdown or YAML specification lives in the repository. AI fills its six fields from approved requirements. The product owner reviews the draft before implementation. A team catalogue lists every active product, owner, and SLA.

**L3 method of work:** An agent reads a business requirements file and source specifications. It generates a product-spec YAML with owner, contract, lineage, SLA, monitor configuration, and deprecation window. The product owner’s GitHub approval is the only manual step before automatic provisioning into monitoring.

# Block 5 — Analytics Development Life Cycle

**The thread:** data grows and reality changes. Delivery therefore needs an iterative lifecycle that continues after deployment.

A software defect usually affects behaviour from release onwards. A data defect can also change historical results and corrupt decisions made from those results.

The EPAM Analytics Development Life Cycle names eight phases for this work.

<img src="media/image14.png" style="width:6.11142in;height:6.00031in" />

<img src="media/image15.png" style="width:6.26806in;height:2.11944in" />

The lifecycle is iterative rather than linear.

Plan and Validate often run in parallel. Some teams plan scope before testing readiness. Others inspect readiness before committing scope.

The loop also moves backwards:

- an Operate quality issue returns to Verify;

- a changing requirement returns to Learn;

- observed drift may change the Plan.

**Deployment ends a build cycle. It starts the evidence cycle.**

**L2 method of work:** Shared phase checklists and prompt sets live in the repository. Phase gates are documented and applied consistently across projects. Every phase uses the same artefact template. A signed Plan specification gates Build, so another team member can pick up the project mid-phase.

**L3 method of work:** Specification files trigger transitions. Completing design-spec.md starts a CI job that generates schema DDL, STTM rows, and DQ-rule skeletons. CI blocks Build if Design artefacts fail schema validation, contain missing required fields, or are absent. A named human approves each phase transition.

# Block 6 — AI in Data Work

**The thread:** AI compresses mechanical drafting. The saved time moves into specification, review, governance, and verification.

**What AI drafts well**

AI can draft:

- cleaning, aggregation, and join SQL;

- schema DDL from plain language;

- data-quality checks from column profiles;

- dashboard scaffolding from metric definitions;

- ingestion, retry, and logging boilerplate;

- STTM rows, lineage notes, and user documentation from code.

A draft is only a starting state. Draft volume measures activity. Verified, useful artefacts measure value.

**Six decisions that stay human**

These decisions require business, legal, compliance, or organisational authority.

<img src="media/image16.png" style="width:5.97947in;height:3.10433in" />

<img src="media/image17.png" style="width:6.26806in;height:2.30556in" />

**AI can generate correct SQL for the wrong definition.** Execution proves syntax and mechanics. Review proves alignment with the approved meaning.

The engineer’s value shifts from writing every line to recognising when generated work is wrong and explaining why.

📎**EPAM connection:** EPAM DIAL is the EPAM-owned general-AI tool used for much of this drafting on EPAM engagements. The six governed decisions form the human approval gates across ADLC phases.

**L2 method of work:** A versioned prompt library covers SQL, schema DDL, DQ checks, Open Data Contract Standard contracts, and documentation. It is referenced in onboarding and used by every team member. More than 70% of deliverables are AI-drafted before human review. The team tracks and shares time per artefact so assistance stays consistent across engineers.

**L3 method of work:** Agents generate transformations, schema, DQ rules, and documentation from specifications. Engineers review pull requests instead of typing each prompt. A weekly improvement loop compares actual DQ failure rates with AI-generated checks and flags coverage gaps. A dashboard tracks AI cost per project.

**Human-owned call:** approve the six governed decisions before generated work becomes a consumer commitment.

# Block 7 — Collaboration Model

**The thread:** data work sits between upstream meaning and downstream use. Weak handoffs create numbers that look precise and remain hard to trust.

<img src="media/image18.png" style="width:6.26806in;height:2.90764in" />

What the data team needs

<img src="media/image19.png" style="width:5.92392in;height:2.52791in" />

**What the data team returns**

- versioned datasets with documented schemas;

- metric definitions with formulas and worked examples;

- lineage from each source to each output;

- data contracts with SLAs and quality guarantees;

- documentation business users can read.

**The handoff that breaks most often**

Data arrives without lineage. Then a metric changes and the consumer cannot tell where the change began.

Before accepting a delivery, ask:

**Can you show me the lineage from the source to this table?**

“It’s complicated” means the lineage remains undocumented. The consumer has inherited the liability.

📎**Cross-role ADLC connection:** ADLC formalises these interfaces:

- Product and BA requirements feed Learn.

- Engineering source schemas feed Build.

- Quality acceptance criteria feed Verify.

**L2 method of work:** Versioned templates cover Product/BA requirements, source-system specifications, and acceptance criteria. They live in the repository and appear in project kickoff checklists. A Mermaid lineage diagram is a required repository artefact. The data product ships only after that trace is reviewable.

**L3 method of work:** Every CI run generates lineage from pipeline code and publishes it to the catalogue. An agent detects downstream effects of schema change, drafts an impact report, and prepares consumer notifications as GitHub comments. A human approves those notifications before sending.

# A Copy-Ready Data-Product Review Prompt

Use this prompt when a dashboard, metric, table, or API arrives for review.

**Role** Act as a data-product review assistant. Evaluate evidence and surface gaps. Leave business meaning, classification, schema commitments, source-of-truth, access, retention, and acceptance with named owners.

**Approved inputs** Review only these files or links:

- {{PRODUCT_SPEC}}

- {{METRIC_DEFINITION}}

- {{SCHEMA_OR_CONTRACT}}

- {{STTM_OR_TRANSFORMATION_LOGIC}}

- {{LINEAGE}}

- {{DQ_RESULTS}}

- {{SLA_AND_MONITOR_CONFIG}}

- {{DEPRECATION_POLICY}}

**Task** Assess whether the supplied evidence supports describing the delivery as a governed data product or only as a working pipeline. Do not approve it on behalf of the accountable owner.

**Required output**

1.  Business question and actionable output.

2.  Metric formula and grain, plus filters and denominator where applicable.

3.  Bronze → silver → gold transformation trace.

4.  Six-component review: owner, contract, lineage, SLA, monitors, deprecation.

5.  Quality evidence and known failure cases.

6.  Downstream consumers and breaking-change risk.

7.  Gaps, conflicts, assumptions, and unverified areas.

8.  Questions for the accountable human owners.

**Evidence rule** Cite the source file and line, section, or table for every claim. Mark inference as Inference. Use Evidence missing when the supplied sources cannot support a claim.

**Boundary** Draft findings and questions. Leave metric meaning, PII classification, schema commitments, source-of-truth, access, retention, and final acceptance to the accountable humans.

The prompt turns a vague “does this look right?” review into an evidence check. It also keeps missing documentation visible.

# Anti-Patterns

These are the main Wide-path failure modes. The ten specialist anti-patterns live in **700-DATA:Deep Theory** (curriculum repo: ./modules/700-data/700-deep-theory.md).

<img src="media/image20.png" style="width:5.73641in;height:3.88214in" />

<img src="media/image21.png" style="width:6.26806in;height:2.8125in" />

# Outcomes

By the end of Wide Theory, you can:

- **Explain and commission** a data product by naming the business question, actionable output, metric definition, platform owner, and lifecycle expectations.

- **Describe and diagnose** bronze, silver, and gold by checking quality evidence and source-to-table lineage at each failure boundary.

- **List and apply** the six components that distinguish a governed data product from a working pipeline.

- **Name** the eight ADLC phases and identify where AI accelerates work and where a human gate sits.

- **Challenge** AI-generated work against the six decisions that remain with accountable humans.

- **Apply and review** the collaboration model by identifying what each role provides and receives, separating evidence from inference, and demanding lineage before acceptance.

# Final Recap

The whole module reduces to one governing model and seven messages.

**A data product is a trustworthy answer someone can act on and trace to its source.**

1.  Deliver an answer, rather than infrastructure.

2.  Build trust through bronze, silver, and gold.

3.  Understand the shared platform before creating another data surface.

4.  Add six guarantees that turn a pipeline into a product.

5.  Run delivery through the eight iterative ADLC phases.

6.  Use AI for drafting and keep governed decisions with accountable people.

7.  Demand lineage from source to table at every handoff.

<img src="media/image22.png" style="width:6.26806in;height:3.75764in" />

# Required Materials

**Module artefacts (in this directory):**

- **Theory diagrams** (diagrams/) — 17 SVG diagrams, one per theory topic, embedded inline in the Wide and Deep Theory. They render in GitHub, VS Code, and any Markdown viewer:

  - diagrams/adlc-data-phases.svg — the EPAM ADLC data-delivery phases.

  - diagrams/pipeline-overview.svg — the bronze/silver/gold pipeline shape.

  - diagrams/sttm-spec.svg — the source-to-target mapping (STTM) spec.

  - diagrams/data-modeling-levels.svg — conceptual, logical, and physical modeling levels.

  - diagrams/schema-naming-contracts.svg — schema, naming standard, and ODCS contract.

  - diagrams/ingestion-patterns.svg — batch, incremental, and streaming ingestion.

  - diagrams/scd-type2.svg — the SCD2 slowly-changing-dimension pattern.

  - diagrams/dq-six-dimensions.svg — the six data-quality dimensions.

  - diagrams/dag-orchestration.svg — DAG-based orchestration.

  - diagrams/lineage-governance.svg — lineage and governance flow.

  - diagrams/data-product-components.svg — the data-product anatomy.

  - diagrams/report-bi-lifecycle.svg — the report and BI lifecycle.

  - diagrams/ai-human-split.svg — what AI drafts versus what a human decides.

  - diagrams/human-owned-decisions.svg — the human-owned-decisions accountability map.

  - diagrams/collaboration-model.svg — the data-team collaboration model.

  - diagrams/adoption-exploration.svg — the AI-adoption exploration curve.

  - diagrams/data-factory-analogy.svg — the data-factory analogy.

- **Runnable notebook** (notebooks/700-wide-katas.ipynb) — a Jupyter / Google Colab notebook that runs every Wide kata (K 7.W.1 through K 7.W.7) end to end on a laptop. Open it in Colab or any local Jupyter and work the cells in order.

- **Wide Theory** (700-wide-theory.md) — 45 minutes, for every learner: the data-delivery lifecycle, the STTM and KPI definitions, schema and contract basics, ingestion and quality, lineage, and the AI / human split.

- **Deep Theory** (700-deep-theory.md) — 180 minutes, for data specialists: physical modeling, ODCS contracts, validation at ingress with retry and dead-letter handling, SCD2 idempotency, end-to-end DQ across bronze/silver/gold, lineage and cataloguing, and the human-owned decisions a data team keeps.

# Internal Knowledge

The three sourceable EPAM anchors this module relies on. Every theory section and every kata in this module attributes to at least one of them.

- [**EPAM ADLC (Analytics Development Life Cycle)**](https://technology.epam.com/artifacts/1062?breadcrumbs=%5B%7B%22id%22%3A%221%22%2C%22label%22%3A%22Artifacts%22%2C%22value%22%3A%22%2Fartifacts%3Fpage%3D1%26sortBy%3DArtifactName%26sortOrder%3Dascending%26onlyMine%3D0%26search%3Dadlc%22%7D%2C%7B%22id%22%3A%22EPAM%E2%80%99s%20Analytics%20Development%20Lifecycle%20(ADLC)%20Framework%22%2C%22label%22%3A%22EPAM%E2%80%99s%20Analytics%20Development%20Lifecycle%20(ADLC)%20Framework%22%2C%22value%22%3A%22%22%7D%5D) — the data-delivery lifecycle framework this module follows: business question first, then contracts, transformation, quality gates, lineage, and serving. The phase diagram is diagrams/adlc-data-phases.svg, and each kata names the ADLC phase it sits in. Access the framework reference through your EPAM practice channel.

- **EPAM** — the internal knowledge base for lakehouse patterns, governance standards, and data-product delivery. Request access through your practice lead.

- [**DIAL**](https://chat.lab.epam.com/) — the EPAM-owned general-AI gateway used as the first AI option in every kata in this module (SQL generation, YAML and contract drafting, schema design, and documentation). Confirm allow-list status against the EPAM data-class matrix before pasting any non-public material.

# External References (Optional)

Pick depth, not breadth. Read at least one per cluster relevant to your work. No raw URLs — every reference is a named link.

**Transformation frameworks**

- [dbt (data build tool)](https://www.getdbt.com/) — SQL-first transformation with testing, docs, and lineage; install with pip install dbt-core dbt-duckdb, and see the [dbt + DuckDB quickstart](https://docs.getdbt.com/guides/duckdb).

- [SQLMesh](https://sqlmesh.com/) — SQL transformation with state management and semantic understanding; install with pip install sqlmesh.

- [Polars](https://pola.rs/) — fast Python DataFrames for large datasets; install with pip install polars.

**Local analytical engine**

- [DuckDB](https://duckdb.org/) — in-process analytical database, no server required; install with pip install duckdb and read the [DuckDB docs](https://duckdb.org/docs/stable/). Used throughout the Wide series.

**Data contracts**

- [Open Data Contract Standard (ODCS)](https://bitol-io.github.io/open-data-contract-standard/) — the industry-standard YAML data-contract specification (Bitol, LF AI & Data); current version is v3.x, keyed on apiVersion with kind: DataContract. Source repo at [open-data-contract-standard on GitHub](https://github.com/bitol-io/open-data-contract-standard). The older [datacontract.com](https://datacontract.com/) *Data Contract Specification* is deprecated in favour of ODCS as of ODCS v3.1.0.

- [Data Contract CLI](https://github.com/datacontract/datacontract-cli) — validate, test, and export ODCS contracts; install with pip install datacontract-cli and lint with datacontract lint contract.yaml.

**Data quality**

- [Great Expectations](https://greatexpectations.io/) — Python-native DQ framework with HTML reports; install with pip install great-expectations.

- [Soda](https://www.soda.io/) — SQL-based DQ checks with the SodaCL DSL; install the DuckDB data-source package with pip install soda-core-duckdb (Soda Core v3; each data source ships its own package).

- [Pandera](https://pandera.readthedocs.io/) — type-safe DataFrame validation for pandas and Polars; install with pip install pandera.

**Orchestration**

- [Apache Airflow](https://airflow.apache.org/) — DAG-based workflow orchestration, the most widely used in enterprise; managed options include [Astronomer](https://www.astronomer.io/) and [MWAA on AWS](https://aws.amazon.com/managed-workflows-for-apache-airflow/).

- [Dagster](https://dagster.io/) — Python-native orchestration with software-defined assets and lineage; install with pip install dagster dagster-webserver.

- [Prefect](https://www.prefect.io/) — Python-native orchestration with a managed cloud tier; install with pip install prefect.

**Lineage and data catalog**

- [OpenLineage](https://openlineage.io/) — open standard for lineage metadata; integrates with Airflow, Spark, and dbt, and pairs with the Marquez backend.

- [DataHub](https://datahubproject.io/) — open-source data catalog with lineage, search, and governance.

- [Apache Atlas](https://atlas.apache.org/) — metadata management and data governance, common in Hadoop and Cloudera environments.

- [dbt docs](https://docs.getdbt.com/) — auto-generated documentation and lineage from a dbt project; run dbt docs generate && dbt docs serve.

**Data platforms**

- [Snowflake](https://www.snowflake.com/) — cloud data warehouse with separated storage and compute; 30-day / \$400-credit trial.

- [Google BigQuery](https://cloud.google.com/bigquery) — serverless data warehouse on GCP; free tier of 10 GB storage and 1 TB queries per month.

- [Databricks](https://www.databricks.com/) — unified lakehouse platform (Spark, Delta Lake, ML); the reference case for this module runs on it. The free [Databricks Free Edition](https://www.databricks.com/learn/free-edition) — which replaced Community Edition (retired January 2026) — runs on a serverless platform, so there is no cluster spin-up wait.

**Foundational reading (books)**

 *Data Mesh: Delivering Data-Driven Value at Scale* — Zhamak Dehghani (2022, O'Reilly). Introduces the data-product paradigm: domain ownership, data as a product, and federated governance. See the [publisher page](https://www.oreilly.com/library/view/data-mesh/9781492092384/).

 *The Data Warehouse Toolkit* — Ralph Kimball and Margy Ross (3rd ed., 2013, Wiley). The reference for dimensional modeling: star schema, SCD types, fact and dimension tables. See the [publisher page](https://www.wiley.com/en-us/The+Data+Warehouse+Toolkit%3A+The+Definitive+Guide+to+Dimensional+Modeling%2C+3rd+Edition-p-9781118530801).

**Reference Cases and task menu**

Practice runs against real project material. **First choice is always your own current project / repo** — your own Customer 360, lakehouse, or analytics work is the highest-signal practice. Three standard cases exist (full detail at [reference-cases.md](https://eu.git.epam.com/airun-mission-26-ai-factory/curriculum/-/blob/main/modules/001-reference-cases.md)):

- **Case A — Omnichannel Commerce Platform (Meridian Retail Group).** A customer-facing, multi-region commerce build. Used by other role modules; not the technical-data fit this module needs.

- **Case B — Cloud-to-Cloud Migration (Kepler Insurance).** A brownfield, compliance-heavy migration. Used by other role modules.

- **Case C — Customer 360 on Databricks (Nordstar Materials).** **This is the case used for the Data module.** Nordstar Materials builds a governed Customer 360 data product on Databricks across 38 countries, connecting direct sales, distributor feeds, e-commerce, logistics, and product master data. Case C is reserved for this module — it is the only case with the data-platform depth (Databricks lakehouse, medallion architecture, entity resolution, Unity Catalog governance) the katas exercise. Pick it and stay on it across every kata so your artefacts compound.

If you carry inputs forward, the Product Management & BA module supplies the business questions and KPI candidates this module turns into definitions, and the QA module supplies the quality expectations the DQ gates enforce. Downstream, your contracts, pipeline, and lineage feed the Infrastructure & Operations module and the assembly module.

When a kata says *"use a real, recurring task,"* pick from this menu — recurring work a data engineer, analytics engineer, ML engineer, or data scientist would own on Nordstar's Customer 360:

- **Define the Customer 360 STTM and the KPI / metric definitions** — translate a strategic commercial question (global account revenue, next-best-offer, churn signal) into a source-to-target mapping and unambiguous metric definitions the country teams agree on. (K 7.W.4, K 7.D.1.)

- **Design the physical schema, naming standard, and ODCS contract** — turn the STTM into a physical Customer 360 schema with a consistent naming standard and a machine-validated ODCS data contract for a priority source. (K 7.D.2.)

- **Build the distributor-feed ingestion with validation at ingress, retry / dead-letter, and checkpoints** — ingest distributor sell-through (EDI, CSV, portal export) with schema validation at the door, a retry and dead-letter path for bad records, and a restartable checkpoint. (K 7.W.2, K 7.D.3.)

- **Implement an SCD2 customer dimension with idempotency** — build a slowly-changing-dimension-type-2 customer dimension that records hierarchy and attribute history and produces the same result on a re-run. (K 7.D.4.)

- **Wire end-to-end DQ across bronze, silver, and gold with auto-ticketing** — place data-quality checks as pipeline gates across all three layers and route a failed gate to an auto-created ticket with the offending records attached. (K 7.W.5, K 7.D.5.)

- **Produce the lineage diagram, data-catalog entry, and a schema-change runbook** — generate the end-to-end lineage diagram, a catalog entry a regional analyst can self-serve from, and a runbook for safely evolving the schema. (K 7.D.6, K 7.D.7.)

#### Wide kata series (all learners)

**Done**

3 minutes

*Goal:* Build a bronze→silver→gold pipeline with AI, then hand the whole pattern to a coding agent and compare what it builds against what you built by directing AI step by step.

*Persona:* non-role-learner. Someone who has shipped software or worked with data and used an AI tool, but has never built a full pipeline with AI in the loop from the first keystroke.

*Superpower moment:* You built an entire data pipeline with AI — set it up, generated data, cleaned it, computed business metrics, quality-checked it, served it on a dashboard — then handed the whole pattern to a coding agent that rebuilt it on a new dataset in minutes.

*Reference case:* Case C (Customer 360 / Nordstar) — practised on a zero-setup synthetic retail dataset standing in for the Case C patterns; no real customer data. The medallion shape you build here (bronze landing → silver cleaning → gold metrics → quality gates → serving) is the same shape the EPAM Analytics Development Life Cycle (ADLC) prescribes for data delivery, so the muscle you build transfers directly to a real engagement.

*Artefact folder (curriculum repo):* ./modules/700-data/artefacts/700-wide/ — you can find output examples there.

**Environment.** Default: DuckDB local + Python + Jupyter or Google Colab. Install once with pip install duckdb pandas matplotlib plotly streamlit. The module ships notebooks/700-wide-katas.ipynb, which implements all seven katas as runnable cells. Alternative: Databricks Free Edition (the serverless free tier that replaced Community Edition, retired January 2026) — no cluster spin-up wait. AI tool: EPAM DIAL is the default; Claude or ChatGPT (free tier) works for K 7.W.1 through K 7.W.6, but K 7.W.7 needs a coding agent (Claude Code, Cursor, or equivalent).

**No "do it manually first, then try it with AI."** AI is in the loop from the first keystroke. That is the L3 method of data work, and the ADLC names it the default mode of delivery — a human directs and verifies, an agent produces.

﻿

**Katas are offered for inspiration, not direct reuse in production setup.** If not adjusted and grounded in your context, they may produce unpredictable and unverified results.
