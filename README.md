<!-- HERO BANNER -->
<p align="center">
  <img src="./assets/banner.svg" alt="KANAGA ABISHEK B - Distributed Systems &amp; Agentic AI Developer" width="100%" />
</p>

<!-- TYPEWRITER -->
<p align="center">
  <img src="./assets/typewriter.svg" alt="Typewriter Identity" width="100%" />
</p>

<br/>

<!-- TERMINAL DASHBOARD -->
<div align="center">
  <table>
    <tr>
      <td align="center" width="45%" valign="top">
        <img src="./assets/portrait.svg" alt="Kanaga Abishek B Terminal Portrait" width="100%" />
      </td>
      <td align="center" width="55%" valign="top">
        <img src="./assets/info.svg" alt="Kanaga Abishek B Info Terminal" width="100%" />
      </td>
    </tr>
  </table>
</div>

<br/>

<!-- CONTRIBUTION ACTIVITY -->
<div align="center">
  <picture>
    <source
      media="(prefers-color-scheme: dark)"
      srcset="https://raw.githubusercontent.com/kanagaabishek/kanagaabishek/output/github-contribution-grid-snake-dark.svg"
    />
    <source
      media="(prefers-color-scheme: light)"
      srcset="https://raw.githubusercontent.com/kanagaabishek/kanagaabishek/output/github-contribution-grid-snake.svg"
    />
    <img
      alt="GitHub contributions activity"
      src="./assets/contributions.svg"
      width="100%"
    />
  </picture>
</div>

<br/>

<!-- ABOUT ME -->
## <img src="https://cdn.simpleicons.org/readme/00E8FF" width="24" height="24" alt=""/> About Me

🏆 **Smart India Hackathon 2025 — National Winner, Ministry of Defence** for Bond, a secure defence communication platform.

🎓 B.Tech IT @ Chennai Institute of Technology '28 · **LeetCode Knight** · 1905 peak rating.

💻 Building with **Java, Spring Boot, Agentic AI, MCP, and Distributed Systems**. Open-source contributor to the Jenkins OpenTelemetry Plugin, with a merged upstream contribution.

**Interests:** Java internals · Autonomous AI agents · Backend architecture · Observability · Open Source

---

<!-- EXPERIENCE -->
## <img src="https://cdn.simpleicons.org/target/00E8FF" width="24" height="24" alt=""/> Experience


<!-- FEATURED PROJECTS -->
## <img src="https://cdn.simpleicons.org/gnubash/00E8FF" width="24" height="24" alt=""/> Featured Projects

### Lumen — Distributed Tracing System
A self-hosted, high-throughput distributed tracing alternative to Jaeger and Zipkin designed for high-concurrency span ingestion, bottleneck detection, and granular execution path breakdown.
- Ingests OpenTelemetry spans over both **gRPC** and **HTTP**, storing them in **Apache Cassandra** via a denormalized schema specifically engineered to eliminate hot partitions under heavy write loads.
- Added latency analysis that pinpoints the critical path, bottlenecks, and idle gaps in slow traces, using interval merging to compute self-time without double-counting parallel child calls.
- Decoupled ingestion from storage with a bounded queue and multi-threaded background workers that batch-flush **500 spans every 100 ms**, protecting upstream services from storage backpressure.

*Focus: Distributed Systems • Java • Spring Boot • gRPC • Apache Cassandra • OpenTelemetry*  
<p align="left">
  <a href="https://github.com/kanagaabishek">
    <img src="https://img.shields.io/badge/GitHub-Repository-black?style=for-the-badge&logo=github" alt="Lumen Repository"/>
  </a>
</p>

---

### Varys — Autonomous Agentic CI Failure Investigator
An intelligent autonomous agent that investigates complex Jenkins CI/CD build failures through dynamic multi-turn reasoning and tool use rather than brittle one-shot prompt classification.
- Designed and deployed an MCP server exposing CI test logs, build artifacts, and commit histories as **4 structured tools** discoverable and chained dynamically over `stdio`.
- Traces failures to their root cause by correlating build history, test regressions, and commit diffs, typically resolving issues within **5 reasoning turns**.

*Focus: Agentic AI • Model Context Protocol (MCP) • Python • Jenkins CI • Automated Debugging*  
<p align="left">
  <a href="https://github.com/kanagaabishek">
    <img src="https://img.shields.io/badge/GitHub-Repository-black?style=for-the-badge&logo=github" alt="Varys Repository"/>
  </a>
</p>

---

### Bond — Secure Defence Communication Platform
An invite-only, end-to-end encrypted military communication platform built for secure hierarchical coordination between command centers, operational officers, and military personnel.
- **Smart India Hackathon 2025 National Winner**: Evaluated, security-tested, and awarded **₹1,50,000** by officials from the **Ministry of Defence** and **Army Cyber Group of India**.
- Implemented strict role-based access control (`Admin → Officer → Family`) with HQ-only cryptographic account provisioning and administrative monitoring features.
- Integrated **LiveKit** alongside a self-hosted **Matrix (Synapse)** homeserver to deliver low-latency encrypted audio/video calling on top of federated messaging.

*Focus: Def-Tech • Secure Communications • Node.js • React • Matrix (Synapse) • LiveKit • Azure • RBAC*  
<p align="left">
  <a href="https://github.com/kanagaabishek">
    <img src="https://img.shields.io/badge/GitHub-Repository-black?style=for-the-badge&logo=github" alt="Bond Repository"/>
  </a>
</p>

---

### Jenkins OpenTelemetry Plugin — Open Source Contribution
Upstream contribution to the official Jenkins observability ecosystem fixing theme inconsistency across modern UI themes ([Issue #1150](https://github.com/jenkinsci/opentelemetry-plugin)).
- Fixed icon rendering issues across dark and light Jenkins themes by adding Jenkins' OSS Symbols dependency and migrating the core OpenTelemetry icon plus six observability backend icons to theme-aware symbols.
- Updated affected Java descriptors and Jelly views, removing legacy icon registrations; contribution was reviewed and merged upstream.

*Focus: Open Source • Java • Jenkins • Observability • Theme-Aware Symbols*

---

<!-- TECH STACK -->
## <img src="https://cdn.simpleicons.org/codersrank/00E8FF" width="24" height="24" alt=""/> Tech Stack

**Languages**  
![Java](https://img.shields.io/badge/Java-ED8B00?style=flat-square&logo=openjdk&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![SQL](https://img.shields.io/badge/SQL-4479A1?style=flat-square&logo=postgresql&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=flat-square&logo=javascript&logoColor=black)
![TypeScript](https://img.shields.io/badge/TypeScript-3178C6?style=flat-square&logo=typescript&logoColor=white)
![C++](https://img.shields.io/badge/C++-00599C?style=flat-square&logo=cplusplus&logoColor=white)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=flat-square&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=flat-square&logo=css3&logoColor=white)

**Frameworks & Libraries**  
![Spring Boot](https://img.shields.io/badge/Spring_Boot-6DB33F?style=flat-square&logo=springboot&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=flat-square&logo=fastapi&logoColor=white)
![Node.js](https://img.shields.io/badge/Node.js-339933?style=flat-square&logo=nodedotjs&logoColor=white)
![React](https://img.shields.io/badge/React.js-20232A?style=flat-square&logo=react&logoColor=61DAFB)
![Next.js](https://img.shields.io/badge/Next.js-000000?style=flat-square&logo=nextdotjs&logoColor=white)
![Express.js](https://img.shields.io/badge/Express.js-000000?style=flat-square&logo=express&logoColor=white)

**Databases, Storage & Streaming**  
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1?style=flat-square&logo=postgresql&logoColor=white)
![Cassandra](https://img.shields.io/badge/Apache_Cassandra-1287B1?style=flat-square&logo=apachecassandra&logoColor=white)
![MySQL](https://img.shields.io/badge/MySQL-4479A1?style=flat-square&logo=mysql&logoColor=white)
![MariaDB](https://img.shields.io/badge/MariaDB-003545?style=flat-square&logo=mariadb&logoColor=white)
![MongoDB](https://img.shields.io/badge/MongoDB-47A248?style=flat-square&logo=mongodb&logoColor=white)

**Systems, Observability & Agentic AI**  
![Distributed Systems](https://img.shields.io/badge/Systems-Distributed_Systems-6366F1?style=flat-square&logo=databricks&logoColor=white)
![OpenTelemetry](https://img.shields.io/badge/Observability-OpenTelemetry-7F52FF?style=flat-square&logo=opentelemetry&logoColor=white)
![gRPC](https://img.shields.io/badge/Protocols-gRPC-244c5a?style=flat-square&logo=grpc&logoColor=white)
![MCP](https://img.shields.io/badge/Agentic_AI-Model_Context_Protocol-00C9FF?style=flat-square&logo=anthropic&logoColor=white)
![RAG](https://img.shields.io/badge/AI-Retrieval_Augmented_Gen-FF6F00?style=flat-square&logoColor=white)

**Cloud, DevOps & Tools**  
![AWS](https://img.shields.io/badge/AWS-232F3E?style=flat-square&logo=amazonaws&logoColor=white)
![Azure](https://img.shields.io/badge/Azure-0078D4?style=flat-square&logo=microsoftazure&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white)
![Git](https://img.shields.io/badge/Git-F05032?style=flat-square&logo=git&logoColor=white)
![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-2088FF?style=flat-square&logo=githubactions&logoColor=white)
![Jenkins](https://img.shields.io/badge/Jenkins-D24939?style=flat-square&logo=jenkins&logoColor=white)
![Postman](https://img.shields.io/badge/Postman-FF6C37?style=flat-square&logo=postman&logoColor=white)

---

<!-- EDUCATION & CERTIFICATIONS -->
## <img src="https://cdn.simpleicons.org/googleclassroom/00E8FF" width="24" height="24" alt=""/> Education &amp; Certifications

- 🎓 **B.Tech, Information Technology** — *Chennai Institute of Technology (CIT)* (Expected: May 2028 | **CGPA: 8.1/10**)
- 📜 **Amazon: Data Structures and Algorithms** — *Algorithmic problem solving, asymptotic complexity, advanced data structures*
- 📜 **Amazon: Programming with Java** — *OOP principles, multithreading, concurrency models, Java collections framework*
- 📜 **NPTEL, IIT: Data Analytics with Python** — *Statistical modeling, exploratory data analysis, numerical computing*

---

<!-- COMPETITIVE PROGRAMMING & CONTEST STATS -->
## <img src="https://cdn.simpleicons.org/github/00E8FF" width="24" height="24" alt=""/> Competitive &amp; Contest Stats

<div align="center">
  <table>
    <tr>
      <td align="center" width="50%" valign="top">
        <a href="https://leetcode.com/u/abishek2981/">
          <img src="./assets/competitive.svg" alt="Competitive Programming Metrics" width="100%" />
        </a>
      </td>
      <td align="center" width="50%" valign="top">
        <a href="https://github.com/kanagaabishek">
          <img src="./assets/competitions.svg" alt="Hackathons and Competitions" width="100%" />
        </a>
      </td>
    </tr>
  </table>
</div>

<br/>

<!-- LIVE LEETCODE CONTEST CARD -->
<div align="center">
  <a href="https://leetcode.com/u/abishek2981/">
    <img src="https://leetcard.jacoblin.cool/abishek2981?theme=nord&font=Fira%20Code&ext=contest" alt="LeetCode Contest Card" width="100%" />
  </a>
</div>

<br/>

---

<!-- HONORS & ACHIEVEMENTS -->
## <img src="https://cdn.simpleicons.org/sublimehacker/00E8FF" width="24" height="24" alt=""/> Honors, Hackathons &amp; Leadership

- 🏆 **Smart India Hackathon 2025 — National Winner (Ministry of Defence)**  
  *Dec 2025* | Awarded **₹1,50,000** for building **Bond**, a defence-grade secure communication platform with hierarchical RBAC, LiveKit real-time calling, and Matrix-encrypted messaging.
- 🥈 **aOS Global Buildathon 2025 — Runner-up**  
  *Aug 2025* | Awarded **$1,500** for building **NeoSlot**, a decentralized Web3 NFT marketplace platform.
- 🎯 **MariaDB Hackathon 2025 — Finalist**  
  *Sep 2025* | Selected as one of **25 finalists out of 2,500+ participants** worldwide for distributed database architecture.
- 🤝 **Co-organizer — HackSymmetric ’26**  
  A 48-hour national hackathon at Chennai Institute of Technology conducted in collaboration with **Unstop** and **Major League Hacking (MLH)**.
- ⚡ **Event Coordinator — Runtime Terror**  
  A national-level competitive programming and coding contest organized as part of **Trojans ’25**, coordinating technical problem curation and platform operations.

---

<!-- CONNECT WITH ME -->
## <img src="https://cdn.simpleicons.org/googlechrome/00E8FF" width="24" height="24" alt=""/> Connect With Me

<div align="center">

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Kanaga_Abishek_B-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://linkedin.com/in/kanaga-abishek)
[![LeetCode](https://img.shields.io/badge/LeetCode-abishek2981-FFA116?style=for-the-badge&logo=leetcode&logoColor=black)](https://leetcode.com/u/abishek2981/)

</div>
