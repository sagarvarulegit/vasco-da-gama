"""Multi-stem audio mixer with dynamic sidechain ducking and broadcast loudness.

Takes cached 1080p clips and mixes 3 audio stems:
1. Stem 1 (Voiceover): ElevenLabs British narrator line, offset by 1.0s.
2. Stem 2 (Music): Regional period suite with sidechain ducking (-7 dB during speech).
3. Stem 3 (Foley): Environmental ambient bed (waves, wind, lived-in atmosphere).
Remuxes with existing 1080p video (-c:v copy) into production/exports/supercut_cache/.
"""

from __future__ import annotations

import argparse
import json
import os
import pathlib
import subprocess
import sys
import time

ROOT = pathlib.Path(r"C:\Sagar\Projects\vasco-da-gama")
CACHE_DIR = ROOT / "production" / "exports" / "supercut_cache"
VO_DIR = ROOT / "production" / "audio" / "voiceover"
MUSIC_DIR = ROOT / "production" / "audio" / "music"
MANIFEST_PATH = ROOT / "production" / "audio" / "narration_manifest.json"

# Act to Music Suite mapping
SUITE_MAP = {
    "ACT_I": MUSIC_DIR / "SUITE_1_LISBON_ATLANTIC.mp3",
    "ACT_II": MUSIC_DIR / "SUITE_1_LISBON_ATLANTIC.mp3",
    "ACT_III": MUSIC_DIR / "SUITE_2_CAPE_STORMS.mp3",
    "ACT_IV": MUSIC_DIR / "SUITE_3_SWAHILI_COAST.mp3",
    "ACT_V": MUSIC_DIR / "SUITE_3_SWAHILI_COAST.mp3",
    "ACT_VI": MUSIC_DIR / "SUITE_4_MONSOON_CALICUT.mp3",
    "ACT_VII": MUSIC_DIR / "SUITE_4_MONSOON_CALICUT.mp3",
    "ACT_VIII": MUSIC_DIR / "SUITE_5_CALICUT_AMBUSH.mp3",
}
MAP_BRIDGE = MUSIC_DIR / "MAP_BRIDGE.mp3"


def get_duration(p: pathlib.Path) -> float:
    cmd = ["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(p)]
    return float(subprocess.check_output(cmd).decode().strip())


def mix_scene(clip_path: pathlib.Path, vo_path: pathlib.Path, music_path: pathlib.Path, scene_idx: int):
    """Mix voiceover + music with sidechain ducking into clip."""
    dur = get_duration(clip_path)
    music_offset = (scene_idx - 1) * 9.5
    temp_out = clip_path.with_name(f"temp_{clip_path.name}")

    # Complex filter:
    # 1. Voiceover delayed by 1.0s
    # 2. Music sliced from suite
    # 3. Foley pink noise ambient
    # 4. Sidechain ducking of music by VO
    # 5. Loudness normalization to -20 LUFS
    vf_filt = (
        f"[1:a]adelay=1000|1000,apad=whole_dur={dur:.2f},volume=1.05[vo];"
        f"[2:a]atrim=start={music_offset:.2f}:duration={dur:.2f},asetpts=PTS-STARTPTS,volume=0.55[m_base];"
        f"anoisesrc=d={dur:.2f}:c=pink:r=48000,lowpass=f=200,volume=0.18[foley];"
        f"[m_base][vo]sidechaincompress=threshold=0.06:ratio=4.5:attack=250:release=550[ducked_m];"
        f"[ducked_m][vo][foley]amix=inputs=3:duration=first:dropout_transition=2,"
        f"loudnorm=I=-20:TP=-1.5:LRA=11[aout]"
    )

    cmd = [
        "ffmpeg", "-y",
        "-i", str(clip_path),
        "-i", str(vo_path),
        "-i", str(music_path),
        "-filter_complex", vf_filt,
        "-map", "0:v",
        "-map", "[aout]",
        "-c:v", "copy",
        "-c:a", "aac", "-b:a", "192k", "-ar", "48000", "-ac", "2",
        str(temp_out)
    ]
    res = subprocess.run(cmd, capture_output=True, text=True)
    if res.returncode != 0:
        raise RuntimeError(f"FFmpeg mixing failed on {clip_path.name}: {res.stderr[-400:]}")

    # Replace original cached clip
    temp_out.replace(clip_path)
    print(f"  [Scored & Voiced] {clip_path.name} ({dur:.1f}s)")


def mix_map_transition(trans_path: pathlib.Path):
    """Mix map transition clip with portolan navigational chords."""
    dur = get_duration(trans_path)
    temp_out = trans_path.with_name(f"temp_{trans_path.name}")

    vf_filt = (
        f"[1:a]atrim=start=0:duration={dur:.2f},asetpts=PTS-STARTPTS,volume=0.70,"
        f"afade=t=in:st=0:d=0.5,afade=t=out:st={dur-0.6:.1f}:d=0.6[m_bridge];"
        f"anoisesrc=d={dur:.2f}:c=pink:r=48000,lowpass=f=260,volume=0.18[breeze];"
        f"[m_bridge][breeze]amix=inputs=2:duration=first,"
        f"loudnorm=I=-20:TP=-1.5:LRA=11[aout]"
    )
    cmd = [
        "ffmpeg", "-y",
        "-i", str(trans_path),
        "-i", str(MAP_BRIDGE),
        "-filter_complex", vf_filt,
        "-map", "0:v",
        "-map", "[aout]",
        "-c:v", "copy",
        "-c:a", "aac", "-b:a", "192k", "-ar", "48000", "-ac", "2",
        str(temp_out)
    ]
    res = subprocess.run(cmd, capture_output=True, text=True)
    if res.returncode != 0:
        raise RuntimeError(f"Map mix failed on {trans_path.name}: {res.stderr[-400:]}")

    temp_out.replace(trans_path)
    print(f"  [Scored Map] {trans_path.name} ({dur:.1f}s)")


def main():
    parser = argparse.ArgumentParser(description="Multi-Stem Audio Mixer & Scorer")
    parser.add_argument("--limit", type=int, default=0, help="Limit number of scenes to mix")
    parser.add_argument("--all", action="store_true", help="Mix all 64 scenes and 7 maps")
    args = parser.parse_args()

    with open(MANIFEST_PATH, "r", encoding="utf-8") as f:
        manifest = json.load(f)

    limit = args.limit if args.limit > 0 else (len(manifest) if args.all else len(manifest))
    scenes_to_process = manifest[:limit]

    print("=" * 60)
    print(f"MULTI-STEM AUDIO MIXER & SCORER: {len(scenes_to_process)} SCENES")
    print("Stem 1: ElevenLabs Voiceover | Stem 2: Historical Suite | Stem 3: Foley")
    print("=" * 60)

    t0 = time.time()
    clip_counter = 1

    for item in scenes_to_process:
        act_id = item["act_id"]
        scene_idx = item["scene_idx"]

        # Match cached clip filename: e.g. 001_ACT_I_S01.mp4
        clip_name = f"{clip_counter:03d}_{act_id}_S{scene_idx:02d}.mp4"
        clip_path = CACHE_DIR / clip_name
        vo_path = VO_DIR / f"{act_id}_S{scene_idx:02d}_vo.mp3"
        music_path = SUITE_MAP[act_id]

        if not clip_path.exists():
            print(f"Warning: {clip_path.name} not found in cache. Skipping.")
            clip_counter += 1
            continue

        if not vo_path.exists():
            print(f"Warning: Voiceover {vo_path.name} not generated yet. Skipping.")
            clip_counter += 1
            continue

        mix_scene(clip_path, vo_path, music_path, scene_idx)
        clip_counter += 1

        # Check if next was a map transition (scenes 8 of acts I..VII)
        if scene_idx == 8 and act_id != "ACT_VIII":
            map_name = f"{clip_counter:03d}_{act_id}_MAP.mp4"
            map_path = CACHE_DIR / map_name
            if map_path.exists() and args.all:
                mix_map_transition(map_path)
            clip_counter += 1

    t1 = time.time()
    print("=" * 60)
    print(f"Mixing completed in {t1 - t0:.1f}s!")
    print("=" * 60)


if __name__ == "__main__":
    main()
