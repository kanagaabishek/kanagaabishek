<div align="center">

<img src="./assets/hero.svg" width="100%" alt="Kanaga Abishek — engineering systems, software, and agentic AI" />

<a href="#about">ABOUT</a> ·
<a href="#selected-work">SELECTED WORK</a> ·
<a href="#open-source">OPEN SOURCE</a> ·
<a href="#defence-tech">DEFENCE TECH</a> ·
<a href="#experience">EXPERIENCE</a> ·
<a href="#connect">CONNECT</a>

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0A66C2?style=flat-square&logo=linkedin)](https://linkedin.com/in/kanaga-abishek)
[![LeetCode](https://img.shields.io/badge/LeetCode-1905_peak_rating-FFA116?style=flat-square&logo=leetcode&logoColor=black)](https://leetcode.com/u/abishek2981/)
[![Email](https://img.shields.io/badge/Email-Say_hello-EA4335?style=flat-square&logo=gmail&logoColor=white)](mailto:abishek2981@gmail.com)

</div>

---

<img src="./assets/terminal.svg" width="100%" alt="Animated terminal introduction" />

## About

I'm **Kanaga Abishek**, an Information Technology student at Chennai Institute of Technology (graduating 2028) and software engineering intern focused on the parts of software that get interesting under real constraints: **backend systems, distributed tracing, developer tooling, and agentic AI**.

I care about the why behind the code: the data model, the failure mode, the trade-off, and whether the result can be measured.

```text
FOCUS      Backend systems · Distributed systems · Agentic AI
BUILD      Java / Spring Boot · Python · MCP · OpenTelemetry
PROVE      Production impact · Merged open source · SIH 2025 winner
```

## Selected work

> Projects are presented as engineering case studies: the problem, the system design, and the result—not just a list of technologies.

<a id="selected-work"></a>

### 01 / Lumen — Distributed tracing from ingestion to insight

<img src="./assets/lumen-architecture.svg" width="100%" alt="Lumen distributed tracing ingestion architecture" />

**The question:** when a distributed request is slow, how do you identify the critical path instead of staring at a wall of spans?

I built a self-hosted tracing platform that ingests OpenTelemetry spans, stores them in Cassandra, reconstructs trace trees, and analyzes latency.

- **Ingestion:** OTLP/gRPC with a bounded queue between ingestion and storage.
- **Storage:** denormalized Cassandra schema designed around trace access patterns and write-heavy ingestion.
- **Analysis:** critical-path and bottleneck detection; interval merging computes self-time without double-counting parallel child spans.
- **Batching:** multi-threaded writers flush 500 spans every 100 ms.

`Java` `Spring Boot` `OpenTelemetry` `gRPC` `Cassandra` `Concurrency`

<details>
<summary><strong>Open the engineering notes</strong></summary>

**Design decision — decouple ingestion from persistence.** The bounded queue separates request ingestion from storage work and gives the writer layer control over batching. It also makes queue capacity and backpressure explicit design concerns.

**Analysis detail — self-time.** Child spans can overlap. Summing child durations naively can overcount time; merging child intervals before subtracting their union from the parent duration avoids double-counting.

**What this demonstrates:** ingestion pipelines, data modelling, concurrent batch writes, trace-tree algorithms, and latency analysis.

</details>

[Browse my repositories →](https://github.com/kanagaabishek?tab=repositories)

---

### 02 / Varys — An agent that investigates CI failures

<img src="./assets/varys-flow.svg" width="100%" alt="Varys agentic CI failure investigation flow" />

**The question:** why stop at labelling a failed build when an agent can gather evidence and investigate the likely cause?

Varys investigates Jenkins CI failures using multi-turn tool use rather than one-shot classification.

- Built an **MCP server** exposing CI information through four structured tools.
- Let the agent discover and chain tools dynamically over stdio.
- Correlated build history, test results, and commits to trace failures to likely causes—typically within five reasoning turns.

`Python` `MCP` `Agentic AI` `Jenkins` `Tool orchestration`

<details>
<summary><strong>Open the agent design notes</strong></summary>

The workflow is evidence-driven: gather CI context, inspect relevant test results and build history, correlate commits, then produce a cause-oriented explanation. MCP provides a structured tool boundary between the agent and CI data.

**What this demonstrates:** tool design, agent orchestration, multi-step reasoning, and integration with developer workflows.

</details>

[Browse my repositories →](https://github.com/kanagaabishek?tab=repositories)

---

### 03 / ZenoHosp — Production workflows across 23 hospitals

**The context:** hospital software has to fit real operational routines. The right feature starts with understanding how doctors and hospital staff work.

At **Zenlocare**, I led Pharmacy, Inventory, and Asset modules for ZenoHosp, a hospital management platform used across **23 hospitals**.

| Engineering work | Outcome |
|---|---|
| Production API performance | p95 latency reduced from **260 ms to 180 ms** — a **30.8% reduction** |
| Cross-app authentication | Built cookie-based SSO with stateless JWT, resolving subdomain login issues |
| Release delivery | Shipped **5 production releases in 6 months** |
| Product discovery | Worked directly with doctors and hospital staff to understand workflows before implementation |

`Java` `Spring Boot` `React` `PostgreSQL` `AWS` `JWT`

<details>
<summary><strong>Open the implementation notes</strong></summary>

My work spanned schema and API design, frontend workflows, authentication across applications, production performance, and iterative releases. The p95 figure is a before/after measurement across production workflows; retain it only if you can explain the measurement window and how it was collected in an interview.

</details>

---

### 04 / Bond — Secure communication for defence use cases

**The problem:** sensitive communication needs controlled access and practical coordination, with administrative oversight.

Bond combines role-based access, encrypted messaging through Matrix, and real-time audio/video through LiveKit.

- Implemented Admin → Officer → Family access roles, with HQ-only account creation.
- Integrated LiveKit with a Matrix (Synapse) homeserver.
- Added admin monitoring features following discussions with Ministry of Defence and Army Cyber Group of India officials, who tested the solution and provided security and oversight feedback.

**Recognition:** 🏆 **Smart India Hackathon 2025 — National Winner**, Ministry of Defence problem statement.

`Node.js` `React` `Matrix/Synapse` `LiveKit` `Azure`

<details>
<summary><strong>My role and the defence-tech experience</strong></summary>

My contribution focused on access control, administrative workflows, and integration. The team received feedback from officials who tested the solution. I do not claim authorship of the underlying cryptographic protocols.

The most valuable part of the experience was learning that defence software must account for operational constraints, permission boundaries, oversight, and the realities of its intended users—not only feature completeness.

</details>

---

## Open source

<a id="open-source"></a>

### Jenkins OpenTelemetry Plugin — merged contribution

**Bug:** plugin icons rendered inconsistently across Jenkins themes.

**Fix:** migrated the OpenTelemetry and six observability-backend icons to Jenkins' theme-aware OSS Symbols, updated Java descriptors and Jelly views, and removed legacy icon registrations. The contribution was **reviewed and merged upstream**.

`Java` `Jenkins` `Jelly` `OpenTelemetry` `OSS contribution`

[Find my GitHub contributions →](https://github.com/kanagaabishek?tab=contributions)

---

## Experience

<a id="experience"></a>

<details open>
<summary><strong>Zenlocare — Software Engineering Intern</strong> · Feb–Jul 2026</summary>

- Led Pharmacy, Inventory, and Asset modules for ZenoHosp, used across 23 hospitals.
- Built cookie-based SSO with stateless JWT across applications.
- Reduced p95 response latency by 30.8%, from 260 ms to 180 ms.
- Shipped five production releases in six months.

**Stack:** Java · Spring Boot · React · PostgreSQL · AWS

</details>

<details>
<summary><strong>Kryptos Technology — Software Development Intern</strong> · Nov–Dec 2025</summary>

- Optimized production Spring Boot endpoints with request deduplication and caching, cutting redundant API calls by 12%.
- Engineered an MCP-powered agentic workflow to analyze logs and trace backend failures across distributed services.
- Exposed operational metrics and database execution states as structured tools, enabling multi-step debugging tasks.

**Stack:** Java · Spring Boot · AWS · MCP · Agentic AI

</details>

---

## Recognition

<div align="center">

| 🏆 Achievement | Evidence |
|:---|:---|
| **SIH 2025 — National Winner** | Ministry of Defence problem statement |
| **aOS Global Buildathon — Runner-up** | $1,500 award for NeoSlot |
| **MariaDB Hackathon — Finalist** | 25 finalists from 2,500+ participants |
| **LeetCode Knight** | 500+ solved · peak rating 1905 · top 4.57% |

</div>

## The toolbox

**Languages** · Java · Python · SQL · JavaScript

**Backend & data** · Spring Boot · FastAPI · Node.js · PostgreSQL · MySQL · MariaDB · Cassandra

**Systems** · Distributed tracing · OpenTelemetry · gRPC · Concurrency · API performance

**AI & automation** · Agentic AI · MCP · RAG · Tool orchestration

**Infrastructure** · AWS · Azure · Docker · GitHub Actions

## GitHub activity

<div align="center">
  <img width="49%" src="https://github-readme-stats.vercel.app/api?username=kanagaabishek&show_icons=true&hide_border=true&theme=transparent&rank_icon=github" alt="GitHub stats" />
  <img width="49%" src="https://github-readme-stats.vercel.app/api/top-langs/?username=kanagaabishek&layout=compact&hide_border=true&theme=transparent" alt="Top languages" />
</div>

<div align="center">
  <img width="90%" src="https://github-readme-activity-graph.vercel.app/graph?username=kanagaabishek&bg_color=00000000&color=8B9CF6&line=22D3EE&point=C4B5FD&area=true&hide_border=true" alt="Contribution activity graph" />
</div>

## Connect

<a id="connect"></a>

If you're working on backend infrastructure, observability, developer tooling, or practical agentic AI, I'd be glad to connect.

<div align="center">

[![GitHub](https://img.shields.io/badge/GitHub-Explore_my_code-181717?style=for-the-badge&logo=github)](https://github.com/kanagaabishek)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0A66C2?style=for-the-badge&logo=linkedin)](https://linkedin.com/in/kanaga-abishek)
[![Email](https://img.shields.io/badge/Email-Start_a_conversation-EA4335?style=for-the-badge&logo=gmail&logoColor=white)](mailto:abishek2981@gmail.com)

<sub>Built around systems, evidence, and the engineering behind the result.</sub>

</div>
