"""Hand-author the neofetch-style info card SVG for Soumya Chakraborty.

Run once, locally (rerun whenever the details change):

    python scripts/make_info_card.py            # writes info-card.svg
    STATIC=1 python scripts/make_info_card.py   # frozen frame, no animation

Each line fades and slides in on a short stagger, plays once, freezes.
Keys are green, values light gray; palette matches the other SVGs.
"""

import os
from html import escape

# Palette (shared across all profile SVGs)
BG = "#0d1117"
BAR = "#161b22"
BORDER = "#30363d"
INK = "#c9d1d9"
DIM = "#8b949e"
ACCENT = "#3fb950"

FONT = "ui-monospace, SFMono-Regular, 'Cascadia Mono', Menlo, Consolas, monospace"
FS = 13.0
LH = 22.0
CW = FS * 0.602
PAD_X = 22.0
BAR_H = 30.0
STAGGER = 0.16
FADE = 0.45

TITLE = "soumyachk101@github: ~/whoami"
HEADER = "soumyachk101@github"

# (key, value) rows; None = blank spacer line
LINES = [
    ("Name", "Soumya Chakraborty"),
    ("Education", "B.Tech CSE · 3rd Year"),
    ("Seeking", "Systems & DevTools roles · Open-source builds"),
    (None, None),
    ("Focus", "AI coding agent runtimes & multi-agent systems"),
    ("Winner", "FusioniX'26 Joint Winner · Algorand x402 track"),
    ("Hackathons", "7 shipped in 2026 (FusioniX, Innofusion, etc.)"),
    (None, None),
    ("Systems", "SwarmAI (parallel agents) · Orbit · Ensembyte"),
    ("Languages", "Rust · TypeScript · Swift · Python · Go · C++"),
    ("Stack", "Tauri v2 · React · Next.js · FastAPI · GPUI · SQLite"),
    (None, None),
    ("Web", "soumya.pro · x.com/soumyachk1"),
]

KEY_COL = max(len(k) for k, _ in LINES if k) + 2  # chars, incl. separator


def main() -> None:
    static = os.environ.get("STATIC") == "1"

    body_rows = 2 + len(LINES) + 2  # header + underline + lines + gap + palette
    longest = max(
        [len(TITLE)] + [KEY_COL + len(v) for k, v in LINES if k]
    )
    width = round(longest * CW + 2 * PAD_X)
    height = round(BAR_H + 14 + body_rows * LH + 10)

    def anim(i: int) -> str:
        if static:
            return ""
        begin = 0.2 + i * STAGGER
        return (
            f'<animate attributeName="opacity" from="0" to="1" '
            f'begin="{begin:.2f}s" dur="{FADE}s" fill="freeze"/>'
            f'<animateTransform attributeName="transform" type="translate" '
            f'from="-8 0" to="0 0" begin="{begin:.2f}s" dur="{FADE}s" '
            f'fill="freeze"/>'
        )

    op = "1" if static else "0"
    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" '
        f'height="{height}" viewBox="0 0 {width} {height}">',
        f'<rect width="100%" height="100%" rx="8" fill="{BG}" '
        f'stroke="{BORDER}" stroke-width="1"/>',
        # terminal title bar
        f'<path d="M1 9 a8 8 0 0 1 8-8 h{width - 18} a8 8 0 0 1 8 8 '
        f'v{BAR_H - 9} h-{width - 2} z" fill="{BAR}"/>',
        f'<line x1="1" y1="{BAR_H}" x2="{width - 1}" y2="{BAR_H}" '
        f'stroke="{BORDER}" stroke-width="1"/>',
        f'<circle cx="20" cy="{BAR_H / 2}" r="5" fill="#f85149"/>',
        f'<circle cx="38" cy="{BAR_H / 2}" r="5" fill="#d29922"/>',
        f'<circle cx="56" cy="{BAR_H / 2}" r="5" fill="{ACCENT}"/>',
        f'<text x="{width / 2}" y="{BAR_H / 2 + FS * 0.36}" fill="{DIM}" '
        f'font-family="{FONT}" font-size="{FS - 1}" '
        f'text-anchor="middle">{escape(TITLE)}</text>',
        f'<g font-family="{FONT}" font-size="{FS}" xml:space="preserve">',
    ]

    y = BAR_H + 14 + LH * 0.75
    i = 0

    # header + underline
    parts.append(
        f'<g opacity="{op}"><text x="{PAD_X}" y="{y:.1f}" fill="{ACCENT}" '
        f'font-weight="bold">{escape(HEADER)}</text>{anim(i)}</g>'
    )
    y += LH
    i += 1
    parts.append(
        f'<g opacity="{op}"><text x="{PAD_X}" y="{y:.1f}" fill="{DIM}">'
        f'{"-" * len(HEADER)}</text>{anim(i)}</g>'
    )
    y += LH
    i += 1

    for key, val in LINES:
        if key is None:
            y += LH * 0.6
            continue
        pad = "&#160;" * (KEY_COL - len(key) - 1)
        parts.append(
            f'<g opacity="{op}">'
            f'<text x="{PAD_X}" y="{y:.1f}">'
            f'<tspan fill="{ACCENT}" font-weight="bold">{escape(key)}</tspan>'
            f'<tspan fill="{DIM}">:</tspan>{pad}'
            f'<tspan fill="{INK}">{escape(val)}</tspan>'
            f"</text>{anim(i)}</g>"
        )
        y += LH
        i += 1

    # neofetch-style palette swatches
    y += LH * 0.35
    sw, gap = 34.0, 6.0
    swatches = ["#161b22", "#0e4429", "#006d32", "#26a641", "#39d353", INK]
    row = [f'<g opacity="{op}">']
    for j, c in enumerate(swatches):
        row.append(
            f'<rect x="{PAD_X + j * (sw + gap):.1f}" y="{y - 11:.1f}" '
            f'width="{sw}" height="14" rx="3" fill="{c}"/>'
        )
    row.append(f"{anim(i)}</g>")
    parts.append("".join(row))

    parts.append("</g></svg>")

    with open("info-card.svg", "w", encoding="utf-8") as f:
        f.write("\n".join(parts))
    print(f"wrote info-card.svg ({width}x{height}, "
          f"{'static' if static else 'animated'})")


if __name__ == "__main__":
    main()
