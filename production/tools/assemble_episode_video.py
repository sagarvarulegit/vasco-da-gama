#!/usr/bin/env python3
"""Assemble Chapter 1 Episode 2 motion video and individual scene clips.

Generates high-resolution, cinema-grade motion clips for the 8 canonical locked stills
under MASTER_STYLE_02, applies specific camera kinematics per blueprint directions,
and stitches them with smooth cross-dissolves and an authentic maritime soundscape into:
    videos/episode-02/Vasco-Da-Gama-CH01-EP02-v1.mp4
"""

from __future__ import annotations

import os
import pathlib
import subprocess
import sys

PROJECT_ROOT = pathlib.Path(__file__).resolve().parent.parent.parent
IMAGES_DIR = PROJECT_ROOT / "images" / "episode-02"
VIDEOS_DIR = PROJECT_ROOT / "videos" / "episode-02"

SCENES = [
    {
        "id": "CH01-EP02-S01",
        "image": "CH01-EP02-S01-v2.png",
        "title": "Open Water After Lisbon",
        "duration": 10.0,
        # Slow forward push-in into open Atlantic swell
        "zoompan": "zoompan=z='min(zoom+0.0007,1.22)':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d=300:s=1920x1080:fps=30",
        "voiceover": "Past the familiar Iberian coast, the four ships found the ocean winds and settled into the long rhythm of open water.",
    },
    {
        "id": "CH01-EP02-S02",
        "image": "CH01-EP02-S02-v1.png",
        "title": "Fog and Separation",
        "duration": 10.0,
        # Slow lateral pan through dense Atlantic fog
        "zoompan": "zoompan=z='1.15':x='if(eq(on,1),0,min(x+1.5,iw-iw/zoom))':y='ih/2-(ih/zoom/2)':d=300:s=1920x1080:fps=30",
        "voiceover": "Off the African coast, dense fog swallowed the horizon. For days, the fleet lost sight of itself in the grey Atlantic mist.",
    },
    {
        "id": "CH01-EP02-S03",
        "image": "CH01-EP02-S03-v2.png",
        "title": "Sal and Reunion",
        "duration": 10.0,
        # Gentle horizontal drift across calm water off Sal
        "zoompan": "zoompan=z='1.12':x='if(eq(on,1),iw-iw/zoom,max(x-1.2,0))':y='ih/2-(ih/zoom/2)':d=300:s=1920x1080:fps=30",
        "voiceover": "Near the island of Sal, sails reappeared through the heat. The separated vessels found one another again across the calm.",
    },
    {
        "id": "CH01-EP02-S04",
        "image": "CH01-EP02-S04-v1.png",
        "title": "São Thiago Stores and Repairs",
        "duration": 10.0,
        # Slow push toward loading harbor labor and yard refit
        "zoompan": "zoompan=z='min(zoom+0.0006,1.20)':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)+0.05*ih':d=300:s=1920x1080:fps=30",
        "voiceover": "At São Thiago, the fleet took its final provisions: meat, fresh water, firewood, and fresh timber to repair strained spars.",
    },
    {
        "id": "CH01-EP02-S05",
        "image": "CH01-EP02-S05-v2.png",
        "title": "The Broken Main Yard",
        "duration": 10.0,
        # Dynamic swell motion on the broken main yard
        "zoompan": "zoompan=z='min(zoom+0.0005,1.18)':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)+sin(on/12)*15':d=300:s=1920x1080:fps=30",
        "voiceover": "Two hundred leagues into the southern ocean, the captain-major’s main yard snapped. The armada halted in open water while the spar was secured.",
    },
    {
        "id": "CH01-EP02-S06",
        "image": "CH01-EP02-S06-v2.png",
        "title": "Birds and Whale in the Open Sea",
        "duration": 10.0,
        # Expansive pull-out revealing the vast sea and whale
        "zoompan": "zoompan=z='if(eq(on,1),1.24,max(1.04,zoom-0.00065))':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d=300:s=1920x1080:fps=30",
        "voiceover": "Far from any known coast, the ocean revealed its own life: migrating birds flying southeast, and whales rising in the deep swell.",
    },
    {
        "id": "CH01-EP02-S07",
        "image": "CH01-EP02-S07-v1.png",
        "title": "Signs of Land",
        "duration": 10.0,
        # Subtle upward tilt from floating weed up to crew on deck
        "zoompan": "zoompan=z='1.16':x='iw/2-(iw/zoom/2)':y='if(eq(on,1),ih-ih/zoom,max(0,y-1.1))':d=300:s=1920x1080:fps=30",
        "voiceover": "By early November, floating weed and coastal birds appeared in the water—the first signs that the vast South Atlantic arc had brought them back toward land.",
    },
    {
        "id": "CH01-EP02-S08",
        "image": "CH01-EP02-S08-v1.png",
        "title": "Landfall Before St Helena",
        "duration": 10.0,
        # Waterline forward glide following sounding boat toward shore
        "zoompan": "zoompan=z='min(zoom+0.00065,1.20)':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)+0.04*ih':d=300:s=1920x1080:fps=30",
        "voiceover": "On 4 November, ninety-six days after leaving Cape Verde, they sighted land. The armada dropped anchor in the Bay of St Helena to mend sails and prepare for the Cape.",
    },
]


def generate_motion_clip(scene: dict, output_path: pathlib.Path) -> None:
    img_path = IMAGES_DIR / scene["image"]
    if not img_path.exists():
        raise FileNotFoundError(f"Missing input image: {img_path}")

    # Upscale to high-res before zoompan to ensure sub-pixel camera motion without jitter
    filter_complex = f"scale=3840:3840,{scene['zoompan']}"

    cmd = [
        "ffmpeg",
        "-y",
        "-loop",
        "1",
        "-i",
        str(img_path),
        "-vf",
        filter_complex,
        "-c:v",
        "libx264",
        "-preset",
        "medium",
        "-crf",
        "18",
        "-pix_fmt",
        "yuv420p",
        "-t",
        str(scene["duration"]),
        "-r",
        "30",
        str(output_path),
    ]

    print(f"Generating motion clip: {output_path.name}...")
    res = subprocess.run(cmd, capture_output=True, text=True)
    if res.returncode != 0:
        print(f"Error generating {output_path.name}:\n{res.stderr}", file=sys.stderr)
        raise RuntimeError(f"FFmpeg failed on {output_path.name}")


def assemble_episode_video(clip_paths: list[pathlib.Path], output_path: pathlib.Path) -> None:
    # 8 clips with 1.2s crossfade between each
    # Total duration = 8 * 10s - 7 * 1.2s = 80 - 8.4 = 71.6 seconds
    num_clips = len(clip_paths)
    transition_duration = 1.2
    clip_duration = 10.0

    # Build ffmpeg input arguments
    inputs = []
    for p in clip_paths:
        inputs.extend(["-i", str(p)])

    # Build video filtergraph with xfade
    filter_parts = []
    last_v = "[0:v]"
    current_offset = clip_duration - transition_duration

    for i in range(1, num_clips):
        next_v = f"[{i}:v]"
        out_v = f"[v{i}]" if i < num_clips - 1 else "[vout]"
        filter_parts.append(
            f"{last_v}{next_v}xfade=transition=fade:duration={transition_duration}:offset={current_offset:.2f}{out_v}"
        )
        last_v = out_v
        current_offset += clip_duration - transition_duration

    total_video_duration = current_offset + transition_duration

    # Audio synthesis: layered oceanic maritime bed (rolling deep sea swell + wind in rigging + subtle low string drone)
    audio_filter = (
        f"anoisesrc=d={total_video_duration:.2f}:c=pink:r=44100,lowpass=f=220,volume=0.45[swell];"
        f"anoisesrc=d={total_video_duration:.2f}:c=white:r=44100,bandpass=f=1200:w=800,volume=0.08[wind];"
        f"aevalsrc='0.04*sin(2*PI*55*t)+0.03*sin(2*PI*110*t)+0.02*sin(2*PI*165*t)':d={total_video_duration:.2f}:s=44100[drone];"
        f"[swell][wind][drone]amix=inputs=3:dropout_transition=2,afade=t=in:st=0:d=2.0,afade=t=out:st={total_video_duration-2.5:.2f}:d=2.5[aout]"
    )

    full_filtergraph = ";".join(filter_parts) + ";" + audio_filter

    cmd = [
        "ffmpeg",
        "-y",
        *inputs,
        "-filter_complex",
        full_filtergraph,
        "-map",
        "[vout]",
        "-map",
        "[aout]",
        "-c:v",
        "libx264",
        "-preset",
        "slow",
        "-crf",
        "18",
        "-pix_fmt",
        "yuv420p",
        "-c:a",
        "aac",
        "-b:a",
        "192k",
        "-movflags",
        "+faststart",
        str(output_path),
    ]

    print(f"Stitching episode video: {output_path.name} (Duration ~{total_video_duration:.1f}s)...")
    res = subprocess.run(cmd, capture_output=True, text=True)
    if res.returncode != 0:
        print(f"Error assembling master episode video:\n{res.stderr}", file=sys.stderr)
        raise RuntimeError("FFmpeg failed on master assembly")


def main() -> int:
    VIDEOS_DIR.mkdir(parents=True, exist_ok=True)
    clip_paths = []

    for idx, scene in enumerate(SCENES, start=1):
        clip_name = f"CH01-EP02-S{idx:02d}-motion-v1.mp4"
        clip_path = VIDEOS_DIR / clip_name
        if not clip_path.exists() or clip_path.stat().st_size == 0:
            generate_motion_clip(scene, clip_path)
        else:
            print(f"Using existing motion clip: {clip_name} ({clip_path.stat().st_size} bytes)")
        clip_paths.append(clip_path)

    master_output = VIDEOS_DIR / "Vasco-Da-Gama-CH01-EP02-v1.mp4"
    assemble_episode_video(clip_paths, master_output)
    print(f"\nEpisode 2 video generation complete: {master_output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
