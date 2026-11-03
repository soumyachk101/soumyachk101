"""Cinematic 'Noir · Gold & Crimson' theme — the single source of truth for every
generated SVG in this profile.

Design intent (so the whole page reads as ONE film, not a collage):
  * warm near-black canvas, champagne-gold primary, oxblood-crimson secondary,
    cool steel-blue tertiary. No green, no saturated neon, no rainbow.
  * a recurring "film slate" chrome (three muted dots + a gold hairline + a
    centered mono title) so every card feels like a frame from the same movie.
  * motion is slow, low-contrast and restrained: sheen sweeps, gentle reveals.
All assets are self-contained (inline SMIL/CSS, no external refs, no JS).
"""

PAL = {
    "base":     "#0a0a0f",  # noir black canvas
    "base2":    "#0e0e14",
    "surface":  "#14141b",  # raised panel
    "surface2": "#1c1c26",  # raised panel 2 / tracks
    "track":    "#191921",
    "border":   "#2a2a34",
    "hair":     "#3a3a46",  # hairline / dividers
    "text":     "#ece4d4",  # champagne / warm off-white
    "dim":      "#9a9488",  # smoke
    "faint":    "#6a6a75",
    "gold":     "#d8a63f",  # champagne gold (primary accent)
    "gold_hi":  "#f2d489",
    "gold_lo":  "#7c5f24",
    "crim":     "#b03a45",  # oxblood crimson (secondary accent)
    "crim_hi":  "#d4606c",
    "steel":    "#6b7f9c",  # cool steel-blue (tertiary accent)
    "steel_hi": "#93a7c4",
    "ember":    "#c07a3a",  # warm amber, used sparingly
}

MONO = "ui-monospace, SFMono-Regular, 'Cascadia Mono', Menlo, Consolas, monospace"
SANS = "-apple-system, BlinkMacSystemFont, 'Segoe UI', 'Helvetica Neue', Arial, sans-serif"


def P(key: str) -> str:
    return PAL[key]


def style() -> str:
    """Global text-smoothing <style> block, unique-safe when duplicated per doc."""
    return (
        "<style>text{-webkit-font-smoothing:antialiased;-moz-osx-font-smoothing:grayscale;}"
        "</style>"
    )


def open_svg(w: int, h: int, title: str = "") -> str:
    aria = f' role="img" aria-label="{title}"' if title else ""
    ttl = f"<title>{title}</title>" if title else ""
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" '
        f'viewBox="0 0 {w} {h}"{aria} text-rendering="geometricPrecision" '
        f'shape-rendering="geometricPrecision">\n{ttl}{style()}\n'
    )


def close_svg() -> str:
    return "</svg>\n"


def canvas(w: int, h: int, rx: int = 10) -> str:
    """Noir rounded canvas + 1px hairline border. The film 'frame'."""
    return (
        f'<rect x="0.5" y="0.5" width="{w - 1}" height="{h - 1}" rx="{rx}" '
        f'fill="url(#gBase)" stroke="{P("border")}" stroke-width="1"/>'
    )


def g_base(id_="gBase") -> str:
    """Warm near-black vertical base gradient (subtle, not flat)."""
    return (
        f'<linearGradient id="{id_}" x1="0" y1="0" x2="0" y2="1">'
        f'<stop offset="0" stop-color="{P("base2")}"/>'
        f'<stop offset="1" stop-color="{P("base")}"/>'
        f"</linearGradient>"
    )


def g_gold(id_="gGold", vertical=True) -> str:
    axis = "x1=0 y1=0 x2=0 y2=1" if vertical else "x1=0 y1=0 x2=1 y2=0"
    return (
        f'<linearGradient id="{id_}" {axis}>'
        f'<stop offset="0" stop-color="{P("gold_hi")}"/>'
        f'<stop offset="1" stop-color="{P("gold")}"/>'
        f"</linearGradient>"
    )


def g_goldline(id_="gGoldline") -> str:
    """Horizontal gold rule that fades at both ends."""
    return (
        f'<linearGradient id="{id_}" x1="0" y1="0" x2="1" y2="0">'
        f'<stop offset="0" stop-color="{P("gold")}" stop-opacity="0"/>'
        f'<stop offset="0.5" stop-color="{P("gold_hi")}"/>'
        f'<stop offset="1" stop-color="{P("gold")}" stop-opacity="0"/>'
        f"</linearGradient>"
    )


def g_crimline(id_="gCrimline") -> str:
    return (
        f'<linearGradient id="{id_}" x1="0" y1="0" x2="1" y2="0">'
        f'<stop offset="0" stop-color="{P("crim")}" stop-opacity="0"/>'
        f'<stop offset="0.5" stop-color="{P("crim_hi")}"/>'
        f'<stop offset="1" stop-color="{P("crim")}" stop-opacity="0"/>'
        f"</linearGradient>"
    )


def g_keyline(id_="gKeyline") -> str:
    """Left-edge 'color grade' keyline: crimson -> gold, top to bottom."""
    return (
        f'<linearGradient id="{id_}" x1="0" y1="0" x2="0" y2="1">'
        f'<stop offset="0" stop-color="{P("crim")}"/>'
        f'<stop offset="0.55" stop-color="{P("gold")}"/>'
        f'<stop offset="1" stop-color="{P("gold_lo")}"/>'
        f"</linearGradient>"
    )


def glow(id_, color, opacity=0.35, blur=5) -> str:
    return (
        f'<filter id="{id_}" x="-50%" y="-50%" width="200%" height="200%">'
        f'<feDropShadow dx="0" dy="0" stdDeviation="{blur}" '
        f'flood-color="{color}" flood-opacity="{opacity}"/>'
        f"</filter>"
    )


def slate_bar(w: int, label: str, h: int = 34) -> str:
    """The recurring 'film slate' title bar: three muted dots + a centered mono
    title + a gold hairline. Reads as a frame, not a browser."""
    cx = w / 2
    L = 20
    return (
        f'<g>'
        f'<rect x="0.5" y="0.5" width="{w - 1}" height="{h - 0.5}" fill="{P("surface")}"/>'
        f'<line x1="1" y1="{h}" x2="{w - 1}" y2="{h}" stroke="{P("hair")}" stroke-width="1"/>'
        f'<circle cx="{L + 6}" cy="{h / 2}" r="3" fill="{P("gold")}"/>'
        f'<circle cx="{L + 18}" cy="{h / 2}" r="3" fill="{P("crim")}"/>'
        f'<circle cx="{L + 30}" cy="{h / 2}" r="3" fill="{P("steel")}"/>'
        f'<text x="{L + 42}" y="{h / 2 + 3.5}" font-family="{MONO}" font-size="10" '
        f'letter-spacing="0.4" fill="{P("faint")}">{label}</text>'
        f'<text x="{cx}" y="{h / 2 + 4}" text-anchor="middle" font-family="{MONO}" '
        f'font-size="11.5" letter-spacing="0.6" fill="{P("text")}">{label}</text>'
        f"</g>"
    )


def sheen(id_, w: int, color, dur="5.5s", op_hi="0.5", h=1) -> str:
    """A slow, low-contrast light band sweeping left-to-right across a hairline.
    Wrap the returned <g> inside a <g clip-path=...> for edge-clean stops."""
    gid = f"{id_}G"
    return (
        f'<linearGradient id="{gid}" x1="0" y1="0" x2="1" y2="0">'
        f'<stop offset="0" stop-color="{color}" stop-opacity="0"/>'
        f'<stop offset="0.5" stop-color="{color}" stop-opacity="{op_hi}"/>'
        f'<stop offset="1" stop-color="{color}" stop-opacity="0"/>'
        f'</linearGradient>'
        f'<g><rect x="-200" y="0" width="200" height="{h}" fill="url(#{gid})">'
        f'<animateTransform attributeName="transform" type="translate" '
        f'from="0 0" to="{w + 40} 0" dur="{dur}" repeatCount="indefinite" '
        f'calcMode="spline" keySplines="0.4 0 0.6 1"/></rect></g>'
    )


def pulse_dot(cx: int, cy: int, color=None, r: int = 3) -> str:
    """A slow, muted 'live' indicator (crimson by default) — calm, not blinking fast."""
    c = color or P("crim")
    return (
        f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{c}">'
        f'<animate attributeName="opacity" values="0.55;1;0.55" keyTimes="0;0.5;1" '
        f'dur="2.6s" repeatCount="indefinite" calcMode="spline" '
        f'keySplines="0.45 0 0.55 1;0.45 0 0.55 1"/></circle>'
    )


def defs_block(*entries) -> str:
    return "<defs>\n" + "".join(entries) + "\n</defs>\n"
