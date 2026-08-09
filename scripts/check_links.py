"""Verify every outbound link in the READMEs, the landing page, and the skill's
own docs still resolves.

These are the links a reader (or Claude, following the skill) actually opens —
install instructions, the research citations backing each step, license and
attribution notices. A moved reference or a renamed repo fails silently
otherwise; nobody notices until someone reports a dead citation. The weekly
schedule catches rot on a repository that otherwise goes weeks without a push,
and doubles as the cadence for the reference-reputation review (see
reference-review.yml).

Some hosts (Claude.ai; journals.sagepub.com, which fronts academic content
with bot-blocking) return 403 to a plain scripted request even though the
page itself is confirmed live in a real browser. Those are treated as
unverifiable rather than failures. Everything else must return a successful
or redirect status.

A push that both adds a page and links to it (e.g. a new index.*.html plus a
README pointing at its Pages URL) races GitHub Pages' own build: check-links
can run and hit a 404 before the deploy that makes the link real has
finished -- seen in practice, ~45s. 404s on our own Pages domain get a few
retries with backoff for exactly that reason; 404s elsewhere fail immediately,
since retrying a truly dead external link would just waste CI time.
"""
from __future__ import annotations

import re
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

if sys.stdout.encoding.lower() != "utf-8":
    sys.stdout.reconfigure(encoding="utf-8")

ROOT = Path(__file__).resolve().parent.parent

FILES = [
    ROOT / "README.md",
    ROOT / "README.sv.md",
    ROOT / "README.fa.md",
    ROOT / "index.html",
    ROOT / "index.sv.html",
    ROOT / "index.fa.html",
    ROOT / "universal-prompt.md",
    ROOT / "CONTRIBUTING.md",
    ROOT / "CHANGELOG.md",
    ROOT / "NOTICE.md",
    ROOT / "project-planning-journaling" / "SKILL.md",
    ROOT / "project-planning-journaling" / "references" / "research.md",
    ROOT / "project-planning-journaling" / "references" / "original-prompt.md",
]

# Markdown `[text](url)` and HTML `href="url"` / `src="url"`, in one pass.
LINK_RE = re.compile(r'\]\((https?://[^)\s]+)\)|(?:href|src)="(https?://[^"]+)"')

BOT_PROTECTED_DOMAINS = ("claude.ai", "journals.sagepub.com")
SELF_PAGES_DOMAIN = "mh-mansouri.github.io"

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
        "(KHTML, like Gecko) Chrome/124.0 Safari/537.36"
    ),
}


def collect_urls() -> list[tuple[str, str]]:
    """(source file, url) pairs, in file order, de-duplicated by url."""
    seen: set[str] = set()
    urls: list[tuple[str, str]] = []
    for path in FILES:
        if not path.is_file():
            continue
        for match in LINK_RE.finditer(path.read_text(encoding="utf-8")):
            url = (match.group(1) or match.group(2)).rstrip(".,")
            if url in seen:
                continue
            seen.add(url)
            urls.append((path.name, url))
    return urls


def check(url: str, retries: int = 3) -> str | None:
    request = urllib.request.Request(url, headers=HEADERS, method="GET")
    for attempt in range(retries):
        try:
            with urllib.request.urlopen(request, timeout=15) as response:
                if 200 <= response.status < 400:
                    return None
                return f"unexpected status {response.status}"
        except urllib.error.HTTPError as exc:
            # Python's redirect handler doesn't chase 308s, but the resource is live.
            if 300 <= exc.code < 400:
                return None
            if exc.code == 403 and any(domain in url for domain in BOT_PROTECTED_DOMAINS):
                return None
            # Several links share a host (e.g. github.com); back off and retry
            # once or twice rather than failing the build over rate-limiting.
            if exc.code == 429 and attempt < retries - 1:
                time.sleep(5 * (attempt + 1))
                continue
            # Our own Pages site, just deployed to, racing this very check.
            if exc.code == 404 and SELF_PAGES_DOMAIN in url and attempt < retries - 1:
                time.sleep(20 * (attempt + 1))
                continue
            return f"HTTP {exc.code}"
        except urllib.error.URLError as exc:
            return str(exc.reason)
    return "exhausted retries"


def main() -> int:
    failures = []
    for source, url in collect_urls():
        error = check(url)
        if error is None:
            print(f"OK   {url}")
        else:
            print(f"FAIL {url} ({source}): {error}")
            failures.append((source, url, error))
        time.sleep(0.5)  # be polite to hosts we hit more than once

    if failures:
        print(f"\n{len(failures)} broken link(s):")
        for source, url, error in failures:
            print(f"  {source}: {url} -> {error}")
        return 1

    print("\nAll links OK.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
