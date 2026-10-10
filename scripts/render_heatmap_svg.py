"""Render data/contributions.json as an animated heatmap SVG for soumyachk101.

The classic 53-week x 7-day calendar of rounded boxes, drawn in a
GitHub-green ramp on the terminal-dark panel. Cells reveal once
with a diagonal stagger.

    python scripts/render_heatmap_svg.py           # writes contrib-heatmap.svg
    STATIC=1 python scripts/render_heatmap_svg.py  # frozen frame
"""

import json
import os
from datetime import date

# Palette: none -> brightest; last entry is neon green for best day
PALETTE = ["#161b22", "#0e4429", "#006d32", "#26a641", "#39d353", "#69f0a0"]

BG = "#0d1117"
BORDER = "#30363d"
DIM = "#8b949e"
FONT = "ui-monospace, SFMono-Regular, 'Cascadia Mono', Menlo, Consolas, monospace"

CELL = 13.0
GAP = 3.0
STEP = CELL + GAP
PAD = 16.0
LABEL_H = 20.0   # month labels row
FOOTER_H = 34.0
DELAY = 0.015    # diagonal stagger per (week + weekday)
DUR = 0.4

MONTHS = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
          "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]


def main() -> None:
    static = os.environ.get("STATIC") == "1"

    with open("data/contributions.json", encoding="utf-8") as f:
        data = json.load(f)
    days = data["days"]
    best_date = data["best_day"]["date"]

    def dow(iso: str) -> int:
        return (date.fromisoformat(iso).weekday() + 1) % 7  # Sun=0

    weeks: list[list[dict]] = [[]]
    for d in days:
        if dow(d["date"]) == 0 and weeks[-1]:
            weeks.append([])
        weeks[-1].append(d)

    n_weeks = len(weeks)
    grid_w = n_weeks * STEP - GAP
    grid_h = 7 * STEP - GAP
    width = round(grid_w + 2 * PAD)
    height = round(LABEL_H + grid_h + FOOTER_H + 2 * PAD - 6)

    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" '
        f'height="{height}" viewBox="0 0 {width} {height}">',
        f'<rect width="100%" height="100%" rx="8" fill="{BG}" '
        f'stroke="{BORDER}" stroke-width="1"/>',
    ]

    if not static:
        parts.append(
            "<style>"
            ".c{opacity:0;animation:pop " + f"{DUR}s" + " ease-out forwards}"
            "@keyframes pop{from{opacity:0;transform:translateY(-6px)}"
            "to{opacity:1;transform:none}}"
            "</style>"
        )

    # Month labels
    parts.append(
        f'<g font-family="{FONT}" font-size="10" fill="{DIM}">'
    )
    last_label_col = -4
    prev_month = None
    for w, col in enumerate(weeks):
        m = date.fromisoformat(col[0]["date"]).month
        if m != prev_month and w - last_label_col >= 3 and w < n_weeks - 2:
            x = PAD + w * STEP
            parts.append(
                f'<text x="{x:.0f}" y="{PAD + 9:.0f}">{MONTHS[m - 1]}</text>'
            )
            last_label_col = w
        prev_month = m
    parts.append("</g>")

    # Day cells
    top = PAD + LABEL_H
    parts.append("<g>")
    for w, col in enumerate(weeks):
        for d in col:
            r = dow(d["date"])
            x = PAD + w * STEP
            y = top + r * STEP
            color = (PALETTE[5] if d["date"] == best_date
                     else PALETTE[min(d["level"], 4)])
            attrs = ""
            if not static:
                attrs = (f' class="c" '
                         f'style="animation-delay:{(w + r) * DELAY:.3f}s"')
            parts.append(
                f'<rect x="{x:.0f}" y="{y:.0f}" width="{CELL:.0f}" '
                f'height="{CELL:.0f}" rx="3" fill="{color}"{attrs}>'
                f'<title>{d["count"]} on {d["date"]}</title></rect>'
            )
    parts.append("</g>")

    # Footer
    fy = top + grid_h + 21
    stats = f'{data["total"]:,} contributions in the last year &#183; {data["current_streak"]} day current streak'
    parts.append(
        f'<text x="{PAD:.0f}" y="{fy:.0f}" font-family="{FONT}" '
        f'font-size="11" fill="{DIM}">{stats}</text>'
    )
    legend = [f'<g font-family="{FONT}" font-size="11" fill="{DIM}">']
    lx = width - PAD - 5 * (CELL + 3) - 66
    legend.append(f'<text x="{lx:.0f}" y="{fy:.0f}">less</text>')
    for i in range(5):
        legend.append(
            f'<rect x="{lx + 30 + i * (CELL + 3):.0f}" y="{fy - 10:.0f}" '
            f'width="{CELL:.0f}" height="{CELL:.0f}" rx="3" '
            f'fill="{PALETTE[i]}"/>'
        )
    legend.append(
        f'<text x="{lx + 30 + 5 * (CELL + 3) + 4:.0f}" y="{fy:.0f}">more</text>'
    )
    legend.append("</g>")
    parts.extend(legend)

    parts.append("</svg>")
    with open("contrib-heatmap.svg", "w", encoding="utf-8") as f:
        f.write("\n".join(parts))
    print(f"wrote contrib-heatmap.svg ({width}x{height}, {n_weeks} weeks, "
          f"{'static' if static else 'animated'})")


if __name__ == "__main__":
    main()
