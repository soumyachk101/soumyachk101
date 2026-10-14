"""Hand-author the highlights card SVG for Soumya Chakraborty.

A sleek terminal panel with rich syntax-highlighted lines, live telemetry badge,
and animated blinking prompt cursor.

    python scripts/make_highlights_card.py            # highlights-card.svg
    STATIC=1 python scripts/make_highlights_card.py   # frozen frame
"""

import json
import os
from html import escape

BG = "#0d1117"
BAR = "#161b22"
BORDER = "#30363d"
INK = "#c9d1d9"
DIM = "#8b949e"
ACCENT = "#3fb950"

FONT = "ui-monospace, SFMono-Regular, 'Cascadia Mono', Menlo, Consolas, monospace"
FS = 13.0
LH = 30.0
PAD_X = 24.0
BAR_H = 34.0
STAGGER = 0.18
FADE = 0.45

W = 860
TITLE = "soumyachk101@github: ~/highlights.txt"


def get_items() -> list[tuple[str, str, str]]:
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
        (
            "❯",
            "#58a6ff",
            '<tspan fill="#58a6ff" font-weight="bold">Ensembyte</tspan>'
            '<tspan fill="#8b949e">: </tspan>'
            '<tspan fill="#c9d1d9">multi-agent client with </tspan>'
            '<tspan fill="#bc8cff" font-weight="600">Swift ∞ Hydra</tspan>'
            '<tspan fill="#8b949e"> &amp; </tspan>'
            '<tspan fill="#79c0ff" font-weight="600">GPUI CRDT</tspan>'
            '<tspan fill="#c9d1d9"> engine</tspan>',
        ),
        (
            "❯",
            "#58a6ff",
            '<tspan fill="#58a6ff" font-weight="bold">Orbit</tspan>'
            '<tspan fill="#8b949e">: </tspan>'
            '<tspan fill="#c9d1d9">lightweight device engine driving </tspan>'
            '<tspan fill="#f0883e" font-weight="600">Claude Code</tspan>'
            '<tspan fill="#8b949e">, </tspan>'
            '<tspan fill="#79c0ff" font-weight="600">Cursor</tspan>'
            '<tspan fill="#8b949e"> &amp; </tspan>'
            '<tspan fill="#a5d6ff" font-weight="600">Codex</tspan>',
        ),
        (
            "❯",
            "#58a6ff",
            '<tspan fill="#58a6ff" font-weight="bold">SwarmAI</tspan>'
            '<tspan fill="#8b949e">: </tspan>'
            '<tspan fill="#c9d1d9">hybrid </tspan>'
            '<tspan fill="#ffa657" font-weight="600">BM25</tspan>'
            '<tspan fill="#8b949e"> + </tspan>'
            '<tspan fill="#7ee787" font-weight="600">dense n-gram</tspan>'
            '<tspan fill="#c9d1d9"> memory for </tspan>'
            '<tspan fill="#d2a8ff" font-weight="600">parallel worktrees</tspan>',
        ),
        (
            "❯",
            "#d29922",
            '<tspan fill="#d29922" font-weight="bold">Credow</tspan>'
            '<tspan fill="#8b949e">: </tspan>'
            '<tspan fill="#c9d1d9">on-chain corporate credit on </tspan>'
            '<tspan fill="#bc8cff" font-weight="600">Algorand</tspan>'
            '<tspan fill="#8b949e"> · </tspan>'
            '<tspan fill="#ff7b72" font-weight="600">x402 vault</tspan>'
            '<tspan fill="#8b949e"> · </tspan>'
            '<tspan fill="#e3b341" font-weight="bold">FusioniX&#x27;26 Joint Winner</tspan>',
        ),
        (
            "◈",
            "#39d353",
            '<tspan fill="#8b949e">Shipped </tspan>'
            f'<tspan fill="#39d353" font-weight="bold">{gh_total:,}+</tspan>'
            '<tspan fill="#c9d1d9"> GitHub contributions with </tspan>'
            f'<tspan fill="#56d364" font-weight="bold">{gh_streak}-day</tspan>'
            '<tspan fill="#c9d1d9"> continuous streak</tspan>',
        ),
        (
            "◆",
            "#ffa116",
            '<tspan fill="#ffa116" font-weight="bold">LeetCode</tspan>'
            '<tspan fill="#8b949e"> top tier: </tspan>'
            f'<tspan fill="#e3b341" font-weight="bold">{lc_all}</tspan>'
            '<tspan fill="#c9d1d9"> solved · </tspan>'
            f'<tspan fill="#ff7b72" font-weight="bold">{lc_hard} Hard</tspan>'
            '<tspan fill="#c9d1d9"> · </tspan>'
            f'<tspan fill="#39d353" font-weight="bold">{lc_streak}-day</tspan>'
            '<tspan fill="#c9d1d9"> max streak</tspan>',
        ),
    ]


def main() -> None:
    static = os.environ.get("STATIC") == "1"
    items = get_items()
    # 6 items + 1 prompt line
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
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" '
        f'height="{height}" viewBox="0 0 {W} {height}">',
        "<defs>",
        '  <linearGradient id="borderGrad" x1="0%" y1="0%" x2="100%" y2="100%">',
        '    <stop offset="0%" stop-color="#30363d"/>',
        '    <stop offset="50%" stop-color="#238636" stop-opacity="0.7"/>',
        '    <stop offset="100%" stop-color="#30363d"/>',
        "  </linearGradient>",
        '  <linearGradient id="barGrad" x1="0%" y1="0%" x2="100%" y2="0%">',
        '    <stop offset="0%" stop-color="#161b22"/>',
        '    <stop offset="100%" stop-color="#0d1117"/>',
        "  </linearGradient>",
        '  <radialGradient id="glow" cx="85%" cy="20%" r="50%">',
        '    <stop offset="0%" stop-color="#238636" stop-opacity="0.08"/>',
        '    <stop offset="100%" stop-color="#0d1117" stop-opacity="0"/>',
        "  </radialGradient>",
        "</defs>",
        f'<rect width="100%" height="100%" rx="9" fill="{BG}" '
        'stroke="url(#borderGrad)" stroke-width="1.2"/>',
        '<rect width="100%" height="100%" rx="9" fill="url(#glow)"/>',
        f'<path d="M1 9 a8 8 0 0 1 8-8 h{W - 18} a8 8 0 0 1 8 8 '
        f'v{BAR_H - 9} h-{W - 2} z" fill="url(#barGrad)"/>',
        f'<line x1="1" y1="{BAR_H}" x2="{W - 1}" y2="{BAR_H}" '
        f'stroke="{BORDER}" stroke-width="1"/>',
        f'<circle cx="20" cy="{BAR_H / 2}" r="5" fill="#f85149"/>',
        f'<circle cx="38" cy="{BAR_H / 2}" r="5" fill="#d29922"/>',
        f'<circle cx="56" cy="{BAR_H / 2}" r="5" fill="{ACCENT}"/>',
        f'<text x="{W / 2}" y="{BAR_H / 2 + 4.5}" fill="{DIM}" '
        f'font-family="{FONT}" font-size="12" '
        f'text-anchor="middle">{escape(TITLE)}</text>',
    ]

    # Live pill badge in top-right
    parts.extend([
        '<g>',
        f'<rect x="{W - 130}" y="8" width="112" height="18" rx="9" fill="#12251a" stroke="#2ea043" stroke-width="0.8"/>',
        f'<circle cx="{W - 118}" cy="17" r="3.5" fill="#39d353">',
        '  <animate attributeName="opacity" values="1;0.3;1" dur="2s" repeatCount="indefinite"/>' if not static else "",
        '</circle>',
        f'<text x="{W - 108}" y="20.5" fill="#39d353" font-family="{FONT}" font-size="9" font-weight="bold" letter-spacing="0.5">LIVE SYNC</text>',
        '</g>',
        f'<g font-family="{FONT}" font-size="{FS}">',
    ])

    y = BAR_H + 16 + LH * 0.65
    for i, (icon, icon_color, html_content) in enumerate(items):
        parts.append(
            f'<g opacity="{op}">'
            f'<text x="{PAD_X}" y="{y:.1f}" fill="{icon_color}" '
            f'font-weight="bold">{icon}</text>'
            f'<text x="{PAD_X + 22}" y="{y:.1f}">'
            f"{html_content}</text>{anim(i)}</g>"
        )
        y += LH

    # Terminal prompt line at bottom with blinking cursor
    prompt_anim = anim(len(items))
    cursor_el = (
        '<rect x="214" y="' + f"{y - 13:.1f}" + '" width="8" height="15" fill="#39d353">'
        '<animate attributeName="opacity" values="1;0;1" dur="1s" repeatCount="indefinite"/>'
        '</rect>' if not static else '<rect x="214" y="' + f"{y - 13:.1f}" + '" width="8" height="15" fill="#39d353"/>'
    )
    parts.append(
        f'<g opacity="{op}">'
        f'<text x="{PAD_X}" y="{y:.1f}">'
        '<tspan fill="#3fb950" font-weight="bold">soumyachk101@github</tspan>'
        '<tspan fill="#8b949e">:</tspan>'
        '<tspan fill="#58a6ff">~</tspan>'
        '<tspan fill="#8b949e">$ </tspan>'
        f'</text>{cursor_el}{prompt_anim}</g>'
    )

    parts.append("</g></svg>")
    with open("highlights-card.svg", "w", encoding="utf-8") as f:
        f.write("\n".join(parts))
    print(f"wrote highlights-card.svg ({W}x{height}, "
          f"{'static' if static else 'animated'})")


if __name__ == "__main__":
    main()
