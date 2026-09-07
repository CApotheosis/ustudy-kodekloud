# KodeKloud Course Refactor — Working Doc

Big refactor of this course-project: KodeKloud changed the AI learning path significantly (courses added/removed). Link: https://kodekloud.com/learning-path/ai

This doc is the persistent handoff between sessions (scraping, grilling, domain modeling, content generation). Update **Status**, tick **Phases**, and log new items in **Questions** / **Insights** as you go — don't let those two sections go stale, they're the memory across sessions.

## Status

- Current phase: **Third phase** (grilling/restructure) — active. Lesson-content fetching is no longer a separate upfront step; it happens on-demand during grilling (see phase 2 note below).
- Blocking question: #1 below (paid subscriptions — cloud *and* AI-tool tiers) — doesn't block starting, but blocks answering student FAQs.

## Operating principle: local-first content, fetched on demand

Phase-1 metadata (`course-details.md`) exists for every course — that's enough to start grilling. Don't bulk-scrape lesson content upfront. Instead, when a grilling/domain-modeling question needs source material to answer (e.g. "does this module need a paid Azure account?"), fetch that specific page then, and save it locally under `docs/AI Learning Path/**`. `1. Prompt Engineering 101`'s lesson files are the template for what "saved locally" looks like, but note: that content was hand-pasted by the user while personally taking the course, **not** fetched via scraping notes.kodekloud.com. Scraping that notes site has not actually been proven from content currently in this repo — treat it as untested until a real fetch succeeds and gets saved the same way. Once content exists locally (however it got there), later sessions read the local file first and only re-fetch/re-request if something's missing.

## Phases

- [x] **First phase** — Scrape kodekloud.com learning path, fetch course metadata/details into `docs/AI Learning Path/**` mirroring the site structure. One page at a time, report failures. Basis for all future work.
- [x] **Second phase (folded into Third)** — Fetching text-based lesson content from notes.kodekloud.com is no longer a standalone bulk pass; it happens on-demand while grilling, per the operating principle above. `1. Prompt Engineering 101` has full lesson content already, but it was hand-pasted by the user from personally taking the course — not a proven scrape. Actual notes.kodekloud.com scraping is still unverified against anything currently in this repo.
- [ ] **Third phase** — Refactor + prepare ground for future sessions:
  - [ ] Grilling + domain modeling session covering: lesson structure, materials, assessing student progress, etc. — fetch lesson content as needed to answer specific questions. Use `/grill-with-docs` (chains `grilling` → `domain-modeling`, produces ADRs/glossary as it goes; user-invoked only, can't be triggered by the model)
  - [ ] Folder restructure to match new course structure
  - [ ] Curriculum correction (`curriculum/curriculum.md`, `curriculum/mentor-sessions.md`, `curriculum/schedule.md`)
  - [ ] Admissions correction (`admissions/qualification.md`, `admissions/screening-interview.md`)
  - [ ] Other docs pass
  - [ ] Decide general lesson structure (relative to existing course content already scraped)
  - [ ] Create skills to fast-forward development — base `/teach`-equivalent skill on Matt Pocock's approach; use `/writing-for-agents` for any doc meant to be read by agents
- [ ] **Fourth phase** — Create courses (content generation, using curriculum + whatever lesson content has been fetched by then as source of truth — fetch remaining gaps as they're found)

## Mission

1. Ensure each student doesn't just pass the course, but learns and can build production-grade agents with the knowledge.
2. Track student progress — confirm they're completing content on schedule, not cramming at the end (midterm/weekly checks).
3. Students should be able to ship production-grade projects using what they learned.

Planned delivery mechanism: Telegram group, split into sections/chats (publish / course questions / announcements). Need an assistant flow to check progress and log it so lagging students are caught early.

## Open Questions

| # | Question | Status | Answer |
|---|---|---|---|
| 1 | Does the course require extra paid subscriptions beyond the KodeKloud platform — cloud (Azure, AWS, S3, etc.) *and* AI-tool tiers (Claude, Cursor, OpenAI, Gemini — free tier vs. paid)? | open | — |

When answering, fill in the Answer column and change status to `resolved` — don't delete the row, it's the record of the decision.

## Insights Log

Append-only, newest first. One line per insight, dated.

- 2026-09-07 (unattributed): Lessons with a listed time are video lessons; lessons without a time are text-based with a terminal + preloaded files in-session.
- 2026-09-07 (unattributed): Platform has internal AI support for student Q&A/task help — likely Mixtral-8x7B or similar (unconfirmed).

## Other Notes

- Use the grilling skill whenever a decision needs stress-testing.
- Any agreed moment can still be renegotiated when presenting to the education center — nothing here is final until then.
- User has limited hands-on practice with the DevOps-heavy sections (mostly theoretical) — needs a teaching/exploration pass before prepping those lessons.
- See `my_learning_status.md` for personal course-completion tracking (separate from student-facing curriculum work).
