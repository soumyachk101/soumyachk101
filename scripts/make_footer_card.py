"""Generate the self-hosted terminal footer card SVG for Soumya Chakraborty.

Replaces the plain text footer with a polished terminal session-closed card:
  ❯ [session closed] · Kolkata, India · UTC+5:30 · open for systems & devtools collaboration

    python scripts/make_footer_card.py            # writes footer-card.svg
    STATIC=1 python scripts/make_footer_card.py   # frozen frame
"""

import os

BG = "#0d1117"
BORDER = "#30363d"
INK = "#c9d1d9"
DIM = "#8b949e"
ACCENT = "#3fb950"

FONT = "ui-monospace, SFMono-Regular, 'Cascadia Mono', Menlo, Consolas, monospace"
W = 860
H = 46


def main() -> None:
    static = os.environ.get("STATIC") == "1"

    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">',
        f'<rect x="0.5" y="0.5" width="{W - 1}" height="{H - 1}" rx="8" fill="{BG}" stroke="{BORDER}" stroke-width="1"/>',
    ]

    # Status pulse dot on left
    if not static:
        parts.append(
            f'<circle cx="28" cy="{H / 2}" r="4" fill="{ACCENT}">'
            f'<animate attributeName="opacity" values="1;0.25;1" dur="2s" repeatCount="indefinite"/>'
            f'</circle>'
        )
    else:
        parts.append(f'<circle cx="28" cy="{H / 2}" r="4" fill="{ACCENT}"/>')

    # Main centered status line
    y_text = H / 2 + 4.5
    parts.append(
        f'<text x="{W / 2}" y="{y_text}" font-family="{FONT}" font-size="12.5" text-anchor="middle">'
        f'<tspan fill="{ACCENT}" font-weight="bold">❯ </tspan>'
        f'<tspan fill="{DIM}">session closed</tspan>'
        f'<tspan fill="{BORDER}">  ·  </tspan>'
        f'<tspan fill="{INK}">Kolkata, India · UTC+5:30</tspan>'
        f'<tspan fill="{BORDER}">  ·  </tspan>'
        f'<tspan fill="{ACCENT}">open for systems &amp; devtools collaboration</tspan>'
        f'</text>'
    )

    # Blinking block cursor on right
    if not static:
        parts.append(
            f'<rect x="{W - 36}" y="{H / 2 - 8}" width="8" height="16" fill="{ACCENT}">'
            f'<animate attributeName="opacity" values="1;0;1" dur="1.2s" repeatCount="indefinite"/>'
            f'</rect>'
        )
    else:
        parts.append(f'<rect x="{W - 36}" y="{H / 2 - 8}" width="8" height="16" fill="{ACCENT}"/>')

    parts.append('</svg>')

    out = "footer-card.svg"
    with open(out, "w", encoding="utf-8") as f:
        f.write("\n".join(parts))
    print(f"wrote {out} ({W}x{H}, terminal footer card)")


if __name__ == "__main__":
    main()
