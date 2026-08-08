"""Rebuild project-planning-journaling.skill from the source folder.

Run this after editing anything inside project-planning-journaling/, then
commit the regenerated .skill alongside your change:

    python build.py

The Scrum Guide PDF in references/ is deliberately excluded — nothing reads
it at runtime and it's 250 KB of mostly-unrelated bulk for a chat bundle.
"""

import os
import sys
import zipfile

ROOT = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(ROOT, "project-planning-journaling")
OUT = os.path.join(ROOT, "project-planning-journaling.skill")

# Paths relative to project-planning-journaling/, in the layout SKILL.md expects.
INCLUDE = [
    "SKILL.md",
    "references/original-prompt.md",
    "references/research.md",
]


def main():
    missing = [r for r in INCLUDE
               if not os.path.isfile(os.path.join(SRC, r.replace("/", os.sep)))]
    if missing:
        sys.exit("error: missing source file(s): %s" % ", ".join(missing))

    with zipfile.ZipFile(OUT, "w", zipfile.ZIP_DEFLATED) as bundle:
        for rel in INCLUDE:
            bundle.write(os.path.join(SRC, rel.replace("/", os.sep)),
                         "project-planning-journaling/" + rel)

    print("wrote %s" % os.path.basename(OUT))
    with zipfile.ZipFile(OUT) as bundle:
        for info in bundle.infolist():
            print("  %7d  %s" % (info.file_size, info.filename))


if __name__ == "__main__":
    main()
