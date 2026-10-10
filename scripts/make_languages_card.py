"""Generate self-hosted animated terminal languages card SVG for Soumya Chakraborty.

Shows core language distribution and systems focus in authentic terminal monospace:
  - Colored language dot
  - Language name
  - ASCII progress bar
  - Percentage
  - Systems / tooling domain note

    python scripts/make_languages_card.py            # writes languages-card.svg
    STATIC=1 python scripts/make_languages_card.py   # frozen frame, no animation
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
FS = 13.0
LH = 28.0
BAR_H = 32.0
W = 860
TITLE = "soumyachk101@github: ~/languages.txt"

# (name, color, percent, domain_description)
LANGS = [
    ("Rust", "#dea584", 36, "systems agent runtimes, tauri v2 desktop, thread pools"),
    ("TypeScript", "#3178c6", 26, "algorand x402 contracts, react, client engines"),
    ("Swift", "#f05138", 18, "ensembyte hydra agent heads, macos worktrees"),
    ("Python", "#3572A5", 12, "drishtinet attack graphs, ml pipelines, automation"),
    ("Go / C++", "#00ADD8", 8, "low-level IPC, socket protocols, system probes"),
]

BAR_LEN = 22  # characters inside [...]


def make_bar(pct: int) -> str:
    filled = round(BAR_LEN * (pct / 100.0))
    empty = BAR_LEN - filled
    return "█" * filled + "░" * empty


def main() -> None:
    static = os.environ.get("STATIC") == "1"

    rows = len(LANGS)
    height = round(BAR_H + 20 + rows * LH + 26 + 18)

    p = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{height}" viewBox="0 0 {W} {height}">',
        f'<rect width="100%" height="100%" rx="8" fill="{BG}" stroke="{BORDER}" stroke-width="1"/>',
        f'<path d="M1 9 a8 8 0 0 1 8-8 h{W - 18} a8 8 0 0 1 8 8 v{BAR_H - 9:.1f} h-{W - 2} z" fill="{BAR}"/>',
        f'<line x1="1" y1="{BAR_H}" x2="{W - 1}" y2="{BAR_H}" stroke="{BORDER}" stroke-width="1"/>',
        f'<circle cx="20" cy="{BAR_H / 2}" r="5" fill="#f85149"/>',
        f'<circle cx="38" cy="{BAR_H / 2}" r="5" fill="#d29922"/>',
        f'<circle cx="56" cy="{BAR_H / 2}" r="5" fill="{ACCENT}"/>',
        f'<text x="{W / 2}" y="{BAR_H / 2 + 4.4}" fill="{DIM}" font-family="{FONT}" font-size="11.5" text-anchor="middle">{TITLE}</text>',
        f'<g font-family="{FONT}" font-size="{FS}">',
    ]

    y = BAR_H + 28
    for i, (name, color, pct, desc) in enumerate(LANGS):
        begin = 0.2 + i * 0.18
        anim = (
            "" if static else (
                f'<animate attributeName="opacity" from="0" to="1" '
                f'begin="{begin:.2f}s" dur="0.45s" fill="freeze"/>'
            )
        )
        op = "1" if static else "0"
        bar = make_bar(pct)
        pct_str = f"{pct:>2}%"
        name_str = f"{name:<11}"

        p.append(f'<g opacity="{op}">')
        p.append(f'<circle cx="26" cy="{y - 4}" r="5" fill="{color}"/>')
        p.append(
            f'<text x="40" y="{y}">'
            f'<tspan fill="{INK}" font-weight="bold">{escape(name_str)}</tspan>'
            f'<tspan fill="{color}">[{bar}]</tspan> '
            f'<tspan fill="{ACCENT}" font-weight="bold">{pct_str}</tspan>'
            f'<tspan fill="{DIM}">  ·  {escape(desc)}</tspan>'
            f'</text>'
        )
        if anim:
            p.append(anim)
        p.append("</g>")
        y += LH

    # Summary footer line
    begin_sum = 0.2 + len(LANGS) * 0.18
    anim_sum = (
        "" if static else (
            f'<animate attributeName="opacity" from="0" to="1" '
            f'begin="{begin_sum:.2f}s" dur="0.45s" fill="freeze"/>'
        )
    )
    op_sum = "1" if static else "0"
    p.append(f'<g opacity="{op_sum}">')
    p.append(
        f'<text x="24" y="{y + 8}" fill="{DIM}" font-size="11.5">'
        f'<tspan fill="{ACCENT}">➜</tspan>  '
        f'production systems across macOS, Linux &amp; bare-metal devices · zero framework bloat'
        f'</text>'
    )
    if anim_sum:
        p.append(anim_sum)
    p.append("</g>")

    p.append("</g></svg>")

    out = "languages-card.svg"
    with open(out, "w", encoding="utf-8") as f:
        f.write("\n".join(p))
    print(f"wrote {out} ({W}x{height}, animated)")


if __name__ == "__main__":
    main()
