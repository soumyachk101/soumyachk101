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
import os

import requests
from PIL import Image

BG = "#0d1117"
BORDER = "#30363d"
INK = "#c9d1d9"
DIM = "#8b949e"

FONT = "ui-monospace, SFMono-Regular, 'Cascadia Mono', Menlo, Consolas, monospace"
W = 860
H = 168
ICON = 64          # displayed icon size
ICON_PX = 128      # embedded bitmap resolution (2x for retina)


def short_name(display: str) -> str:
    return display.replace(" Badge", "").replace(" LeetCoding Challenge", "")


def sort_key(b: dict) -> tuple:
    rank = {"Knight": 0, "Guardian": 0, "Annual Badge": 1, "Daily Coding Challenge": 2}
    return (rank.get(b.get("name"), 3), b.get("creationDate", ""))


def fetch_icon(url: str) -> str:
    if url.startswith("/"):
        url = "https://leetcode.com" + url
    resp = requests.get(url, timeout=30,
                        headers={"User-Agent": "profile-art-refresh/1.0"})
    resp.raise_for_status()
    img = Image.open(io.BytesIO(resp.content)).convert("RGBA")
    img.thumbnail((ICON_PX, ICON_PX), Image.LANCZOS)
    buf = io.BytesIO()
    img.save(buf, "PNG", optimize=True)
    return base64.b64encode(buf.getvalue()).decode()


def main() -> None:
    static = os.environ.get("STATIC") == "1"

    with open("data/leetcode.json", encoding="utf-8") as f:
        d = json.load(f)
    badges = sorted(d.get("badges", []), key=sort_key)
    badges = [b for i, b in enumerate(badges)
              if i == 0 or b["displayName"] != badges[i - 1]["displayName"]]
    if not badges:
        print("no badges; skipping")
        return

    slot = (W - 40) / len(badges)

    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" '
        f'viewBox="0 0 {W} {H}">',
        f'<rect width="100%" height="100%" rx="8" fill="{BG}" '
        f'stroke="{BORDER}" stroke-width="1"/>',
    ]
    if not static:
        parts.append(
            "<style>.f{opacity:0;animation:fi .5s ease-out forwards}"
            "@keyframes fi{to{opacity:1}}</style>"
        )

    parts.append(f'<g font-family="{FONT}" text-anchor="middle">')
    for i, b in enumerate(badges):
        cx = 20 + slot * i + slot / 2
        print(f"embedding {b['displayName']}...")
        b64 = fetch_icon(b["icon"])
        anim = ("" if static else
                f' class="f" style="animation-delay:{0.15 + i * 0.12:.2f}s"')
        parts.append(
            f"<g{anim}>"
            f'<image x="{cx - ICON / 2:.0f}" y="24" width="{ICON}" '
            f'height="{ICON}" href="data:image/png;base64,{b64}"/>'
            f'<text x="{cx:.0f}" y="116" font-size="11" fill="{INK}">'
            f"{short_name(b['displayName'])}</text>"
            f'<text x="{cx:.0f}" y="134" font-size="9.5" fill="{DIM}">'
            f"{b.get('creationDate', '')}</text>"
            f"</g>"
        )
    parts.append(
        f'<text x="{W - 20}" y="{H - 14}" font-size="10" fill="{DIM}" '
        f'text-anchor="end">leetcode.com/u/{d["username"]}</text>'
    )
    parts.append("</g></svg>")

    with open("leetcode-badges.svg", "w", encoding="utf-8") as f:
        f.write("\n".join(parts))
    size = os.path.getsize("leetcode-badges.svg") // 1024
    print(f"wrote leetcode-badges.svg ({W}x{H}, {len(badges)} badges, "
          f"{size} KB, {'static' if static else 'animated'})")


if __name__ == "__main__":
    main()
