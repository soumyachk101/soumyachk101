"""Render the LeetCode streak card SVG for soumya-chk101.

Reads data/leetcode.json and writes:
  leetcode-streak.svg - active days, max streak (ring), problems solved

The center stat sits in a green ring that draws itself once (SMIL stroke-dashoffset).

    python scripts/render_streak_cards.py
    STATIC=1 python scripts/render_streak_cards.py   # frozen frame
"""

import json
import math
import os

BG = "#0d1117"
BORDER = "#30363d"
INK = "#c9d1d9"
DIM = "#8b949e"
ACCENT = "#3fb950"

FONT = "ui-monospace, SFMono-Regular, 'Cascadia Mono', Menlo, Consolas, monospace"
W = 860
H = 170
R = 46.0  # ring radius


def card(out: str, left: tuple, center: tuple, right: tuple,
         static: bool) -> None:
    """Each stat is (big_value, label, sublabel)."""
    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" '
        f'viewBox="0 0 {W} {H}">',
        f'<rect width="100%" height="100%" rx="8" fill="{BG}" '
        f'stroke="{BORDER}" stroke-width="1"/>',
    ]
    if not static:
        parts.append(
            "<style>.f{opacity:0;animation:fi .6s ease-out forwards}"
            "@keyframes fi{to{opacity:1}}</style>"
        )

    def fade(delay: float) -> str:
        return "" if static else (
            f' class="f" style="animation-delay:{delay:.2f}s"'
        )

    parts.append(f'<g font-family="{FONT}">')

    # Side columns
    for cx, (value, label, sub), delay in (
        (150.0, left, 0.15),
        (W - 150.0, right, 0.35),
    ):
        parts.append(
            f'<g text-anchor="middle"{fade(delay)}>'
            f'<text x="{cx}" y="76" font-size="30" font-weight="bold" '
            f'fill="{INK}">{value}</text>'
            f'<text x="{cx}" y="100" font-size="12" fill="{DIM}">{label}</text>'
            f'<text x="{cx}" y="120" font-size="11" fill="{DIM}">{sub}</text>'
            f"</g>"
        )

    # Faint separators
    for x in (300, W - 300):
        parts.append(
            f'<line x1="{x}" y1="30" x2="{x}" y2="{H - 30}" '
            f'stroke="{BORDER}" stroke-width="1"/>'
        )

    # Center ring + stat
    cx, cy = W / 2, H / 2 - 8
    circumference = 2 * math.pi * R
    ring = (
        f'<circle cx="{cx}" cy="{cy}" r="{R}" fill="none" '
        f'stroke="{ACCENT}" stroke-width="3" stroke-linecap="round" '
        f'transform="rotate(-90 {cx} {cy})"'
    )
    if static:
        parts.append(ring + "/>")
    else:
        parts.append(
            ring + f' stroke-dasharray="{circumference:.1f}" '
            f'stroke-dashoffset="{circumference:.1f}">'
            f'<animate attributeName="stroke-dashoffset" '
            f'from="{circumference:.1f}" to="0" begin="0.2s" dur="1.1s" '
            f'fill="freeze"/></circle>'
        )
    value, label, sub = center
    parts.append(
        f'<g text-anchor="middle"{fade(0.5)}>'
        f'<text x="{cx}" y="{cy + 10}" font-size="34" font-weight="bold" '
        f'fill="{ACCENT}">{value}</text>'
        f'<text x="{cx}" y="{cy + R + 24}" font-size="12" '
        f'fill="{DIM}">{label}</text>'
        f'<text x="{cx}" y="{cy + R + 42}" font-size="11" '
        f'fill="{DIM}">{sub}</text>'
        f"</g>"
    )

    parts.append("</g></svg>")
    with open(out, "w", encoding="utf-8") as f:
        f.write("\n".join(parts))
    print(f"wrote {out}")


def main() -> None:
    static = os.environ.get("STATIC") == "1"

    if os.path.exists("data/contributions.json"):
        with open("data/contributions.json", encoding="utf-8") as f:
            gh = json.load(f)
        card(
            "streak-card.svg",
            (f"{gh['total']:,}", "total contributions", "last 12 months"),
            (str(gh["current_streak"]), "day current streak", "daily active shipping"),
            (str(gh["longest_streak"]), "day longest streak", f"best day {gh['best_day']['count']} commits"),
            static,
        )

    with open("data/leetcode.json", encoding="utf-8") as f:
        lc = json.load(f)

    active_days = lc["calendar"]["active_days"]
    max_streak = lc["calendar"]["max_streak"]
    solved_all = lc["solved"]["All"]
    hard_solved = lc["solved"]["Hard"]

    card(
        "leetcode-streak.svg",
        (str(active_days), "total active days", "on leetcode"),
        (str(max_streak), "day max streak", "consistent problem solving"),
        (f"{solved_all}", "problems solved", f"{hard_solved} hard &#183; 142 med"),
        static,
    )


if __name__ == "__main__":
    main()
