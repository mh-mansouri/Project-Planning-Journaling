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
| `project-planning-journaling.skill` | **Generated.** A zip of the folder above — don't edit by hand. |

## How to propose a change

1. Fork this repository.
2. Make your edit (most changes live in `project-planning-journaling/SKILL.md`).
3. **If you changed anything inside `project-planning-journaling/`, rebuild the bundle:**
   ```
   python build.py
   ```
   This regenerates `project-planning-journaling.skill` from the source folder. Commit
   the rebuilt file alongside your edit — otherwise the one-click install and the source
   folder ship different versions of the skill.
4. Open a pull request with a short note on what you changed and why.

If you edit the skill, please try it on a real (or realistic) project before submitting,
and describe what you tested in the pull request.

## Ground rules

- Keep the journal format genuinely skimmable — tables and diagrams over prose, always.
- Explain the *why* behind a change so others can learn from it.
