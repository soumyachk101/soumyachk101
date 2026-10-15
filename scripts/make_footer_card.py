"""Generate the self-hosted terminal footer card SVG for Soumya Chakraborty.

Clean, Human-Engineered Terminal Footer:
- Zero AI-slop: No rainbow spectrum beams, no bouncing glowing balls
- Quiet, professional terminal session closure:
  ❯ [session closed] · Kolkata, India · UTC+5:30 · open for systems & devtools collaboration
- Blinking cursor
"""

import os

BG = "#0d1117"
BORDER = "#30363d"
INK = "#c9d1d9"
DIM = "#8b949e"
ACCENT = "#2ea043"

FONT = "ui-monospace, SFMono-Regular, 'Cascadia Mono', Menlo, Consolas, monospace"
W = 860
H = 52


def main() -> None:
    static = os.environ.get("STATIC") == "1"

    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" text-rendering="geometricPrecision" shape-rendering="geometricPrecision">',
        "<style>",
        f"text{{-webkit-font-smoothing:antialiased;-moz-osx-font-smoothing:grayscale;font-family:{FONT};}}",
        ".cur{animation:blink 1.1s step-end infinite;}",
        "@keyframes blink{0%,100%{opacity:1;}50%{opacity:0;}}",
        "</style>",
        f'<rect x="0.5" y="0.5" width="{W - 1}" height="{H - 1}" rx="8" fill="{BG}" stroke="{BORDER}" stroke-width="1"/>',
    ]

    # Status pulse dot on left
    parts.append(f'<circle cx="28" cy="{H / 2}" r="3.5" fill="{ACCENT}"/>')

    # Main centered status line
    parts.append(
        f'<text x="{W / 2}" y="{H / 2 + 4.5}" font-size="12" text-anchor="middle">'
        f'<tspan fill="{ACCENT}" font-weight="600">❯ </tspan>'
        f'<tspan fill="{DIM}">session closed</tspan>'
        f'<tspan fill="{BORDER}">  ·  </tspan>'
        f'<tspan fill="{INK}">Kolkata, India · UTC+5:30</tspan>'
        f'<tspan fill="{BORDER}">  ·  </tspan>'
        f'<tspan fill="{DIM}">open for systems &amp; devtools collaboration</tspan>'
        f'</text>'
    )

    # Blinking block cursor on right
    if not static:
        parts.append(
            f'<rect class="cur" x="{W - 36}" y="{H / 2 - 7}" width="7" height="14" fill="{ACCENT}"/>'
        )
    else:
        parts.append(f'<rect x="{W - 36}" y="{H / 2 - 7}" width="7" height="14" fill="{ACCENT}"/>')

    parts.append('</svg>')

    out = "footer-card.svg"
    with open(out, "w", encoding="utf-8") as f:
        f.write("\n".join(parts))
    print(f"wrote {out} ({W}x{H}, terminal footer card)")


if __name__ == "__main__":
    main()
