# Research behind this skill

The steps in `SKILL.md` aren't invented from nothing — they draw on established
software-planning and documentation practices. This file lists the sources, what each
one contributes, which part of the skill it backs, and — since a source only earns a
place here if it's independently recognized, not just the first thing a search engine
returns — the evidence that it's actually adopted or cited elsewhere. Read it when
someone asks *why* a step exists, when you're looking for ways to extend the skill
further, or during the weekly review (see "Keeping this current" below).

Two kinds of source, handled differently:
- **Open** — freely available online under a license that permits reuse. Linked, and in
  one case (the Scrum Guide) mirrored locally as a PDF because its license allows it —
  see [`../../NOTICE.md`](../../NOTICE.md) for attribution.
- **Closed** — commercially published books/standards. Cited for the *concept* only, in
  our own words. No text from these is reproduced anywhere in this repo.

## Open references

| Source | What it contributes | Backs | Independent evidence it's reputable |
|---|---|---|---|
| Michael Nygard, ["Documenting Architecture Decisions"](https://www.cognitect.com/blog/2011/11/15/documenting-architecture-decisions) (Cognitect blog, 2011) | The original one-decision-per-file format that started Architecture Decision Records. | `decisions/` folder — one short file per major decision | Placed in the **"Adopt"** ring of [ThoughtWorks' Technology Radar](https://www.thoughtworks.com/radar/techniques/lightweight-architecture-decision-records) — ThoughtWorks' strongest recommendation level, given seven years after publication |
| [joelparkerhenderson/architecture-decision-record](https://github.com/joelparkerhenderson/architecture-decision-record) (GitHub, MIT) | Ready-to-use ADR templates, including MADR, for teams wanting more structure. | `decisions/` folder — optional stricter template | One of the most-starred ADR template collections on GitHub; its MADR template is maintained under the community [adr.github.io](https://adr.github.io/) umbrella |
| [Diátaxis](https://diataxis.fr/) documentation framework, Daniele Procida (CC BY-SA 4.0) | Splits documentation into four distinct needs — tutorial, how-to, reference, explanation. | README.md format — dashboard vs. `<details>`-wrapped explanation, kept separate | Adopted for the official docs of [Django, Canonical/Ubuntu, Cloudflare, and Gatsby](https://ubuntu.com/blog/diataxis-a-new-foundation-for-canonical-documentation) |
| [Keep a Changelog](https://keepachangelog.com/) by Olivier Lacan (MIT) | A human-readable changelog convention: grouped by release, newest first. | Git History table — readable by humans, not a raw `git log` dump | De facto standard for `CHANGELOG.md` across the open-source ecosystem; its format is what most changelog-generation tooling targets |
| [Conventional Commits](https://www.conventionalcommits.org/) specification (CC BY 3.0) | Structured commit messages (`type(scope): subject`) that stay parseable. | Git History table — consistent messages keep the table accurate | Built directly on the Angular project's commit convention; the default preset used by [`semantic-release`](https://github.com/semantic-release/commit-analyzer), one of the most-used release-automation tools |
| [Semantic Versioning 2.0.0](https://semver.org/) by Tom Preston-Werner (CC BY 4.0) | MAJOR.MINOR.PATCH tied to the meaning of a change, not a build counter. | Market/product path (Step 0) — versioning deliberately once it's a product | The version syntax npm's `package.json` and the `node-semver` resolver require — effectively mandatory across the Node.js/npm ecosystem |
| GitHub [Open Source Guides](https://opensource.guide/) — ["Starting a Project"](https://opensource.guide/starting-a-project/) & ["Legal: Choosing a License"](https://opensource.guide/legal/) (CC BY 4.0) | Naming a repo, picking an initial license, setting expectations pre-commit. | Step 0 — repo name, visibility, and license questions | Published by GitHub itself with outside community reviewers; the resource GitHub's own docs point new maintainers to |
| GOV.UK Service Manual, ["how the discovery phase works"](https://www.gov.uk/service-manual/agile-delivery/how-the-discovery-phase-works) (Open Government Licence v3.0) | Understand the problem/users/constraints *before* building; produce a recommendation. | Step 0 as a whole — intake-before-code is the discovery-phase idea | The methodology behind the UK's Government Digital Service, which [directly inspired equivalent digital-service units in the US, Australia, Canada, and Japan](https://gds.blog.gov.uk/2018/07/06/gds-across-the-globe-where-our-alumni-are-now/); GDS's professionalization is the subject of a peer-reviewed paper in *ACM Digital Government: Research and Practice*, open-access copy at [UCL Discovery](https://discovery.ucl.ac.uk/id/eprint/10185731/1/3630024.pdf) |
| [The Scrum Guide](https://scrumguides.org/) (2020), Ken Schwaber & Jeff Sutherland (CC BY-SA 4.0) — mirrored at [`scrum-guide-2020.pdf`](./scrum-guide-2020.pdf) | The definition of Scrum: fixed-length Sprints, one backlog, inspect-and-adapt points. | Step 0 — grounds "hybrid" (Sprint-based) and the iterative half of "interactive/iterative" | The sole canonical Scrum definition, translated into 30+ languages, and the basis for Scrum.org/Scrum Alliance certifications held by well over a million practitioners |
| [arc42](https://arc42.org/) architecture template, Gernot Starke & Peter Hruschka (CC BY-SA 4.0) | A lightweight, consistent template for documenting software architecture. | README.md format — precedent for a standard, navigable set of headings | Endorsed by [iSAQB](https://www.isaqb.org/isaqbproviders/arc42-dr-gernot-starke/), the body that certifies software architects; in production use at SAP, Siemens, Deutsche Telekom/T-Systems, and in German public-sector IT |

## Closed references (concept only, no material reproduced)

| Source | Concept | Backs | Independent evidence it's reputable |
|---|---|---|---|
| Frederick P. Brooks Jr., *The Mythical Man-Month* (Addison-Wesley, 1975/1995) | Adding people to a late project makes it later — no "silver bullet" removes essential complexity. | Step 0, Timeline — push back on optimistic estimates | Brooks won the 1999 ACM A.M. Turing Award, computing's highest honor; the book's enduring reach is the subject of its own peer-reviewed citation-context study, [McCain & Salvucci (2006), *Journal of Information Science*](https://journals.sagepub.com/doi/abs/10.1177/0165551506064397) |
| Eric Ries, *The Lean Startup* (Crown Business, 2011) | Build–measure–learn: ship an MVP for validated learning instead of fully specifying up front. | Step 0, Timeline & Dev-style — the MVP-vs-vision split, iterative over spec-first when uncertain | The methodology behind the program structure of accelerators including Y Combinator, Techstars, 500 Startups, and AngelPad |
| Nadia Eghbal (Asparouhova), *Working in Public* (Stripe Press, 2020) | How open-source projects actually grow — built-for-strangers vs. later becoming a funded product. | Step 0, Market/product path — criteria for "stay public" vs. "fork private and productize" | Follow-up to Eghbal's *Roads and Bridges*, published by the Ford Foundation; widely and independently reviewed across the open-source-sustainability community on release |
| Project Management Institute, *PMBOK Guide* | Formal, upfront scope/schedule/stakeholder planning before execution begins. | Step 0, Dev-style — "spec-first" as a legitimate, named alternative | An accredited **ANSI standard** since 1999 (ANSI/PMI 99-001) and formerly an **IEEE standard** (IEEE Std 1490-2003) |
| Nicole Forsgren, Jez Humble, Gene Kim, *Accelerate* (IT Revolution Press, 2018) | DORA metrics — deployment frequency, lead time, change-failure rate — as continuous delivery-health signals. | Step 5, Ongoing maintenance — update after *every* change, not in batches | Grew out of the multi-year, tens-of-thousands-of-respondents State of DevOps Report research program and won the Shingo Publication Award. *Caveat, noted for balance:* the underlying survey instruments and raw datasets were never publicly released, so some reviewers flag the findings as hard to independently reproduce — treat the DORA metrics as a well-regarded industry framework, not a peer-reviewed proof |

## Keeping this current

Two scheduled GitHub Actions, both weekly (Monday), keep this list honest instead of
letting it fossilize:

- **`check-links.yml`** — mechanical. Re-fetches every link in this repo's docs and
  fails the build if one is dead.
- **`reference-review.yml`** — judgment-based. Opens a single tracking issue (never
  duplicates one that's still open) checklisting every source above, for a maintainer —
  or Claude, if asked to run the review — to re-confirm each one is still the most
  reputable choice available: still cited or adopted elsewhere, no newer edition
  (a future Scrum Guide or PMBOK revision, for instance) superseding the one cited here.

If a source fails either check, open a PR updating this file (and `NOTICE.md` too, if a
bundled file changes).
