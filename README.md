<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:38bdf8,50:7c3aed,100:0d1117&height=220&section=header&text=Soumya%20Chakraborty&fontSize=42&fontColor=ffffff&animation=fadeIn&fontAlignY=35&desc=Full-Stack%20Engineer&descSize=18&descAlignY=55&descAlign=50"/>

<br/>

<a href="https://chksoumya.in">
<img src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&weight=600&size=15&duration=2800&pause=800&color=38BDF8&center=true&vCenter=true&multiline=true&width=720&height=60&lines=building+Phygital-Trace+%E2%80%94+camera+to+blockchain+media+provenance;architecture+first.+code+second.+ship+always."/>
</a>

<br/>

[![Portfolio](https://img.shields.io/badge/-chksoumya.in-0d1117?style=for-the-badge&logo=vercel&logoColor=38bdf8)](https://chksoumya.in)&nbsp;
[![Email](https://img.shields.io/badge/-soumya.chk101@gmail.com-0d1117?style=for-the-badge&logo=gmail&logoColor=EA4335)](mailto:soumya.chk101@gmail.com)&nbsp;
[![GitHub](https://img.shields.io/badge/-soumyachk101-0d1117?style=for-the-badge&logo=github&logoColor=white)](https://github.com/soumyachk101)&nbsp;
[![LinkedIn](https://img.shields.io/badge/-LinkedIn-0d1117?style=for-the-badge&logo=linkedin&logoColor=0A66C2)](https://linkedin.com/in/soumyachk101)

<br/>

<img src="https://komarev.com/ghpvc/?username=soumyachk101&style=for-the-badge&color=38bdf8&label=Profile+Views" alt="profile views"/>

</div>

<br/>

<!-- ═══════════════════════════════════════════════════════════════════ -->

<table width="100%" border="0">
<tr>
<td width="55%" valign="top">

```typescript
// identity.ts — 2026

export const engineer = {
  name:     "Soumya Chakraborty",
  role:     "Full-Stack Engineer",
  base:     "West Bengal, India 🇮🇳",
  status:   "B.Tech CSE · 2nd Year",
  campus:   "NSHM Knowledge Campus, Durgapur",

  principles: [
    "you can't design what you don't understand",
    "schema mistakes compound — model data first",
    "shipped and imperfect > perfect and imaginary",
    "the best abstraction is the one you don't write",
  ],

  obsessions: [
    "distributed systems & eventual consistency",
    "media provenance & trustless verification",
    "AI-native developer tooling",
    "making complex systems feel simple",
  ],

  currentlyBuilding: "Phygital-Trace 🔗",
  openTo: [
    "meaningful open-source work",
    "real product collaborations",
    "architecture conversations",
  ],
} as const;
```

</td>
<td width="4%"></td>
<td width="41%" valign="top" align="center">

<br/>

<img src="https://user-images.githubusercontent.com/74038190/212749447-bfb7e725-6987-49d9-ae85-2015e3e7cc41.gif" width="330"/>

</td>
</tr>
</table>

<br/>

<!-- ═══════════════════════════════════════════════════════════════════ -->
<!--                      MY WORKFLOW / PROCESS                        -->
<!-- ═══════════════════════════════════════════════════════════════════ -->

<div align="center">
<img src="https://user-images.githubusercontent.com/74038190/235224431-e8c8c12e-6826-47f1-89fb-2ddad83b3abf.gif" width="280"/>

## ⚡ &nbsp; My Workflow

</div>

<br/>

```mermaid
graph LR
    A["🧠 Understand<br/>Map the domain"] --> B["📐 Architect<br/>Schema + boundaries"]
    B --> C["⚡ Build<br/>Ship the thing"]
    C --> D["🔍 Iterate<br/>Prod teaches everything"]
    D --> A

    style A fill:#0d1117,stroke:#38bdf8,stroke-width:2px,color:#38bdf8
    style B fill:#0d1117,stroke:#7c3aed,stroke-width:2px,color:#7c3aed
    style C fill:#0d1117,stroke:#38bdf8,stroke-width:2px,color:#38bdf8
    style D fill:#0d1117,stroke:#7c3aed,stroke-width:2px,color:#7c3aed
```

<br/>

<table width="100%" border="0">
<tr>
<td width="25%" align="center">

<img src="https://user-images.githubusercontent.com/74038190/212284158-e840e285-664b-44d7-b79b-e264b5e54825.gif" width="50"/>

**`01 — Understand`**

Map domain concepts before opening the IDE.

</td>
<td width="25%" align="center">

<img src="https://user-images.githubusercontent.com/74038190/212284100-561aa473-3905-4a80-b561-0d28506553ee.gif" width="50"/>

**`02 — Architect`**

Schema & boundary mistakes compound silently.

</td>
<td width="25%" align="center">

<img src="https://user-images.githubusercontent.com/74038190/212749447-bfb7e725-6987-49d9-ae85-2015e3e7cc41.gif" width="50"/>

**`03 — Ship`**

An imperfect v1 beats a perfect imaginary one.

</td>
<td width="25%" align="center">

<img src="https://user-images.githubusercontent.com/74038190/212284081-bbe51290-556b-4562-8249-17c9ba0d3112.gif" width="50"/>

**`04 — Own It`**

Read the source. Know *why* it works.

</td>
</tr>
</table>

<br/>

<!-- ═══════════════════════════════════════════════════════════════════ -->
<!--                         FEATURED PROJECTS                         -->
<!-- ═══════════════════════════════════════════════════════════════════ -->

<div align="center">
<img src="https://user-images.githubusercontent.com/74038190/235224431-e8c8c12e-6826-47f1-89fb-2ddad83b3abf.gif" width="200"/>

## 🚀 &nbsp; Featured Projects

</div>

<br/>

<!-- ── Phygital-Trace ────────────────────────────────────────────── -->

<div align="center">

### 🔗 Phygital-Trace — Camera to Blockchain Media Provenance

`media · blockchain · provenance`

</div>

```mermaid
graph TB
    subgraph Capture Layer
        A["📷 Camera Capture"] --> B["🔍 pHash + PRNU<br/>Hardware Fingerprint"]
        B --> C["🔏 Steganographic<br/>Watermark"]
    end

    subgraph Verification Layer
        C --> D["📋 C2PA Provenance<br/>Chain"]
        D --> E["🤖 Gemini 1.5 Pro<br/>Forensic Analysis"]
    end

    subgraph Trust Layer
        E --> F["⛓️ Solidity Smart<br/>Contract"]
        F --> G["📦 IPFS Immutable<br/>Storage"]
    end

    style A fill:#0d1117,stroke:#38bdf8,stroke-width:2px,color:#38bdf8
    style B fill:#0d1117,stroke:#38bdf8,stroke-width:2px,color:#38bdf8
    style C fill:#0d1117,stroke:#38bdf8,stroke-width:2px,color:#38bdf8
    style D fill:#0d1117,stroke:#7c3aed,stroke-width:2px,color:#7c3aed
    style E fill:#0d1117,stroke:#7c3aed,stroke-width:2px,color:#7c3aed
    style F fill:#0d1117,stroke:#38bdf8,stroke-width:2px,color:#38bdf8
    style G fill:#0d1117,stroke:#38bdf8,stroke-width:2px,color:#38bdf8
```

<sub>`FastAPI` `Next.js` `Solidity` `IPFS` `PostgreSQL` `Gemini API`</sub>

<br/>

<!-- ── NexusOps ──────────────────────────────────────────────────── -->

<div align="center">

### ⚙️ NexusOps — AIOps Crash Resolution Platform

`aiops · sre · crash resolution`

</div>

```mermaid
graph LR
    subgraph LocalLens
        A["💬 Telegram"] --> D["🧠 AI Memory"]
        B["🎙️ Voice"] --> D
        C["📹 Meetings"] --> D
        D --> E["📚 pgvector KB"]
    end

    subgraph SlothOps
        F["💥 Crash Detected"] --> G["🔍 Query Team Context"]
        G --> H["🔧 Generate Fix"]
        H --> I["📬 GitHub PR<br/>+ Rollback Guard"]
    end

    E --> G

    style A fill:#0d1117,stroke:#38bdf8,stroke-width:1px,color:#38bdf8
    style B fill:#0d1117,stroke:#38bdf8,stroke-width:1px,color:#38bdf8
    style C fill:#0d1117,stroke:#38bdf8,stroke-width:1px,color:#38bdf8
    style D fill:#0d1117,stroke:#7c3aed,stroke-width:2px,color:#7c3aed
    style E fill:#0d1117,stroke:#7c3aed,stroke-width:2px,color:#7c3aed
    style F fill:#0d1117,stroke:#ef4444,stroke-width:2px,color:#ef4444
    style G fill:#0d1117,stroke:#38bdf8,stroke-width:2px,color:#38bdf8
    style H fill:#0d1117,stroke:#38bdf8,stroke-width:2px,color:#38bdf8
    style I fill:#0d1117,stroke:#22c55e,stroke-width:2px,color:#22c55e
```

<sub>`FastAPI` `Next.js 14` `pgvector` `Celery` `Redis` `Claude API`</sub>

<br/>

<!-- ── Neeti AI ──────────────────────────────────────────────────── -->

<div align="center">

### 🛡️ Neeti AI — Multi-Agent Interview Integrity

`interview integrity · multi-agent`

</div>

```mermaid
graph TB
    subgraph Candidate Session
        A["📹 WebRTC Proctoring"] --> F["Trust Score Engine"]
        B["💻 Monaco Code Editor"] --> F
        C["🎙️ pyannote Voice ID"] --> F
    end

    subgraph 5 Parallel AI Agents
        D1["🧠 Agent 1:<br/>Technical Depth"] --> F
        D2["📊 Agent 2:<br/>Code Quality"] --> F
        D3["🗣️ Agent 3:<br/>Communication"] --> F
        D4["🔒 Agent 4:<br/>Behavioral"] --> F
        D5["⚡ Agent 5:<br/>Problem Solving"] --> F
    end

    F --> G["📄 Forensic<br/>Hiring Report"]

    style A fill:#0d1117,stroke:#38bdf8,stroke-width:2px,color:#38bdf8
    style B fill:#0d1117,stroke:#38bdf8,stroke-width:2px,color:#38bdf8
    style C fill:#0d1117,stroke:#38bdf8,stroke-width:2px,color:#38bdf8
    style D1 fill:#0d1117,stroke:#7c3aed,stroke-width:2px,color:#7c3aed
    style D2 fill:#0d1117,stroke:#7c3aed,stroke-width:2px,color:#7c3aed
    style D3 fill:#0d1117,stroke:#7c3aed,stroke-width:2px,color:#7c3aed
    style D4 fill:#0d1117,stroke:#7c3aed,stroke-width:2px,color:#7c3aed
    style D5 fill:#0d1117,stroke:#7c3aed,stroke-width:2px,color:#7c3aed
    style F fill:#0d1117,stroke:#22c55e,stroke-width:3px,color:#22c55e
    style G fill:#0d1117,stroke:#38bdf8,stroke-width:2px,color:#38bdf8
```

<sub>`Node/Express` `MongoDB` `Bull` `Socket.IO` `MediaPipe` `React 19`</sub>

<br/>

<!-- ── FiXr ──────────────────────────────────────────────────────── -->

<div align="center">

### 🛠️ FiXr — Multi-Agent Code Intelligence CLI

`cli · multi-agent · code intelligence`

</div>

```mermaid
graph LR
    A["📥 Code Input"] --> B["🔍 Bug Detective"]
    B --> C["🔧 Bug Fixer"]
    C --> D["📊 Code Quality"]
    D --> E["🛡️ Security Auditor<br/>OWASP Top 10"]
    E --> F["✅ Report + Patch"]

    style A fill:#0d1117,stroke:#94a3b8,stroke-width:2px,color:#94a3b8
    style B fill:#0d1117,stroke:#ef4444,stroke-width:2px,color:#ef4444
    style C fill:#0d1117,stroke:#f59e0b,stroke-width:2px,color:#f59e0b
    style D fill:#0d1117,stroke:#38bdf8,stroke-width:2px,color:#38bdf8
    style E fill:#0d1117,stroke:#7c3aed,stroke-width:2px,color:#7c3aed
    style F fill:#0d1117,stroke:#22c55e,stroke-width:2px,color:#22c55e
```

<sub>`TypeScript` `Node.js` `Commander.js` `Groq` `Claude API`</sub>

<br/>

<!-- ═══════════════════════════════════════════════════════════════════ -->
<!--                       CURRENTLY IN THE LAB                        -->
<!-- ═══════════════════════════════════════════════════════════════════ -->

---

<br/>

<div align="center">

## 🔬 &nbsp; Currently in the Lab

</div>

<br/>

<table width="100%" border="0">
<tr>
<td align="center" width="33%" valign="top" style="border: 1px solid #1e293b; border-radius: 12px; padding: 20px;">

**Phygital-Trace**

`pHash + PRNU + steganography + C2PA + Gemini forensics`

<sub>6-part architecture upgrade</sub>

</td>
<td align="center" width="33%" valign="top" style="border: 1px solid #1e293b; border-radius: 12px; padding: 20px;">

**Local LLMs**

`Ollama + Llama 3.2 / Qwen 2.5 Coder`

<sub>Running on M5 MacBook Air bare metal</sub>

</td>
<td align="center" width="33%" valign="top" style="border: 1px solid #1e293b; border-radius: 12px; padding: 20px;">

**Claude Code Pipelines**

`PRD → TRD → Backend → DB → AI Instructions`

<sub>Docs as first-class artifacts</sub>

</td>
</tr>
</table>

<br/>

<!-- ═══════════════════════════════════════════════════════════════════ -->
<!--                          TECH STACK                               -->
<!-- ═══════════════════════════════════════════════════════════════════ -->

---

<br/>

<div align="center">

## 🧰 &nbsp; Tech Stack

</div>

<br/>

<div align="center">

<table border="0" width="94%">
<tr>
<td align="center" valign="top" width="50%">

**Languages**

<img src="https://skillicons.dev/icons?i=ts,js,python,c,html,css&theme=dark&perline=6"/>

<sub>TypeScript first. Python when it makes sense. C when the machine matters.</sub>

<br/><br/>

**Frontend**

<img src="https://skillicons.dev/icons?i=nextjs,react,tailwind,vite,figma&theme=dark&perline=5"/>

<sub>Next.js 14 App Router is home base. Tailwind for velocity, Figma to think first.</sub>

</td>
<td width="4%"></td>
<td align="center" valign="top" width="46%">

**Backend & Data**

<img src="https://skillicons.dev/icons?i=nodejs,express,django,fastapi,mongodb,postgres,redis&theme=dark&perline=7"/>

<sub>FastAPI + PostgreSQL for serious work. Redis when latency counts.</sub>

<br/><br/>

**Infrastructure**

<img src="https://skillicons.dev/icons?i=docker,aws,gcp,github,git,linux&theme=dark&perline=6"/>

<sub>Docker always. Railway for fast deploys. Don't fear the terminal.</sub>

</td>
</tr>
</table>

</div>

<br/>

<!-- ═══════════════════════════════════════════════════════════════════ -->
<!--                         GITHUB STATS                              -->
<!-- ═══════════════════════════════════════════════════════════════════ -->

---

<br/>

<div align="center">
<img src="https://user-images.githubusercontent.com/74038190/213910845-af37a709-8995-40d6-be59-724526e3c3d7.gif" width="800"/>

## 📊 &nbsp; GitHub Stats

</div>

<br/>

<div align="center">

<!-- Streak Stats -->
<img src="https://streak-stats.demolab.com/?user=soumyachk101&theme=tokyonight&hide_border=true&background=0d1117&ring=38bdf8&fire=7c3aed&currStreakLabel=38bdf8&sideLabels=94a3b8&dates=475569&border_radius=8&timezone=Asia%2FKolkata" width="92%"/>

<br/><br/>

<!-- Stats Card + Top Langs -->
<img src="https://github-readme-stats.vercel.app/api?username=soumyachk101&show_icons=true&theme=tokyonight&hide_border=true&bg_color=0d1117&title_color=38bdf8&icon_color=7c3aed&text_color=94a3b8&ring_color=38bdf8&border_radius=8" width="48%"/>&nbsp;
<img src="https://github-readme-stats.vercel.app/api/top-langs/?username=soumyachk101&layout=compact&theme=tokyonight&hide_border=true&bg_color=0d1117&title_color=38bdf8&text_color=94a3b8&border_radius=8" width="39%"/>

<br/><br/>

<!-- Contribution Snake -->
<img src="https://raw.githubusercontent.com/soumyachk101/soumyachk101/output/github-contribution-grid-snake-dark.svg" width="92%"/>

<br/><br/>

<!-- Activity Graph -->
[![Soumya's github activity graph](https://github-readme-activity-graph.vercel.app/graph?username=soumyachk101&bg_color=0d1117&color=38bdf8&line=7c3aed&point=ffffff&area=true&area_color=38bdf8&hide_border=true)](https://github.com/ashutosh00710/github-readme-activity-graph)

</div>

<br/>


<!-- ═══════════════════════════════════════════════════════════════════ -->
<!--                          COLLABORATION                            -->
<!-- ═══════════════════════════════════════════════════════════════════ -->

---

<br/>

<div align="center">

## 🤝 &nbsp; Let's Work Together

I am particularly interested in collaborating on:

| Area | Focus |
| :--- | :--- |
| **AI Tooling** | Multi-agent systems, local LLM integrations, and developer productivity hacks. |
| **Web3 & Media** | Content provenance, decentralized identity, and blockchain-based media verification. |
| **System Design** | High-performance backends, distributed architectures, and schema-first development. |

</div>

<br/>
<!-- ═══════════════════════════════════════════════════════════════════ -->
<!--                              CTA                                  -->
<!-- ═══════════════════════════════════════════════════════════════════ -->

---

<br/>

<div align="center">

<img src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&weight=600&size=18&pause=9999&color=38BDF8&center=true&vCenter=true&width=700&lines=building+something+hard%3F+let%27s+talk."/>

<br/>

<img src="https://user-images.githubusercontent.com/74038190/219923823-bf1ce878-c6b8-4faa-be07-93e6b1006521.gif" width="200"/>

<br/>

I work on problems at the intersection of trust, distributed systems, and media —<br/>technically hard and actually worth solving.

<br/><br/>

[![Portfolio](https://img.shields.io/badge/Portfolio-chksoumya.in-38bdf8?style=for-the-badge&logo=vercel&logoColor=white&labelColor=0d1117)](https://chksoumya.in)&nbsp;
[![Email](https://img.shields.io/badge/Email-soumya.chk101-EA4335?style=for-the-badge&logo=gmail&logoColor=white&labelColor=0d1117)](mailto:soumya.chk101@gmail.com)&nbsp;
[![LinkedIn](https://img.shields.io/badge/Connect-LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white&labelColor=0d1117)](https://linkedin.com/in/soumyachk101)

<br/><br/>

<sub>📍 West Bengal, India &nbsp;·&nbsp; UTC+5:30</sub>

<br/>

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:38bdf8,50:1e293b,100:0d1117&height=120&section=footer&animation=fadeIn"/>

</div>
