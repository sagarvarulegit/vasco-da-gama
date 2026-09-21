"""Synthesize ElevenLabs voiceover for all 64 documentary scenes.

Features:
- British Documentary Narrator (George: JBFqnCBsd6RMkjVDRZzb)
- Model: eleven_multilingual_v2
- Idempotent caching in production/audio/voiceover/
- Exponential backoff retry logic for API resilience
- CLI flags: --limit N, --all, --force
"""

from __future__ import annotations

import argparse
import json
import os
import pathlib
import sys
import time
import requests

ROOT = pathlib.Path(r"C:\Sagar\Projects\vasco-da-gama")
MANIFEST_PATH = ROOT / "production" / "audio" / "narration_manifest.json"
VO_DIR = ROOT / "production" / "audio" / "voiceover"
VO_DIR.mkdir(parents=True, exist_ok=True)

# George - Warm, Captivating Storyteller (British Male, Narrative/Story)
DEFAULT_VOICE_ID = "JBFqnCBsd6RMkjVDRZzb"
DEFAULT_MODEL_ID = "eleven_multilingual_v2"


def get_api_key() -> str:
    key = os.environ.get("ELEVEN_LAB_API_KEY") or os.environ.get("ELEVENLABS_API_KEY")
    if not key:
        raise ValueError("Missing ELEVEN_LAB_API_KEY or ELEVENLABS_API_KEY in environment variables.")
    return key


def synthesize_text(text: str, out_path: pathlib.Path, voice_id: str = DEFAULT_VOICE_ID, force: bool = False) -> bool:
    """Synthesize voiceover line with caching and retries."""
    if out_path.exists() and out_path.stat().st_size > 1000 and not force:
        print(f"  [Cached] {out_path.name}")
        return True

    api_key = get_api_key()
    url = f"https://api.elevenlabs.io/v1/text-to-speech/{voice_id}"

    headers = {
        "xi-api-key": api_key,
        "Content-Type": "application/json",
        "Accept": "audio/mpeg",
    }
    payload = {
        "text": text,
        "model_id": DEFAULT_MODEL_ID,
        "voice_settings": {
            "stability": 0.55,
            "similarity_boost": 0.80,
            "style": 0.0,
            "use_speaker_boost": True,
        },
    }

    max_retries = 3
    for attempt in range(1, max_retries + 1):
        try:
            res = requests.post(url, headers=headers, json=payload, timeout=30)
            if res.status_code == 200:
                with open(out_path, "wb") as f:
                    f.write(res.content)
                size_kb = out_path.stat().st_size // 1024
                print(f"  [Generated] {out_path.name} ({size_kb} KB)")
                return True
            elif res.status_code == 429:
                wait_sec = attempt * 5
                print(f"  [Rate Limit] Waiting {wait_sec}s before retry {attempt}/{max_retries}...")
                time.sleep(wait_sec)
            else:
                print(f"  [API Error {res.status_code}] {res.text[:200]}")
                time.sleep(2)
        except Exception as e:
            print(f"  [Network Error] {e} (attempt {attempt}/{max_retries})")
            time.sleep(3)

    return False


def main():
    parser = argparse.ArgumentParser(description="ElevenLabs Voiceover Batch Synthesizer")
    parser.add_argument("--limit", type=int, default=0, help="Limit number of scenes to synthesize")
    parser.add_argument("--all", action="store_true", help="Synthesize all 64 scenes")
    parser.add_argument("--force", action="store_true", help="Force re-generation of existing files")
    args = parser.parse_args()

    if not MANIFEST_PATH.exists():
        print(f"Error: Manifest not found at {MANIFEST_PATH}. Run extract_scene_narration.py first.")
        sys.exit(1)

    with open(MANIFEST_PATH, "r", encoding="utf-8") as f:
        manifest = json.load(f)

    limit = args.limit if args.limit > 0 else (len(manifest) if args.all else len(manifest))
    items_to_process = manifest[:limit]

    print("=" * 60)
    print(f"ELEVENLABS VOICEOVER SYNTHESIZER: {len(items_to_process)} SCENES")
    print(f"Voice: George ({DEFAULT_VOICE_ID}) | Model: {DEFAULT_MODEL_ID}")
    print("=" * 60)

    success_count = 0
    t0 = time.time()

    for idx, item in enumerate(items_to_process, 1):
        act_id = item["act_id"]
        scene_idx = item["scene_idx"]
        text = item["text"]
        out_name = f"{act_id}_S{scene_idx:02d}_vo.mp3"
        out_path = VO_DIR / out_name

        print(f"[{idx}/{len(items_to_process)}] {act_id} Scene {scene_idx:02d} ({item['word_count']} words): \"{text[:50]}...\"")
        if synthesize_text(text, out_path, force=args.force):
            success_count += 1

        # Gentle throttle between API requests (0.4s)
        time.sleep(0.4)

    t1 = time.time()
    print("=" * 60)
    print(f"Completed: {success_count}/{len(items_to_process)} voiceover clips ready in {t1 - t0:.1f}s")
    print(f"Output directory: {VO_DIR}")
    print("=" * 60)


if __name__ == "__main__":
    main()
