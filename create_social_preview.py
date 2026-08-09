"""Generate the social-preview image used for link unfurls (LinkedIn, Slack,
GitHub's own repo card) and for the og:image / twitter:image meta tags on
index.html.

GitHub's recommended social-preview size is 1280x640. Regenerate after any
rename/tagline change with `python create_social_preview.py`, then re-upload
it at Settings -> General -> Social preview (this repo's own OG tags pick up
the file automatically once pushed; GitHub's copy does not).
"""
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

WIDTH, HEIGHT = 1280, 640
OUTPUT = Path("assets/social-preview.png")

BG = "#0e1016"
PANEL = "#161922"
BORDER = "#2b2f3b"
ACCENT = "#7c93ff"
ACCENT_DARK = "#3457d5"
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


TITLE_FONT = get_font(58, bold=True)
TAGLINE_FONT = get_font(26)
PILL_FONT = get_font(20)
FOOTER_FONT = get_font(20)

PILLS = ["Step 0 \u2014 Intake", "Living Journal", "Weekly Routine Review"]


def build_image() -> None:
    img = Image.new("RGB", (WIDTH, HEIGHT), BG)
    draw = ImageDraw.Draw(img)

    draw.rounded_rectangle((28, 28, WIDTH - 28, HEIGHT - 28), radius=32, outline=BORDER, width=3)

    # Accent bar
    draw.rounded_rectangle((80, 96, 80 + 64, 96 + 10), radius=5, fill=ACCENT)

    draw.text((80, 148), "Project Planning", font=TITLE_FONT, fill=TEXT)
    draw.text((80, 218), "& Journaling", font=TITLE_FONT, fill=TEXT)

    draw.text((80, 300), "A Claude Skill \u2014 scope first, journal as you go,", font=TAGLINE_FONT, fill=MUTED)
    draw.text((80, 336), "review on a cadence.", font=TAGLINE_FONT, fill=MUTED)

    x = 80
    y = 404
    for label in PILLS:
        bbox = draw.textbbox((0, 0), label, font=PILL_FONT)
        w = bbox[2] - bbox[0]
        pill_w = w + 44
        pill_h = 46
        draw.rounded_rectangle((x, y, x + pill_w, y + pill_h), radius=23, fill=PANEL, outline=ACCENT_DARK, width=2)
        draw.text((x + 22, y + 12), label, font=PILL_FONT, fill=TEXT)
        x += pill_w + 16

    draw.text((80, HEIGHT - 90), "github.com/mh-mansouri/Project-Planning-Journaling", font=FOOTER_FONT, fill=MUTED)

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    img.save(OUTPUT)


if __name__ == "__main__":
    build_image()
    print(f"Created {OUTPUT}")
