"""
Generate a cinematic Studio Showcase card for the SWOC Season 7 Contributor Badge.
Renders an 860px wide Noir studio backdrop with ambient glow, tech grid,
lanyard strap, realistic drop shadow, and film-slate chrome.
"""
from PIL import Image, ImageDraw, ImageFilter, ImageFont
import math
from collections import deque

def generate_swoc_showcase():
    # 1. Load original badge
    badge_path = "/Users/soumyachakraborty/Documents/Github profile/soumyachk101/SWOC_Season_7_Badge.png"
    badge_orig = Image.open(badge_path).convert("RGB")
    bw, bh = badge_orig.size

    # 2. Extract clean alpha mask (flood fill black corners & slot hole)
    visited = bytearray(bw * bh)
    q = deque([(0, 0), (bw-1, 0), (0, bh-1), (bw-1, bh-1), (bw//2, 45)])
    threshold = 28
    for x, y in q:
        visited[y * bw + x] = 1

    while q:
        x, y = q.popleft()
        for nx, ny in ((x+1, y), (x-1, y), (x, y+1), (x, y-1)):
            if 0 <= nx < bw and 0 <= ny < bh:
                idx = ny * bw + nx
                if not visited[idx]:
                    p = badge_orig.getpixel((nx, ny))
                    if max(p) <= threshold:
                        visited[idx] = 1
                        q.append((nx, ny))

    badge_mask = Image.new("L", (bw, bh), 0)
    for y in range(bh):
        for x in range(bw):
            if not visited[y * bw + x]:
                badge_mask.putpixel((x, y), 255)

    smooth_mask = badge_mask.filter(ImageFilter.GaussianBlur(radius=0.9))
    badge_rgba = badge_orig.copy()
    badge_rgba.putalpha(smooth_mask)

    # 3. Canvas setup: 860 width x 1120 height
    cw, ch = 860, 1140
    canvas = Image.new("RGBA", (cw, ch), (10, 10, 15, 255))
    draw = ImageDraw.Draw(canvas)

    # Base vertical gradient
    for y in range(ch):
        t = y / ch
        r = int(14 * (1 - t) + 7 * t)
        g = int(17 * (1 - t) + 9 * t)
        b = int(24 * (1 - t) + 14 * t)
        draw.line([(0, y), (cw, y)], fill=(r, g, b, 255))

    # Ambient radial glow behind badge
    glow_cx, glow_cy = cw // 2, 490
    glow_radius = 420
    glow_layer = Image.new("RGBA", (cw, ch), (0, 0, 0, 0))
    glow_draw = ImageDraw.Draw(glow_layer)

    # Draw radial gradient rings
    for r in range(glow_radius, 0, -6):
        t = r / glow_radius
        # Ice blue / navy glow
        alpha = int(75 * (1 - t) ** 1.8)
        gr = int(22 * (1 - t) + 12 * t)
        gg = int(48 * (1 - t) + 20 * t)
        gb = int(88 * (1 - t) + 36 * t)
        glow_draw.ellipse(
            [glow_cx - r, glow_cy - int(r * 0.95), glow_cx + r, glow_cy + int(r * 0.95)],
            fill=(gr, gg, gb, alpha)
        )
    canvas = Image.alpha_composite(canvas, glow_layer)
    draw = ImageDraw.Draw(canvas)

    # Subtle tech grid lines
    grid_color = (32, 42, 60, 45)
    for gx in range(40, cw, 40):
        draw.line([(gx, 44), (gx, ch - 48)], fill=grid_color, width=1)
    for gy in range(44 + 40, ch - 48, 40):
        draw.line([(0, gy), (cw, gy)], fill=grid_color, width=1)

    # Subtle crosshairs at grid intersections
    cross_color = (60, 80, 110, 80)
    for cx_mark, cy_mark in [(80, 120), (cw - 80, 120), (80, ch - 120), (cw - 80, ch - 120)]:
        draw.line([(cx_mark - 8, cy_mark), (cx_mark + 8, cy_mark)], fill=cross_color, width=1)
        draw.line([(cx_mark, cy_mark - 8), (cx_mark, cy_mark + 8)], fill=cross_color, width=1)

    # 4. Scale badge to fit comfortably in canvas
    target_bw = 570
    target_bh = int(bh * (target_bw / bw))
    badge_scaled = badge_rgba.resize((target_bw, target_bh), Image.Resampling.LANCZOS)
    badge_x = (cw - target_bw) // 2
    badge_y = 145

    # 5. Lanyard strap extending from top through badge slot
    strap_w = 60
    strap_x = (cw - strap_w) // 2
    strap_bottom = badge_y + int(target_bh * 0.055)

    # Strap shadow
    draw.rectangle([strap_x - 3, 44, strap_x + strap_w + 3, strap_bottom + 5], fill=(0, 0, 0, 90))
    # Strap body (dark textured ribbon)
    draw.rectangle([strap_x, 44, strap_x + strap_w, strap_bottom], fill=(16, 20, 28, 255))
    # Pinstripes on strap (ice blue and champagne gold seams)
    draw.line([(strap_x + 6, 44), (strap_x + 6, strap_bottom)], fill=(75, 115, 185, 200), width=2)
    draw.line([(strap_x + strap_w - 7, 44), (strap_x + strap_w - 7, strap_bottom)], fill=(75, 115, 185, 200), width=2)
    draw.line([(strap_x + strap_w // 2, 44), (strap_x + strap_w // 2, strap_bottom)], fill=(216, 166, 63, 140), width=1)

    # Metal clasp / buckle right at the badge hook
    clasp_y = badge_y - 2
    draw.rounded_rectangle(
        [strap_x + 10, clasp_y - 14, strap_x + strap_w - 10, clasp_y + 12],
        radius=4, fill=(45, 55, 72, 255), outline=(130, 145, 170, 255), width=1
    )
    draw.line([strap_x + 16, clasp_y - 1, strap_x + strap_w - 16, clasp_y - 1], fill=(20, 26, 36, 255), width=3)

    # 6. Multi-layer drop shadow for the badge
    # Layer A: Deep soft ambient shadow
    shadow_soft = Image.new("RGBA", (cw, ch), (0, 0, 0, 0))
    # Extract alpha from badge_scaled
    badge_alpha = badge_scaled.split()[3]
    shadow_mask_soft = Image.new("L", (cw, ch), 0)
    shadow_mask_soft.paste(badge_alpha, (badge_x, badge_y + 26))
    shadow_mask_soft = shadow_mask_soft.filter(ImageFilter.GaussianBlur(radius=34))
    shadow_color_soft = Image.new("RGBA", (cw, ch), (0, 2, 8, 190))
    shadow_soft.paste(shadow_color_soft, (0, 0), shadow_mask_soft)
    canvas = Image.alpha_composite(canvas, shadow_soft)

    # Layer B: Tighter contact shadow
    shadow_contact = Image.new("RGBA", (cw, ch), (0, 0, 0, 0))
    shadow_mask_contact = Image.new("L", (cw, ch), 0)
    shadow_mask_contact.paste(badge_alpha, (badge_x, badge_y + 10))
    shadow_mask_contact = shadow_mask_contact.filter(ImageFilter.GaussianBlur(radius=12))
    shadow_color_contact = Image.new("RGBA", (cw, ch), (0, 0, 0, 160))
    shadow_contact.paste(shadow_color_contact, (0, 0), shadow_mask_contact)
    canvas = Image.alpha_composite(canvas, shadow_contact)

    # 7. Paste scaled badge
    canvas.paste(badge_scaled, (badge_x, badge_y), badge_scaled)
    draw = ImageDraw.Draw(canvas)

    # 8. Chrome Top Bar (Slate style)
    top_bar_h = 44
    draw.rectangle([0, 0, cw, top_bar_h], fill=(18, 20, 27, 255))
    draw.line([(0, top_bar_h), (cw, top_bar_h)], fill=(45, 52, 68, 255), width=1)
    # Gold hairline under top bar
    draw.line([(cw // 4, top_bar_h), (3 * cw // 4, top_bar_h)], fill=(216, 166, 63, 180), width=1)

    # 3 dots
    dot_y = top_bar_h // 2
    draw.ellipse([24, dot_y - 4, 32, dot_y + 4], fill=(216, 166, 63, 255))  # gold
    draw.ellipse([40, dot_y - 4, 48, dot_y + 4], fill=(176, 58, 69, 255))   # crimson
    draw.ellipse([56, dot_y - 4, 64, dot_y + 4], fill=(107, 127, 156, 255)) # steel

    # Fonts
    try:
        font_mono = ImageFont.truetype("/System/Library/Fonts/SFNSMono.ttf", 13)
        font_mono_sm = ImageFont.truetype("/System/Library/Fonts/SFNSMono.ttf", 11)
        font_sans_bold = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 13)
    except:
        font_mono = ImageFont.load_default()
        font_mono_sm = ImageFont.load_default()
        font_sans_bold = ImageFont.load_default()

    # Top title
    title_text = "SWOC SEASON 7 · OPEN SOURCE CONTRIBUTOR PASS"
    bbox = draw.textbbox((0, 0), title_text, font=font_mono)
    tw = bbox[2] - bbox[0]
    draw.text(((cw - tw) // 2, dot_y - 7), title_text, fill=(236, 228, 212, 255), font=font_mono)

    # Status tag at right of top bar
    status_text = "● VERIFIED"
    draw.text((cw - 120, dot_y - 7), status_text, fill=(147, 167, 196, 255), font=font_mono)

    # 9. Chrome Bottom Bar
    bottom_bar_h = 48
    bottom_y = ch - bottom_bar_h
    draw.rectangle([0, bottom_y, cw, ch], fill=(14, 16, 22, 255))
    draw.line([(0, bottom_y), (cw, bottom_y)], fill=(38, 46, 60, 255), width=1)

    left_meta = "ID // @soumyachk101"
    draw.text((28, bottom_y + 16), left_meta, fill=(154, 148, 136, 255), font=font_mono_sm)

    center_meta = "SOCIAL WINTER OF CODE 2026 · BUILD TOGETHER"
    bbox_cm = draw.textbbox((0, 0), center_meta, font=font_mono_sm)
    cm_w = bbox_cm[2] - bbox_cm[0]
    draw.text(((cw - cm_w) // 2, bottom_y + 16), center_meta, fill=(216, 166, 63, 220), font=font_mono_sm)

    right_meta = "ROLE: CONTRIBUTOR"
    draw.text((cw - 170, bottom_y + 16), right_meta, fill=(147, 167, 196, 255), font=font_mono_sm)

    # 10. Outer border (1px hairline)
    draw.rounded_rectangle([0.5, 0.5, cw - 1.5, ch - 1.5], radius=14, outline=(42, 54, 75, 255), width=1)

    # Save output
    out_path = "/Users/soumyachakraborty/Documents/Github profile/soumyachk101/SWOC_Season_7_Badge_Card.png"
    canvas.save(out_path, "PNG", optimize=True)
    print("Showcase card generated at:", out_path)

if __name__ == "__main__":
    generate_swoc_showcase()
