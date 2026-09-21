"""Generate the Master High-CTR Documentary Thumbnail for Episodes 1–8 Supercut.

Follows Section 26 YouTube Algorithmic Packaging rules:
- 3-Element Mobile CTR Rule:
  1. Focal Subject: High-contrast Vasco da Gama / São Gabriel surging through ocean swell.
  2. Spectacle: Raging waves, dramatic atmospheric light, golden sun breaking through storm clouds.
  3. Text Punch: 2-3 words MAX in bold yellow/white with heavy black stroke ("THE IMPOSSIBLE" / "VOYAGE").
  4. Tested at 10% display scale for smartphone legibility.
"""

from __future__ import annotations

import pathlib
from PIL import Image, ImageDraw, ImageEnhance, ImageFilter, ImageFont, ImageOps

ROOT = pathlib.Path(r"C:\Sagar\Projects\vasco-da-gama")
OUTPUT_DIR = ROOT / "production" / "exports"
THUMB_OUTPUT = OUTPUT_DIR / "Vasco-da-Gama-Outbound-Voyage-Supercut-thumbnail-v1.png"
THUMB_MOBILE_PREVIEW = OUTPUT_DIR / "Vasco-da-Gama-Outbound-Voyage-Supercut-thumbnail-10pct.png"

# Base image candidates
BASE_STORM = ROOT / "chapters" / "chapter-01-first-voyage" / "episode-03-cape" / "images" / "CH01-EP03-S04-v1.png"
BASE_INDIA = ROOT / "chapters" / "chapter-01-first-voyage" / "episode-06-monsoon-crossing" / "images" / "CH01-EP06-S08-v1.png"
BASE_FLEET = ROOT / "chapters" / "chapter-01-first-voyage" / "episode-01-lisbon" / "images" / "CH01-S07-v1.png"


def create_master_thumbnail():
    print("Generating Master YouTube Thumbnail...")

    # Load base image (EP03-S04 Cape of Good Hope Storm / São Gabriel)
    # This provides the ultimate high-drama spectacle (Element 2)
    if BASE_STORM.exists():
        img = Image.open(BASE_STORM).convert("RGB")
    else:
        img = Image.open(BASE_INDIA).convert("RGB")

    # Resize to standard YouTube 1280x720 (16:9)
    target_w, target_h = 1280, 720
    img = ImageOps.fit(img, (target_w, target_h), Image.Resampling.LANCZOS, centering=(0.5, 0.5))

    # Apply algorithmic visual punch: Contrast +28%, Saturation +25%, Sharpness +35%
    enh_c = ImageEnhance.Contrast(img)
    img = enh_c.enhance(1.28)
    enh_s = ImageEnhance.Color(img)
    img = enh_s.enhance(1.25)
    enh_sh = ImageEnhance.Sharpness(img)
    img = enh_sh.enhance(1.35)

    # Vignette overlay for depth and text legibility
    vignette = Image.new("RGBA", (target_w, target_h), (0, 0, 0, 0))
    v_draw = ImageDraw.Draw(vignette)
    
    # Dark left gradient for typography backing
    for x in range(750):
        alpha = int(220 * ((750 - x) / 750) ** 1.3)
        v_draw.line([(x, 0), (x, target_h)], fill=(5, 8, 14, alpha))

    # Dark bottom edge gradient
    for y in range(540, target_h):
        alpha = int(180 * ((y - 540) / 180) ** 1.2)
        v_draw.line([(0, y), (target_w, y)], fill=(5, 8, 14, alpha))

    img = Image.alpha_composite(img.convert("RGBA"), vignette).convert("RGB")
    draw = ImageDraw.Draw(img)

    # Fonts
    font_impact_bold = r"C:\Windows\Fonts\impact.ttf"
    font_georgia_bold = r"C:\Windows\Fonts\georgiab.ttf" if pathlib.Path(r"C:\Windows\Fonts\georgiab.ttf").exists() else r"C:\Windows\Fonts\georgia.ttf"

    f_badge = ImageFont.truetype(font_georgia_bold, 28)
    f_title1 = ImageFont.truetype(font_impact_bold, 115)
    f_title2 = ImageFont.truetype(font_impact_bold, 128)
    f_sub = ImageFont.truetype(font_georgia_bold, 34)

    # Badge: "FULL DOCUMENTARY"
    badge_x, badge_y = 60, 50
    badge_w, badge_h = 360, 52
    draw.rectangle([badge_x, badge_y, badge_x + badge_w, badge_y + badge_h], fill=(185, 20, 20), outline=(255, 215, 0), width=3)
    draw.text((badge_x + badge_w // 2, badge_y + badge_h // 2), "FULL DOCUMENTARY", font=f_badge, fill=(255, 255, 255), anchor="mm")

    # Function to draw heavy-stroke punch text (Element 3)
    def draw_stroked_text(pos, text, font, fill_color, stroke_color, stroke_width):
        x, y = pos
        # Heavy drop shadow
        for dx in range(-stroke_width - 3, stroke_width + 5):
            for dy in range(-stroke_width - 3, stroke_width + 5):
                draw.text((x + dx + 4, y + dy + 5), text, font=font, fill=(0, 0, 0, 255))
        # Stroke
        draw.text((x, y), text, font=font, fill=fill_color, stroke_width=stroke_width, stroke_fill=stroke_color)

    # Line 1: "THE IMPOSSIBLE" (White with massive black stroke)
    draw_stroked_text((60, 115), "THE IMPOSSIBLE", f_title1, fill_color=(255, 255, 255), stroke_color=(0, 0, 0), stroke_width=8)

    # Line 2: "VOYAGE" (Vibrant Impact Golden Yellow with massive black stroke)
    draw_stroked_text((60, 230), "VOYAGE", f_title2, fill_color=(255, 220, 0), stroke_color=(0, 0, 0), stroke_width=9)

    # Sub-tag: "1497–1498 • EPISODES 1–8 COMPLETE"
    sub_x, sub_y = 65, 375
    draw.rectangle([sub_x - 10, sub_y - 6, sub_x + 580, sub_y + 44], fill=(10, 15, 22, 230), outline=(212, 175, 55, 240), width=2)
    draw.text((sub_x + 5, sub_y + 2), "1497–1498 • THE OUTBOUND EXPEDITION", font=f_sub, fill=(255, 215, 0))

    # Lower hook: "4 SHIPS • 24,000 MILES • THE TRUE STORY"
    f_hook = ImageFont.truetype(font_georgia_bold, 28)
    draw.rectangle([55, 620, 680, 670], fill=(0, 0, 0, 220), outline=(255, 255, 255, 180), width=1)
    draw.text((70, 630), "4 SHIPS  •  24,000 MILES  •  THE TRUE STORY", font=f_hook, fill=(255, 255, 255))

    # Save full resolution thumbnail
    img.save(THUMB_OUTPUT, quality=95)
    print(f"Saved Master Thumbnail (1280x720): {THUMB_OUTPUT}")

    # Generate 10% Mobile Preview (128x72) to verify 3-Element Mobile Rule
    mobile_thumb = img.resize((128, 72), Image.Resampling.LANCZOS)
    mobile_thumb.save(THUMB_MOBILE_PREVIEW)
    print(f"Saved Mobile 10% Preview (128x72): {THUMB_MOBILE_PREVIEW}")


if __name__ == "__main__":
    create_master_thumbnail()
