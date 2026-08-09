"""Generate a mock-up demo GIF showing how the skill is used.

No screen recording exists yet for `project-planning-journaling`, so this
draws a synthetic mock-up instead: a scripted scenario (a photo-renaming CLI
tool, the same example used in the README) walked through Step 0 intake and
into the generated journal dashboard. It has no bearing on the skill's
behaviour -- it only illustrates it. Replace `assets/skill-demo-mockup.gif`
with a real screen recording under the same filename if one is ever made;
nothing else needs to change.
"""
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

WIDTH, HEIGHT = 1200, 680
OUTPUT = Path("assets/skill-demo-mockup.gif")

ACCENT = "#7c93ff"
ACCENT_DARK = "#3457d5"
BG = "#0e1016"
PANEL = "#161922"
BORDER = "#2b2f3b"
TEXT = "#eceef2"
MUTED = "#a2a9b6"


def get_font(size: int, bold: bool = False) -> ImageFont.ImageFont:
    candidates = [
        "C:/Windows/Fonts/arialbd.ttf" if bold else "C:/Windows/Fonts/arial.ttf",
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf" if bold else "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
        "/System/Library/Fonts/Supplemental/Arial.ttf",
    ]
    for path in candidates:
        try:
            return ImageFont.truetype(path, size)
        except Exception:
            continue
    return ImageFont.load_default()


TITLE_FONT = get_font(34, bold=True)
SUBTITLE_FONT = get_font(20)
BODY_FONT = get_font(21)
SMALL_FONT = get_font(17)
TINY_FONT = get_font(15)

STEP0_QUESTIONS = [
    "Scope & type: CLI tool, just you",
    "Repo: none yet -> propose photo-batch-rename, public, MIT",
    "Timeline: MVP this weekend vs. a real releasable tool later",
    "Public repo, or private if it becomes a product?",
    "Dev style: interactive/iterative",
    "Review cadence: weekly",
]

ROADMAP_ITEMS = [
    "Scope & repo info recorded",
    "project-journal/ folder created",
    "Core rename logic (dry-run first)",
    "Undo log for renamed files",
    "Publish to PyPI",
]

DECISION_ROW = ("Dry-run by default", "Renaming files is hard to undo; safety first", "Day 1")


def rounded_panel(draw, box, fill=PANEL, outline=BORDER, width=2, radius=20):
    draw.rounded_rectangle(box, radius=radius, fill=fill, outline=outline, width=width)


def draw_header(draw):
    draw.rectangle((0, 0, WIDTH, HEIGHT), fill=BG)
    draw.rounded_rectangle((30, 30, WIDTH - 30, HEIGHT - 30), radius=28, outline=BORDER, width=2)
    draw.text((66, 46), "Project Planning & Journaling", font=TITLE_FONT, fill=TEXT)
    draw.text((66, 86), "Scope first. Journal as you go. Review on a cadence.", font=SUBTITLE_FONT, fill=MUTED)


def draw_frame_intro(step: int) -> Image.Image:
    img = Image.new("RGB", (WIDTH, HEIGHT), BG)
    draw = ImageDraw.Draw(img)
    draw_header(draw)

    rounded_panel(draw, (66, 140, 700, 240))
    draw.text((92, 160), "You", font=BODY_FONT, fill=TEXT)
    draw.text((92, 195), "\u201cI'm starting a CLI tool that renames photo", font=SMALL_FONT, fill=MUTED)
    draw.text((92, 217), "batches, just me working on it for now.\u201d", font=SMALL_FONT, fill=MUTED)

    if step >= 1:
        rounded_panel(draw, (760, 140, 1134, 260), fill="#151b30", outline=ACCENT)
        draw.text((786, 158), "Claude", font=BODY_FONT, fill=TEXT)
        draw.text((786, 192), "Before any code \u2014 six quick questions", font=SMALL_FONT, fill=ACCENT)
        draw.text((786, 216), "(Step 0: intake)", font=TINY_FONT, fill=MUTED)

    rounded_panel(draw, (66, 290, 1134, 610))
    draw.text((92, 312), "Step 0 \u2014 Project intake", font=BODY_FONT, fill=TEXT)

    shown = min(step, len(STEP0_QUESTIONS))
    for i in range(shown):
        y = 356 + i * 40
        cx, cy = 100, y + 8
        draw.ellipse((cx - 9, cy - 9, cx + 9, cy + 9), fill=ACCENT_DARK)
        draw.line((cx - 4, cy, cx - 1, cy + 4), fill="white", width=2)
        draw.line((cx - 1, cy + 4, cx + 5, cy - 5), fill="white", width=2)
        draw.text((120, y), STEP0_QUESTIONS[i], font=SMALL_FONT, fill=TEXT)

    return img


def draw_frame_journal(step: int) -> Image.Image:
    img = Image.new("RGB", (WIDTH, HEIGHT), BG)
    draw = ImageDraw.Draw(img)
    draw_header(draw)

    rounded_panel(draw, (66, 140, 1134, 610))
    draw.text((92, 162), "project-journal/README.md", font=BODY_FONT, fill=TEXT)
    draw.line((92, 198, 1108, 198), fill=BORDER, width=1)

    draw.text((92, 216), "Roadmap / Milestones", font=SMALL_FONT, fill=ACCENT)
    shown_roadmap = 0
    if step >= 1:
        shown_roadmap = min(step, len(ROADMAP_ITEMS))
    for i, item in enumerate(ROADMAP_ITEMS):
        y = 248 + i * 34
        done = i < shown_roadmap
        box_fill = ACCENT_DARK if done else "#232837"
        draw.rounded_rectangle((92, y, 112, y + 20), radius=4, fill=box_fill, outline=BORDER)
        if done:
            draw.line((96, y + 10, 100, y + 15), fill="white", width=2)
            draw.line((100, y + 15, 108, y + 5), fill="white", width=2)
        color = TEXT if done else MUTED
        draw.text((122, y - 1), item, font=SMALL_FONT, fill=color)

    draw.text((640, 216), "Key Decisions Log", font=SMALL_FONT, fill=ACCENT)
    if step >= 4:
        rounded_panel(draw, (640, 246, 1108, 330), fill="#151b30", outline=BORDER, radius=12)
        draw.text((656, 258), DECISION_ROW[0], font=SMALL_FONT, fill=TEXT)
        draw.text((656, 284), DECISION_ROW[1], font=TINY_FONT, fill=MUTED)
        draw.text((656, 306), "Date: " + DECISION_ROW[2], font=TINY_FONT, fill=MUTED)

    if step >= 5:
        rounded_panel(draw, (640, 344, 1108, 420), fill="#151b30", outline=BORDER, radius=12)
        draw.text((656, 356), "Step 6 \u2014 Routine review (weekly)", font=SMALL_FONT, fill=ACCENT)
        draw.text((656, 384), "[x] Links   [x] Decisions   [x] Roadmap   [x] Sources", font=TINY_FONT, fill=MUTED)

    draw.text((92, 560), "Open this file in any new session \u2014 no chat history needed.", font=TINY_FONT, fill=MUTED)

    return img


def build_gif() -> None:
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    frames = (
        [draw_frame_intro(step) for step in [0, 1, 2, 3, 4, 5, 6, 6, 6]]
        + [draw_frame_journal(step) for step in [0, 1, 2, 3, 4, 5, 5, 5, 5]]
    )
    durations = (
        [700, 700, 700, 700, 700, 700, 700, 1400, 1800]
        + [500, 500, 500, 500, 700, 700, 700, 1000, 2200]
    )
    assert len(frames) == len(durations), (len(frames), len(durations))
    frames[0].save(
        OUTPUT,
        save_all=True,
        append_images=frames[1:],
        duration=durations,
        loop=0,
        optimize=False,
    )


if __name__ == "__main__":
    build_gif()
    print(f"Created {OUTPUT}")
