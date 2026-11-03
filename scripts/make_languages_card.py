"""Generate self-hosted animated 'Noir · Gold & Crimson' languages card.
Core language distribution + systems focus, in authentic terminal monospace:
  colored (muted) language dot · name · ASCII bar · % · domain note.

    python scripts/make_languages_card.py            # writes languages-card.svg
    STATIC=1 python scripts/make_languages_card.py   # frozen frame
"""

import os
from html import escape

from theme import P, MONO

FONT = MONO
FS = 13.0
LH = 28.0
BAR_H = 34.0
W = 860
TITLE = "soumyachk101@github:~/languages.txt"

# (name, muted-noir dot, percent, domain_description)
LANGS = [
    ("Rust",       "#c9705a", 36, "systems agent runtimes, tauri v2 desktop, thread pools"),
    ("TypeScript", "#6b7f9c", 26, "algorand x402 contracts, react, client engines"),
    ("Swift",      "#b03a45", 18, "ensembyte hydra agent heads, macos worktrees"),
    ("Python",     "#9a8a5e", 12, "drishtinet attack graphs, ml pipelines, automation"),
    ("Go / C++",   "#5e7d8a",  8, "low-level IPC, socket protocols, system probes"),
]

BAR_LEN = 22  # characters inside [...]


def make_bar(pct: int) -> str:
    filled = round(BAR_LEN * (pct / 100.0))
    empty = BAR_LEN - filled
    return "█" * filled + "░" * empty


def main() -> None:
    static = os.environ.get("STATIC") == "1"
    rows = len(LANGS)
    height = round(BAR_H + 20 + rows * LH + 26 + 34)

    p = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{height}" viewBox="0 0 {W} {height}" text-rendering="geometricPrecision" shape-rendering="geometricPrecision">',
        "<style>text{-webkit-font-smoothing:antialiased;-moz-osx-font-smoothing:grayscale;}</style>",
        "<defs>",
        '  <linearGradient id="langSpectrum" x1="0" y1="0" x2="1" y2="0">',
        f'    <stop offset="0%" stop-color="{P("base")}"/>',
        '    <stop offset="15%" stop-color="#c9705a"/>',
        '    <stop offset="35%" stop-color="#6b7f9c"/>',
        '    <stop offset="55%" stop-color="#b03a45"/>',
        '    <stop offset="75%" stop-color="#d8a63f"/>',
        '    <stop offset="90%" stop-color="#5e7d8a"/>',
        f'    <stop offset="100%" stop-color="{P("crim")}"/>',
        "  </linearGradient>",
        '  <linearGradient id="langBeam" x1="0" y1="0" x2="1" y2="0">',
        f'    <stop offset="0%" stop-color="{P("gold_hi")}" stop-opacity="0"/>',
        f'    <stop offset="50%" stop-color="{P("gold_hi")}" stop-opacity="0.5"/>',
        f'    <stop offset="100%" stop-color="{P("gold_hi")}" stop-opacity="0"/>',
        "  </linearGradient>",
        '  <linearGradient id="gBase" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#0e0e14"/><stop offset="1" stop-color="#0a0a0f"/></linearGradient>',
        '  <linearGradient id="gKeyline" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#b03a45"/><stop offset="0.55" stop-color="#d8a63f"/><stop offset="1" stop-color="#7c5f24"/></linearGradient>',
        "</defs>",
        f'<rect x="0.5" y="0.5" width="{W - 1}" height="{height - 1}" rx="10" fill="url(#gBase)" stroke="{P("border")}" stroke-width="1"/>',
        f'<rect x="0.5" y="8.5" width="3.5" height="{height - 17}" fill="url(#gKeyline)"/>',
        f'<rect x="0.5" y="0.5" width="{W - 1}" height="{BAR_H - 0.5}" fill="{P("surface")}"/>',
        f'<line x1="1" y1="{BAR_H}" x2="{W - 1}" y2="{BAR_H}" stroke="{P("hair")}" stroke-width="1"/>',
        f'<circle cx="20" cy="{BAR_H / 2}" r="4" fill="{P("gold")}"/>',
        f'<circle cx="36" cy="{BAR_H / 2}" r="4" fill="{P("crim")}"/>',
        f'<circle cx="52" cy="{BAR_H / 2}" r="4" fill="{P("steel")}"/>',
        f'<text x="{W / 2}" y="{BAR_H / 2 + 4.4}" fill="{P("dim")}" font-family="{FONT}" font-size="11.5" text-anchor="middle">{TITLE}</text>',
        f'<g font-family="{FONT}" font-size="{FS}">',
    ]

    y = BAR_H + 28
    for i, (name, color, pct, desc) in enumerate(LANGS):
        begin = 0.2 + i * 0.18
        anim = "" if static else f'<animate attributeName="opacity" from="0" to="1" begin="{begin:.2f}s" dur="0.45s" fill="freeze"/>'
        op = "1" if static else "0"
        bar = make_bar(pct)
        pct_str = f"{pct:>2}%"
        name_str = f"{name:<11}"
        p.append(f'<g opacity="{op}">')
        p.append(f'<circle cx="26" cy="{y - 4}" r="5" fill="{color}"/>')
        p.append(
            f'<text x="40" y="{y}">'
            f'<tspan fill="{P("text")}" font-weight="bold">{escape(name_str)}</tspan>'
            f'<tspan fill="{color}">[{bar}]</tspan> '
            f'<tspan fill="{P("gold_hi")}" font-weight="bold">{pct_str}</tspan>'
            f'<tspan fill="{P("dim")}">  ·  {escape(desc)}</tspan>'
            f'</text>'
        )
        if anim:
            p.append(anim)
        p.append("</g>")
        y += LH

    # summary footer line
    begin_sum = 0.2 + len(LANGS) * 0.18
    anim_sum = "" if static else f'<animate attributeName="opacity" from="0" to="1" begin="{begin_sum:.2f}s" dur="0.45s" fill="freeze"/>'
    op_sum = "1" if static else "0"
    p.append(f'<g opacity="{op_sum}">')
    p.append(
        f'<text x="24" y="{y + 8}" fill="{P("dim")}" font-size="11.5">'
        f'<tspan fill="{P("gold")}">➜</tspan>  '
        f'production systems across macOS, Linux &amp; bare-metal devices · zero framework bloat'
        f'</text>'
    )
    if anim_sum:
        p.append(anim_sum)
    p.append("</g>")

    # bottom spectrum bar + cycling orb (crimson->gold->steel, no green)
    bar_x, bar_w = 24, W - 24 * 2
    bar_y, bar_h = y + 22, 8
    orb_cy = bar_y + bar_h / 2
    lang_orb_anim = "" if static else (
        f'<circle cy="{orb_cy:.1f}" r="3.5" fill="#c9705a">'
        f'<animate attributeName="cx" values="{bar_x + 6};{bar_x + bar_w - 6};{bar_x + 6}" dur="4s" repeatCount="indefinite" calcMode="spline" keySplines="0.45 0 0.55 1;0.45 0 0.55 1"/>'
        f'<animate attributeName="fill" values="#c9705a;#6b7f9c;#b03a45;#d8a63f;#5e7d8a;#c9705a" dur="4s" repeatCount="indefinite"/>'
        f'<animate attributeName="r" values="3;4.2;3" dur="1.2s" repeatCount="indefinite"/></circle>'
    )
    lang_beam_layer = f'<rect x="{bar_x}" y="{bar_y}" width="{bar_w}" height="{bar_h}" rx="4" fill="url(#langBeam)"/>' if not static else ""
    p.append(f'<g opacity="{op_sum}">')
    p.append(f'<rect x="{bar_x}" y="{bar_y}" width="{bar_w}" height="{bar_h}" rx="4" fill="{P("track")}" stroke="{P("border")}" stroke-width="0.8"/>')
    p.append(f'<rect x="{bar_x}" y="{bar_y}" width="{bar_w}" height="{bar_h}" rx="4" fill="url(#langSpectrum)" opacity="0.9"/>')
    p.append(lang_beam_layer)
    p.append(lang_orb_anim)
    if anim_sum:
        p.append(anim_sum)
    p.append("</g>")

    p.append("</g></svg>")
    with open("languages-card.svg", "w", encoding="utf-8") as f:
        f.write("\n".join(p))
    print(f"wrote languages-card.svg ({W}x{height}, animated)")


if __name__ == "__main__":
    main()
