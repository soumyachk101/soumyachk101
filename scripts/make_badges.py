"""Generate self-hosted terminal-style link badges for Soumya Chakraborty.

Small pill SVGs in the shared palette, one per external link. The README
wraps each in an <a>, so nothing depends on shields.io or any external badge service.

    python scripts/make_badges.py   # writes badges/*.svg
"""

import os
from html import escape

BG = "#0d1117"
BORDER = "#30363d"
INK = "#c9d1d9"
ACCENT = "#3fb950"

FONT = "ui-monospace, SFMono-Regular, 'Cascadia Mono', Menlo, Consolas, monospace"
FS = 15.0
CW = FS * 0.602
H = 38

# (filename, label)
BADGES = [
    ("portfolio", "soumya.pro"),
    ("email", "email"),
    ("github", "github"),
    ("x", "x / @soumyachk1"),
    ("leetcode", "leetcode"),
    ("fusionix", "fusionix '26 (winner)"),
    ("credow", "credow app ↗"),
    ("innofusion", "innofusion 3.0"),
    ("drishti", "drishti demo ↗"),
    ("isro-cert", "isro cert ↗"),
    ("swarmai", "swarmai repo"),
    ("orbit", "orbit repo"),
    ("ensembyte", "ensembyte repo"),
]


def main() -> None:
    os.makedirs("badges", exist_ok=True)
    for name, label in BADGES:
        text = escape(label)
        w = round(38 + len(label) * CW + 18)
        svg = (
            f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" '
            f'height="{H}" viewBox="0 0 {w} {H}">'
            f'<rect x="0.5" y="0.5" width="{w - 1}" height="{H - 1}" rx="8" '
            f'fill="{BG}" stroke="{BORDER}"/>'
            f'<text x="15" y="25" font-family="{FONT}" font-size="{FS}" '
            f'font-weight="bold" fill="{ACCENT}">&#10095;</text>'
            f'<text x="{32}" y="25" font-family="{FONT}" font-size="{FS}" '
            f'fill="{INK}">{text}</text>'
            f"</svg>"
        )
        path = f"badges/{name}.svg"
        with open(path, "w", encoding="utf-8") as f:
            f.write(svg)
        print(f"wrote {path} ({w}x{H})")


if __name__ == "__main__":
    main()
