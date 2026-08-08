# Research behind this skill

The steps in `SKILL.md` aren't invented from nothing — they draw on established
software-planning and documentation practices. This file lists the sources, what each
one contributes, and which part of the skill it backs. Read it when someone asks *why*
a step exists, or when you're looking for ways to extend the skill further.

Two kinds of source, handled differently:
- **Open** — freely available online under a license that permits reuse. Linked, and in
  one case (the Scrum Guide) mirrored locally as a PDF because its license allows it —
  see [`../../NOTICE.md`](../../NOTICE.md) for attribution.
- **Closed** — commercially published books/standards. Cited for the *concept* only, in
  our own words. No text from these is reproduced anywhere in this repo.

## Open references

| Source | What it contributes | Backs |
|---|---|---|
| Michael Nygard, ["Documenting Architecture Decisions"](https://www.cognitect.com/blog/2011/11/15/documenting-architecture-decisions) (Cognitect blog, 2011) | The original one-decision-per-file format that started Architecture Decision Records: a short, immutable record of a significant decision, its context, and its consequences. | `decisions/` folder — the "one short file per major decision" pattern |
| [joelparkerhenderson/architecture-decision-record](https://github.com/joelparkerhenderson/architecture-decision-record) (GitHub, MIT License) | A large set of ready-to-use ADR templates, including the MADR (Markdown Any Decision Records) format, for teams who want more structure than a plain paragraph. | `decisions/` folder — optional template for anyone who wants a stricter decision format |
| [Diátaxis](https://diataxis.fr/) documentation framework, by Daniele Procida (CC BY-SA 4.0) | A framework for splitting documentation into four distinct needs — tutorials, how-to guides, reference, and explanation — so a single document doesn't try to serve all of them badly. | README.md format — the split between the skimmable dashboard and `<details>`-wrapped explanation backs the same idea: don't mix quick-reference and deep-explanation in one flow |
| [Keep a Changelog](https://keepachangelog.com/) by Olivier Lacan (MIT License) | A simple, human-readable changelog convention: grouped by release, newest first, plain language over commit-log dumps. | Git History table — "readable by humans, not just `git log`" is the same principle applied to the journal's commit table |
| [Conventional Commits](https://www.conventionalcommits.org/) specification (CC BY 3.0) | A lightweight convention for structuring commit messages (`type(scope): subject`) so history is machine- and human-parseable. | Git History table — informs recommending consistent commit messages so the table stays easy to populate accurately |
| [Semantic Versioning 2.0.0](https://semver.org/) by Tom Preston-Werner (CC BY 4.0) | MAJOR.MINOR.PATCH versioning tied to the meaning of a change (breaking / additive / fix), not just a build counter. | Market/product path (Step 0) — the point at which a project should start versioning deliberately is usually the same point it's being treated as a product, not just a local project |
| GitHub [Open Source Guides](https://opensource.guide/) — "[Starting a Project](https://opensource.guide/starting-a-project/)" and "[Legal: Choosing a License](https://opensource.guide/legal/)" (CC BY 4.0) | Practical guidance on naming a new repo, picking an initial license, and setting expectations before the first commit. | Step 0 — repo name, visibility, and license questions |
| GOV.UK Service Manual, ["Agile delivery: how the discovery phase works"](https://www.gov.uk/service-manual/agile-delivery/how-the-discovery-phase-works) (Open Government Licence v3.0) | The UK government's own methodology for the phase *before* any building starts: understand the problem, the users, and the constraints, and produce a recommendation on how to proceed. | Step 0 as a whole — intake-before-code is exactly the discovery-phase idea, applied to any project size |
| [The Scrum Guide](https://scrumguides.org/) (2020), Ken Schwaber & Jeff Sutherland (CC BY-SA 4.0) — mirrored locally at [`scrum-guide-2020.pdf`](./scrum-guide-2020.pdf) | The definition of Scrum: fixed-length iterations (Sprints), a single prioritized backlog, and regular inspect-and-adapt points. Inherently iterative. | Step 0 — grounds the "hybrid" (milestone/Sprint-based) development-style option, and the iterative half of "interactive/iterative" |
| [arc42](https://arc42.org/) architecture documentation template, Gernot Starke & Peter Hruschka (CC BY-SA 4.0) | A widely used template for documenting software architecture in a lightweight, consistent set of sections. | README.md format — general precedent for a standard, skimmable set of headings that a reader already knows how to navigate |

## Closed references (concept only, no material reproduced)

| Source | Concept | Backs |
|---|---|---|
| Frederick P. Brooks Jr., *The Mythical Man-Month* (Addison-Wesley, 1975/1995) | Adding people to a late project makes it later; there's no "silver bullet" that removes the essential complexity of a build. A caution against optimistic timeline estimates. | Step 0, Timeline question — encourages asking for a realistic short-term goal rather than accepting an aggressive one at face value |
| Eric Ries, *The Lean Startup* (Crown Business, 2011) | Build–measure–learn: ship a minimum viable product to get validated learning, rather than fully specifying a product before any real-world feedback. | Step 0, Timeline and Development-style questions — the short-term-MVP-vs-long-term-vision split, and the case for "interactive/iterative" over "spec-first" when the goal is still uncertain |
| Nadia Eghbal (Asparouhova), *Working in Public: The Making and Maintenance of Open Source Software* (Stripe Press, 2020) | How open-source projects actually grow (or don't) — the difference between a project built for strangers vs. one that later needs to become a funded, maintained product. | Step 0, Market/product path question — the criteria for "stay public" vs. "fork private and productize" |
| Project Management Institute, *A Guide to the Project Management Body of Knowledge (PMBOK Guide)* | Formal, upfront scope/schedule/stakeholder planning before execution begins. | Step 0, Development-style question — grounds "spec-first" as a legitimate, named alternative to iterative planning, not just "the slow way" |
| Nicole Forsgren, Jez Humble, Gene Kim, *Accelerate: The Science of Lean Software and DevOps* (IT Revolution Press, 2018) | The DORA research: deployment frequency, lead time, and change failure rate as concrete signals of delivery health, tracked continuously rather than assessed once. | Step 5, Ongoing maintenance — the case for updating the journal after *every* meaningful change rather than in periodic batches |
