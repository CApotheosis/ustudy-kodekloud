# Study Center Meeting — Refactor Draft (v1, self-grilled, unreviewed)

Prepared without a live Q&A pass — every non-obvious call below is marked **[DECISION]** (I picked one, flag if you disagree) or **[ASSUMPTION]** (I'm guessing, needs confirming). Nothing here is final; scan, strike, discuss with the center, bring back for refinement.

## 0. Headline for the meeting

KodeKloud didn't reshuffle the AI learning path — they **swapped tracks**. Removed from the old curriculum entirely: PyTorch, AI-Assisted Development, GitHub Copilot (both courses), Cline, AI-Assisted Ansible, Mastering GenAI with OpenAI, NVIDIA GenAI Cert, Fundamentals of RAG, LangChain, the full AI Agents course, LangGraph. Added: **Loop Engineering, Fundamentals of MLOps, and a 6-course AIOps Learn-By-Doing track** (Prometheus/Grafana monitoring → Python-based auto-remediation → ML anomaly/forecasting → distributed tracing/RCA → MLflow/Kubeflow). Net effect: the program moved away from "AI-assisted coding tools + agent frameworks" and toward **cloud AI operations / AIOps**.

Known knowns vs. unknowns: **[ASSUMPTION]** several new courses (Vector DB, MCP, AI Agents Fundamentals, Cursor AI, Loop Engineering, Fundamentals of MLOps, all 6 AIOps sub-courses) were still unreleased on KodeKloud's platform as of the Sep 5 fetch — their durations/module counts are provisional and may shift before launch.

## 1. First phase — recap (done)

Scraped the full new learning path into `AI Learning Path/**`, mirroring KodeKloud's own 3-cluster structure. 19 courses total (4 + 5 + 4-core-plus-6-AIOps). All have `course-details.md` (metadata). Nothing to decide here — just confirming it's solid ground for everything below.

## 2. Second phase — recap (folded into ongoing work)

Full lesson content exists locally only for **Prompt Engineering 101** so far — but that was **hand-pasted by you while personally taking the course**, not a proven scrape of notes.kodekloud.com. Scraping that notes site is still unverified against anything currently in this repo; don't treat Prompt Engineering 101 as evidence the fetch mechanism works. Going forward, remaining lesson content gets fetched on-demand (scraped where possible, requested from you where not) rather than bulk-scraped upfront — **[DECISION]** made last session, holding.

## 3. Third phase — draft decisions

### 3a. Curriculum correction — proposed new phase structure

**[DECISION]** Rather than re-deriving a custom prerequisite graph like the old curriculum did, I mostly followed KodeKloud's own 3-cluster grouping — it's what students see in-platform and is easier to defend to the study center than a from-scratch reordering. One exception: I pulled the two certification courses (AI-900, AWS AI Practitioner) out of cluster 3 and moved them to the front, preserving the old plan's "certs first for quick wins + shared vocabulary" logic. AIOps stays at the very end as a capstone specialization track, in the Beginner→Intermediate→Advanced order KodeKloud itself used for those six courses.

| Phase | Courses | Duration | Notes |
|---|---|---|---|
| **0 — Cloud & AI Foundations** | AI-900 (4h20m), AWS AI Practitioner (8h20m) | ~12h33m | Cert-first, quick wins, shared vocabulary before hands-on work |
| **1 — AI & Context Foundations** | Prompt Engineering 101 (0.58h), Vector Database for GenAI (4h48m), MCP For Beginners (2h23m), AI Agents Fundamentals (1h55m) | ~9h40m | Matches KodeKloud cluster 1 |
| **2 — GenAI Dev Tools** | Intro to OpenAI (6h23m), Claude Code For Beginners (8h37m), Cursor AI (3h53m, *optional*), Generative AI in Practice (3h49m, *optional*), Ollama (2h15m) | ~25h | Matches KodeKloud cluster 2 |
| **3 — Operationalize: MLOps & AIOps** | Loop Engineering (0h45m), Fundamentals of MLOps (5h12m, *optional*), AIOps Learn-By-Doing ×6 (Beginner→Advanced) | ~6h + AIOps (duration TBD, unreleased) | Capstone/specialization track |

**Known total: ~53h**, down from the old plan's ~99h22m — roughly **half** the video content. **[ASSUMPTION]** I'm treating this as good news to present (room for more hands-on/mentor time per hour of video, or a shorter program), not a gap to backfill — but that's a call the study center may want to weigh in on, since program length is part of what they're selling. Flagging, not deciding, for you.

**[ASSUMPTION]** With AIOps durations unknown, I can't commit to a week count yet. Rough placeholder: **14–16 weeks** instead of 20, pending AIOps hours once those courses go live. Don't quote this number to the study center as final.

### 3b. Folder restructure

**[DECISION]** Current flat-file convention (`1. Introduction.md`, `2. Detailing for Clarity.md`, ... + `course-details.md` per course folder) works fine for single-module courses like Prompt Engineering 101, but won't scale to multi-module courses (e.g. Generative AI in Practice has 6 modules / 33 topics). Proposed convention going forward:

- **Single-module course** → keep flat: `<course>/N. Lesson Name.md`
- **Multi-module course** → `<course>/Module N - Name/M. Lesson Name.md`

No renaming of already-scraped content needed yet (only Prompt Eng 101 has lesson files, and it's single-module — no conflict). Applies going forward as more content gets fetched.

### 3c. Admissions correction

**[DECISION]** Driven directly by the catalog shift:

- **Drop JS/Node.js entirely** from prerequisites — it was already "optional/nice-to-have," gated only by the now-removed AI-Assisted Development frontend phase and the old MCP lab. Nothing left in the new catalog needs it.
- **Raise the bar on Docker/K8s exposure** — the AIOps Advanced track (MLflow/Kubeflow, K8s serving) and Automated Remediation (Docker SDK) lean on it harder than the old curriculum ever did. Current qualification doc treats Docker as "basics, comes up in demos" — that undersells the new Advanced AIOps requirement (explicitly lists Python, Kubernetes, ML fundamentals as prereqs for that one course).
- **Keep Python as required** — if anything more central now (AIOps automation, ML anomaly detection, MLflow pipelines all Python-based).
- **Cloud accounts** — still need Azure + AWS free-tier (AI-900, AWS AI Practitioner, S3 vector labs), same as before. Feeds directly into your still-open question #1 in `tasks.md` about paid tiers.
- **Screening interview** — the Docker question (#4) probably needs to shift from "conceptual answer is enough" to at least "have you run a container / used docker-compose," given the new Advanced AIOps course assumes real K8s/Docker comfort. **[ASSUMPTION]** — flagging, didn't rewrite the interview script itself pending your call.

### 3d. Lesson structure decision

**[DECISION]** Keep the existing S1 (Kickoff) / S2 (Practice) / S3 (Feedback+Stretch) weekly rhythm from `mentor-sessions.md` — it's a mentor-cadence framework, not tied to specific course content, so it survives the catalog swap unchanged.

**[DECISION]** New rule for short courses: several new courses are under 1 hour of video (Prompt Engineering 101 at 0.58h, Loop Engineering at 0.75h). Rather than dedicating a full week to each (as the old plan did per-course), **bundle courses under ~1h combined into a single week**, or let a short course occupy only part of a week (e.g. S1+S2) and use the freed session for a mentor-set stretch project. See the worked example below — Prompt Engineering 101 fits comfortably into one week on its own with room to spare.

### 3e. Skills to fast-forward development

Not drafted yet — deferred. Once the above structural decisions are validated, next session should look at basing a `/teach`-style skill on Matt Pocock's approach for turning a `course-details.md` + fetched lesson content into a mentor session plan automatically, plus `/writing-for-agents` for any resulting doc meant to be read by future sessions.

## 4. Worked example — one full week (Phase 1, Week 2: Prompt Engineering 101)

Built from the actual lesson content on file (`AI Learning Path/1. Master AI, ML & Context Foundations/1. Prompt Engineering 101/`) — hand-pasted by you while taking the course, not scraped, but it's real course content and the most concrete example available right now, not a placeholder.

**Course:** Prompt Engineering 101 — Associate level, 1 module, 8 lessons/7 labs, 0.58h video (budget 2–3x for hands-on = ~1.5–2h total, comfortably fits one week).

| Session | Role | Content | Activity |
|---|---|---|---|
| **S1 — Kickoff** | Lead | Lab tour (Introduction) + Detailing for Clarity + Persona Play | Live demo using the course's own generic→precise examples (e.g. "Tell me about climate change" → "How is climate change affecting the frequency of hurricanes in the Atlantic over the past decade?"). Assign S2 prep: each student drafts 3 versions of one real prompt from their own work — generic, detailed, persona-based. |
| **S2 — Practice** | Coach | Delimiters (triple backticks, triple quotes, XML tags, keyword delimiters) + Step-by-Step Clarification | Pair exercise: take the messy real prompt from S1 prep, restructure it with delimiters and break it into explicit steps. Mentor circulates, unblocks. |
| **S3 — Feedback + Stretch** | Review | Illustrating Through Examples (few-shot) + Specifying Output Length | **Stretch challenge:** write one prompt for a real coding task combining all 5 techniques (detail + persona + delimiters + step-by-step + output length) — builds directly on their own S1/S2 prompt. Individual HW review against the standard rubric (ran/completed · quality · could explain approach · one improvement). Preview next week. |

**Extra HW (carried over from old plan, still fits):** submit a personal prompt-pattern library — one worked example per technique, from their own domain.

## 5. Fourth phase

Not drafted — depends on 3a–3d being validated first. Content generation should reuse whatever gets fetched on-demand during grilling (per the local-first principle in `tasks.md`), not a separate bulk content pass.

## 6. Open items to raise with the study center

1. Program length: hold at ~20 weeks with more hands-on ratio, or shorten to ~14–16 weeks given the ~50% drop in known video hours? (§3a)
2. Paid subscriptions — cloud *and* AI-tool tiers — still unanswered (`tasks.md` Q1), now sharper since AIOps adds Docker/K8s-adjacent tooling questions.
3. Should AIOps Learn-By-Doing be core curriculum or an elective bolt-on, given several of its courses were still unreleased at scrape time?
4. Sign-off on dropping JS/Node from admissions and raising the Docker bar (§3c).
