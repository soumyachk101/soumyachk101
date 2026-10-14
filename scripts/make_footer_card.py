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
H = 64


def main() -> None:
    static = os.environ.get("STATIC") == "1"

    bar_x = 28
    bar_w = W - bar_x * 2  # 804px
    bar_y = 48
    bar_h = 7
    orb_cy = bar_y + bar_h / 2

    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" text-rendering="geometricPrecision" shape-rendering="geometricPrecision">',
        "<style>text{-webkit-font-smoothing:antialiased;-moz-osx-font-smoothing:grayscale;text-rendering:geometricPrecision;}</style>",
        "<defs>",
        '  <linearGradient id="footerSpectrum" x1="0%" y1="0%" x2="100%" y2="0%">',
        '    <stop offset="0%" stop-color="#161b22"/>',
        '    <stop offset="10%" stop-color="#0e4429"/>',
        '    <stop offset="25%" stop-color="#238636"/>',
        '    <stop offset="40%" stop-color="#39d353"/>',
        '    <stop offset="55%" stop-color="#56d4dd"/>',
        '    <stop offset="70%" stop-color="#58a6ff"/>',
        '    <stop offset="85%" stop-color="#bc8cff"/>',
        '    <stop offset="100%" stop-color="#f0f6fc"/>',
        '  </linearGradient>',
        '  <linearGradient id="footerBeam" x1="0%" y1="0%" x2="100%" y2="0%">',
        '    <stop offset="0%" stop-color="#ffffff" stop-opacity="0"/>',
        '    <stop offset="50%" stop-color="#ffffff" stop-opacity="0.8"/>',
        '    <stop offset="100%" stop-color="#ffffff" stop-opacity="0"/>',
        '    <animate attributeName="x1" from="-40%" to="100%" dur="2.4s" repeatCount="indefinite"/>',
        '    <animate attributeName="x2" from="0%" to="140%" dur="2.4s" repeatCount="indefinite"/>',
        '  </linearGradient>',
        "</defs>",
        f'<rect x="0.5" y="0.5" width="{W - 1}" height="{H - 1}" rx="8" fill="{BG}" stroke="{BORDER}" stroke-width="1.2"/>',
    ]

    # Status pulse dot on left
    if not static:
        parts.append(
            f'<circle cx="28" cy="25" r="4" fill="{ACCENT}">'
            f'<animate attributeName="opacity" values="1;0.25;1" dur="2s" repeatCount="indefinite"/>'
            f'</circle>'
        )
    else:
        parts.append(f'<circle cx="28" cy="25" r="4" fill="{ACCENT}"/>')

    # Main centered status line
    y_text = 29.5
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
            f'<rect x="{W - 36}" y="17" width="8" height="16" fill="{ACCENT}">'
            f'<animate attributeName="opacity" values="1;0;1" dur="1.2s" repeatCount="indefinite"/>'
            f'</rect>'
        )
    else:
        parts.append(f'<rect x="{W - 36}" y="17" width="8" height="16" fill="{ACCENT}"/>')

    # Cute spectrum bar + traveling glowing orb
    orb_anim = "" if static else (
        f'<circle cy="{orb_cy:.1f}" r="3.5" fill="#39d353">'
        f'<animate attributeName="cx" values="{bar_x + 6};{bar_x + bar_w - 6};{bar_x + 6}" dur="3.8s" repeatCount="indefinite" calcMode="spline" keySplines="0.45 0 0.55 1; 0.45 0 0.55 1"/>'
        f'<animate attributeName="fill" values="#39d353;#56d4dd;#58a6ff;#bc8cff;#39d353" dur="3.8s" repeatCount="indefinite"/>'
        f'<animate attributeName="r" values="3;4.2;3" dur="1.2s" repeatCount="indefinite"/>'
        f'</circle>'
    )
    beam_layer = f'<rect x="{bar_x}" y="{bar_y}" width="{bar_w}" height="{bar_h}" rx="3.5" fill="url(#footerBeam)"/>' if not static else ""

    parts.append(
        f'<g>'
        f'<rect x="{bar_x}" y="{bar_y}" width="{bar_w}" height="{bar_h}" rx="3.5" fill="#161b22" stroke="#30363d" stroke-width="0.7"/>'
        f'<rect x="{bar_x}" y="{bar_y}" width="{bar_w}" height="{bar_h}" rx="3.5" fill="url(#footerSpectrum)" opacity="0.9"/>'
        f'{beam_layer}'
        f'{orb_anim}'
        f'</g>'
    )

    parts.append('</svg>')

    out = "footer-card.svg"
    with open(out, "w", encoding="utf-8") as f:
        f.write("\n".join(parts))
    print(f"wrote {out} ({W}x{H}, terminal footer card)")


if __name__ == "__main__":
    main()
