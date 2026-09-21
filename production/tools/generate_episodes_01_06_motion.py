#!/usr/bin/env python3
"""Batch generate high-resolution cinema-grade motion clips for Episodes 1 through 6.

Transforms the 48 canonical locked stills under MASTER_STYLE_02 into 1080p 30fps
motion clips with dynamic camera kinematics (push, pan, swell, tilt) and an authentic
historical maritime audio atmosphere.
"""

from __future__ import annotations

import os
import pathlib
import subprocess
import sys
import time

PROJECT_ROOT = pathlib.Path(__file__).resolve().parent.parent.parent
CHAPTER_DIR = PROJECT_ROOT / "chapters" / "chapter-01-first-voyage"

EPISODES = [
    {
        "id": "EP01",
        "folder": "episode-01-lisbon",
        "prefix": "CH01",
        "ambience": "coastal",
    },
    {
        "id": "EP02",
        "folder": "episode-02-atlantic",
        "prefix": "CH01-EP02",
        "ambience": "deep_ocean",
    },
    {
        "id": "EP03",
        "folder": "episode-03-cape",
        "prefix": "CH01-EP03",
        "ambience": "stormy_cape",
    },
    {
        "id": "EP04",
        "folder": "episode-04-east-africa",
        "prefix": "CH01-EP04",
        "ambience": "tropical_coast",
    },
    {
        "id": "EP05",
        "folder": "episode-05-mombasa-malindi",
        "prefix": "CH01-EP05",
        "ambience": "swahili_port",
    },
    {
        "id": "EP06",
        "folder": "episode-06-monsoon-crossing",
        "prefix": "CH01-EP06",
        "ambience": "monsoon_ocean",
    },
]

# 8 Kinematic camera movements cycling through scene types
KINEMATICS = [
    # S01: Slow dramatic push-in to focal subject
    "zoompan=z='min(zoom+0.0007,1.22)':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d=300:s=1920x1080:fps=30",
    # S02: Horizontal lateral drift (left to right)
    "zoompan=z='1.15':x='if(eq(on,1),0,min(x+1.5,iw-iw/zoom))':y='ih/2-(ih/zoom/2)':d=300:s=1920x1080:fps=30",
    # S03: Upward tilt from waterline/deck up to horizon
    "zoompan=z='1.16':x='iw/2-(iw/zoom/2)':y='if(eq(on,1),ih-ih/zoom,max(0,y-1.2))':d=300:s=1920x1080:fps=30",
    # S04: Ocean swell roll and heave
    "zoompan=z='min(zoom+0.0006,1.20)':x='iw/2-(iw/zoom/2)+sin(on/10)*20':y='ih/2-(ih/zoom/2)+cos(on/8)*15':d=300:s=1920x1080:fps=30",
    # S05: Expansive pull-out revealing grand scale
    "zoompan=z='if(eq(on,1),1.24,max(1.04,zoom-0.00065))':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d=300:s=1920x1080:fps=30",
    # S06: Reverse horizontal pan (right to left)
    "zoompan=z='1.14':x='if(eq(on,1),iw-iw/zoom,max(0,x-1.3))':y='ih/2-(ih/zoom/2)':d=300:s=1920x1080:fps=30",
    # S07: Low waterline forward glide
    "zoompan=z='min(zoom+0.00065,1.20)':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)+0.04*ih':d=300:s=1920x1080:fps=30",
    # S08: Centered push-in with subtle breathing motion
    "zoompan=z='min(zoom+0.0008,1.25)':x='iw/2-(iw/zoom/2)+sin(on/12)*10':y='ih/2-(ih/zoom/2)':d=300:s=1920x1080:fps=30",
]


def get_audio_filter(ambience_type: str, duration: float = 10.0) -> str:
    """Generate layered ambient audio bed based on chapter environment."""
    if ambience_type == "coastal":
        return (
            f"anoisesrc=d={duration:.2f}:c=pink:r=48000,lowpass=f=350,volume=0.35[surf];"
            f"anoisesrc=d={duration:.2f}:c=white:r=48000,bandpass=f=2000:w=1200,volume=0.06[breeze];"
            f"aevalsrc='0.03*sin(2*PI*110*t)+0.02*sin(2*PI*220*t)':d={duration:.2f}:s=48000[drone];"
            f"[surf][breeze][drone]amix=inputs=3,afade=t=in:st=0:d=1.0,afade=t=out:st={duration-1.0:.2f}:d=1.0[aout]"
        )
    elif ambience_type == "deep_ocean":
        return (
            f"anoisesrc=d={duration:.2f}:c=pink:r=48000,lowpass=f=200,volume=0.45[swell];"
            f"anoisesrc=d={duration:.2f}:c=white:r=48000,bandpass=f=1000:w=600,volume=0.08[wind];"
            f"aevalsrc='0.04*sin(2*PI*55*t)+0.02*sin(2*PI*165*t)':d={duration:.2f}:s=48000[drone];"
            f"[swell][wind][drone]amix=inputs=3,afade=t=in:st=0:d=1.0,afade=t=out:st={duration-1.0:.2f}:d=1.0[aout]"
        )
    elif ambience_type == "stormy_cape":
        return (
            f"anoisesrc=d={duration:.2f}:c=pink:r=48000,lowpass=f=180,volume=0.60[surge];"
            f"anoisesrc=d={duration:.2f}:c=white:r=48000,bandpass=f=1400:w=900,volume=0.15[gale];"
            f"aevalsrc='0.05*sin(2*PI*45*t)+0.03*sin(2*PI*90*t)':d={duration:.2f}:s=48000[bass];"
            f"[surge][gale][bass]amix=inputs=3,afade=t=in:st=0:d=1.0,afade=t=out:st={duration-1.0:.2f}:d=1.0[aout]"
        )
    else:  # tropical / monsoon
        return (
            f"anoisesrc=d={duration:.2f}:c=pink:r=48000,lowpass=f=260,volume=0.40[water];"
            f"anoisesrc=d={duration:.2f}:c=white:r=48000,bandpass=f=1600:w=1000,volume=0.10[monsoon];"
            f"aevalsrc='0.04*sin(2*PI*65*t)+0.02*sin(2*PI*130*t)':d={duration:.2f}:s=48000[drone];"
            f"[water][monsoon][drone]amix=inputs=3,afade=t=in:st=0:d=1.0,afade=t=out:st={duration-1.0:.2f}:d=1.0[aout]"
        )


def find_scene_image(img_dir: pathlib.Path, prefix: str, scene_idx: int) -> pathlib.Path | None:
    """Find the canonical v1 still for this scene."""
    patterns = [
        f"{prefix}-S{scene_idx:02d}-v1.png",
        f"{prefix}-S{scene_idx:02d}.png",
        f"CH01-S{scene_idx:02d}-v1.png",
        f"CH01-S{scene_idx:02d}.png",
        f"*S{scene_idx:02d}*v1.png",
        f"*S{scene_idx:02d}*.png",
    ]
    for pat in patterns:
        matches = list(img_dir.glob(pat))
        if matches:
            # Sort to prefer v1
            matches.sort(key=lambda p: (0 if "v1" in p.name else 1, p.name))
            return matches[0]
    return None


def generate_motion_clip(img_path: pathlib.Path, out_path: pathlib.Path, zoompan: str, ambience: str) -> bool:
    """Render a single 10.0s 1080p motion clip with audio."""
    duration = 10.0
    audio_filt = get_audio_filter(ambience, duration)
    video_filt = f"scale=2560:2560,{zoompan}"

    cmd = [
        "ffmpeg", "-y",
        "-loop", "1", "-i", str(img_path),
        "-filter_complex", f"[0:v]{video_filt}[v];{audio_filt}",
        "-map", "[v]", "-map", "[aout]",
        "-c:v", "libx264", "-preset", "fast", "-crf", "20",
        "-pix_fmt", "yuv420p",
        "-c:a", "aac", "-b:a", "192k", "-ar", "48000",
        "-t", str(duration), "-r", "30",
        str(out_path)
    ]
    res = subprocess.run(cmd, capture_output=True, text=True)
    if res.returncode != 0:
        print(f"Error rendering {out_path.name}:\n{res.stderr[-300:]}", file=sys.stderr)
        return False
    return True


def main():
    print("=" * 60)
    print("BATCH GENERATING MOTION CLIPS FOR EPISODES 1 THROUGH 6")
    print("=" * 60)

    total_scenes = 0
    generated_count = 0
    t_start = time.time()

    for ep in EPISODES:
        ep_dir = CHAPTER_DIR / ep["folder"]
        img_dir = ep_dir / "images"
        vid_dir = ep_dir / "videos"
        vid_dir.mkdir(parents=True, exist_ok=True)

        print(f"\nProcessing {ep['folder']}...")

        for s_idx in range(1, 9):
            total_scenes += 1
            out_clip = vid_dir / f"{ep['prefix']}-S{s_idx:02d}-motion-v1.mp4"

            if out_clip.exists() and out_clip.stat().st_size > 500000:
                print(f"  [OK: Exists] S{s_idx:02d}: {out_clip.name} ({out_clip.stat().st_size // 1024} KB)")
                continue

            img_file = find_scene_image(img_dir, ep["prefix"], s_idx)
            if not img_file:
                print(f"  [MISSING IMAGE] S{s_idx:02d}: No image found in {img_dir}", file=sys.stderr)
                continue

            zoompan = KINEMATICS[(s_idx - 1) % len(KINEMATICS)]
            print(f"  [Rendering] S{s_idx:02d} from {img_file.name} -> {out_clip.name}...")
            ok = generate_motion_clip(img_file, out_clip, zoompan, ep["ambience"])
            if ok:
                generated_count += 1
                print(f"    -> Done ({out_clip.stat().st_size // 1024} KB)")

    elapsed = time.time() - t_start
    print(f"\n{'=' * 60}")
    print(f"Batch generation completed: {generated_count} clips rendered in {elapsed:.1f}s")
    print(f"Total verified scenes: {total_scenes}/48 across Episodes 1–6")
    print("=" * 60)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
