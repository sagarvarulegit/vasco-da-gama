"""Generate the 16:9 Master YouTube Thumbnail for Chapter 1 Episode 3 (Cape of Good Hope)."""

import pathlib
import subprocess
import sys

PROJECT_ROOT = pathlib.Path(__file__).resolve().parent.parent.parent
IMAGES_EP03_DIR = PROJECT_ROOT / "images" / "episode-03"
PROMPT_GEN_SCRIPT = PROJECT_ROOT / "production" / "tools" / "gemini_image_generate.py"

THUMBNAIL_PROMPT = """MASTER_STYLE_02. 16:9 widescreen epic YouTube thumbnail composition. 22 November 1497, rounding the Cape of Good Hope. Majestic, high-drama maritime breakthrough: the massive flagship São Gabriel (SHIP_SG01) surges proudly through deep sapphire waves past the colossal, towering golden sandstone cliffs of the Cape of Good Hope. Intense golden god-rays pierce through dark parting storm clouds, illuminating the blazing crimson Order of Christ crosses on the huge billowing square sails and sparkling white ocean foam. On the poop deck, VASCO_01 stands like an iron commander with wind-blown dark hair, his hand raised toward the uncharted eastern horizon, surrounded by brass trumpeters sounding fanfares. Epic chiaroscuro contrast, grand European historical masterpiece, extreme visual clarity, no text, no modern elements."""


def main():
    output_path = IMAGES_EP03_DIR / "CH01-EP03-thumbnail-v1.png"
    print(f"Generating Episode 3 16:9 Thumbnail: {output_path.name}...")
    cmd = [
        sys.executable,
        str(PROMPT_GEN_SCRIPT),
        "--prompt",
        THUMBNAIL_PROMPT,
        "--output",
        str(output_path),
    ]
    res = subprocess.run(cmd, capture_output=True, text=True)
    if res.returncode != 0:
        print(f"Error generating thumbnail:\n{res.stderr}", file=sys.stderr)
        return 1
    print(f"Thumbnail successfully created: {output_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
