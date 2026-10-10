**Introduction**

**Not Started**

10 minutes

**Focus:** Set the SDLC's entry-point quality bar — turn ambiguous business intent into an opportunity brief that downstream PROD/BA, Design, Architecture, and Delivery can act on without re-doing discovery. **Deep for:** Consultants and SMEs (vertical/horizontal), plus principal consultants and solution architects in client-facing strategy or discovery roles. **Total time per learner:**

- Wide path: 50 min Theory + 120 min Katas (8 × 15) + 60 min Final Kata ≈ 3.8h

- Deep path (own role): + 180 min Theory + 240 min Katas (8 × 30) ≈ +7h (Final Kata is universal — done once)

Consulting and SME work sits at the gateway of the SDLC. Every downstream stage — PROD/BA, Design, Architecture, Engineering, QA, Data, Infra, Security, Management — inherits whatever decisions strategy, discovery made or skipped. The L3 distinction for this role is **discovery-as-asset** or **analysis-as-asset**: opportunity briefs, context packs, and **Decision Memory** entries are version-controlled artefacts that compound across engagements rather than slide decks that decay. This module trains you to produce that asset — and to consume it well when someone else hands one to you.

**Objectives**

- **Learn to do:** turn ambiguous business intent into a validated, decision-grade opportunity brief (Wide); apply the EPAM Agentic Transformation Framework (ATX) end-to-end on one bounded function to produce a CIO-ready transformation pack (Deep).

- **Skills (role):** opportunity framing with six-gate risk evaluation, commodity-vs-novel positioning, eval-shaped ROI rigour, Decision Memory authoring.

- **Skills (tooling):** multi-source research synthesis with provenance, primary-signal capture from transcripts, ROI modelling in spreadsheets, ATX cognitive-load mapping.

- **Outcome:** an exec-ready opportunity pack on Case A or B (Wide); an ATX transformation pack — CSA, redesign, viability, prototype brief, metrics, roadmap, business case (Deep); a Consulting/SME role-agent (Final Kata).

- **Tested by:** the Wide kata chain K 1.W.1–8 + the Final Kata K 1.3; the Deep path adds K 1.D.1–8.

**3 — Main processes**

The recurring workflows this role runs:

- **Engagement kickoff** — receive client goals, regulatory context, prior learnings; agree on scope and the decisions to be made.

- **Idea capture** — collect and document new product ideas, opportunities, or improvement suggestions from internal sources (sales conversations, support tickets, production signal, executive prompts, team retrospectives) and external sources (market feeds, analyst notes, customer interviews) into a structured idea backlog. Deduplicate against existing entries on intake.

- **Current-state assessment** — document the function as it runs today: as-is process, volume, FTEs, and baseline KPIs, with each pain point and gap tied to a named KPI deficit (which KPI sits below benchmark, by how much, costing how much per quarter). Produces the baseline the opportunity brief's value and ROI hypotheses are measured against.

- **Discovery cycle** — multi-source research → synthesis → opportunity framing → risk-gate evaluation → recommendation.

- **Opportunity assessment** — evaluate one or more candidate opportunities against the four (extended to six for AI-native) risk gates and produce a recommendation.

- **Handoff to PM/BA** — transfer the opportunity brief, context pack, and Decision Memory; clarify open questions; agree on what re-opens the brief.

- **Delivery advisory** — ongoing input through delivery on long engagements: monitor production signal and eval drift, surface scope-drift candidates, advise on go/no-go at stage gates, refresh the opportunity brief and Decision Memory when learning lands.

- **Outcome feedback** — once functionality ships, review what was built against the opportunity brief and provide structured feedback: does the implemented behavior match the value hypothesis, do measured outcomes (KPIs, eval scores, adoption signal) track the ROI hypothesis, and which gaps need a brief amendment, a context-pack update, or a new Decision Memory entry. The loop closes back into Continuous Discovery.

- **Continuous Discovery** — on long engagements, the discovery cycle becomes an ongoing rhythm: weekly customer-contact, monthly opportunity-backlog review, quarterly context-pack refresh, plus on-trigger reviews fired by market, regulatory, or production signal.

- **Cross-engagement reuse** — at engagement end, extract reusable assets (horizontal context-pack additions, prompt-library entries, eval-rubric refinements) into firm-level storage.

**4 — Role in classic SDLC**

The consultant/SME sits **upstream of PROD/BA** — at the engagement entry point in the SDLC. They receive from the client: business goals, regulatory context, prior delivery learnings, production signal from live systems. They hand off downstream:

- **To PROD/BA (Module 200):** the opportunity brief (value hypothesis, ROI hypothesis, risk-gate evaluation), the context pack, and Decision Memory entries.

- **To Design (Module 300):** the target customer segment and the binding-gate verdict that grounds personas and journeys.

- **To Architecture (Module 400):** the commodity-vs-novel positioning and the no-AI baseline that grounds build-vs-buy.

- **To Delivery & Management (Module 1000):** Decision Memory and the opportunity backlog for portfolio rollup.

Interfaces during the engagement: executive sponsors, regulatory/compliance counsel, finance, the client's internal product lead. The consultant/SME is also the role that says *"this isn't the right problem"* — the line nobody else in the SDLC is positioned to draw.

**5 — How the role changed with AI (general)**

Three shifts, at high level:

- **Collapsed:** the bottom-of-pyramid work — deck production, framework population, market-scan synthesis, research-only deliverables. LLMs and AI agents are competent at exactly the work the entry-level consultant used to do. Consulting deliverables without unique body of knowledge and data are now a commodity; the work that survives is judgment, calibration, and reusable artefacts.

- **Amplified:** depth, parallelism, source coverage. A consultant in 2026 can run three parallel research passes on different angles, surface contradictions a single pass smooths over, draft and stress-test five strategic framings in the time it used to take to populate one. Discovery throughput is higher than it has ever been.

- **Disappeared:** the slide deck as the deliverable. What survived is *discovery-as-asset* — opportunity briefs, context packs, prototypes-on-real-data — and the **Forward Deployed Engineering** posture that the asset is the artefact, not a slide about one.

**6 — What changed at L2 (AI-assistant)**

At L2, the human still owns the brief. AI is a copilot. The concrete tasks where AI assists:

- Multi-source aggregation across market reports, analyst notes, regulatory filings, support tickets, sales transcripts, production telemetry.

- First-pass theme extraction with verbatim source quotes attached.

- Opportunity-canvas drafting from interview snapshots.

- ROI-sketch generation with assumption ranges and sensitivity tables.

- Adversarial review and pre-mortem of the executive narrative.

- Drafting Decision Memory entries from meeting notes.

Stays human at L2 (the lines that do not move):

- **Problem selection** — which problem to solve, and which to deliberately *not* solve.

- **Value-hypothesis design** — the falsifiable claim, including the *"we will know we are wrong if"* clause.

- **ROI rigour** — the named business outcome with baseline, target, horizon, and measurement method.

- **Ethical boundaries** — what we will not build, regardless of business case.

- **Stakeholder trust** — the relational work that cannot be drafted.

- **Calibration** — distinguishing fluent AI output from accurate AI output.

**7 — What changed at L3 (AI-native)**

At L3 the work is restructured around agents and reusable assets. The role doesn't disappear; it gains reach. The concrete shifts:

- **SME-as-platform.** The vertical or horizontal SME stops being *"the person who knows"* and starts being *"the source of an artefact, context every downstream agent consumes."* Their domain knowledge is codified into a queryable, version-controlled industry context pack and data.

- **Discovery agents in the loop.** Continuous-discovery agents monitor production signal (usage patterns and statistics, data and metrics, agent traces, NPS) between engagements and surface candidate opportunities for human review — the consultant validates and frames, the agent does the watch.

- **Agentic Capabilities for Business.** The Agentic Transformation Framework by EPAM (ATX) that you will learn in Deep katas for this role apply to *client* functions also applies to the discovery function. Tasks classify as agent-led (multi-source aggregation, deduplication, draft synthesis), agent-assisted (canvas drafting, ROI sketching, narrative drafting), or human-only (problem selection, ethical go/no-go, stakeholder commitments).

- **New artefacts the role produces:**

  - A native-format role-agent (a Claude Skill or sub-agent) — the L3 cut on *"the SME's approach, written down and runnable."* When the SME is unavailable, the agent runs the discovery loop in their style.

  - A version-controlled context pack with named owner, refresh cadence, and retirement criteria.

  - A Decision Memory corpus the team consults (not a write-only artefact).

  - Eval rubrics for the briefs themselves — the L3 firm grades its own briefs the same way it grades the AI capabilities the briefs propose.

**Practice rule for every kata and the Final Kata in this module:** use a real, recurring task from your current project. If you don't have one, pick ONE Reference Case (§2 → Reference Cases) and stay on it across every kata so your artefacts compound on the same project. Switching cases mid-module breaks the carry-forward chain.

**Carry-Forward**

Two distinct artefacts leave this module.

**1 — Opportunity Brief (canonical, 14 fields)**

- **Artefact name:** Opportunity Brief.

- **Source:** assembled from Wide katas K 1.W.1 → K 1.W.8 (exec-ready opportunity pack) for non-specialists; extended by Deep katas K 1.D.1 → K 1.D.8 (ATX transformation pack) for specialists.

- **Consuming stage(s):**

  - **PROD/BA (Module 200)** — the brief becomes the input to spec co-creation; the value hypothesis seeds acceptance criteria; the ROI hypothesis seeds the eval criteria.

  - **Design (Module 300)** — grounds intent in the value hypothesis; personas reference the target customer segment; the binding-gate verdict shapes journey priorities.

  - **Architecture (Module 400)** — evaluates technical alternatives against the brief; commodity-vs-novel framing and the no-AI baseline shape build-vs-buy.

  - **Delivery & Management (Module 1000)** — rolls up opportunity-level decisions into portfolio view; Decision Memory connects to Module 1000's portfolio-scope Decision Memory. The brief's ROI hypothesis is *decision-grade* (pursue / don't); ongoing commercial and portfolio finance is owned by Module 1000 §10.7, not duplicated here (see §1.2 Deep Theory A5).

  - **Final Assembly Line (Module 1111)** — the brief is station 1 of the end-to-end agentic delivery scenario.

- **Format:** Markdown at /discovery/opportunity-brief.md in the engagement repo. 14 fields (see §1.2 Intermediate). Supporting artefacts (discovery prompt/agent, opportunity map, industry context pack, Decision Memory log, prototype brief (04-prototype-brief.md, Deep kata K 1.D.5), ATX transformation pack) live in the same repo and are linked from the brief.

**2 — Role-agent (native-format Skill or sub-agent)**

- **Artefact name:** Consulting/SME Role-Agent.

- **Source:** Final Kata K 1.3 (all learners). Deep learners extend the Wide-required seven fields with the four depth-add items nested in (Reserved Decisions, Escalation Triggers, Eval Rubric, bundled context pack).

- **Consuming stage(s):**

  - **Modules 200–1000** — each loads the agent from .claude/skills/ or .claude/agents/ when no consultant is on the team. It is consumed in place — read by other role-agents when they need consulting context, not transformed.

  - **Final Assembly Line (Module 1111)** — the agent roster is part of the portfolio handoff: a teammate joining the project reads .claude/skills/ and .claude/agents/ to see what role-agents already exist and what each is grounded to.

- **Format:** A single runnable agent file — .claude/skills/consulting-sme/SKILL.md (Skill) or .claude/agents/consulting-sme.md (sub-agent). Version-controlled, body ≤ 2 pages, with the minimal YAML frontmatter and the seven discoverable fields defined in Kata K 1.3, the guardrails (human-owned decisions) inline.

- **Engine guide target:** .ai-run/guides/project.md, under header \## Business context + scope guardrails (from Module 100 — Consulting/SME). This is the authoritative chain mapping; the spec's \<!-- chain:rules:start guide=… topic=… --\> delimiter attributes mirror it, and on any disagreement this line wins.

- **Optional stand-in override (Deep only):** none (no stand-in for this role).

The .claude/skills/ and .claude/agents/ paths are the Claude Code convention. Other coding agents use different directories — for example, GitHub Copilot uses .github/skills/ and .github/agents/. Adapt the path to whichever agent harness your team runs.

**Course Repo: <https://epa.ms/ai-run-26-curriculum-repo>**

**Why This Matters for You**

Consulting and SME work is the discovery at the front of the SDLC — the work that frames what's worth building before there's a backlog. Most teams have no consultant or subject-matter expert (SME) doing that for a whole project, yet **someone still has to produce what the role produces**, and AI agents now put that within reach of any role. So this block pays off even if you never hold the title:

- On a team with **no consultant** — delivery manager, BA, engineer, designer, architect, QA, data, infra, or security — you can run an AI-assisted discovery pass yourself: an opportunity brief, a thin industry context pack, a value hypothesis with its risk gates spelled out. These outputs were once the consultant's private currency; now they are a context pack the whole team shares.

- Doing it once **changes how you read the work that lands in your inbox**. The brief stops being a fixed input and becomes something you can pressure-test, extend, or rewrite when it's wrong.

- It also lets you **push back upstream**. When a brief is thin, you have the words for the gap — four risk gates, commodity vs novel, value hypothesis, falsifiability — so you object to the specific hole instead of only saying it feels off.

If your team *does* have a consultant or SME, the same 45 minutes still pays. You learn what a *good* brief looks like on the way in, you recognise an *"AI told us this is a great opportunity"* pitch for what it is, and you know which decisions stay human-owned no matter who runs the prompt.

🎓**Before you start — managerial on-ramp.** In a managerial role with beginner-level AI experience? [The EPAM AI RUN — Gen AI Introduction for AMs & BDMs course](https://kb.epam.com/pages/viewpage.action?pageId=2812808369&spaceKey=EPMGPT&title=Curriculum%2BAI%2BRUN%2BGen%2BAI%2BIntroduction%2Bfor%2BAMs%2BBDMs) is the recommended on-ramp: practical GenAI katas for non-technical specialists, a short overview of EPAM GenAI services, and an introduction to vibe coding with Lovable and Claude Code. You could take this learn course as additional study.

**Goal**

Equip every learner, whatever their role, to **name** what Consulting/SME contributes to L3 AI delivery, **tell** good discovery from bad on a real brief, and **work with** consultants and SMEs when their output feeds yours.

**Time**

~45 min.

**Audience**

Anyone *not* specialising in Consulting/SME — engineers, QAs, designers, PMs, architects, data, infra, security, management.

**Prerequisites**

The Onboarding and Fundamentals modules completed.

**Must Cover**

**Discovery is the gateway to the SDLC. A problem that enters badly here corrupts every stage downstream — and no amount of AI excellence further down the line makes up for it.**

**The Big Picture**

Consulting and SME work is the front door of the SDLC: it turns vague business intent into a decision — what's worth building, for whom, on what evidence — before a backlog exists. Every downstream stage inherits that decision, or inherits the gap where it should have been.

The deliverable is not a slide deck. It is an **opportunity brief** — a one-page, version-controlled artefact carrying a value hypothesis, an ROI hypothesis, and a risk read that PROD/BA, Design, and Architecture act on without re-running discovery. At L3 that brief, the industry context behind it, and the decisions that shaped it compound across engagements rather than decay with each deck.

What makes it non-trivial: AI now produces fluent discovery output cheaply, and fluent is not accurate. The skill that survives is knowing which judgments stay human, which risk actually kills the bet, and how to keep the breadth pass AI runs honest.

This section covers six topics, in the order you run them:

- **Where Consulting/SME creates value** — discovery is the SDLC gateway; keep it always-on, ground it in a vertical *and* a horizontal SME, and let AI run the breadth passes while humans keep problem selection.

- **Strategy lenses** — a real opportunity is named with two lenses (business: where to play; technology: reachable this year, and at what cost); one lens alone is the most common shallow brief.

- **The collaboration model** — what discovery takes in, the repo artefacts it produces, and the downstream stage that consumes each slice — with the named failure when that slice is thin.

- **Delivery boundaries & Responsible AI** — the external constraints the opportunity inherits, plus the Responsible-AI limits decided *here* at discovery, not patched at the security stage.

- **Ways of working** — discovery as a six-step procedure, run in order, then right-sized to the engagement.

- **Anti-patterns other roles can spot** — the tells of a weak brief, each paired with the push-back question that names the gap.

**Key Messages / Ideas**

- **Discovery is where work enters the SDLC. If it enters badly, no downstream AI excellence saves the project.**

- **AI doesn't choose problems. Humans choose problems; AI helps explore them.**

- **A Consultant and SME's L3 superpower is codifying domain knowledge into reusable context, not gatekeeping it.**

- **Continuous Discovery means the opportunity backlog is alive — refreshed by production signal, not frozen at kickoff.**

- **The four risk gates (value / usability / feasibility / viability) are how you tell a real opportunity from an AI-generated mirage.**

- **Consensus is a Decision Memory entry, not a meeting summary.**

- **A framed opportunity counts for nothing until it's a repo artefact a named downstream stage consumes. If recovering the context means booking time with you, the artefact doesn't exist yet.**

- **Eval-shaped metrics measure value; adoption-shaped metrics measure usage. Both go up; only the first justifies investment.**

- **Vertical and horizontal SMEs see different failure modes. A brief with only one consulted has a known blind spot.**

- **Responsible AI is a discovery-stage concern, not a security-stage cleanup.**

- **A real opportunity is named with two lenses — business (where to play) and technology (reachable this year, and at what cost). One lens alone is the most common shallow brief.**

- **Commodity vs novel is the strategic positioning question of 2026. Build what's novel, consume what's commodity, re-evaluate quarterly.**

- **A weak brief has tells any role can spot. Match the pattern, trace it to the principle it breaks, and ask the specific push-back question — not a vague "this doesn't feel right."**

**Structure (Per-topic context blocks)**

Each block elaborates one topic from the list above — mental model first, then the precise definition.

# Block 1 — Role context and where Consulting/SME creates value in L3

*The thread — discovery is the gateway → so it must be always-on → which works only if grounded in the right expertise (vertical + horizontal) → which is scarce, forcing triage → so the role shifts from knower to platform → and converges with engineering (FDE).*

This block is one argument, not a list of facts. Discovery is the gateway to the SDLC, and everything after follows from protecting it — keeping it always-on, grounding it in the right expertise, working around how scarce that expertise is, and drawing the line between what AI can carry and what it can't.

*1. The discovery stage as the gateway to the SDLC.* Discovery is the first stage where ambiguity turns into commitments — what problem is worth solving, for whom, on what value hypothesis, against what risks. A team can nail the architecture and still ship the wrong product, because discovery never pressure-tested the value hypothesis. It can have a solid eval suite and still move no business outcome, because the ROI hypothesis was a wish, not a claim you could prove wrong. **Enter badly here and every downstream stage inherits the damage** — no amount of later AI excellence buys it back.

*2. → Continuous Discovery as an L3 marker.* Because a bad frame spreads, you can't check the gateway once at kickoff and move on. The system never stops changing, so discovery can't either. That is what separates the maturity levels:

- **L1 — Ad hoc.** Research happens occasionally, usually to validate a decision someone already made.

- **L2 — Project-based.** A dedicated research phase at the start of each initiative. Outputs go stale the moment the project starts building.

- **L3 — Continuous.** Weekly contact with users and production signal, embedded in the team's rhythm. The opportunity backlog is alive — refreshed by what customers do, what tickets surface, what evals drift to. Discovery never ends because the system never stops changing.

<img src="media/image1.png" style="width:6.53125in;height:1.79348in" />

*3. → Vertical vs horizontal SMEs.* Always-on discovery only stays accurate if it sits on the right expertise — and that expertise comes in two forms that don't substitute for each other, so a strong brief usually consults both:

- **Vertical SMEs** know an industry — banking, pharma, retail, telco. They ground the opportunity in industry value drivers, regulatory context, and operating reality. They are the people who tell you the model's 97% accuracy is meaningless because the 3% it misses are the cases that trigger a regulator visit.

- **Horizontal SMEs** know a discipline that recurs across industries — HR, legal, finance, supply chain. They ground the opportunity in patterns that repeat across verticals.

Consult only vertical SMEs and you ship solutions that are domain-accurate but technically unsafe. Consult only horizontal SMEs and you ship technically clean solutions to the wrong problem. **When a brief names only one type consulted, that is the missing input.**

<img src="media/image2.png" style="width:6.70833in;height:3.23013in" />

*4. → SME availability and triage.* Consulting both is the ideal; delivery reality gets in the way. The two types are rarely available at the same depth — calendars are tight and the deepest people are over-booked. So the L3 move is to **triage SME time on purpose**, not pretend the constraint isn't there:

- Highest-risk briefs (regulated domains, novel tech, high-value unfamiliar segments) get *both* SME types — non-negotiable.

- Lower-risk briefs may proceed with *one* type — but the brief names which is missing and treats the absence as a known blind spot on the corresponding gate.

- The triage call is itself captured in Decision Memory.

*5. → The SME's evolving role.* That scarcity reshapes the role. The 2026 shift is from *"the person who knows things"* to *"the person whose knowledge feeds the agents"* — a bottleneck you can only clear in person doesn't scale, and written-down knowledge does. The L1–L2 SME is a bottleneck. The L3 SME has written the load-bearing knowledge down: an industry context pack the team and its agents can query, annotated examples that calibrate model output, decision rules for recurring edge cases, and a role-agent spec that runs the discovery loop in their style. The SME keeps the same authority; what changes is that the knowledge now works without them in the room.

*6. → Forward Deployed Engineering (FDE).* The same pressure that turns the SME into a context-provider also closes the gap between knowing the business and shipping against it. The pattern started at Palantir and has gone mainstream — Anthropic, OpenAI, and the big consulting firms have all adopted it for enterprise work. A **Forward Deployed Engineer (FDE)** is an engineer embedded at the client site who builds, deploys, and iterates on software right alongside the customer — blurring the line between product, consulting, and engineering.

*7. → Where AI adds value in discovery.* Put those shifts together and the split of work gets concrete. AI earns its place wherever breadth, aggregation, and first-pass synthesis dominate. The pattern across all three insight activities below is the same: **AI runs the breadth pass; the SME calibrates what matters.**

- **User Insights Analysis** — clustering and synthesis of qualitative and quantitative user data (interviews, support tickets, NPS verbatims, product-usage signal) to surface needs, behaviours, pain points, and opportunities. AI accelerates the clustering; the SME calibrates relevance. *(Practised in Kata K 1.W.3.)*

- **Competitor Analysis** — evaluation of competing products and solutions (features, positioning, pricing, strengths and weaknesses relative to the target opportunity). AI runs the breadth pass; the SME calibrates which threats are credible. *(Practised in Kata K 1.W.3.)*

- **Reference Analysis** — structured review of analogous solutions, industry examples, and best-practice patterns to learn from *before* committing — what worked, what failed, what was learned. AI accelerates the lookup; the SME calibrates which precedents actually transfer. *(Practised within the market scan in Kata K 1.W.2, and maintained as a named field in the industry context pack — see §1.2 Deep Theory A1.)*

The same breadth-then-calibrate split covers the supporting moves: multi-source aggregation, research synthesis with verbatim source quotes, opportunity mapping, prior-art lookup, framing assistance, ROI-hypothesis drafting, and stakeholder pre-read drafting.

*8. → Where AI does NOT add value in discovery.* The boundary is the other half of the same call. The judgments that decide what the discovery is *for* stay human: problem selection; go/no-go at ambiguous stage gates; ethical boundaries; building stakeholder trust; telling fluent output from accurate output.

<img src="media/image3.png" style="width:6.4375in;height:3.27772in" />

**The point:** Discovery is the gate the rest of the SDLC inherits. Keep it always-on, ground it in both a vertical and a horizontal SME, and let AI run the breadth passes while the human keeps problem selection and the go/no-go.

# Block 2 — Strategy lenses

*The thread — pick the business lens (where to play, how to win) → pair it with the technology lens (is the win reachable this year, and at what cost) → choose both deliberately and flag the one that's missing.*

Knowing where AI helps doesn't tell you what to point it at. Choosing what's worth pursuing is a framing decision, and two lenses sit at the front of any serious discovery: a *business* lens (where to play, how to win) and a *technology* lens (what can we do this year that we couldn't last year). A good brief uses both. A brief that uses only one is the most common shallow-discovery pattern.

*1. Business-strategy frames — pick deliberately rather than defaulting to whatever framework is in the deck library:*

- **Jobs to be Done (JTBD) / Outcome-Driven Innovation (Ulwick).** Reframes *"users want X"* into *"users are trying to get a job done, and they'll fire whatever solution doesn't do it."* For AI specifically, segment by **the decision the AI replaces, who currently owns it, and the cost of errors** — three categories with different oversight implications (standardised logic / contested logic / exploratory synthesis).

- **Working Backwards / PR-FAQ (Amazon).** A forcing function for value-hypothesis clarity *before* any build. The antidote to *"AI told us this is a great opportunity"*.

- **Playing to Win (Lafley & Martin).** Five-question cascade: aspiration / where to play / how to win / capabilities / management systems. Run the cascade against the use case, not the technology.

- **Blue Ocean Strategy (Kim & Mauborgne).** Useful when AI changes the cost of an attribute and reshuffles the competitive landscape — translation, summarisation, and generation have all collapsed in unit cost.

*2. → Technology-strategy frames.* The business lens decides where the win is; the technology lens decides whether it's reachable this year and at what cost:

- **Technology range** — no-AI baseline → classical ML → predictive ML → generative AI → agentic AI → multi-agent. A brief that proposes the most advanced option without naming the no-AI baseline is dodging the comparison.

- **Build vs buy vs consume** — build only what's differentiating, consume what's commodity, buy what's productised in between.

- **Wardley Mapping** is the spine for this lens. Plot solution components by visibility (top: user-facing → bottom: infrastructure) and evolution (left: Genesis → Custom-Built → Product → Commodity). **Build novel components, consume commodities, watch for evolution-driven disruption.** In 2026: frontier LLM APIs are approaching full commodity; context engineering and evals sit in the Custom-Built/Product transition; agent orchestration is moving from Genesis into Custom-Built.

- **Cost trajectory** — inference cost per token has fallen ~10× per year on frontier models since 2023; build-vs-buy math that assumed last year's prices is already wrong.

*3. → Choosing the lens.* This is why the two SME types matter again: vertical SMEs lean toward the business lens, horizontal SMEs toward the technology lens. A strong L3 brief consults both before naming the opportunity, and says out loud which is missing when only one is available. A named, two-lens opportunity is the first thing other roles can act on — which makes *what comes in and what goes out* the next question.

<img src="media/image4.png" style="width:6.48958in;height:2.8996in" />

**The point:** A real opportunity is named with two lenses — where the win is (business) and whether it's reachable this year and at what cost (technology). One lens alone is the most common shallow brief, so name which one is missing.

# Block 3 — Collaboration model

*The thread — take in the inputs → process them into a fixed set of output artefacts → kept in the repo, not in heads → each consumed by a specific downstream stage, with a named failure when the slice is thin.*

A framed opportunity is worth nothing until it moves. The collaboration model is the chain that moves it: what you take in, what you turn that into, and who downstream consumes the result — with a named failure at each interface.

*1. Inputs Consulting/SME expects.* Client/business context · business goals · market signals · prior delivery learnings · production signal from live systems (telemetry, eval results, support volume, NPS, churn cohorts, agent traces). The last is the L3 input most often missing in L2 teams: discovery without production signal is discovery against an idealised customer who doesn't exist.

*2. → Outputs Consulting/SME produces.* Those inputs turn into a fixed set of outputs — each a project artefact in the repo, not a slide in a deck:

- **Opportunity brief** — one page; problem, segment, value hypothesis, ROI hypothesis with named business outcome, four-gate risk evaluation, Responsible-AI section, commodity-vs-novel positioning. The canonical artefact.

- **Problem framing** — what's being solved, in customer language, with what's explicitly out of scope.

- **Value hypothesis** — a claim you can prove wrong. Format: *"For \[segment\], we believe that \[solution\] will move \[outcome\] by \[amount\] within \[horizon\] because \[mechanism\]. We will know we are wrong if \[signal\]."* The *"we will know we are wrong"* clause is the L3 cut.

- **ROI hypothesis with named business outcomes** — the value hypothesis in financial terms, with magnitude, horizon, and sensitivity assumptions.

- **Decision Memory** — an append-only log of significant decisions: context, alternatives, decision, rationale, confidence level, named downstream consumers, supersession links. The easiest way to keep one is a decision-NNN.md file per call — context, options, decision, rationale, rejected alternative, what would re-open it; the template carries the shape and a worked example. When AI drafts the entry, the draft must carry the rationale and the rejected alternative, not only the decision.

- **Industry Context Pack** — a bundled, queryable reference for a vertical or horizontal: regulatory map, canonical workflows and KPIs, terminology, integration map, known failure modes, recent customer research.

- **Role-agent** — a native-format Skill or sub-agent that runs the discovery loop. It encodes the SME's approach: what to ask, what sources to consult, how to weigh conflicting signals, what red lines never to cross.

*3. → Knowledge and content as project artefacts, not in heads.* The one-sentence test: *"we have a context pack and a Decision Memory in the repo,"* not *"we ran a workshop and people remember it."* If a teammate has to book time with you to recover the context, the artefact does not exist.

*4. → How discovery connects to downstream stages.* Artefacts in the repo matter only because specific stages consume them — and each consumes a specific slice of the brief, with a specific failure when that slice is thin:

1.  **PROD/BA (Module 200)** — consumes the value hypothesis and ROI hypothesis to seed acceptance criteria and eval criteria. Breaks when the value hypothesis can't be proved wrong: PROD/BA falls back to *"does what the brief says,"* and the team ships the spec, not the outcome.

2.  **Design (Module 300)** — consumes the target segment and the binding-gate verdict. Breaks when the usability gate was graded green by reflex: Design inherits an unexamined assumption and finds the gap in usability testing, too late and too expensive.

3.  **Architecture (Module 400)** — consumes the commodity-vs-novel framing and the no-AI baseline. Breaks when the brief skips the no-AI baseline: Architecture can't defend its options against *"why not do this without AI."*

4.  **Delivery & Management (Module 1000)** — consumes Decision Memory and the opportunity backlog. Breaks when Decision Memory is a meeting summary, not an artefact: portfolio decisions get made on the loudest voice rather than the recorded rationale.

The handoff that breaks most often is *"we did discovery"* → throws a slide deck over the wall → PM has to rediscover. The L3 fix: the deck is a *view* on the underlying artefacts, and the artefacts are what PROD/BA actually consumes.

<img src="media/image5.png" style="width:6.11856in;height:3.48958in" />

**The point:** A framed opportunity counts for nothing until it's a repo artefact some named downstream stage consumes. If recovering the context means booking time with you, the artefact doesn't exist yet.

# Block 4 — Delivery boundaries and Responsible AI

*The thread — name the external constraints the opportunity inherits → add the Responsible-AI limits discovery imposes on itself → then the risks of running discovery with AI in the loop → which bottom out at the decisions that never move to the model.*

The brief that moves downstream carries more than an opportunity — it carries the limits the opportunity has to live inside. Naming those limits is part of discovery, not a later compliance step, because the choices that create the risks are made here.

*1. Constraints to name in the brief.* Every opportunity inherits a constraint envelope. For EU and AI-related projects, for example, it includes:

- **Client confidentiality and IP boundaries** — what training data, prompts, outputs, and traces can leave which environments.

- **Regulatory context** — GDPR, EU AI Act, sectoral overlays, and the like.

- **Risk-tier classification under the EU AI Act** — prohibited / high-risk / limited-risk / minimal-risk. A brief that doesn't name the risk tier is missing a load-bearing constraint.

*2. → Responsible AI in discovery — not a security-stage cleanup.* Those constraints are imposed from outside; Responsible AI is the constraint discovery puts on itself. In 2026, the load-bearing Responsible-AI decisions happen at discovery, not at deployment. By the time security reviews the system, the design choices that produced the risks are already made and expensive to unwind. The Responsible-AI section names, for *this* opportunity: bias amplification · contestability · traceability of training data · environmental cost · displacement risk. **A generic compliance paragraph does not pass the section; opportunity-specific named risks with named mitigations do.**

*3. → Risks of the discovery process itself, amplified by AI.* The constraints and the Responsible-AI section are about the opportunity; the next set of risks is about the act of running discovery with AI in the loop — fluency that outpaces evidence:

- **Confirmation bias** — AI synthesis is fluent and confident, which is exactly what makes it dangerous: teams accept it because it reads well, not because it's been pressure-tested. Mitigation: run a *"what would contradict this finding"* pass on every AI-assisted synthesis.

- **Shallow framing** — AI fills in plausible content around a thin problem statement, hiding the thinness. Mitigation: do the problem framing *before* AI assistance.

- **Anchoring on the first opportunity AI surfaces** — generate three alternatives before evaluating any.

- **Provenance collapse** — structured extraction with a verbatim source quote attached to every claim.

*4. → Decision boundaries (human-owned).* Those process risks all point at the same floor: some decisions never move to the model. Problem selection · ethical go/no-go · scope · stakeholder commitments. These are negotiated by humans because they take contextual judgment that doesn't exist in any training corpus. With the gateway, the lenses, the collaboration model, and the boundaries established, the last block is the procedure itself — how you actually run a discovery from intake to handoff.

**The point:** The brief carries the limits the opportunity has to live inside. Responsible-AI risks are decided here at discovery, not patched at the security stage — and problem selection, ethics, scope, and stakeholder commitments never move to the model.

# Block 5 — Ways of working

*The thread — six stages, each feeding the next: (1) capture the idea → gather its evidence · (2) synthesise → frame the opportunity · (3) measure → gate · (4) position → right-size · (5) tell → agree · (6) advise through delivery. Two things run across all six: the delegation vocabulary and the SME-as-platform pattern.*

This block is the discovery procedure itself, written in the order you run it. An idea enters; it gets researched, then synthesised into findings; the findings are framed and quantified into a hypothesis; the hypothesis is measured for rigour, gated against risk, and positioned strategically; the whole thing is right-sized to the engagement, told as a story, locked into a decision, and advised through delivery. Each step hands its output to the next — skip one and the next has nothing solid to stand on. Two things run *across* every step rather than sitting at one of them, and close the block: the delegation vocabulary and the SME-as-platform pattern.

<img src="media/image6.png" style="width:6.33333in;height:1.29939in" />

*1. Capture the idea — then gather the evidence it needs to survive.* The pipeline starts here, because the opportunity backlog is only as good as what enters it. The L3 discipline:

- **Capture** — every idea source (internal sales conversations, support tickets, production signal, market feeds, executive prompts, retro outputs) has a named owner and a single structured intake path. Ideas land with provenance attached (who said it, when, in what context) — never as a one-line bullet floating in a backlog.

- **Deduplicate** — every new idea is checked against the existing backlog with an AI-led dedup pass. Near-duplicates are consolidated with a link to the surviving entry; partial overlaps are flagged for the SME, not auto-merged. **The dedup pass is a discrete activity, not an afterthought** — the failure mode is the same opportunity surfacing three times under different names, getting evaluated three times, and burning calendar.

- **Triage** — at the end of each intake cycle, ideas split into *evaluate now* / *queue with trigger* / *drop with rationale*. Drops are recorded in Decision Memory, not deleted — the next surge of the same idea finds the prior reasoning instead of re-litigating it.

**Gathering the evidence — separate streams, not blended.** An idea that survives triage needs evidence before it can be framed, and that evidence arrives in distinct streams: customer conversations · industry analyst material · regulatory updates · product-usage signal. Blend them and you lose the disagreement between sources, which is where the strategic insight usually lives. **Ingest separately, surface conflicts explicitly, and require the synthesis to resolve or name each conflict.**

*2. → Synthesise the evidence into findings — then frame it into an opportunity.* Never trust one source: separate streams are raw material; synthesis turns them into findings. The 2026 pattern: aggregate raw sources into one accessible repository with provenance preserved → three-pass synthesis (themes with verbatim quotes / tensions and contradictions / what is missing or unrepresented) → source-anchored output where every claim links to a specific source quote → human validation (a domain expert reviews the synthesis, not the raw inputs; their disagreement is the signal).

**Framing the opportunity — problem framing → value hypothesis → ROI, in that order.** Findings are not yet an opportunity; framing turns them into one, and the sequence is load-bearing. Skip to ROI without a value hypothesis and you get numbers without mechanism. Skip to a value hypothesis without problem framing and you get solutions to undefined problems. Without an ROI hypothesis tied to a named business outcome, **the brief is a wish list**.

*3. → Measure the claim credibly — then pressure-test it at the gates.* Eval-shaped vs adoption-shaped metrics is the L3 cut on ROI rigour: the ROI claim that framing produces is only as good as how you measure it.

- **Eval-shaped metrics:** versioned ground truth · treatment-and-control comparison · sampled human review. These measure whether the system is making the *right* decisions, and whether those decisions move the business outcome named in the ROI hypothesis. They answer the CFO's question: *"what does this number actually mean for the business?"*

- **Adoption-shaped metrics:** tokens consumed · queries answered · daily active users · satisfaction surveys. These measure whether the team uses the tool. Useful as a sanity check; dangerous as a value claim.

Three adoption metrics are now *systematically biased toward the wrong answer* in AI contexts: adoption goes up because the feature is ambient (not because it works); token consumption rises because the system is verbose (not because it creates value); satisfaction surveys rise because the AI is novel (not because outputs are better). **Both adoption-shaped and eval-shaped metrics go up; only the eval-shaped one is value.** Define the eval-shaped metric at discovery, not at launch.

<img src="media/image7.png" style="width:6.0625in;height:2.54788in" />

**Pressure-testing it — the four risk gates, concrete dimensions, not binary verdicts.** A measured opportunity still has to survive pressure-testing. The Cagan / SVPG taxonomy gives four gates, each carrying operational depth:

1.  **Value risk** — will the target segment want, use, and pay, and will it move the named outcome? **L3 discipline:** name what was validated, what was assumed, which user groups went unconsulted, what blind spots remain, and what evidence would later invalidate the opportunity. Most discovery can't fully validate adoption, so a green value verdict that hides its own blind spots overstates confidence.

2.  **Usability risk** — can the user figure out how to use it, and for AI specifically, can they calibrate trust and recover from errors? **Usability is more than interface design:** the gate carries a **change-management dimension** — who must change behaviour, what training is required, whether change management is funded, who owns adoption after delivery. *Usable* is not the same as *adopted*.

3.  **Feasibility risk** — can engineering build this with the available time, skills, technology, and data? For AI specifically, distinguish three tiers: **demo feasible** (controlled example) · **POC feasible** (limited sample data) · **operationally feasible** (real data, real access, real users, real integrations). **The L3 cut: the gate is graded at the operational tier or it isn't graded at all.**

4.  **Viability risk** — does this work for legal, finance, sales, marketing, brand, partner contracts, and unit economics? **Viability also carries operational timeline dependencies** — legal review, contracting, data-sharing approvals, procurement constraints, the budget-approval path, and whether the fixed delivery date is realistic. The common failure: legal or procurement delays eat project time, but the delivery end date doesn't move.

For AI-native opportunities, Deep Theory extends this taxonomy to **six gates** by adding **Model Risk** and **Data / Ethical Risk**. The Wide-level discipline is to know the four and grade with operational dimensions; the L3 specialist runs all six.

<img src="media/image8.png" style="width:6.27926in;height:3.61458in" />

For each opportunity, name the *dominant unresolved risk* — the one that, if it fails, kills the bet — and design the cheapest test that resolves it within 1–2 weeks. Define the pass/fail threshold *before* running the test. **Value risk demands user interviews. Feasibility risk demands a technical spike. Viability risk demands a finance / legal conversation.** The tag tells you which discovery activity actually de-risks the bet.

*4. → Position the opportunity — then right-size the discovery to the engagement.* An opportunity that clears the gates next needs a strategic position — commodity vs novel: build it, buy it, or consume it. Using Wardley evolution stages:

- **Novel (Genesis)** — uncertain, expensive, high failure rate, breakthrough potential. Move: build, accept risk. 2026 examples: fully autonomous multi-agent operations, AI-native operating models.

- **Custom Built** — emerging understanding, some successful implementations, customisation required. Move: build where differentiation is critical. 2026: domain-specific retrieval-augmented generation (RAG), eval infrastructure tied to specific outcomes, agent orchestration for novel workflows.

- **Product** — standardisation, multiple vendors, market competition. Move: buy or configure; compete on fit. 2026: agent frameworks, vector databases, eval platforms.

- **Commodity** — fully standardised, interchangeable, price-driven. Move: consume; don't build. 2026: frontier LLM inference, embeddings, basic transcription.

The L2 cut is recognising the categories; the L3 cut is **acting on them** — refusing to fund a custom build for a commodity component, refusing to consume a vendor offering for a differentiating component, re-evaluating quarterly.

<img src="media/image9.png" style="width:6.14322in;height:1.63542in" />

**Right-sizing it — the floor scales differently from the ceiling.** Everything above is the full shape, and not every engagement can carry it — so you right-size on purpose. The full L3 shape is right for strategic, high-risk, AI-heavy, regulated, or long-running engagements. **It is too heavy for short fixed-scope projects unless deliberately lightened.** *The floor is non-negotiable; the ceiling scales with project size, risk, and resources.*

| Tier                           | Typical duration | Mandatory floor                                                                                                                        | What scales up                                                                                  |
|--------------------------------|------------------|----------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------|
| Short fixed-scope              | ≤ 6 weeks        | One-page brief: problem, value hypothesis with blind spots, four-gate scan with binding gate, Responsible-AI one-liner, no-AI baseline | Skip industry context pack; skip full Decision Memory ceremony; defer continuous-discovery loop |
| Medium                         | 1–3 months       | Above + Decision Memory for binding decisions + a periodic discovery checkpoint (every ~2 weeks)                                       | Lightweight context pack                                                                        |
| Long-term                      | 3+ months        | Above + full six-gate evaluation + named refresh cadence + industry context pack with named owner                                      | Full forward-deployed prototype if budget allows                                                |
| Product / platform partnership | Ongoing          | Above + telemetry-driven continuous discovery + cross-engagement Decision-Memory retrieval                                             | The full L3 stack                                                                               |

What you lighten gets **named in a Decision Memory entry** — never silently skipped, never silently re-introduced.

*5. → Tell the story — then turn the room into a recorded decision.* A right-sized, gated, positioned opportunity still has to *land* with sponsors before anyone commits to it. AI fluency makes this both easier and more dangerous — polish gets mistaken for substance. Minimum communication payload: one-line vision · single value hypothesis · one before/after narrative. Storytelling is increasingly cited as a top leadership skill for 2026, precisely because AI has commoditised the surrounding artefacts; conviction, clarity, and the human voice are what's left to differentiate on.

**Recording the decision.** The story landing is not the same as the room agreeing. **Consensus is a Decision Memory entry, not a feeling** — the room going quiet is not agreement. The L3 move on a contested opportunity: frame the disagreement against the four risk gates (most disagreements collapse once the question becomes *"are we disagreeing about value, usability, feasibility, or viability?"*) → surface the binding constraint (what evidence would change the answer?) → capture the agreement (a Decision Memory entry naming who agreed, what was deferred, what triggers reopening, named downstream consumers).

*6. → Advise through delivery — the consultant's role after handoff.* A locked decision and the handoff to PROD/BA are not the end of the Consulting/SME engagement on long programmes. The L3 cut is that Consulting/SME stays *named, scheduled, and lightweight* through delivery, with three recurring duties:

- **Production-signal monitoring** — eval drift, hallucination rate, support-volume spikes, and agent-trace anomalies surface candidate re-opens of the brief; the consultant frames whether the signal warrants a refresh or a no-op.

- **Scope-drift detection** — when delivery learns that one part of the brief is wrong (the ROI sensitivity doesn't hold; the binding gate moved), the consultant updates the brief and writes the superseding Decision Memory entry — not the delivery lead, not the PM.

- **Stage-gate advisory** — at funding / promotion / decommission decisions, the consultant re-reads the brief against current evidence and recommends pursue / pivot / drop in writing. The recommendation is itself a Decision Memory entry.

**The point:** Discovery is a six-step procedure you run in order — capture, synthesise, measure-and-gate, position-and-right-size, tell-and-record, advise. Skip a step and the next has nothing solid to stand on. Right-size the weight to the engagement, and write down whatever you chose to lighten.

# Block 6 — Anti-patterns visible to other roles

*Not a sequence — a checklist. Each item below is a skim-and-match: spot it in a brief, trace it to the principle it violates above, and use the push-back question.*

These are patterns to call out constructively when you see them. Each maps to a specific failure of the principles above.

- **The *"AI told us this is a great opportunity"* pitch** — no risk gates evaluated, no source triangulation, no risk section. Push back with: *"which of the four gates is this strongest on, which is weakest, and what's the cheapest test for the weakest one?"*

- **Discovery as deliverable theatre** — a polished deck that would be hard to reuse and keep updated, no underlying artefacts, no Decision Memory. Push back with: *"where's the queryable artefact behind this slide?"*

- **SMEs hoarding context in their heads** — *"go talk to Tim"* is not a context pack. Push back with: *"if Tim's on holiday, can we still answer this?"*

- **Skipping discovery entirely because *"we already know what to build."*** Push back with: *"what's the value hypothesis we'd be wrong about, and what would tell us we're wrong?"*

- **Letting AI choose the problem** — problem selection is a human call; AI can rank the options, not own the decision to pursue one. Push back with: *"who decided this is worth solving, and what alternatives were considered?"*

- **ROI bullets that grade *activity* (queries answered) instead of *business outcome* (cost saved, revenue moved, risk lowered).** Push back with: *"what's the eval-shaped version of this number?"*

- **Vertical-only or horizontal-only SME staffing.** Push back with: *"which type of SME is missing from this brief?"*

- **Token consumption or adoption rate cited as success.** Push back with: *"if usage doubled tomorrow, what business outcome moves?"*

- **No no-AI baseline named.** Push back with: *"what's the no-AI version, and why is it worse?"*

- **The Responsible-AI section is a paragraph of generalities, not opportunity-specific risks.** Push back with: *"what specifically about this opportunity creates bias / contestability / traceability risk?"*

- **One-size-fits-all discovery.** Push back with: *"is the discovery weight matched to the engagement size, and what was deliberately lightened?"*

- **Demo feasible mistaken for operationally feasible.** Push back with: *"which tier — demo, POC, or operationally feasible — was the feasibility verdict made on, and what were the conditions?"*

- **Change management out of scope, adoption assumed.** Push back with: *"who owns adoption after delivery, what's the training plan, and is that role funded?"*

**The point:** These are the tells of a weak brief. Match the pattern, trace it to the principle it breaks, and use the specific push-back question — not a vague "this doesn't feel right."

**Anti-Patterns**

*Author-side patterns — what to avoid when you produce a brief. For patterns to call out in **others'** briefs (with push-back questions), see Block 6 above.*

- Trusting a single AI synthesis pass as *"the research"* → fluent output ships unchallenged, and the wrong frame spreads to every stage downstream.

- Producing opportunity briefs without an explicit value hypothesis → there's no claim to prove wrong, so the team ships the spec instead of the outcome.

- Shipping an opportunity brief with no Responsible-AI section → bias, contestability, and traceability surface at the security stage, where they're expensive to unwind.

- Mistaking activity (many opportunities surfaced) for insight (one opportunity worth pursuing) → calendar burns on triage with no bet actually placed.

- Skipping the *"where AI should NOT be applied"* call during discovery → the costly misfit is discovered in build, not in framing.

- Treating stakeholder agreement as captured because the meeting ended quietly → no Decision Memory entry, and the "consensus" evaporates the moment the question resurfaces.

- Picking a strategy framework by default (whatever's in the deck library) rather than by fit → the frame fits the deck, not the problem in front of you.

**Outcomes**

By the end of Wide Theory, the non-specialist can:

 Explain why discovery is an explicit, **always-on** stage in an L3 SDLC, distinguish a **vertical** from a **horizontal SME**, and name where AI runs the breadth pass versus where the human owns the call.

 Name an opportunity with both a business and a technology lens, choosing between named strategy frames (JTBD, Working Backwards, Playing to Win, Blue Ocean, Wardley) by fit to the problem.

 Reproduce a thin version of the role's outputs — opportunity brief, value hypothesis, ROI hypothesis tied to a business outcome — with AI on a team that has no consultant, and name the downstream stages that consume each.

 Identify the Responsible-AI risks a brief must name, and push back specifically when one lacks a value hypothesis, source trail, Responsible-AI section, or no-AI baseline.

 Pressure-test an opportunity through the four risk gates — naming the load-bearing one — tell eval-shaped from adoption-shaped metrics, and grade feasibility at the *demo / POC / operational* tier rather than the wrong one.

 Position an opportunity commodity-versus-novel with the right build / buy / consume move, right-size the discovery weight to the engagement, and move a contested call to a Decision Memory entry using the gates as shared vocabulary.

 Recognise the weak-brief anti-patterns in a real team and call them out with the specific push-back question.

<img src="media/image10.png" style="width:6.04167in;height:3.32115in" />

**Assessment Questions \[Optional\]**

**Awaiting Action**

5 minutes

What should be done

\*

**Knowledge Check (3 retrieval-practice questions)**

1.  **(Wide Theory)** Name the four risk gates Wide-level discovery evaluates, plus the two extension gates Deep-level discovery adds for AI-native opportunities. For each of the two extensions, name one concrete checklist item the brief must answer.

2.  **(Deep Theory)** Walk through *Discovery → Decision Memory → Actions → Backlog* on one example: name an opportunity, the Decision Memory entry, two named actions, and the backlog entry that traces back. Show how an auditor would chain from the backlog entry back to the original signal.

3.  **(Katas / Final Kata)** What does the Final-Kata role-agent require that a generic agent.md does not? Name three sections that make it project-grounded rather than role-generic, and one example of what *project-grounded* looks like in each section.

﻿

**Self-Reflection (2–3 comparison prompts against the L3 standard)**

1.  Compare your current discovery practice to the **discovery-as-asset** L3 standard set by this module. Of the artefacts your last engagement produced — opportunity briefs, context packs, Decision Memory entries, role-agent specs — which would survive past the engagement end, and which would decay because they live as slides, meeting notes, or in someone's head?

2.  Compare your team's current opportunity brief format (if one exists) to the 14-field canonical version in §1.2 Intermediate. Which fields are missing — and where does the gap show up downstream (PROD/BA spec ambiguity, Architecture build-vs-buy without a no-AI baseline, Compliance late surprises)?

3.  Honest self-evaluation on your Final-Kata role-agent: would it actually run on a teammate's machine without you in the room? If a teammate fed it a fresh Reference-Case task tomorrow, would the output be useful — or would it require you to re-explain the context?

﻿

**Type your answers into the "Answer" block:**

**Materials and Links**

**Not Started**

5 minutes

**Required Materials**

**Documents (canonical templates the module uses)**

- Opportunity brief template (14 fields including value hypothesis, six risk gates, ROI hypothesis with eval-shaped measurement, source trail, Responsible-AI section).

- Industry context pack template (vertical and horizontal variants).

- Decision Memory format — ADR shape adapted for discovery decisions.

- Eval rubric for opportunity briefs.

- NIST AI RMF *Govern / Map / Measure / Manage* cheat-sheet.

- EU AI Act risk-tier quick reference.

- *"Where AI should NOT be applied"* checklist from Module 020.

**Tools for AI-native discovery** — pick one per row. EPAM teams confirm allow-list status against the internal data-class matrix before pasting non-public material; external learners pick whichever vendor in each row they can access.

| Capability                                       | Tools                                                                                     | Use in this block                                                                                               |
|--------------------------------------------------|-------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------|
| Multi-source research synthesis                  | Perplexity Deep Research; ChatGPT / Claude / Gemini Deep Research modes; agentic browsers | Wide Katas 100.1.2 market scan, 100.1.4 use case generation; Deep Kata 100.2.2 CSA                              |
| Document-grounded research                       | NotebookLM                                                                                | Industry context pack drafting from curated PDFs, transcripts, internal docs                                    |
| Customer-feedback synthesis                      | Dovetail; Insight7; BuildBetter; Gong                                                     | Wide Kata 100.1.3 primary-signal synthesis (interviews, sales/support calls, NPS verbatims)                     |
| Call-transcript capture                          | Otter; Granola; Fireflies; Read.ai                                                        | Wide Kata 100.1.3 / Vertical-SME interview capture                                                              |
| Opportunity Solution Trees & discovery mapping   | Vistaly; Miro; FigJam                                                                     | Continuous-discovery scaffolding; OST authoring                                                                 |
| Wardley & strategic mapping                      | OnlineWardleyMaps; Miro; Lucidchart; ArcKit                                               | Strategy-lens framing; build-vs-buy and commodity-vs-novel mapping                                              |
| Context-pack & decision-memory storage           | Atlan; Guru; Document360; Confluence                                                      | Discovery-as-asset storage with refresh discipline and provenance                                               |
| Eval platforms                                   | Confident AI; Braintrust; LangSmith; Galileo                                              | Scoring opportunity briefs against the rubric; monitoring discovery-agent outputs                               |
| Continuous-discovery orchestration               | n8n; Make; LangGraph                                                                      | Scheduled refresh of context packs, production-signal triggers                                                  |
| Role-agent build (for the Final Kata role-agent) | Claude Skills; OpenAI Agents SDK; Anthropic Computer Use; Cursor / Claude Code subagents  | Building the Consulting/SME role-agent the Final Kata specs out; Deep Kata 100.2.5 optional vibe-code prototype |
| Spreadsheet / ROI modelling                      | Google Sheets; Excel                                                                      | Wide Kata 100.1.6 ROI sketch; Deep Kata 100.2.8 business case                                                   |

| Slide / narrative rendering   | Gamma; Google Slides; Beautiful.ai | Wide Kata 100.1.7 exec narrative; Deep Kata 100.2.8 5-slide exec pack |
|-------------------------------|------------------------------------|-----------------------------------------------------------------------|
| Process / roadmap diagramming | draw.io; Whimsical; Miro           | Deep Kata 100.2.2 process map; Deep Kata 100.2.7 roadmap              |

**Internal Knowledge (EPAM-specific)**

- Mature anonymised context packs from past EPAM engagements.

- EPAM AI-tool allow-list (data-class matrix) — canonical source for *"what can I paste where."*

- Internal AI-assisted research prompt library; Forward Deployed Engineering case studies.

- Consulting capability page on the internal playbook.

**External References — self-study shelf**

Organised by theme. Read at least one item from each cluster relevant to your engagement. The shelf is intentionally curated — pick depth, not breadth.

**Continuous Discovery & problem framing**

- [Teresa Torres — *Continuous Discovery Habits* and *Product Talk*](https://www.producttalk.org/). Canonical Opportunity Solution Tree source.

- [Tony Ulwick — *What Customers Want*](https://strategyn.com/jobs-to-be-done/) (Outcome-Driven Innovation / Jobs-to-be-Done).

- [Marty Cagan — Silicon Valley Product Group](https://www.svpg.com/). Origin of the four product risks.

- [Bryar & Carr — *Working Backwards*](https://www.workingbackwards.com/). The Amazon PR/FAQ as a forcing function.

**Strategic & landscape mapping**

- [Simon Wardley — *Wardley Maps*](https://learnwardleymapping.com/) (free under CC-BY-SA).

- [A.G. Lafley & Roger Martin — *Playing to Win*](https://www.playingtowin.com/). Five-question strategy cascade.

- W. Chan Kim & Renée Mauborgne — *Blue Ocean Strategy*. Reframing competitive landscapes by uncontested value attributes.

- Michael Porter — *Competitive Strategy* (Five Forces). Industry-structure baselining.

**Decision Memory & knowledge as asset**

- [Michael Nygard — *Documenting Architecture Decisions*](https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions) (2011). The ADR shape Decision Memory adapts.

- [ThoughtWorks Technology Radar — ADR entries](https://www.thoughtworks.com/radar). A decade of operator lessons.

- [AGENTS.md patterns](https://agentsmd.net/) (2026) — how project context for agents differs from ADRs.

**Forward Deployed Engineering & AI-native delivery**

- [Palantir — Forward Deployed Engineering](https://www.palantir.com/careers/forward-deployed-software-engineer/). Origin of the embedded engineer-consultant model.

- *Durkin, Minick, Gaikwad — AI-Native Software Delivery* (O'Reilly). Intent → Build → Operate.

- *OpenAI Frontier Alliances* (Feb 2026) and *Anthropic / Blackstone joint venture* (May 2026) announcements.

**Storytelling & communication**

- Cole Nussbaumer Knaflic — *Storytelling with Data*.

- Edward Tufte — *The Visual Display of Quantitative Information*.

- Stephen Few — *Now You See It* and *Information Dashboard Design*.

**Responsible AI & governance**

- [NIST AI Risk Management Framework (AI RMF 1.0)](https://www.nist.gov/itl/ai-risk-management-framework). The Govern / Map / Measure / Manage spine.

- [EU AI Act (Regulation 2024/1689)](https://artificialintelligenceact.eu/). Risk-tier rules for any EU-touching system.

- ISO/IEC 42001:2023 — AI management system standard.

- Singapore IMDA agentic-AI governance framework (January 2026).

- Margaret Mitchell et al. — *Model Cards for Model Reporting*.

- Timnit Gebru et al. — *Datasheets for Datasets*.

**Eval engineering for discovery**

- Eric Weber — *North-star metrics for AI data products* (2026).

- Hamel Husain — *Your AI product needs evals*.

**Context engineering**

- Anthropic engineering writing on context engineering (2025–2026).

- Atlan — *Context Engineering Framework for Enterprise AI* (2026).

**Consulting transformation — read at least one to calibrate the macro shift**

- *The Agent Architect* — *Consulting Deliverables Are Now a Commodity* (May 2026).

- *BCG AI Radar 2026* — annual benchmark on enterprise AI adoption.

- McKinsey *State of AI 2025*.

# Reference Cases (use if you have no current project)

Practice in this module runs against real project material. First choice is always your own current project — that is the highest-signal practice. The course maintains two standard fallback cases shared across every role module; full case details (scenario, stakeholders, scope, sample inputs) live at [reference-cases.md](https://eu.git.epam.com/airun-mission-26-ai-factory/curriculum/-/blob/main/modules/001-reference-cases.md).

**Pick ONE case and use it across every kata in this module.** The carry-forward chain only works if your artefacts compound on the same project. Switching cases mid-module breaks the chain.

- **Case A — Omnichannel Commerce Platform for a Global Retailer.** Meridian Retail Group unifies 22 country sites, 12 mobile apps, and 1,400 POS systems into a single headless commerce platform with shared identity, cart, and loyalty — 18 months, \$42M, no Big Bang cutover, strict EU/JP/US regulatory layer.

- **Case B — Cloud-to-Cloud Migration of 50 Legacy Applications.** Kepler Insurance must move 50 critical applications from AWS and on-prem to Azure within 18 months — \$31M remaining, zero downtime on claims, SOX-ready audit trail, 11 applications with no current owner.

**Recommended fit for Consulting/SME:** Case B is a slightly stronger fit when your engagement work centres on legacy / regulated / brownfield contexts; Case A is the stronger fit when it centres on customer-facing / multi-region opportunities. Both cases work — pick the one closer to your day job.

**Role-specific task menu:**

When a kata asks you to *"name a real, recurring task,"* pick from this menu — these are tasks the Consulting/SME role would actually handle on each case.

**Case A — recurring tasks for Consulting/SME on the Meridian engagement:**

- Frame the unified-identity-and-loyalty opportunity as a four-gate AI-aware brief with the EU/JP/US regulatory layer named (GDPR, CCPA, PCI-DSS L1, PSD2 SCA, local payment-method requirements).

- Run a vertical-vs-horizontal SME triage call for a regional GM's payment-method dispute (Italy / Japan); record the triage decision in Decision Memory.

- Sketch ROI for *next-best-offer* personalisation across the headless platform with **eval-shaped metrics** (versioned ground truth, treatment/control on comparable carts), not adoption-shaped ones.

- Run the no-AI baseline against the proposed AI personalisation for cross-channel marketing — what would the best human-only segmentation do, and at what unit cost?

- Author the Responsible-AI section for the unified-customer-identity feature — consent across 22 country sites, cross-border data flows, contestability when an identity merge is wrong.

**Case B — recurring tasks for Consulting/SME on the Kepler engagement:**

- Reverse-engineer the value hypothesis for the 11 owner-less applications (which migrate, which retire, which retain) and frame each as a one-page brief with named binding gate.

- Run a six-gate evaluation on an AI-assisted application-discovery agent against the 50-app portfolio — name the dominant residual risk and the cheapest test.

- Sketch ROI for an AI-assisted compliance-documentation pipeline (SOX / GDPR / HIPAA / LGPD / APPI) — name the eval-shaped metric and the no-AI baseline.

- Frame the *demo / POC / operationally feasible* verdict for the NOTIFY-WORKER-V2 mystery-traffic investigation; name the conditions that would move the verdict up a tier.

- Author a Decision Memory entry for the rehost-vs-replatform call on a Tier-2 application with no current owner — name the rejected alternative, the reopening trigger, and the named downstream consumer.
