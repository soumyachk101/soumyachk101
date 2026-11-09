"""Render earned LeetCode badges as a self-hosted card SVG for soumya-chk101.

Downloads each badge icon once at generation time, downscales it with
Pillow, and base64-embeds it into the SVG, so the displayed card makes
no external requests.

    python scripts/fetch_leetcode.py
    python scripts/render_leetcode_badges_svg.py   # leetcode-badges.svg
"""

import base64
import io
import json
import math
import os
from html import escape

import requests
from PIL import Image

BG = "#0a0a0f"
BORDER = "#2a2a34"
INK = "#ece4d4"
DIM = "#9a9488"

FONT = "ui-monospace, SFMono-Regular, 'Cascadia Mono', Menlo, Consolas, monospace"
W = 860
ICON_PX = 128      # embedded bitmap resolution (2x for retina)


def short_name(display: str) -> str:
    return display.replace(" Badge", "").replace(" LeetCoding Challenge", "")


def sort_key(b: dict) -> tuple:
    rank = {"Knight": 0, "Guardian": 0, "Annual Badge": 1, "Daily Coding Challenge": 2}
    return (rank.get(b.get("name"), 3), b.get("creationDate", ""))


def fetch_icon(url: str) -> str:
    if not url:
        return ""
    if url.startswith("/"):
        url = "https://leetcode.com" + url
    try:
        resp = requests.get(url, timeout=30,
                            headers={"User-Agent": "profile-art-refresh/1.0"})
        resp.raise_for_status()
        img = Image.open(io.BytesIO(resp.content)).convert("RGBA")
        img.thumbnail((ICON_PX, ICON_PX), Image.LANCZOS)
        buf = io.BytesIO()
        img.save(buf, "PNG", optimize=True)
        return base64.b64encode(buf.getvalue()).decode()
    except Exception as exc:
        print(f"warning: failed to fetch icon {url}: {exc}")
        return ""


def main() -> None:
    static = os.environ.get("STATIC") == "1"

    with open("data/leetcode.json", encoding="utf-8") as f:
        d = json.load(f)
    seen = set()
    badges = []
    for b in sorted(d.get("badges", []), key=sort_key):
        disp = b.get("displayName", "")
        if disp not in seen:
            seen.add(disp)
            badges.append(b)
    if not badges:
        print("no badges; skipping")
        return

    n = len(badges)
    if n <= 8:
        rows = [badges]
        icon = 58 if n >= 8 else 64
        name_fs = 10.5 if n >= 8 else 11.0
        date_fs = 9.0 if n >= 8 else 9.5
        h = 168
    else:
        per_row = math.ceil(n / 2)
        rows = [badges[:per_row], badges[per_row:]]
        icon = 58
        name_fs = 11.0
        date_fs = 9.5
        h = 290

    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{h}" '
        f'viewBox="0 0 {W} {h}">',
        f'<rect width="100%" height="100%" rx="8" fill="{BG}" '
        f'stroke="{BORDER}" stroke-width="1"/>',
    ]
    if not static:
        parts.append(
            "<style>.f{opacity:0;animation:fi .5s ease-out forwards}"
            "@keyframes fi{to{opacity:1}}</style>"
        )

    parts.append(f'<g font-family="{FONT}" text-anchor="middle">')
    idx = 0
    for r_i, row in enumerate(rows):
        y_top = 24 + r_i * 124
        slot = (W - 40) / len(row)
        for c_i, b in enumerate(row):
            cx = 20 + slot * c_i + slot / 2
            print(f"embedding {b['displayName']}...")
            b64 = fetch_icon(b.get("icon", ""))
            anim = ("" if static else
                    f' class="f" style="animation-delay:{0.15 + idx * 0.12:.2f}s"')
            img_el = (
                f'<image x="{cx - icon / 2:.0f}" y="{y_top}" width="{icon}" '
                f'height="{icon}" href="data:image/png;base64,{b64}"/>'
                if b64 else ""
            )
            label_y = y_top + icon + 28
            date_y = label_y + 18
            parts.append(
                f"<g{anim}>"
                f"{img_el}"
                f'<text x="{cx:.0f}" y="{label_y}" font-size="{name_fs}" fill="{INK}">'
                f"{escape(short_name(b['displayName']))}</text>"
                f'<text x="{cx:.0f}" y="{date_y}" font-size="{date_fs}" fill="{DIM}">'
                f"{escape(b.get('creationDate', ''))}</text>"
                f"</g>"
            )
            idx += 1
    parts.append(
        f'<text x="{W - 20}" y="{h - 14}" font-size="10" fill="{DIM}" '
        f'text-anchor="end">leetcode.com/u/{escape(d["username"])}</text>'
    )
    parts.append("</g></svg>")

    with open("leetcode-badges.svg", "w", encoding="utf-8") as f:
        f.write("\n".join(parts))
    size = os.path.getsize("leetcode-badges.svg") // 1024
    print(f"wrote leetcode-badges.svg ({W}x{h}, {len(badges)} badges, "
          f"{size} KB, {'static' if static else 'animated'})")


if __name__ == "__main__":
    main()
