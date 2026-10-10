"""Hand-author the highlights card SVG for Soumya Chakraborty.

A wide terminal panel matching the info card: title bar, then one
prompt-prefixed line per highlight, fading in on a stagger. Rerun
whenever the highlights change:

    python scripts/make_highlights_card.py            # highlights-card.svg
    STATIC=1 python scripts/make_highlights_card.py   # frozen frame
"""

import os
from html import escape

BG = "#0d1117"
BAR = "#161b22"
BORDER = "#30363d"
INK = "#c9d1d9"
DIM = "#8b949e"
ACCENT = "#3fb950"

FONT = "ui-monospace, SFMono-Regular, 'Cascadia Mono', Menlo, Consolas, monospace"
FS = 13.5
LH = 30.0
PAD_X = 24.0
BAR_H = 32.0
STAGGER = 0.22
FADE = 0.5

W = 860
TITLE = "soumyachk101@github: ~/highlights.txt"

LINES = [
    "Ensembyte: multi-agent client with Swift ∞ Hydra & GPUI CRDT engine",
    "Orbit: lightweight device engine driving Claude Code, Cursor & Codex",
    "SwarmAI: hybrid BM25 + dense n-gram memory for parallel worktrees",
    "Credow: on-chain corporate credit allocation on Algorand with x402 vault",
    "Shipped 7,960+ GitHub contributions with 192-day continuous streak",
    "LeetCode top tier: 297 solved with 67 Hard problems & 152-day max streak",
]


def main() -> None:
    static = os.environ.get("STATIC") == "1"

    height = round(BAR_H + 18 + len(LINES) * LH + 12)

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

    y = BAR_H + 18 + LH * 0.6
    for i, line in enumerate(LINES):
        parts.append(
            f'<g opacity="{op}">'
            f'<text x="{PAD_X}" y="{y:.1f}" fill="{ACCENT}" '
            f'font-weight="bold">&#10095;</text>'
            f'<text x="{PAD_X + 22}" y="{y:.1f}" fill="{INK}">'
            f"{escape(line)}</text>{anim(i)}</g>"
        )
        y += LH

    parts.append("</g></svg>")
    with open("highlights-card.svg", "w", encoding="utf-8") as f:
        f.write("\n".join(parts))
    print(f"wrote highlights-card.svg ({W}x{height}, "
          f"{'static' if static else 'animated'})")


if __name__ == "__main__":
    main()
