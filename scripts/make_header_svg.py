"""Hand-author the typed-name header SVG for Soumya Chakraborty.

One terminal line that types itself out character by character (discrete
SMIL steps, like a real keystroke buffer), with a green glow on the name
and a block cursor that blinks three times and then stays lit. Plays
once, then freezes. Rerun only if the text changes:

    python scripts/make_header_svg.py            # writes name-header.svg
    STATIC=1 python scripts/make_header_svg.py   # frozen frame
"""

import os
from html import escape

BG = "#0d1117"
BORDER = "#30363d"
INK = "#c9d1d9"
DIM = "#8b949e"
ACCENT = "#3fb950"

FONT = "ui-monospace, SFMono-Regular, 'Cascadia Mono', Menlo, Consolas, monospace"
FS = 26.0
CW = FS * 0.602
W = 860
H = 84

PROMPT = "❯ "                     # green chevron
PLAIN = "hi, i'm "                # typed in ink
NAME = "Soumya Chakraborty"       # typed in glowing green
TYPE_SPEED = 0.075                # seconds per keystroke
BEGIN = 0.4


def main() -> None:
    static = os.environ.get("STATIC") == "1"

    typed = PLAIN + NAME
    n = len(typed)
    prompt_w = len(PROMPT) * CW
    text_w = n * CW
    total_w = prompt_w + text_w
    x0 = (W - total_w) / 2
    tx = x0 + prompt_w
    y = H / 2 + FS * 0.34
    dur = n * TYPE_SPEED

    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" '
        f'viewBox="0 0 {W} {H}">',
        "<defs>",
        '<filter id="glow" x="-30%" y="-30%" width="160%" height="160%">'
        '<feGaussianBlur stdDeviation="2.6" result="b"/>'
        '<feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/>'
        "</feMerge></filter>",
    ]

    if not static:
        widths = ";".join(f"{i * CW:.1f}" for i in range(n + 1))
        parts.append(
            f'<clipPath id="type"><rect x="{tx:.1f}" y="0" width="0" '
            f'height="{H}"><animate attributeName="width" '
            f'calcMode="discrete" values="{widths}" begin="{BEGIN}s" '
            f'dur="{dur:.2f}s" fill="freeze"/></rect></clipPath>'
        )
    parts.append("</defs>")

    parts.append(
        f'<rect width="100%" height="100%" rx="8" fill="{BG}" '
        f'stroke="{BORDER}" stroke-width="1"/>'
    )

    parts.append(
        f'<g font-family="{FONT}" font-size="{FS}" font-weight="bold">'
    )
    parts.append(
        f'<text x="{x0:.1f}" y="{y:.1f}" fill="{ACCENT}">{PROMPT}</text>'
    )
    clip = "" if static else ' clip-path="url(#type)"'
    parts.append(
        f'<g{clip}><text x="{tx:.1f}" y="{y:.1f}" '
        f'textLength="{text_w:.1f}" lengthAdjust="spacing">'
        f'<tspan fill="{INK}">{escape(PLAIN)}</tspan>'
        f'<tspan fill="{ACCENT}" filter="url(#glow)">{escape(NAME)}</tspan>'
        f"</text></g>"
    )
    parts.append("</g>")

    # Block cursor rides the keystrokes, blinks, then stays lit.
    cy = H / 2 - FS * 0.48
    if static:
        parts.append(
            f'<rect x="{tx + text_w + 3:.1f}" y="{cy:.1f}" width="{CW:.1f}" '
            f'height="{FS:.1f}" fill="{ACCENT}"/>'
        )
    else:
        xs = ";".join(f"{tx + i * CW + 3:.1f}" for i in range(n + 1))
        done = BEGIN + dur
        parts.append(
            f'<rect x="{tx + 3:.1f}" y="{cy:.1f}" width="{CW:.1f}" '
            f'height="{FS:.1f}" fill="{ACCENT}">'
            f'<animate attributeName="x" calcMode="discrete" values="{xs}" '
            f'begin="{BEGIN}s" dur="{dur:.2f}s" fill="freeze"/>'
            f'<animate attributeName="opacity" values="1;0;1;0;1;0;1" '
            f'begin="{done:.2f}s" dur="2.1s" fill="freeze"/>'
            f"</rect>"
        )

    parts.append("</svg>")
    with open("name-header.svg", "w", encoding="utf-8") as f:
        f.write("\n".join(parts))
    print(f"wrote name-header.svg ({W}x{H}, "
          f"{'static' if static else 'animated'})")


if __name__ == "__main__":
    main()
