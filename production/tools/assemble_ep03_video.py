#!/usr/bin/env python3
"""Assemble Chapter 1 Episode 3 motion video and individual scene clips.

Generates high-resolution, cinema-grade motion clips for the 8 canonical locked stills (v2)
under MASTER_STYLE_02, applies specific camera kinematics per blueprint directions,
and stitches them with smooth cross-dissolves and an authentic maritime soundscape into:
    videos/episode-03/Vasco-Da-Gama-CH01-EP03-v1.mp4
"""

from __future__ import annotations

import pathlib
import subprocess
import sys

PROJECT_ROOT = pathlib.Path(__file__).resolve().parent.parent.parent
IMAGES_DIR = PROJECT_ROOT / "images" / "episode-03"
VIDEOS_DIR = PROJECT_ROOT / "videos" / "episode-03"

SCENES = [
    {
        "id": "CH01-EP03-S01",
        "image": "CH01-EP03-S01-v2.png",
        "title": "Careening and Wood Gathering at St Helena Bay",
        "duration": 10.0,
        # Lateral pan across beach camp and heeled ship
        "zoompan": "zoompan=z='1.15':x='if(eq(on,1),0,min(x+1.5,iw-iw/zoom))':y='ih/2-(ih/zoom/2)':d=300:s=1920x1080:fps=30",
        "voiceover": "Four months in the open ocean had rotted their hulls and pushed the crew to the brink of collapse. On the barren sands of St Helena Bay, they raced against time to scrape the rot before the Cape claimed them.",
    },
    {
        "id": "CH01-EP03-S02",
        "image": "CH01-EP03-S02-v2.png",
        "title": "First Encounter on the Strand",
        "duration": 10.0,
        # Slow dramatic push-in on the dunes standoff
        "zoompan": "zoompan=z='min(zoom+0.0007,1.22)':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d=300:s=1920x1080:fps=30",
        "voiceover": "In the silence of the dunes, two alien worlds stood face to face. With daggers concealed and spears at the ready, the first contact was forged in the glint of brass and glass.",
    },
    {
        "id": "CH01-EP03-S03",
        "image": "CH01-EP03-S03-v2.png",
        "title": "Skirmish on the Beach",
        "duration": 10.0,
        # Waterline surf track
        "zoompan": "zoompan=z='1.18':x='iw/2-(iw/zoom/2)':y='if(eq(on,1),ih-ih/zoom,max(0,y-1.2))':d=300:s=1920x1080:fps=30",
        "voiceover": "The fragile peace shattered into blood. From the dunes, a barrage of spears rained upon the shore—and as the longboat pushed into the churning surf, a horn-tipped spear struck the captain-major.",
    },
    {
        "id": "CH01-EP03-S04",
        "image": "CH01-EP03-S04-v2.png",
        "title": "Battling the Cape Headwinds",
        "duration": 10.0,
        # Dynamic violent roll and swell
        "zoompan": "zoompan=z='min(zoom+0.0006,1.20)':x='iw/2-(iw/zoom/2)+sin(on/10)*25':y='ih/2-(ih/zoom/2)+cos(on/8)*18':d=300:s=1920x1080:fps=30",
        "voiceover": "Off the edge of the known world, the ocean unleashed its fury. For six agonizing days, the four fragile hulls fought against the colossal swells of the Cape of Storms, where one mistake meant watery death.",
    },
    {
        "id": "CH01-EP03-S05",
        "image": "CH01-EP03-S05-v2.png",
        "title": "Rounding the Cape of Good Hope",
        "duration": 10.0,
        # Majestic forward glide past the cliffs
        "zoompan": "zoompan=z='min(zoom+0.00065,1.22)':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)+0.03*ih':d=300:s=1920x1080:fps=30",
        "voiceover": "On Wednesday, 22 November, the impossible barrier broke. In a flood of golden light, the armada doubled the legendary Cape—the Atlantic was behind them, and the Indian Ocean lay open.",
    },
    {
        "id": "CH01-EP03-S06",
        "image": "CH01-EP03-S06-v2.png",
        "title": "Music and Trade at Mossel Bay",
        "duration": 10.0,
        # Slow horizontal sweep across dancing pastoralists
        "zoompan": "zoompan=z='1.14':x='if(eq(on,1),iw-iw/zoom,max(x-1.3,0))':y='ih/2-(ih/zoom/2)':d=300:s=1920x1080:fps=30",
        "voiceover": "At Mossel Bay, the tension of the voyage dissolved into music. To the hypnotic rhythm of four-holed reed flutes, Portuguese mariners and Khoikhoi pastoralists danced together on the sand in an extraordinary moment of shared humanity.",
    },
    {
        "id": "CH01-EP03-S07",
        "image": "CH01-EP03-S07-v2.png",
        "title": "Breaking Up the Supply Ship",
        "duration": 10.0,
        # Atmospheric dusk pull-out from the burning wreck
        "zoompan": "zoompan=z='if(eq(on,1),1.24,max(1.05,zoom-0.00065))':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d=300:s=1920x1080:fps=30",
        "voiceover": "To survive the unknown ahead, a sacrifice was demanded. Stripped to her bones, the supply ship was set ablaze on the sands—burning the armada’s lifeline and leaving three lone ships with no choice but victory or death.",
    },
    {
        "id": "CH01-EP03-S08",
        "image": "CH01-EP03-S08-v2.png",
        "title": "Departure into the Unknown East",
        "duration": 10.0,
        # Epic forward glide into the sunrise
        "zoompan": "zoompan=z='min(zoom+0.0007,1.24)':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)+0.04*ih':d=300:s=1920x1080:fps=30",
        "voiceover": "On 8 December, the three surviving ships weighed anchor and stood out to sea. Behind them lay Africa and the Atlantic. Ahead lay thousands of leagues of uncharted ocean, and the destiny of nations.",
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

    # Audio synthesis: layered oceanic maritime bed (rolling deep sea swell + Cape gale wind + harmonic modal strings & brass)
    audio_filter = (
        f"anoisesrc=d={total_video_duration:.2f}:c=pink:r=44100,lowpass=f=240,volume=0.45[swell];"
        f"anoisesrc=d={total_video_duration:.2f}:c=white:r=44100,bandpass=f=1400:w=900,volume=0.09[gale];"
        f"aevalsrc='0.05*sin(2*PI*65*t)+0.03*sin(2*PI*130*t)+0.02*sin(2*PI*195*t)+0.015*sin(2*PI*260*t)':d={total_video_duration:.2f}:s=44100[drone];"
        f"[swell][gale][drone]amix=inputs=3:dropout_transition=2,afade=t=in:st=0:d=2.0,afade=t=out:st={total_video_duration-2.5:.2f}:d=2.5[aout]"
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
        clip_name = f"CH01-EP03-S{idx:02d}-motion-v1.mp4"
        clip_path = VIDEOS_DIR / clip_name
        if not clip_path.exists() or clip_path.stat().st_size == 0:
            generate_motion_clip(scene, clip_path)
        else:
            print(f"Using existing motion clip: {clip_name} ({clip_path.stat().st_size} bytes)")
        clip_paths.append(clip_path)

    master_output = VIDEOS_DIR / "Vasco-Da-Gama-CH01-EP03-v1.mp4"
    assemble_episode_video(clip_paths, master_output)
    print(f"\nEpisode 3 video generation complete: {master_output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
