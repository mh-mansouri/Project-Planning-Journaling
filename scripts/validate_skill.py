"""Catch SKILL.md frontmatter problems before an upload attempt does.

Written after v1.0.0 shipped with a description field 26 characters over
Claude's 1024-char skill-upload limit -- caught only when a real upload
failed. This checks the same constraints locally/in CI so that class of bug
can't reach a release again.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILL_MD = ROOT / "project-planning-journaling" / "SKILL.md"
SKILL_DIR_NAME = "project-planning-journaling"

NAME_PATTERN = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
MAX_DESCRIPTION_CHARS = 1024
ALLOWED_FIELDS = {"name", "description"}


def parse_frontmatter(text: str) -> dict[str, str]:
    if not text.startswith("---\n"):
        sys.exit(f"error: {SKILL_MD} does not start with a '---' frontmatter block")
    end = text.find("\n---", 4)
    if end == -1:
        sys.exit(f"error: {SKILL_MD} frontmatter has no closing '---'")
    block = text[4:end]

    fields: dict[str, str] = {}
    current_key: str | None = None
    for line in block.split("\n"):
        if line.startswith((" ", "\t")):
            # Continuation of a multi-line value (unlikely here, but don't misparse it).
            if current_key:
                fields[current_key] += " " + line.strip()
            continue
        if ":" not in line:
            continue
        key, _, value = line.partition(":")
        current_key = key.strip()
        fields[current_key] = value.strip()
    return fields


def main() -> int:
    text = SKILL_MD.read_text(encoding="utf-8")
    fields = parse_frontmatter(text)
    errors = []

    for required in ("name", "description"):
        if not fields.get(required):
            errors.append(f"missing or empty '{required}' field")

    extra = set(fields) - ALLOWED_FIELDS
    if extra:
        errors.append(f"unexpected frontmatter field(s): {', '.join(sorted(extra))}")

    name = fields.get("name", "")
    if name and not NAME_PATTERN.match(name):
        errors.append(f"'name: {name}' must be lowercase, digits, and hyphens only")
    if name and name != SKILL_DIR_NAME:
        errors.append(f"'name: {name}' must match the skill folder name '{SKILL_DIR_NAME}'")

    description = fields.get("description", "")
    if len(description) > MAX_DESCRIPTION_CHARS:
        errors.append(
            f"description is {len(description)} chars, over Claude's "
            f"{MAX_DESCRIPTION_CHARS}-char skill-upload limit by "
            f"{len(description) - MAX_DESCRIPTION_CHARS}"
        )

    if errors:
        print(f"FAIL {SKILL_MD}")
        for error in errors:
            print(f"  - {error}")
        return 1

    print(f"OK   {SKILL_MD}")
    print(f"     name: {name}")
    print(f"     description: {len(description)}/{MAX_DESCRIPTION_CHARS} chars")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
