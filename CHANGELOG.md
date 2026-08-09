# Changelog

All notable changes to this project are documented here. The format follows
[Keep a Changelog](https://keepachangelog.com/en/1.1.0/); this project uses
[Semantic Versioning](https://semver.org/spec/v2.0.0.html) — see CONTRIBUTING.md's
"Cutting a release" for what counts as a release and how a change is classified.

## [Unreleased]

## [1.0.0] - 2026-08-09

First stable release: scope a project before any code is written, then keep a living,
resumable documentation journal with a weekly routine review.

### Added
- `project-planning-journaling` Skill — Step 0 project intake (scope & type, repo status,
  timeline, public-vs-private-product path, dev style, review cadence), a
  `project-journal/` documentation system (dashboard README, decisions log, snippets,
  sessions), and a Step 6 routine review distinct from event-triggered updates.
- `universal-prompt.md` — condensed copy-paste version for ChatGPT, Grok, Gemini, and any
  other AI chat, no install required.
- `project-planning-journaling.skill` — one-click installable bundle for Claude.
- `references/research.md` — 10 open + 5 closed references backing every step, each with
  independent-reputation evidence, not just a top search result.
- Weekly GitHub Actions — `check-links.yml` (link liveness) and `reference-review.yml`
  (reputation-review reminder issue).
- English, Swedish, and Persian READMEs and landing pages (`index.html`, `index.sv.html`,
  `index.fa.html`), served via GitHub Pages.
- Demo GIF (`assets/skill-demo-mockup.gif`) showing Step 0 intake through to the
  generated journal dashboard.

### Fixed
- `SKILL.md`'s frontmatter description trimmed to fit Claude's 1024-character
  skill-upload limit; confirmed the `.skill` bundle installs and runs correctly.

[Unreleased]: https://github.com/mh-mansouri/Project-Planning-Journaling/compare/v1.0.0...HEAD
[1.0.0]: https://github.com/mh-mansouri/Project-Planning-Journaling/releases/tag/v1.0.0
