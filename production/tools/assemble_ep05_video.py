#!/usr/bin/env python3
"""Assemble Chapter 1 Episode 5 motion video and individual scene clips.

Generates high-resolution, cinema-grade motion clips for the 8 canonical locked stills (v1)
under MASTER_STYLE_02, applies specific camera kinematics per blueprint directions,
and stitches them with smooth cross-dissolves and an authentic Indian Ocean maritime soundscape into:
    videos/episode-05/Vasco-Da-Gama-CH01-EP05-v1.mp4
"""

from __future__ import annotations

import pathlib
import subprocess
import sys

PROJECT_ROOT = pathlib.Path(__file__).resolve().parent.parent.parent
IMAGES_DIR = PROJECT_ROOT / "chapters" / "chapter-01-first-voyage" / "episode-05-mombasa-malindi" / "images"
VIDEOS_DIR = PROJECT_ROOT / "chapters" / "chapter-01-first-voyage" / "episode-05-mombasa-malindi" / "videos"

SCENES = [
    {
        "id": "CH01-EP05-S01",
        "image": "CH01-EP05-S01-v1.png",
        "title": "Grounded on the Shoals of São Rafael",
        "duration": 10.0,
        "zoompan": "zoompan=z='min(zoom+0.0006,1.18)':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)+0.04*ih':d=300:s=1920x1080:fps=30",
        "voiceover": "On 5 April 1498, disaster struck the coral shoals. São Rafael grounded on the jagged reef, forcing mariners to haul heavy kedge lines waist-deep in turquoise shallows.",
    },
    {
        "id": "CH01-EP05-S02",
        "image": "CH01-EP05-S02-v1.png",
        "title": "The Roadstead of Mombasa",
        "duration": 10.0,
        "zoompan": "zoompan=z='1.15':x='if(eq(on,1),0,min(x+1.5,iw-iw/zoom))':y='ih/2-(ih/zoom/2)':d=300:s=1920x1080:fps=30",
        "voiceover": "Two days later, the white coral-stone ramparts of Mombasa rose against the sky. Across the water, Swahili zambucos brought gifts of oranges—and the first whispers of betrayal.",
    },
    {
        "id": "CH01-EP05-S03",
        "image": "CH01-EP05-S03-v1.png",
        "title": "The Gujarati Merchant's Shrine",
        "duration": 10.0,
        "zoompan": "zoompan=z='min(zoom+0.0007,1.22)':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d=300:s=1920x1080:fps=30",
        "voiceover": "Inside Mombasa, Portuguese emissaries entered a Gujarati merchant's house. Seeing sweet sandalwood incense burning before a decorated icon, they mistook Indian devotion for Christian faith.",
    },
    {
        "id": "CH01-EP05-S04",
        "image": "CH01-EP05-S04-v1.png",
        "title": "Chaos at the Harbor Mouth",
        "duration": 10.0,
        "zoompan": "zoompan=z='min(zoom+0.0008,1.25)':x='iw/2-(iw/zoom/2)+sin(on/8)*20':y='ih/2-(ih/zoom/2)+cos(on/6)*15':d=300:s=1920x1080:fps=30",
        "voiceover": "10 April: As the flagship neared the harbor shoals, panic erupted. Swahili pilots leaped into the sea as iron anchors plunged into the churning breakers, narrowly escaping destruction.",
    },
    {
        "id": "CH01-EP05-S05",
        "image": "CH01-EP05-S05-v1.png",
        "title": "Midnight Interrogation by Brazier Glow",
        "duration": 10.0,
        "zoompan": "zoompan=z='1.16':x='iw/2-(iw/zoom/2)':y='if(eq(on,1),ih-ih/zoom,max(0,y-1.0))':d=300:s=1920x1080:fps=30",
        "voiceover": "Under cover of darkness, Vasco da Gama extracted the truth. By the orange glow of a roaring deck brazier, captive pilots confessed: the authorities of Mombasa planned to massacre the fleet.",
    },
    {
        "id": "CH01-EP05-S06",
        "image": "CH01-EP05-S06-v1.png",
        "title": "Arrival at Malindi on Easter Sunday",
        "duration": 10.0,
        "zoompan": "zoompan=z='1.12':x='if(eq(on,1),iw-iw/zoom,max(x-1.2,0))':y='ih/2-(ih/zoom/2)':d=300:s=1920x1080:fps=30",
        "voiceover": "Fleeing Mombasa on Easter Sunday, the battered fleet anchored off Malindi. Here, where white stone houses met golden sands, the Sultan welcomed them with green ginger and peace.",
    },
    {
        "id": "CH01-EP05-S07",
        "image": "CH01-EP05-S07-v1.png",
        "title": "The Water Summit with the Sultan",
        "duration": 10.0,
        "zoompan": "zoompan=z='min(zoom+0.0005,1.16)':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d=300:s=1920x1080:fps=30",
        "voiceover": "In the lagoon, a historic summit took place between royal barges. Carved ivory horns sounded across the waves as Vasco da Gama bowed with hand on heart, securing a true ally in the East.",
    },
    {
        "id": "CH01-EP05-S08",
        "image": "CH01-EP05-S08-v1.png",
        "title": "The Pilot of the Stars",
        "duration": 10.0,
        "zoompan": "zoompan=z='min(zoom+0.0007,1.22)':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)-0.03*ih':d=300:s=1920x1080:fps=30",
        "voiceover": "24 April 1498: On the quarterdeck, the Gujarati pilot Kanji Malam raised his wooden kamal to the sky, sighting the stars and pointing east. The sprint across the Indian Ocean had begun.",
    },
]


def generate_motion_clip(scene: dict, output_path: pathlib.Path) -> None:
    img_path = IMAGES_DIR / scene["image"]
    if not img_path.exists():
        raise FileNotFoundError(f"Missing image: {img_path}")

    cmd = [
        "ffmpeg",
        "-y",
        "-loop",
        "1",
        "-i",
        str(img_path),
        "-vf",
        f"scale=2560x1440,{scene['zoompan']}",
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
    num_clips = len(clip_paths)
    transition_duration = 1.2
    clip_duration = 10.0

    inputs = []
    for p in clip_paths:
        inputs.extend(["-i", str(p)])

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

    # Audio synthesis: Indian Ocean trade winds + tropical coastal surf + exotic modal drone & bells
    audio_filter = (
        f"anoisesrc=d={total_video_duration:.2f}:c=pink:r=44100,lowpass=f=260,volume=0.40[surf];"
        f"anoisesrc=d={total_video_duration:.2f}:c=white:r=44100,bandpass=f=1200:w=800,volume=0.08[wind];"
        f"aevalsrc='0.04*sin(2*PI*73.4*t)+0.03*sin(2*PI*110*t)+0.02*sin(2*PI*146.8*t)+0.015*sin(2*PI*220*t)':d={total_video_duration:.2f}:s=44100[drone];"
        f"[surf][wind][drone]amix=inputs=3:dropout_transition=2,afade=t=in:st=0:d=2.0,afade=t=out:st={total_video_duration-2.5:.2f}:d=2.5[aout]"
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
        clip_name = f"CH01-EP05-S{idx:02d}-motion-v1.mp4"
        clip_path = VIDEOS_DIR / clip_name
        if not clip_path.exists() or clip_path.stat().st_size == 0:
            generate_motion_clip(scene, clip_path)
        else:
            print(f"Using existing motion clip: {clip_name} ({clip_path.stat().st_size} bytes)")
        clip_paths.append(clip_path)

    master_output = VIDEOS_DIR / "Vasco-Da-Gama-CH01-EP05-v1.mp4"
    assemble_episode_video(clip_paths, master_output)
    print(f"\nEpisode 5 video generation complete: {master_output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
