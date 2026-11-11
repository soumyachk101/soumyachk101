"""Hand-author the neofetch-style 2-column whoami card SVG, re-themed to the
cinematic 'Noir · Gold & Crimson' system. Data logic (live activity read + STATIC
mode) is unchanged; only the palette / chrome / motion were re-styled."""

import os
from html import escape

from theme import PAL, P, MONO, SANS

FONT = MONO
FS = 12.5
LH = 23.0
BAR_H = 32.0
STAGGER = 0.12
FADE = 0.40

W = 860
TITLE = "soumyachk101@github:~/whoami"

LEFT_COL = [
    ("Name", "Soumya Chakraborty"),
    ("Education", "B.Tech CSE · 3rd Year"),
    ("Seeking", "Systems & DevTools roles"),
    ("Focus", "AI agent runtimes & engines"),
    ("Winner", "FusioniX'26 Joint Winner"),
    ("Hackathons", "15+ shipped · Hacktoberfest '26"),
    ("Web", "soumya.pro · x.com/techie_newws"),
]


def get_live_activity() -> str:
    try:
        script_dir = os.path.dirname(os.path.abspath(__file__))
        root_dir = os.path.dirname(script_dir)
        contrib_path = os.path.join(root_dir, "data", "contributions.json")
        if os.path.exists(contrib_path):
            import json
            with open(contrib_path, "r", encoding="utf-8") as f:
                cdata = json.load(f)
            total = cdata.get("total")
            streak = cdata.get("current_streak", cdata.get("longest_streak"))
            if total and streak:
                return f"{total:,} commits · {streak}d streak"
    except Exception:
        pass
    return "9,626+ commits · 208d streak"


def main() -> None:
    static = os.environ.get("STATIC") == "1"
    activity = get_live_activity()

    right_col = [
        ("OS", "MacOS · Linux · Windows"),
        ("Languages", "Rust · TypeScript · Swift · Python"),
        ("Engines", "Hydra · GPUI · Tauri v2 · CRDT"),
        ("Storage", "SQLite · Local-First"),
        ("Workflow", "Parallel Git Worktrees"),
        ("Activity", activity),
        ("Telemetry", "Kolkata, IN · UTC+5:30"),
    ]

    rows = max(len(LEFT_COL), len(right_col)) + 2
    height = round(BAR_H + 16 + rows * LH + 32)

    ACCENT = P("gold")

    def anim(i: int) -> str:
        if static:
            return ""
        begin = 0.15 + i * STAGGER
        return (
            f'<animate attributeName="opacity" from="0" to="1" '
            f'begin="{begin:.2f}s" dur="{FADE}s" fill="freeze"/>'
            f'<animateTransform attributeName="transform" type="translate" '
            f'from="-8 0" to="0 0" begin="{begin:.2f}s" dur="{FADE}s" fill="freeze"/>'
        )

    op = "1" if static else "0"
    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" '
        f'height="{height}" viewBox="0 0 {W} {height}" text-rendering="geometricPrecision" shape-rendering="geometricPrecision">',
        "<style>text{-webkit-font-smoothing:antialiased;-moz-osx-font-smoothing:grayscale;}</style>",
        "<defs>",
        '  <linearGradient id="barGrad" x1="0" y1="0" x2="0" y2="1">',
        f'    <stop offset="0" stop-color="{P("surface")}"/>',
        f'    <stop offset="1" stop-color="{P("base")}"/>',
        "  </linearGradient>",
        # cinematic grade: crimson -> gold -> steel (no green)
        '  <linearGradient id="spectrumBar" x1="0" y1="0" x2="1" y2="0">',
        f'    <stop offset="0%" stop-color="{P("base")}"/>',
        f'    <stop offset="12%" stop-color="{P("crim")}"/>',
        f'    <stop offset="38%" stop-color="{P("gold")}"/>',
        f'    <stop offset="62%" stop-color="{P("gold_hi")}"/>',
        f'    <stop offset="85%" stop-color="{P("steel")}"/>',
        f'    <stop offset="100%" stop-color="{P("steel_hi")}"/>',
        "  </linearGradient>",
        '  <linearGradient id="cuteBeam" x1="0" y1="0" x2="1" y2="0">',
        f'    <stop offset="0%" stop-color="{P("gold_hi")}" stop-opacity="0"/>',
        f'    <stop offset="50%" stop-color="{P("gold_hi")}" stop-opacity="0.5"/>',
        f'    <stop offset="100%" stop-color="{P("gold_hi")}" stop-opacity="0"/>',
        '  </linearGradient>',
        '  <linearGradient id="gKeyline" x1="0" y1="0" x2="0" y2="1">',
        f'    <stop offset="0" stop-color="{P("crim")}"/>',
        f'    <stop offset="0.55" stop-color="{P("gold")}"/>',
        f'    <stop offset="1" stop-color="{P("gold_lo")}"/>',
        "  </linearGradient>",
        "</defs>",
        f'<rect width="100%" height="100%" rx="10" fill="{P("base")}" stroke="{P("border")}" stroke-width="1"/>',
        f'<rect x="0.5" y="8.5" width="3.5" height="{height - 17}" fill="url(#gKeyline)"/>',
        f'<path d="M1 11 a10 10 0 0 1 10-10 h{W - 22} a10 10 0 0 1 10 10 v{BAR_H - 11} h-{W - 2} z" fill="url(#barGrad)"/>',
        f'<line x1="1" y1="{BAR_H}" x2="{W - 1}" y2="{BAR_H}" stroke="{P("hair")}" stroke-width="1"/>',
        # film-slate trio (gold / crimson / steel) — NOT traffic lights
        f'<circle cx="20" cy="{BAR_H / 2}" r="4" fill="{P("gold")}"/>',
        f'<circle cx="36" cy="{BAR_H / 2}" r="4" fill="{P("crim")}"/>',
        f'<circle cx="52" cy="{BAR_H / 2}" r="4" fill="{P("steel")}"/>',
        f'<text x="70" y="{BAR_H / 2 + 3.5}" fill="{P("faint")}" font-family="{FONT}" font-size="10.5">~/whoami</text>',
        f'<text x="{W / 2}" y="{BAR_H / 2 + 4.5}" fill="{P("dim")}" font-family="{FONT}" font-size="12" text-anchor="middle">{escape(TITLE)}</text>',
        (
            f'<circle cx="735" cy="{BAR_H / 2}" r="3.5" fill="{ACCENT}">'
            f'<animate attributeName="opacity" values="1;0.4;1" dur="2.6s" repeatCount="indefinite"/></circle>'
        ) if not static else (
            f'<circle cx="735" cy="{BAR_H / 2}" r="3.5" fill="{ACCENT}"/>'
        ),
        f'<text x="746" y="{BAR_H / 2 + 4.2}" fill="{P("dim")}" font-family="{FONT}" font-size="11">status: <tspan fill="{P("text")}">active</tspan></text>',
        f'<g font-family="{FONT}" font-size="{FS}" xml:space="preserve">',
    ]

    div_top = BAR_H + 16
    div_bot = height - 36
    parts.append(
        f'<line x1="425" y1="{div_top}" x2="425" y2="{div_bot}" stroke="{P("border")}" stroke-dasharray="3 3"/>'
    )

    y_start = BAR_H + 16 + LH * 0.75
    y = y_start
    step = 0
    parts.append(
        f'<g opacity="{op}"><text x="36.0" y="{y:.1f}" fill="{ACCENT}" font-weight="bold">soumyachk101@github</text>{anim(step)}</g>'
    )
    y += LH
    step += 1
    parts.append(
        f'<g opacity="{op}"><text x="36.0" y="{y:.1f}" fill="{P("faint")}">-------------------</text>{anim(step)}</g>'
    )
    y += LH
    step += 1
    for k, v in LEFT_COL:
        pad = " " * (12 - len(k))
        parts.append(
            f'<g opacity="{op}"><text x="36.0" y="{y:.1f}">'
            f'<tspan fill="{ACCENT}" font-weight="bold">{escape(k)}</tspan>'
            f'<tspan fill="{P("dim")}">:</tspan>{pad}'
            f'<tspan fill="{P("text")}">{escape(v)}</tspan></text>{anim(step)}</g>'
        )
        y += LH
        step += 1

    y = y_start
    parts.append(
        f'<g opacity="{op}"><text x="445.0" y="{y:.1f}" fill="{ACCENT}" font-weight="bold">runtime &amp; sys specs</text>{anim(step)}</g>'
    )
    y += LH
    step += 1
    parts.append(
        f'<g opacity="{op}"><text x="445.0" y="{y:.1f}" fill="{P("faint")}">---------------------</text>{anim(step)}</g>'
    )
    y += LH
    step += 1
    for k, v in right_col:
        pad = " " * (12 - len(k))
        parts.append(
            f'<g opacity="{op}"><text x="445.0" y="{y:.1f}">'
            f'<tspan fill="{ACCENT}" font-weight="bold">{escape(k)}</tspan>'
            f'<tspan fill="{P("dim")}">:</tspan>{pad}'
            f'<tspan fill="{P("text")}">{escape(v)}</tspan></text>{anim(step)}</g>'
        )
        y += LH
        step += 1

    bar_x, bar_w = 36, W - 36 * 2
    bar_y, bar_h = height - 23, 10
    orb_anim = "" if static else (
        f'<circle cy="{bar_y + bar_h / 2:.1f}" r="4" fill="{P("gold")}">'
        f'<animate attributeName="cx" values="{bar_x + 8};{bar_x + bar_w - 8};{bar_x + 8}" dur="4s" repeatCount="indefinite" calcMode="spline" keySplines="0.45 0 0.55 1;0.45 0 0.55 1"/>'
        f'<animate attributeName="fill" values="{P("crim_hi")};{P("gold_hi")};{P("steel_hi")};{P("crim_hi")}" dur="4s" repeatCount="indefinite"/>'
        f'<animate attributeName="r" values="3.5;5;3.5" dur="1.2s" repeatCount="indefinite"/></circle>'
    )
    beam_layer = f'<rect x="{bar_x}" y="{bar_y}" width="{bar_w}" height="{bar_h}" rx="5" fill="url(#cuteBeam)"/>' if not static else ""
    parts.append(
        f'<g opacity="{op}">'
        f'<rect x="{bar_x}" y="{bar_y}" width="{bar_w}" height="{bar_h}" rx="5" fill="{P("track")}" stroke="{P("border")}" stroke-width="0.8"/>'
        f'<rect x="{bar_x}" y="{bar_y}" width="{bar_w}" height="{bar_h}" rx="5" fill="url(#spectrumBar)" opacity="0.9"/>'
        f'{beam_layer}{orb_anim}{anim(step)}</g>'
    )
    parts.append("</g></svg>")

    out_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    with open(os.path.join(out_dir, "info-card.svg"), "w", encoding="utf-8") as f:
        f.write("\n".join(parts))
    print(f"wrote info-card.svg ({W}x{height}, {'static' if static else 'animated'})")


if __name__ == "__main__":
    main()
