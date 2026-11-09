"""Hand-author the highlights card, re-themed to 'Noir · Gold & Crimson'.
Syntax-highlighted project highlights + live telemetry; muted, filmic, no green.

    python scripts/make_highlights_card.py            # highlights-card.svg
    STATIC=1 python scripts/make_highlights_card.py   # frozen frame
"""

import json
import os
from html import escape

from theme import P, MONO

FONT = MONO
FS = 13.0
LH = 30.0
PAD_X = 24.0
BAR_H = 34.0
STAGGER = 0.18
FADE = 0.45

W = 860
TITLE = "soumyachk101@github:~/highlights.txt"

# Muted-noir syntax palette (no green, no saturated neon)
N_GOLD = P("gold")        # d8a63f
N_GOLDHI = P("gold_hi")   # f2d489
N_CRIM = P("crim")       # b03a45
N_CRIMHI = P("crim_hi")  # d4606c
N_STEEL = P("steel")     # 6b7f9c
N_STEELHI = P("steel_hi")# 93a7c4
N_EMBER = P("ember")     # c07a3a
N_TEXT = P("text")
N_DIM = P("dim")


def get_items():
    # GitHub contributions & streak
    gh_total, gh_streak = 8000, 195
    if os.path.exists("data/contributions.json"):
        try:
            with open("data/contributions.json", encoding="utf-8") as f:
                gh = json.load(f)
            gh_total = gh.get("total", gh_total)
            gh_streak = gh.get("current_streak", gh.get("longest_streak", gh_streak))
        except Exception:
            pass

    # LeetCode stats
    lc_all, lc_hard, lc_streak = 302, 68, 155
    if os.path.exists("data/leetcode.json"):
        try:
            with open("data/leetcode.json", encoding="utf-8") as f:
                lc = json.load(f)
            lc_all = lc.get("solved", {}).get("All", lc_all)
            lc_hard = lc.get("solved", {}).get("Hard", lc_hard)
            lc_streak = lc.get("calendar", {}).get("max_streak", lc_streak)
        except Exception:
            pass

    return [
        ("❯", N_GOLDHI,
         f'<tspan fill="{N_GOLDHI}" font-weight="bold">Ensembyte</tspan>'
         f'<tspan fill="{N_DIM}">: </tspan>'
         f'<tspan fill="{N_TEXT}">multi-agent client with </tspan>'
         f'<tspan fill="{N_STEEL}" font-weight="600">Swift ∞ Hydra</tspan>'
         f'<tspan fill="{N_DIM}"> &amp; </tspan>'
         f'<tspan fill="{N_STEELHI}" font-weight="600">GPUI CRDT</tspan>'
         f'<tspan fill="{N_TEXT}"> engine</tspan>'),
        ("❯", N_GOLDHI,
         f'<tspan fill="{N_GOLDHI}" font-weight="bold">Orbit</tspan>'
         f'<tspan fill="{N_DIM}">: </tspan>'
         f'<tspan fill="{N_TEXT}">lightweight device engine driving </tspan>'
         f'<tspan fill="{N_EMBER}" font-weight="600">Claude Code</tspan>'
         f'<tspan fill="{N_DIM}">, </tspan>'
         f'<tspan fill="{N_STEELHI}" font-weight="600">Cursor</tspan>'
         f'<tspan fill="{N_DIM}"> &amp; </tspan>'
         f'<tspan fill="{N_STEEL}" font-weight="600">Codex</tspan>'),
        ("❯", N_GOLDHI,
         f'<tspan fill="{N_GOLDHI}" font-weight="bold">SwarmAI</tspan>'
         f'<tspan fill="{N_DIM}">: </tspan>'
         f'<tspan fill="{N_TEXT}">hybrid </tspan>'
         f'<tspan fill="{N_EMBER}" font-weight="600">BM25</tspan>'
         f'<tspan fill="{N_DIM}"> + </tspan>'
         f'<tspan fill="{N_STEEL}" font-weight="600">dense n-gram</tspan>'
         f'<tspan fill="{N_TEXT}"> memory for </tspan>'
         f'<tspan fill="{N_CRIMHI}" font-weight="600">parallel worktrees</tspan>'),
        ("❯", N_GOLDHI,
         f'<tspan fill="{N_GOLDHI}" font-weight="bold">VERCODE</tspan>'
         f'<tspan fill="{N_DIM}">: </tspan>'
         f'<tspan fill="{N_TEXT}">deterministic AI PR review · </tspan>'
         f'<tspan fill="{N_STEELHI}" font-weight="600">Semgrep &amp; ESLint</tspan>'
         f'<tspan fill="{N_DIM}"> + </tspan>'
         f'<tspan fill="{N_CRIM}" font-weight="600">task-routed LLMs</tspan>'),
        ("❯", N_GOLD,
         f'<tspan fill="{N_GOLD}" font-weight="bold">Credow</tspan>'
         f'<tspan fill="{N_DIM}">: </tspan>'
         f'<tspan fill="{N_TEXT}">on-chain corporate credit on </tspan>'
         f'<tspan fill="{N_STEEL}" font-weight="600">Algorand</tspan>'
         f'<tspan fill="{N_DIM}"> · </tspan>'
         f'<tspan fill="{N_CRIMHI}" font-weight="600">x402 vault</tspan>'
         f'<tspan fill="{N_DIM}"> · </tspan>'
         f'<tspan fill="{N_GOLDHI}" font-weight="bold">FusioniX&#x27;26 Joint Winner</tspan>'),
        ("★", N_STEELHI,
         f'<tspan fill="{N_STEELHI}" font-weight="bold">Events</tspan>'
         f'<tspan fill="{N_DIM}">: </tspan>'
         f'<tspan fill="{N_TEXT}">ISRO BAH &#x27;26 </tspan>'
         f'<tspan fill="{N_DIM}">· </tspan>'
         f'<tspan fill="{N_CRIMHI}" font-weight="600">AKI HACKS × Hacktoberfest &#x27;26</tspan>'
         f'<tspan fill="{N_DIM}"> (MLH · DEV · Kolkata)</tspan>'),
        ("◈", N_GOLD,
         f'<tspan fill="{N_DIM}">Shipped </tspan>'
         f'<tspan fill="{N_GOLDHI}" font-weight="bold">{gh_total:,}+</tspan>'
         f'<tspan fill="{N_TEXT}"> GitHub contributions with </tspan>'
         f'<tspan fill="{N_STEELHI}" font-weight="bold">{gh_streak}-day</tspan>'
         f'<tspan fill="{N_TEXT}"> continuous streak</tspan>'),
        ("◆", N_EMBER,
         f'<tspan fill="{N_EMBER}" font-weight="bold">LeetCode</tspan>'
         f'<tspan fill="{N_DIM}"> top tier: </tspan>'
         f'<tspan fill="{N_GOLDHI}" font-weight="bold">{lc_all}</tspan>'
         f'<tspan fill="{N_TEXT}"> solved · </tspan>'
         f'<tspan fill="{N_CRIMHI}" font-weight="bold">{lc_hard} Hard</tspan>'
         f'<tspan fill="{N_TEXT}"> · </tspan>'
         f'<tspan fill="{N_STEELHI}" font-weight="bold">{lc_streak}-day</tspan>'
         f'<tspan fill="{N_TEXT}"> max streak</tspan>'),
    ]


def main() -> None:
    static = os.environ.get("STATIC") == "1"
    items = get_items()
    num_lines = len(items) + 1
    height = round(BAR_H + 16 + num_lines * LH + 14)

    def anim(i: int) -> str:
        if static:
            return ""
        begin = 0.18 + i * STAGGER
        return (
            f'<animate attributeName="opacity" from="0" to="1" '
            f'begin="{begin:.2f}s" dur="{FADE}s" fill="freeze"/>'
            f'<animateTransform attributeName="transform" type="translate" '
            f'from="-8 0" to="0 0" begin="{begin:.2f}s" dur="{FADE}s" fill="freeze"/>'
        )

    op = "1" if static else "0"
    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{height}" viewBox="0 0 {W} {height}" text-rendering="geometricPrecision" shape-rendering="geometricPrecision">',
        "<style>text{-webkit-font-smoothing:antialiased;-moz-osx-font-smoothing:grayscale;}</style>",
        "<defs>",
        '  <linearGradient id="gBase" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#0e0e14"/><stop offset="1" stop-color="#0a0a0f"/></linearGradient>',
        '  <linearGradient id="gKeyline" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#b03a45"/><stop offset="0.55" stop-color="#d8a63f"/><stop offset="1" stop-color="#7c5f24"/></linearGradient>',
        '  <linearGradient id="borderGrad" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#2a2a34"/><stop offset="0.5" stop-color="#d8a63f" stop-opacity="0.55"/><stop offset="1" stop-color="#2a2a34"/></linearGradient>',
        '  <radialGradient id="glow" cx="85%" cy="20%" r="50%"><stop offset="0%" stop-color="#d8a63f" stop-opacity="0.08"/><stop offset="100%" stop-color="#0a0a0f" stop-opacity="0"/></radialGradient>',
        "  <linearGradient id=\"gSheen\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"0\"><stop offset=\"0\" stop-color=\"#f2d489\" stop-opacity=\"0\"/><stop offset=\"0.5\" stop-color=\"#f2d489\" stop-opacity=\"0.4\"/><stop offset=\"1\" stop-color=\"#f2d489\" stop-opacity=\"0\"/></linearGradient>",
        "</defs>",
        f'<rect width="100%" height="100%" rx="10" fill="url(#gBase)" stroke="url(#borderGrad)" stroke-width="1.2"/>',
        '<rect width="100%" height="100%" rx="10" fill="url(#glow)"/>',
        f'<rect x="0.5" y="8.5" width="3.5" height="{height - 17}" fill="url(#gKeyline)"/>',
        f'<rect x="0.5" y="0.5" width="{W - 1}" height="{BAR_H - 0.5}" fill="{P("surface")}"/>',
        f'<line x1="1" y1="{BAR_H}" x2="{W - 1}" y2="{BAR_H}" stroke="{P("hair")}" stroke-width="1"/>',
        f'<circle cx="20" cy="{BAR_H / 2}" r="4" fill="{P("gold")}"/>',
        f'<circle cx="36" cy="{BAR_H / 2}" r="4" fill="{P("crim")}"/>',
        f'<circle cx="52" cy="{BAR_H / 2}" r="4" fill="{P("steel")}"/>',
        f'<text x="{W / 2}" y="{BAR_H / 2 + 4.5}" fill="{P("dim")}" font-family="{FONT}" font-size="12" text-anchor="middle">{escape(TITLE)}</text>',
    ]

    # Live pill top-right (crimson, not green)
    parts.extend([
        "<g>",
        f'<rect x="{W - 130}" y="8" width="112" height="18" rx="9" fill="{P("surface")}" stroke="{P("crim")}" stroke-width="0.8"/>',
        f'<circle cx="{W - 118}" cy="17" r="3.5" fill="{P("crim")}">',
        '  <animate attributeName="opacity" values="1;0.3;1" dur="2s" repeatCount="indefinite"/>' if not static else "",
        "</circle>",
        f'<text x="{W - 108}" y="20.5" fill="{P("crim_hi")}" font-family="{FONT}" font-size="9" font-weight="bold" letter-spacing="0.5">LIVE SYNC</text>',
        "</g>",
        f'<g font-family="{FONT}" font-size="{FS}">',
    ])

    y = BAR_H + 16 + LH * 0.65
    for i, (icon, icon_color, html_content) in enumerate(items):
        parts.append(
            f'<g opacity="{op}">'
            f'<text x="{PAD_X}" y="{y:.1f}" fill="{icon_color}" font-weight="bold">{icon}</text>'
            f'<text x="{PAD_X + 22}" y="{y:.1f}">{html_content}</text>{anim(i)}</g>'
        )
        y += LH

    # terminal prompt line with a slow gold cursor
    prompt_anim = anim(len(items))
    cursor_el = (
        f'<rect x="214" y="{y - 13:.1f}" width="8" height="15" fill="{N_GOLD}">'
        '<animate attributeName="opacity" values="1;0;1" dur="1.2s" repeatCount="indefinite"/></rect>'
        if not static
        else f'<rect x="214" y="{y - 13:.1f}" width="8" height="15" fill="{N_GOLD}"/>'
    )
    parts.append(
        f'<g opacity="{op}">'
        f'<text x="{PAD_X}" y="{y:.1f}">'
        f'<tspan fill="{N_GOLD}" font-weight="bold">soumyachk101@github</tspan>'
        f'<tspan fill="{N_DIM}">:</tspan>'
        f'<tspan fill="{N_STEEL}">~</tspan>'
        f'<tspan fill="{N_DIM}">$ </tspan>'
        f"</text>{cursor_el}{prompt_anim}</g>"
    )
    # slow bottom sheen
    parts.append(
        f'<g><rect x="-200" y="{height - 11}" width="200" height="1.4" fill="url(#gSheen)">'
        f'<animateTransform attributeName="transform" type="translate" from="0 0" to="{W + 40} 0" dur="5.5s" repeatCount="indefinite" calcMode="spline" keySplines="0.4 0 0.6 1"/></rect></g>'
    )

    parts.append("</g></svg>")
    with open("highlights-card.svg", "w", encoding="utf-8") as f:
        f.write("\n".join(parts))
    print(f"wrote highlights-card.svg ({W}x{height}, {'static' if static else 'animated'})")


if __name__ == "__main__":
    main()
