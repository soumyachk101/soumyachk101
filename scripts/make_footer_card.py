"""Generate the cinematic footer card SVG — 'Noir · Gold & Crimson'.
A quiet 'fin' bar: a crimson pulse dot, "session closed", the sign-off, and a
slow gold block cursor. Muted, filmic, no neon.
"""

import os

from theme import P, MONO

W = 860
H = 52


def main() -> None:
    static = os.environ.get("STATIC") == "1"
    ACCENT = P("gold")

    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" text-rendering="geometricPrecision" shape-rendering="geometricPrecision">',
        "<style>",
        f"text{{-webkit-font-smoothing:antialiased;-moz-osx-font-smoothing:grayscale;font-family:{MONO};}}",
        ".cur{animation:blink 1.1s step-end infinite;}",
        "@keyframes blink{0%,100%{opacity:1;}50%{opacity:0;}}",
        "</style>",
        f'<rect x="0.5" y="0.5" width="{W - 1}" height="{H - 1}" rx="10" fill="{P("base")}" stroke="{P("border")}" stroke-width="1"/>',
        f'<rect x="0.5" y="10.5" width="3.5" height="{H - 21}" fill="{P("crim")}"/>',
    ]

    parts.append(
        f'<circle cx="30" cy="{H / 2}" r="3.5" fill="{P("crim")}">'
        f'<animate attributeName="opacity" values="0.55;1;0.55" keyTimes="0;0.5;1" dur="2.6s" '
        f'repeatCount="indefinite" calcMode="spline" keySplines="0.45 0 0.55 1;0.45 0 0.55 1"/></circle>'
    )

    parts.append(
        f'<text x="{W / 2}" y="{H / 2 + 4.5}" font-size="12" text-anchor="middle">'
        f'<tspan fill="{P("gold")}">❯ </tspan>'
        f'<tspan fill="{P("dim")}">session closed</tspan>'
        f'<tspan fill="{P("hair")}">  ·  </tspan>'
        f'<tspan fill="{P("text")}">Kolkata, India · UTC+5:30</tspan>'
        f'<tspan fill="{P("hair")}">  ·  </tspan>'
        f'<tspan fill="{P("dim")}">open for systems &amp; devtools collaboration</tspan>'
        f'</text>'
    )

    if not static:
        parts.append(f'<rect class="cur" x="{W - 36}" y="{H / 2 - 7}" width="7" height="14" rx="1" fill="{ACCENT}"/>')
    else:
        parts.append(f'<rect x="{W - 36}" y="{H / 2 - 7}" width="7" height="14" rx="1" fill="{ACCENT}"/>')

    parts.append("</svg>")
    with open("footer-card.svg", "w", encoding="utf-8") as f:
        f.write("\n".join(parts))
    print(f"wrote footer-card.svg ({W}x{H}, cinematic footer card)")


if __name__ == "__main__":
    main()
