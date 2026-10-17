#!/usr/bin/env python3
"""
Builds the two photo-based animated SVGs for the profile README:
  assets/avatar.svg      round portrait with a rotating neon ring
  assets/milestones.svg  auto-advancing slideshow (SIH, aOS, ...)

Why SVG? GitHub READMEs cannot run JavaScript. An SVG shown through <img>
CAN animate, but it cannot load external files, so the photos are resized
and embedded inside the SVG itself (that is what this script does).

Setup:
  pip install pillow
  put your photos in assets/photos/  (portrait.jpeg, sih-winning.jpeg, aos-winning.jpeg)
  python build_assets.py
  commit assets/avatar.svg and assets/milestones.svg

To add a slide, add an entry to SLIDES below and run the script again.
"""
import base64
import io
import sys
from pathlib import Path
from xml.sax.saxutils import escape

from PIL import Image, ImageOps

ROOT = Path(__file__).resolve().parent
PHOTOS = ROOT / "assets" / "photos"
OUT = ROOT / "assets"

SECONDS_PER_SLIDE = 5.0

# focus = (x, y) crop centre, 0..1. Lower y keeps heads in frame for group photos.
SLIDES = [
    {
        "photo": "sih-winning.jpeg",
        "focus": (0.5, 0.35),
        "title": ["Smart India Hackathon 2025"],
        "lines": ["National Winner · Ministry of Defence",
                  "Bond · secure communication for defence use cases"],
    },
    {
        "photo": "aos-winning.jpeg",
        "focus": (0.5, 0.35),
        "title": ["aOS Global Buildathon 2025"],
        "lines": ["Runner-up · $1,500 award",
                  "NeoSlot · NFT marketplace"],
    },
]

MONO = "ui-monospace,SFMono-Regular,Menlo,Consolas,monospace"
SANS = "'Segoe UI',Helvetica,Arial,sans-serif"


def encode(name, size, quality, focus=(0.5, 0.4)):
    path = PHOTOS / name
    if not path.exists():
        sys.exit(f"Missing photo: {path}")
    img = ImageOps.exif_transpose(Image.open(path)).convert("RGB")
    img = ImageOps.fit(img, (size, size), Image.LANCZOS, centering=focus)
    buf = io.BytesIO()
    img.save(buf, "JPEG", quality=quality, optimize=True, progressive=True)
    return "data:image/jpeg;base64," + base64.b64encode(buf.getvalue()).decode()


def build_avatar():
    data = encode("portrait.jpeg", 400, 78)
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 240 240" width="240" height="240" role="img" aria-label="Kanaga Abishek portrait">
  <defs>
    <clipPath id="c"><circle cx="120" cy="120" r="100"/></clipPath>
    <linearGradient id="ring" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#22D3EE"/><stop offset="1" stop-color="#6366F1"/>
    </linearGradient>
  </defs>
  <circle cx="120" cy="120" r="116" fill="none" stroke="url(#ring)" stroke-width="2"/>
  <circle cx="120" cy="120" r="108" fill="none" stroke="#22D3EE" stroke-width="2" stroke-dasharray="6 14" stroke-linecap="round">
    <animateTransform attributeName="transform" type="rotate" from="0 120 120" to="360 120 120" dur="14s" repeatCount="indefinite"/>
  </circle>
  <image xlink:href="{data}" x="20" y="20" width="200" height="200" clip-path="url(#c)" preserveAspectRatio="xMidYMid slice"/>
  <circle cx="120" cy="120" r="100" fill="none" stroke="#0F172A" stroke-opacity="0.5" stroke-width="2"/>
</svg>
'''
    (OUT / "avatar.svg").write_text(svg, encoding="utf-8")


def build_slideshow():
    n = len(SLIDES)
    T = SECONDS_PER_SLIDE
    D = n * T
    fade = 0.5
    key_times = f"0;{fade / D:.4f};{(T - fade) / D:.4f};{T / D:.4f};1"
    values = "0;1;1;0;0"

    slides = []
    dots_base = []
    for i, s in enumerate(SLIDES):
        data = encode(s["photo"], 480, 70, s.get("focus", (0.5, 0.4)))
        begin = f"{i * T:g}s"
        dot_x = 830 - (n - 1 - i) * 20

        text = [f'<text x="310" y="78" font-family="{MONO}" font-size="12" letter-spacing="3" fill="#67E8F9">MILESTONE {i + 1:02d} / {n:02d}</text>']
        y = 122
        for line in s["title"]:
            text.append(f'<text x="310" y="{y}" font-family="{SANS}" font-size="26" font-weight="800" fill="#F8FAFC">{escape(line)}</text>')
            y += 34
        y += 4
        for line in s["lines"]:
            text.append(f'<text x="310" y="{y}" font-family="{SANS}" font-size="15" fill="#CBD5E1">{escape(line)}</text>')
            y += 26
        text_block = "\n      ".join(text)

        dots_base.append(f'<circle cx="{dot_x}" cy="44" r="4" fill="#334155"/>')
        slides.append(f'''  <g opacity="0">
    <animate attributeName="opacity" values="{values}" keyTimes="{key_times}" dur="{D:g}s" begin="{begin}" repeatCount="indefinite"/>
    <image xlink:href="{data}" x="30" y="30" width="240" height="240" clip-path="url(#pc)" preserveAspectRatio="xMidYMid slice"/>
    <g clip-path="url(#pc)">
      <rect x="30" y="30" width="240" height="2" fill="#22D3EE" opacity="0.8">
        <animate attributeName="y" values="30;268;30" dur="3s" repeatCount="indefinite"/>
      </rect>
    </g>
      {text_block}
    <circle cx="{dot_x}" cy="44" r="4" fill="#22D3EE"/>
    <rect x="310" y="272" width="0" height="3" rx="1.5" fill="#22D3EE">
      <animate attributeName="width" values="0;520;520" keyTimes="0;{T / D:.4f};1" dur="{D:g}s" begin="{begin}" repeatCount="indefinite"/>
    </rect>
  </g>''')

    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 860 300" width="860" height="300" role="img" aria-label="Milestones slideshow">
  <defs>
    <clipPath id="pc"><rect x="30" y="30" width="240" height="240" rx="14"/></clipPath>
    <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#0B1220"/><stop offset="1" stop-color="#111B33"/>
    </linearGradient>
  </defs>
  <rect x="1" y="1" width="858" height="298" rx="16" fill="url(#bg)" stroke="#1E293B" stroke-width="2"/>
  <rect x="30" y="30" width="240" height="240" rx="14" fill="none" stroke="#22D3EE" stroke-opacity="0.5" stroke-width="2"/>
  <path d="M14 38V14H38 M822 14H846V38 M846 262V286H822 M38 286H14V262" fill="none" stroke="#22D3EE" stroke-width="2"/>
  <rect x="310" y="272" width="520" height="3" rx="1.5" fill="#1E293B"/>
  {chr(10).join("  " + d for d in dots_base).strip()}
{chr(10).join(slides)}
</svg>
'''
    (OUT / "milestones.svg").write_text(svg, encoding="utf-8")


if __name__ == "__main__":
    build_avatar()
    build_slideshow()
    for f in ("avatar.svg", "milestones.svg"):
        kb = (OUT / f).stat().st_size / 1024
        print(f"{f}: {kb:.0f} KB")
