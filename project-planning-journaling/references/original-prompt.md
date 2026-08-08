# Original source prompt

This is the original chat prompt this skill was converted from. It's kept here for
provenance — the skill's actual instructions live in
[`../SKILL.md`](../SKILL.md) and are what Claude follows. If you're improving the
skill, edit `SKILL.md`, not this file.

---

I want you to create a comprehensive, living documentation system for this project, capturing everything we've done together so far and keeping it updated going forward. Do this now:

## 0. Project intake (ask before anything else)
Before touching code or docs, ask me:
1. **Scope & type** — what is this (prototype / internal tool / library / SaaS product / learning project)? Who is it for?
2. **Repo status** — does a Git repo already exist for this?
   - If yes: confirm remote, current branch, visibility.
   - If no: propose a repo name (kebab-case, matches project purpose), visibility (public/private), and license.
3. **Timeline** — what's the short-term goal (e.g. working MVP by X) vs the long-term vision (e.g. scale to N users, become a paid product)?
4. **Market/product path** — is this meant to stay open-source/public indefinitely, or could it later be forked to a private branch/repo, developed separately, and pitched as a standalone product? Note the decision criteria (proprietary IP, licensing, timing) so it can be revisited later.
5. **Development style** — pick one:
   - **Spec-first**: full plan written and agreed before coding starts.
   - **Interactive/iterative**: flexible, plan evolves as we go, journal captures decisions after the fact.
   - **Hybrid**: milestone-based plan, iterate freely within each milestone.

Record the answers in `README.md` under a new "Project Scope & Repo Info" section (name, type, repo, visibility, license, short/long-term goals, product path, chosen dev style) — this becomes the reference point for every later planning and journaling step.

## 1. Review full history
Go through our entire conversation history and the project's git log from the very beginning. Reconstruct: the original idea and brainstorming, key decisions and the reasoning behind them, my feedback and how you responded to it, the steps we took in order, every code snippet/file you proposed (whether or not it was ultimately kept), every commit and push you made (with hashes, messages, dates), and where the project currently stands.

## 2. Folder structure
Create a dedicated top-level folder, e.g. `/project-journal/`, separate from the source code, containing:
- `README.md` — the main index/dashboard (see format below)
- `decisions/` — one short file per major decision, if a decision needs more than a paragraph
- `snippets/` — every code example discussed in chat, saved as real files with proper extensions and descriptive names (not inline in the markdown), referenced from README.md via relative markdown links
- `sessions/` — optional, one file per work session/date if useful for history

## 3. README.md format requirements
- Write in plain, simple language — no jargon, no filler, no long paragraphs.
- Prefer tables and Mermaid diagrams over prose wherever there's a list, comparison, flow, sequence, or architecture to show.
- Structure content under clear headings, title-style, skimmable in seconds.
- Use a checklist with checkboxes (`- [x]` / `- [ ]`) for every milestone/step, so progress is visually trackable and stays accurate as the project moves forward.
- For anything that needs more depth, use collapsible sections:
  <details><summary>Short label</summary> ...longer explanation... </details>
  so the top-level view stays short and details are opt-in.
- Include these sections at minimum:
  1. Project Scope & Repo Info (type, repo name, visibility, license, short/long-term goals, market/product path, chosen dev style — from step 0)
  2. Project Overview (what & why, 2-3 lines)
  3. Roadmap / Milestones (checklist, chronological)
  4. Key Decisions Log (table: decision | reasoning | date)
  5. Architecture / How it works (Mermaid diagram)
  6. Code Changes (table linking to files in `snippets/` and/or real commits)
  7. Git History (table: date | commit hash | message | pushed y/n)
  8. Current Status (what's done, what's in progress)
  9. Next Steps / Open Questions (checklist + short notes)

## 4. Resumability
Structure everything so that in a brand-new session, I can open `/project-journal/README.md` and immediately know exactly where we left off and what to do next — without needing to scroll through old chat history.

## 5. Ongoing maintenance
From now on, treat this folder as a living document: after any meaningful step, decision, commit, or push, update the relevant sections (roadmap checkboxes, decisions log, git history, current status, next steps) automatically, without me having to ask each time. If a change affects scope, timeline, or the market/product path decided in step 0, update the "Project Scope & Repo Info" section too.

Start by asking the step 0 questions if they haven't been answered yet, then generate the full initial version of this documentation based on everything we've done so far.
