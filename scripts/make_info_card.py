"""Hand-author the neofetch-style 2-column info card SVG for Soumya Chakraborty.

Two-column balanced layout matching the 860px grid:
- Left: Identity, education, focus, hackathon wins
- Right: OS, languages, runtimes, storage, workflow, telemetry
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
FS = 12.5
LH = 23.0
BAR_H = 32.0
STAGGER = 0.12
FADE = 0.40

W = 860
TITLE = "soumyachk101@github: ~/whoami"

LEFT_COL = [
    ("Name", "Soumya Chakraborty"),
    ("Education", "B.Tech CSE · 3rd Year"),
    ("Seeking", "Systems & DevTools roles"),
    ("Focus", "AI agent runtimes & engines"),
    ("Winner", "FusioniX'26 Joint Winner"),
    ("Hackathons", "10+ shipped in 2026"),
    ("Web", "soumya.pro · x.com/soumyachk1"),
]

def get_live_activity() -> str:
    try:
        import urllib.request, re
        req = urllib.request.Request(
            "https://soumya-leetcode.vercel.app/github-streak.svg",
            headers={"User-Agent": "Mozilla/5.0"}
        )
        with urllib.request.urlopen(req, timeout=5) as r:
            txt = r.read().decode("utf-8")
            matches = re.findall(r'<text[^>]*>([^<]+)</text>', txt)
            if len(matches) >= 7:
                total = matches[0].strip()
                streak = matches[6].strip()
                return f"{total} commits · {streak}d streak"
    except Exception:
        pass
    return "8,009+ commits · 196d streak"


def main() -> None:
    static = os.environ.get("STATIC") == "1"
    activity = get_live_activity()

    right_col = [
        ("OS", "macOS · Linux · Windows"),
        ("Languages", "Rust · TypeScript · Swift · Python"),
        ("Engines", "Hydra · GPUI · Tauri v2 · CRDT"),
        ("Storage", "SQLite · Local-First"),
        ("Workflow", "Parallel Git Worktrees"),
        ("Activity", activity),
        ("Telemetry", "Kolkata, IN · UTC+5:30"),
    ]

    rows = max(len(LEFT_COL), len(right_col)) + 2  # header + underline + items
    height = round(BAR_H + 16 + rows * LH + 32)

    def anim(i: int) -> str:
        if static:
            return ""
        begin = 0.15 + i * STAGGER
        return (
            f'<animate attributeName="opacity" from="0" to="1" '
            f'begin="{begin:.2f}s" dur="{FADE}s" fill="freeze"/>'
            f'<animateTransform attributeName="transform" type="translate" '
            f'from="-8 0" to="0 0" begin="{begin:.2f}s" dur="{FADE}s" '
            f'fill="freeze"/>'
        )

    op = "1" if static else "0"
    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" '
        f'height="{height}" viewBox="0 0 {W} {height}">',
        "<defs>",
        '  <linearGradient id="barGrad" x1="0%" y1="0%" x2="100%" y2="0%">',
        '    <stop offset="0%" stop-color="#161b22"/>',
        '    <stop offset="100%" stop-color="#0d1117"/>',
        "  </linearGradient>",
        "</defs>",
        f'<rect width="100%" height="100%" rx="8" fill="{BG}" '
        f'stroke="{BORDER}" stroke-width="1"/>',
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
        f'<g font-family="{FONT}" font-size="{FS}" xml:space="preserve">',
    ]

    # Subtle vertical separator between left and right column
    div_top = BAR_H + 16
    div_bot = height - 36
    parts.append(
        f'<line x1="425" y1="{div_top}" x2="425" y2="{div_bot}" '
        f'stroke="#21262d" stroke-dasharray="3 3"/>'
    )

    y_start = BAR_H + 16 + LH * 0.75

    # 1. Left Column (Identity & Focus)
    y = y_start
    step = 0
    parts.append(
        f'<g opacity="{op}">'
        f'<text x="36.0" y="{y:.1f}" fill="{ACCENT}" font-weight="bold">soumyachk101@github</text>'
        f"{anim(step)}</g>"
    )
    y += LH
    step += 1
    parts.append(
        f'<g opacity="{op}">'
        f'<text x="36.0" y="{y:.1f}" fill="{DIM}">-------------------</text>'
        f"{anim(step)}</g>"
    )
    y += LH
    step += 1

    for k, v in LEFT_COL:
        pad = " " * (12 - len(k))
        parts.append(
            f'<g opacity="{op}">'
            f'<text x="36.0" y="{y:.1f}">'
            f'<tspan fill="{ACCENT}" font-weight="bold">{escape(k)}</tspan>'
            f'<tspan fill="{DIM}">:</tspan>{pad}'
            f'<tspan fill="{INK}">{escape(v)}</tspan></text>'
            f"{anim(step)}</g>"
        )
        y += LH
        step += 1

    # 2. Right Column (System Specs & Runtime)
    y = y_start
    parts.append(
        f'<g opacity="{op}">'
        f'<text x="445.0" y="{y:.1f}" fill="{ACCENT}" font-weight="bold">runtime &amp; sys specs</text>'
        f"{anim(step)}</g>"
    )
    y += LH
    step += 1
    parts.append(
        f'<g opacity="{op}">'
        f'<text x="445.0" y="{y:.1f}" fill="{DIM}">---------------------</text>'
        f"{anim(step)}</g>"
    )
    y += LH
    step += 1

    for k, v in right_col:
        pad = " " * (12 - len(k))
        parts.append(
            f'<g opacity="{op}">'
            f'<text x="445.0" y="{y:.1f}">'
            f'<tspan fill="{ACCENT}" font-weight="bold">{escape(k)}</tspan>'
            f'<tspan fill="{DIM}">:</tspan>{pad}'
            f'<tspan fill="{INK}">{escape(v)}</tspan></text>'
            f"{anim(step)}</g>"
        )
        y += LH
        step += 1

    # Bottom Terminal Color Swatches (left & right columns)
    swatch_y = height - 24
    colors = [
        "#161b22",
        "#0e4429",
        "#006d32",
        "#26a641",
        "#39d353",
        "#58a6ff",
        "#bc8cff",
        "#c9d1d9",
    ]
    swatches_left = [(col, 36 + i * 40) for i, col in enumerate(colors)]
    swatches_right = [(col, 445 + i * 40) for i, col in enumerate(colors)]
    
    left_tags = "".join(
        f'<rect x="{x}" y="{swatch_y}" width="32" height="12" rx="3" fill="{col}"/>'
        for col, x in swatches_left
    )
    right_tags = "".join(
        f'<rect x="{x}" y="{swatch_y}" width="32" height="12" rx="3" fill="{col}"/>'
        for col, x in swatches_right
    )
    parts.append(
        f'<g opacity="{op}">{left_tags}{right_tags}{anim(step)}</g>'
    )

    parts.append("</g></svg>")
    with open("info-card.svg", "w", encoding="utf-8") as f:
        f.write("\n".join(parts))
    print(f"wrote info-card.svg ({W}x{height}, {'static' if static else 'animated'})")


if __name__ == "__main__":
    main()
