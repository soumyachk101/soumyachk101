"""Hand-author the hackathons card, re-themed to 'Noir · Gold & Crimson'.

    python scripts/make_hackathons_card.py            # hackathons-card.svg
    STATIC=1 python scripts/make_hackathons_card.py   # frozen frame
"""

import os
from html import escape

from theme import P, MONO

FONT = MONO
FS = 13.0
LH = 32.0
PAD_X = 24.0
BAR_H = 34.0
STAGGER = 0.20
FADE = 0.45

W = 860
TITLE = "soumyachk101@github:~/hackathons.txt"

# tag color: winner=gold, security=crimson, space=steel, shipped=ember
ENTRIES = [
    ("WINNER", P("gold_hi"), "FusioniX'26 · Joint Winner", "Credow: corporate credit on Algorand with x402 vault"),
    ("SECURITY", P("crim_hi"), "Innofusion 3.0 · Cybersecurity", "DRISHTI: graphs network attack paths by dollar impact"),
    ("ISRO BAH", P("steel_hi"), "Bharatiya Antariksh '26 (ISRO)", "National space tech hackathon idea submission & cert"),
    ("HACKFEST", P("gold"), "AKI HACKS × Hacktoberfest '26", "MLH · DEV · Diversion 2K27 — Kolkata (Oct 31, 2026)"),
    ("TRACK", P("ember"), "10+ Shipped Hackathons in 2026", "FusioniX, Innofusion, Citadel, HackTropica, etc."),
]


def main() -> None:
    static = os.environ.get("STATIC") == "1"
    height = round(BAR_H + 20 + len(ENTRIES) * LH + 14)

    def anim(i: int) -> str:
        if static:
            return ""
        begin = 0.2 + i * STAGGER
        return f'<animate attributeName="opacity" from="0" to="1" begin="{begin:.2f}s" dur="{FADE}s" fill="freeze"/>'

    op = "1" if static else "0"
    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{height}" viewBox="0 0 {W} {height}" text-rendering="geometricPrecision" shape-rendering="geometricPrecision">',
        "<style>text{-webkit-font-smoothing:antialiased;-moz-osx-font-smoothing:grayscale;}</style>",
        "<defs>",
        '  <linearGradient id="gBase" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#0e0e14"/><stop offset="1" stop-color="#0a0a0f"/></linearGradient>',
        '  <linearGradient id="gKeyline" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#b03a45"/><stop offset="0.55" stop-color="#d8a63f"/><stop offset="1" stop-color="#7c5f24"/></linearGradient>',
        "  <linearGradient id=\"gSheen\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"0\"><stop offset=\"0\" stop-color=\"#f2d489\" stop-opacity=\"0\"/><stop offset=\"0.5\" stop-color=\"#f2d489\" stop-opacity=\"0.4\"/><stop offset=\"1\" stop-color=\"#f2d489\" stop-opacity=\"0\"/></linearGradient>",
        "</defs>",
        f'<rect x="0.5" y="0.5" width="{W - 1}" height="{height - 1}" rx="10" fill="url(#gBase)" stroke="{P("border")}" stroke-width="1"/>',
        f'<rect x="0.5" y="8.5" width="3.5" height="{height - 17}" fill="url(#gKeyline)"/>',
        # film-slate chrome bar
        f'<rect x="0.5" y="0.5" width="{W - 1}" height="{BAR_H - 0.5}" fill="{P("surface")}"/>',
        f'<line x1="1" y1="{BAR_H}" x2="{W - 1}" y2="{BAR_H}" stroke="{P("hair")}" stroke-width="1"/>',
        f'<circle cx="20" cy="{BAR_H / 2}" r="4" fill="{P("gold")}"/>',
        f'<circle cx="36" cy="{BAR_H / 2}" r="4" fill="{P("crim")}"/>',
        f'<circle cx="52" cy="{BAR_H / 2}" r="4" fill="{P("steel")}"/>',
        f'<text x="{W / 2}" y="{BAR_H / 2 + 4}" text-anchor="middle" font-family="{FONT}" font-size="12" fill="{P("dim")}">{escape(TITLE)}</text>',
        # slow top sheen
        f'<g><rect x="-200" y="9.5" width="200" height="1.4" fill="url(#gSheen)">'
        f'<animateTransform attributeName="transform" type="translate" from="0 0" to="{W + 40} 0" dur="5.5s" repeatCount="indefinite" calcMode="spline" keySplines="0.4 0 0.6 1"/></rect></g>',
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
            f'<tspan fill="{P("text")}" font-weight="bold">{escape(title_str)}</tspan>'
            f'<tspan fill="{P("dim")}">·  {escape(desc)}</tspan>'
            f'</text>{anim(i)}</g>'
        )
        y += LH

    parts.append("</g></svg>")
    with open("hackathons-card.svg", "w", encoding="utf-8") as f:
        f.write("\n".join(parts))
    print(f"wrote hackathons-card.svg ({W}x{height}, {'static' if static else 'animated'})")


if __name__ == "__main__":
    main()
