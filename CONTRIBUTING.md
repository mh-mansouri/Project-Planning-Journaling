# Contributing

Thanks for helping make this skill better! Real project stories are the most useful kind
of contribution — a case where the journal format didn't fit, or the intake questions
missed something you needed answered up front.

## Ways to help

- **Share a case that broke the format.** A project whose journal got messy, or a
  decision that didn't fit the "decisions log" table, is a great real-world test case.
  Open an issue describing what happened.
- **Improve the intake questions** in Step 0 — if there's a question every project needs
  answered before planning starts that isn't covered yet, propose it.
- **Improve the wording** of the skill's instructions so Claude follows them more
  reliably.

## Where things live

| Path | What it is |
|---|---|
| `project-planning-journaling/SKILL.md` | The instructions Claude follows. Most changes go here. |
| `project-planning-journaling/references/original-prompt.md` | The original chat prompt this skill was converted from, kept for provenance only — don't edit it to change behavior. |
| `project-planning-journaling/references/research.md` | Annotated bibliography — the sources behind each step and what they back. Add new sources here. |
| `project-planning-journaling/references/scrum-guide-2020.pdf` | Third-party file, CC BY-SA 4.0 — see [NOTICE.md](./NOTICE.md). Not part of the `.skill` bundle (build.py excludes it deliberately). |
| `project-planning-journaling.skill` | **Generated.** A zip of the folder above — don't edit by hand. |
| `universal-prompt.md` | The same skill as a copy-paste prompt, for any AI chat that isn't Claude (ChatGPT, Grok, Gemini, ...). Not part of the `.skill` bundle. |
| `NOTICE.md` | Attribution for third-party files. |
| `README.md` / `README.sv.md` / `README.fa.md` | English, Swedish, and Persian versions of the repo README, cross-linked at the top of each. Keep all three in sync when the content changes. |
| `index.html` / `index.sv.html` / `index.fa.html` | Static GitHub Pages landing pages, cross-linked at the top of each (the language switcher stays on the Pages site, it doesn't jump to GitHub). Same install options as the READMEs — keep all three, and the matching README, in sync. |
| `scripts/check_links.py` | Checks that every link in the READMEs, `index.html`, and the skill's docs still resolves. Add a file to `FILES` here if you add a new doc with outbound links. |
| `.github/workflows/check-links.yml` | Runs `check_links.py` weekly plus on every push/PR. |
| `.github/workflows/reference-review.yml` | Weekly reminder issue for the judgment half of reference review (still reputable, no newer edition) — see `research.md`'s "Keeping this current". |
| `assets/skill-demo-mockup.gif` | **Generated** (by default) or a real screen recording, under this same filename either way. Shown at the top of all three READMEs and on `index.html`. |
| `create_skill_demo_gif.py` | Regenerates the mock-up GIF from a scripted scenario (`python create_skill_demo_gif.py`, needs Pillow). Replace the output file with a real recording under the same name if one is ever made — nothing else needs to change. |
| `assets/social-preview.png` | Link-unfurl image (LinkedIn, Slack, GitHub's repo card) — referenced by `index.html`'s `og:image`/`twitter:image` tags. Also re-upload manually at Settings → General → Social preview after regenerating; GitHub doesn't read it from the repo. |
| `create_social_preview.py` | Regenerates `assets/social-preview.png` (`python create_social_preview.py`, needs Pillow). |
| `.github/workflows/release-reminder.yml` | Weekly check for unshipped changes since the last tag — see "Cutting a release" below. |
| `scripts/validate_skill.py` | Checks `SKILL.md`'s frontmatter: required fields present, no extra fields, `name` matches the folder and is lowercase-hyphenated, `description` under Claude's 1024-char upload limit. |
| `.github/workflows/validate-skill.yml` | Runs `validate_skill.py` on every push/PR that touches `SKILL.md`. |
| `CHANGELOG.md` | Human-readable release history, [Keep a Changelog](https://keepachangelog.com/) format. Add an `[Unreleased]` entry alongside any shipped-surface change; move it under the version heading when you tag. |

## How to propose a change

1. Fork this repository.
2. Make your edit (most changes live in `project-planning-journaling/SKILL.md`).
3. **If you changed `SKILL.md`, validate it before anything else:**
   ```
   python scripts/validate_skill.py
   ```
   Catches an over-limit description or a malformed `name` locally, instead of on upload.
4. **If you changed anything inside `project-planning-journaling/`, rebuild the bundle:**
   ```
   python build.py
   ```
   This regenerates `project-planning-journaling.skill` from the source folder. Commit
   the rebuilt file alongside your edit — otherwise the one-click install and the source
   folder ship different versions of the skill.
5. **If the behavior changed, mirror the change in `universal-prompt.md`** — it's a
   separate, condensed copy for non-Claude chats, so it doesn't update automatically.
6. **Add an entry under `[Unreleased]` in `CHANGELOG.md`** if the change touches the
   shipped surface (see "Cutting a release" below).
7. Open a pull request with a short note on what you changed and why.

If you edit the skill, please try it on a real (or realistic) project before submitting,
and describe what you tested in the pull request.

## Adding a research source

If you cite new research in `research.md`, link to a freely accessible copy rather than
committing the file. Only commit a file when its license clearly permits redistribution —
and if you do, add the attribution to [NOTICE.md](./NOTICE.md). Commercially published
books and paid standards almost never permit it; open web standards and CC-licensed
guides often do.

## Cutting a release

`release-reminder.yml` runs weekly and opens an issue *only* when something in the
**shipped surface** — `project-planning-journaling/` (what `build.py` bundles into the
`.skill`), `universal-prompt.md`, or `build.py` itself — has changed since the last tag.
That's the actual criterion: **does this change what a user installs or pastes?**

- **Triggers a reminder:** any edit to `SKILL.md`, `references/`, `universal-prompt.md`,
  or the bundling logic. The attached `.skill` release asset is a frozen snapshot, so it
  silently goes stale the moment these change without a new tag.
- **Doesn't trigger one:** README/translation wording, `index.html`, CI/workflow files,
  this file. None of that changes what gets installed, so it doesn't need a version bump
  — cosmetic and doc-only changes just land on `main` between releases.

When a reminder fires, classify the change before tagging (SemVer, per
[`references/research.md`](./project-planning-journaling/references/research.md)):

| Bump | When |
|---|---|
| **PATCH** | Wording/typo fix, no behavior change (e.g. the description-length fix in v1.0.0) |
| **MINOR** | New capability, backward compatible — an existing `project-journal/` still works (e.g. adding Step 6) |
| **MAJOR** | Breaks or invalidates an existing `project-journal/` — a Step 0 question removed/renamed, a required README section dropped |

Then: `python build.py` to rebuild the bundle, move `CHANGELOG.md`'s `[Unreleased]`
entries under a new version heading, tag and publish via Releases (reuse that section as
the release notes), attach the rebuilt `.skill`, close the reminder issue.

## Ground rules

- Keep the journal format genuinely skimmable — tables and diagrams over prose, always.
- Explain the *why* behind a change so others can learn from it.
