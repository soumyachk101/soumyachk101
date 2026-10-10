"""Hand-author the hackathons card SVG for Soumya Chakraborty.

A sleek terminal panel with title bar and staggered event rows,
mirroring the info-card and highlights-card aesthetic.

    python scripts/make_hackathons_card.py            # hackathons-card.svg
    STATIC=1 python scripts/make_hackathons_card.py   # frozen frame
"""

import os
from html import escape

BG = "#0d1117"
BAR = "#161b22"
BORDER = "#30363d"
INK = "#c9d1d9"
DIM = "#8b949e"
ACCENT = "#3fb950"
GOLD = "#d29922"
CYAN = "#58a6ff"

FONT = "ui-monospace, SFMono-Regular, 'Cascadia Mono', Menlo, Consolas, monospace"
FS = 13.0
LH = 32.0
PAD_X = 24.0
BAR_H = 32.0
STAGGER = 0.20
FADE = 0.45

W = 860
TITLE = "soumyachk101@github: ~/hackathons.txt"

ENTRIES = [
    ("WINNER", GOLD, "FusioniX'26 · Joint Winner", "Credow: corporate credit on Algorand with x402 vault"),
    ("SECURITY", ACCENT, "Innofusion 3.0 · Cybersecurity", "DRISHTI: graphs network attack paths by dollar impact"),
    ("ISRO BAH", CYAN, "Bharatiya Antariksh '26 (ISRO)", "National space tech hackathon idea submission & cert"),
    ("TRACK", INK, "7 Shipped Hackathons in 2026", "FusioniX, Innofusion, Citadel, Code for Change, HackTropica"),
]


def main() -> None:
    static = os.environ.get("STATIC") == "1"

    height = round(BAR_H + 20 + len(ENTRIES) * LH + 14)

    def anim(i: int) -> str:
        if static:
            return ""
        begin = 0.2 + i * STAGGER
        return (
            f'<animate attributeName="opacity" from="0" to="1" '
            f'begin="{begin:.2f}s" dur="{FADE}s" fill="freeze"/>'
        )

    op = "1" if static else "0"
    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" '
        f'height="{height}" viewBox="0 0 {W} {height}">',
        f'<rect width="100%" height="100%" rx="8" fill="{BG}" '
        f'stroke="{BORDER}" stroke-width="1"/>',
        f'<path d="M1 9 a8 8 0 0 1 8-8 h{W - 18} a8 8 0 0 1 8 8 '
        f'v{BAR_H - 9} h-{W - 2} z" fill="{BAR}"/>',
        f'<line x1="1" y1="{BAR_H}" x2="{W - 1}" y2="{BAR_H}" '
        f'stroke="{BORDER}" stroke-width="1"/>',
        f'<circle cx="20" cy="{BAR_H / 2}" r="5" fill="#f85149"/>',
        f'<circle cx="38" cy="{BAR_H / 2}" r="5" fill="#d29922"/>',
        f'<circle cx="56" cy="{BAR_H / 2}" r="5" fill="{ACCENT}"/>',
        f'<text x="{W / 2}" y="{BAR_H / 2 + FS * 0.34}" fill="{DIM}" '
        f'font-family="{FONT}" font-size="{FS - 1.5}" '
        f'text-anchor="middle">{escape(TITLE)}</text>',
        f'<g font-family="{FONT}" font-size="{FS}">',
    ]

    y = BAR_H + 20 + LH * 0.65
    for i, (tag, color, title, desc) in enumerate(ENTRIES):
        tag_str = f"[{tag}]".ljust(11)
        title_str = title.ljust(34)
        parts.append(
            f'<g opacity="{op}">'
            f'<text x="{PAD_X}" y="{y:.1f}">'
            f'<tspan fill="{color}" font-weight="bold">{escape(tag_str)}</tspan>'
            f'<tspan fill="{INK}" font-weight="bold">{escape(title_str)}</tspan>'
            f'<tspan fill="{DIM}">·  {escape(desc)}</tspan>'
            f'</text>{anim(i)}</g>'
        )
        y += LH

    parts.append("</g></svg>")
    with open("hackathons-card.svg", "w", encoding="utf-8") as f:
        f.write("\n".join(parts))
    print(f"wrote hackathons-card.svg ({W}x{height}, "
          f"{'static' if static else 'animated'})")


if __name__ == "__main__":
    main()
