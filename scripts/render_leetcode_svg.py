"""Render data/leetcode.json as an animated stats card SVG for soumya-chk101.

Layout mirrors leetcode.com's own progress widget: a segmented donut
(teal Easy, yellow Medium, red Hard arcs, proportional to solved counts)
around the total, difficulty bars in the middle, and streak / ranking stats on the
right. Arcs draw themselves once (SMIL stroke-dashoffset), then freeze.

    python scripts/render_leetcode_svg.py           # writes leetcode-card.svg
    STATIC=1 python scripts/render_leetcode_svg.py  # frozen frame
"""

import json
import math
import os

BG = "#0d1117"
TRACK = "#161b22"
BORDER = "#30363d"
INK = "#c9d1d9"
DIM = "#8b949e"
ACCENT = "#3fb950"

# LeetCode difficulty colors
LC = {"Easy": "#00b8a3", "Medium": "#ffc01e", "Hard": "#ef4743"}

FONT = "ui-monospace, SFMono-Regular, 'Cascadia Mono', Menlo, Consolas, monospace"

W = 860
H = 200
CX, CY, R = 128.0, 100.0, 62.0   # donut center and radius
STROKE = 11.0
GAP_DEG = 8.0                     # gap between arc segments


def main() -> None:
    static = os.environ.get("STATIC") == "1"

    with open("data/leetcode.json", encoding="utf-8") as f:
        d = json.load(f)

    solved, totals = d["solved"], d["totals"]
    ranking = d.get("ranking", 0)
    cal = d.get("calendar", {})
    streak = cal.get("max_streak", 0)
    active_days = cal.get("active_days", 0)

    circ = 2 * math.pi * R

    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" '
        f'viewBox="0 0 {W} {H}">',
        f'<rect width="100%" height="100%" rx="8" fill="{BG}" '
        f'stroke="{BORDER}" stroke-width="1"/>',
    ]
    if not static:
        parts.append(
            "<style>"
            ".f{opacity:0;animation:fi .5s ease-out forwards}"
            ".b{transform:scaleX(0);transform-origin:left;"
            "animation:gr .9s ease-out forwards}"
            "@keyframes fi{to{opacity:1}}"
            "@keyframes gr{to{transform:scaleX(1)}}"
            "</style>"
        )

    def cls(name: str, delay: float) -> str:
        if static:
            return ""
        return f' class="{name}" style="animation-delay:{delay:.2f}s"'

    parts.append(f'<g font-family="{FONT}">')

    # --- Donut: track ring, then one arc per difficulty. ---
    parts.append(
        f'<circle cx="{CX}" cy="{CY}" r="{R}" fill="none" '
        f'stroke="{TRACK}" stroke-width="{STROKE}"/>'
    )
    start_deg = -90.0
    order = ["Easy", "Medium", "Hard"]
    for i, name in enumerate(order):
        frac = solved[name] / max(solved["All"], 1)
        sweep_deg = max(frac * 360.0 - GAP_DEG, 2.0)
        seg = circ * sweep_deg / 360.0
        rot = start_deg + GAP_DEG / 2.0
        arc = (
            f'<circle cx="{CX}" cy="{CY}" r="{R}" fill="none" '
            f'stroke="{LC[name]}" stroke-width="{STROKE}" '
            f'stroke-linecap="round" '
            f'stroke-dasharray="{seg:.1f} {circ - seg:.1f}" '
            f'transform="rotate({rot:.1f} {CX} {CY})"'
        )
        if static:
            parts.append(arc + "/>")
        else:
            parts.append(
                arc + f' stroke-dashoffset="{seg:.1f}">'
                f'<animate attributeName="stroke-dashoffset" '
                f'from="{seg:.1f}" to="0" begin="{0.2 + i * 0.35:.2f}s" '
                f'dur="0.7s" fill="freeze"/></circle>'
            )
        start_deg += frac * 360.0

    parts.append(
        f'<g text-anchor="middle"{cls("f", 0.4)}>'
        f'<text x="{CX}" y="{CY + 2}" font-size="30" font-weight="bold" '
        f'fill="{INK}">{solved["All"]}</text>'
        f'<text x="{CX}" y="{CY + 24}" font-size="11" '
        f'fill="{DIM}">solved</text>'
        f"</g>"
    )

    # --- Middle: difficulty rows with colored bars. ---
    bx = 268.0
    bar_w = 200.0
    count_x = bx + 60 + bar_w + 92
    y = 62.0
    for i, name in enumerate(order):
        frac = solved[name] / max(totals[name], 1)
        parts.append(
            f'<g{cls("f", 0.3 + i * 0.15)}>'
            f'<circle cx="{bx + 5}" cy="{y - 4}" r="5" fill="{LC[name]}"/>'
            f'<text x="{bx + 18}" y="{y}" font-size="12" '
            f'fill="{DIM}">{name}</text>'
            f'<text x="{count_x}" y="{y}" font-size="12" fill="{INK}" '
            f'text-anchor="end">{solved[name]} / {totals[name]}</text>'
            f"</g>"
        )
        parts.append(
            f'<rect x="{bx + 78}" y="{y - 12}" width="{bar_w}" height="10" '
            f'rx="5" fill="{TRACK}"/>'
            f'<rect x="{bx + 78}" y="{y - 12}" '
            f'width="{max(bar_w * frac, 10):.1f}" height="10" rx="5" '
            f'fill="{LC[name]}"{cls("b", 0.35 + i * 0.15)}/>'
        )
        y += 42

    # --- Divider + right block: streak / rating stats. ---
    rx = count_x + 34
    parts.append(
        f'<line x1="{rx - 18}" y1="34" x2="{rx - 18}" y2="{H - 34}" '
        f'stroke="{BORDER}" stroke-width="1"/>'
    )
    
    parts.append(
        f'<g{cls("f", 0.55)}>'
        f'<text x="{rx}" y="72" font-size="32" font-weight="bold" '
        f'fill="{ACCENT}">{streak}</text>'
        f'<text x="{rx}" y="94" font-size="12" fill="{DIM}">day max streak</text>'
    )
    
    badge_label = "100 Days Badge"
    bw = 9 * len(badge_label) + 24
    parts.append(
        f'<rect x="{rx}" y="112" width="{bw}" height="26" rx="13" '
        f'fill="none" stroke="{ACCENT}" stroke-width="1.2"/>'
        f'<text x="{rx + bw / 2}" y="{129}" font-size="12" '
        f'font-weight="bold" fill="{ACCENT}" '
        f'text-anchor="middle">{badge_label}</text>'
    )
    parts.append(
        f'<text x="{rx}" y="{166}" font-size="11" fill="{DIM}">'
        f'rank #{ranking:,} &#183; {active_days} active days</text>'
        f"</g>"
    )

    parts.append(
        f'<text x="{W - 20}" y="{H - 14}" font-size="10" fill="{DIM}" '
        f'text-anchor="end">leetcode.com/u/{d["username"]}</text>'
    )
    parts.append("</g></svg>")

    with open("leetcode-card.svg", "w", encoding="utf-8") as f:
        f.write("\n".join(parts))
    print(f"wrote leetcode-card.svg ({W}x{H}, "
          f"{'static' if static else 'animated'})")


if __name__ == "__main__":
    main()
