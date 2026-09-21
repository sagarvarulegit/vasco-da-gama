"""Assemble the 14-Minute Master Supercut: Episodes 1 through 8.

The Outbound Voyage of Vasco da Gama (1497-1498).
Full documentary assembly with OpenMontage / FFmpeg.
- 71 scenes and map transitions + opening & outro
- 1920x1080 Full HD @ 30fps
- Broadcast EBU R128 loudness normalized audio (-20 LUFS)
- Elegant historical documentary lower-third Act titles
- High-speed concurrent normalization via ThreadPoolExecutor
"""

from __future__ import annotations

import concurrent.futures
import json
import os
import pathlib
import subprocess
import sys
import time
from PIL import Image, ImageDraw, ImageFont

# Root workspace
ROOT = pathlib.Path(r"C:\Sagar\Projects\vasco-da-gama")
CACHE_DIR = ROOT / "production" / "exports" / "supercut_cache"
OVERLAYS_DIR = ROOT / "production" / "exports" / "overlays"
OUTPUT_DIR = ROOT / "production" / "exports"
MASTER_OUTPUT = OUTPUT_DIR / "Vasco-da-Gama-Outbound-Voyage-Supercut-v1.mp4"

CACHE_DIR.mkdir(parents=True, exist_ok=True)
OVERLAYS_DIR.mkdir(parents=True, exist_ok=True)
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

GEORGIA_FONT = r"C:\Windows\Fonts\georgia.ttf"
GEORGIA_BOLD = r"C:\Windows\Fonts\georgiab.ttf" if os.path.exists(r"C:\Windows\Fonts\georgiab.ttf") else GEORGIA_FONT


# ----------------------------------------------------------------------
# 1. Overlay Graphic Generation
# ----------------------------------------------------------------------

def create_title_card(out_path: pathlib.Path):
    """Create master title card graphic."""
    if out_path.exists():
        return
    img = Image.new("RGBA", (1920, 1080), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    draw.rectangle([200, 260, 1720, 820], fill=(12, 16, 22, 225), outline=(212, 175, 55, 230), width=3)
    draw.rectangle([210, 270, 1710, 810], outline=(160, 130, 40, 120), width=1)

    f_super = ImageFont.truetype(GEORGIA_FONT, 28)
    f_title = ImageFont.truetype(GEORGIA_BOLD, 72)
    f_sub = ImageFont.truetype(GEORGIA_FONT, 34)
    f_quote = ImageFont.truetype(GEORGIA_FONT, 22)

    draw.text((960, 310), "HISTORICAL DOCUMENTARY SERIES", font=f_super, fill=(212, 175, 55, 255), anchor="mm")
    draw.text((960, 420), "VASCO DA GAMA", font=f_title, fill=(255, 255, 255, 255), anchor="mm")
    draw.line([(560, 485), (1360, 485)], fill=(212, 175, 55, 200), width=2)
    draw.text((960, 545), "THE OUTBOUND EXPEDITION TO INDIA (1497–1498)", font=f_sub, fill=(235, 235, 235, 255), anchor="mm")
    draw.text((960, 615), "EPISODES 1–8 COMPLETE STORY", font=f_sub, fill=(212, 175, 55, 255), anchor="mm")
    draw.text((960, 740), "Reconstructed from the Surviving First-Voyage Journal (Alvaro Velho / Ravenstein 1898)", 
              font=f_quote, fill=(180, 185, 195, 220), anchor="mm")

    img.save(out_path)
    print(f"Created master title card: {out_path.name}")


def create_lower_third(act_num: str, title: str, subtitle: str, out_path: pathlib.Path):
    """Create broadcast documentary lower-third overlay."""
    if out_path.exists():
        return
    img = Image.new("RGBA", (1920, 1080), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    x0, y0, x1, y1 = 100, 860, 1820, 990
    draw.rectangle([x0, y0, x1, y1], fill=(10, 14, 18, 215), outline=(212, 175, 55, 220), width=2)
    draw.rectangle([x0, y0, x0 + 12, y1], fill=(212, 175, 55, 255))

    f_act = ImageFont.truetype(GEORGIA_BOLD, 36)
    f_sub = ImageFont.truetype(GEORGIA_FONT, 24)

    draw.text((x0 + 40, y0 + 20), f"{act_num}: {title.upper()}", font=f_act, fill=(255, 255, 255, 255))
    draw.text((x0 + 40, y0 + 75), subtitle.upper(), font=f_sub, fill=(212, 175, 55, 255))

    img.save(out_path)
    print(f"Created lower-third: {out_path.name}")


def create_outro_card(out_path: pathlib.Path):
    """Create outro credit / subscribe card."""
    if out_path.exists():
        return
    img = Image.new("RGBA", (1920, 1080), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    draw.rectangle([240, 300, 1680, 780], fill=(10, 14, 18, 230), outline=(212, 175, 55, 220), width=3)
    draw.rectangle([250, 310, 1670, 770], outline=(160, 130, 40, 120), width=1)

    f_super = ImageFont.truetype(GEORGIA_FONT, 26)
    f_title = ImageFont.truetype(GEORGIA_BOLD, 54)
    f_sub = ImageFont.truetype(GEORGIA_FONT, 30)

    draw.text((960, 360), "END OF THE OUTBOUND EXPEDITION", font=f_super, fill=(212, 175, 55, 255), anchor="mm")
    draw.text((960, 460), "THE EXPEDITION REACHES CALICUT & ANJEDIVA", font=f_title, fill=(255, 255, 255, 255), anchor="mm")
    draw.line([(500, 520), (1420, 520)], fill=(212, 175, 55, 200), width=2)
    draw.text((960, 580), "NEXT: EPISODE 9 — THE DEADLY RETURN VOYAGE", font=f_sub, fill=(255, 255, 255, 255), anchor="mm")
    draw.text((960, 680), "Subscribe to witness the 84-Day Crossing of the Dead Ocean", font=f_sub, fill=(212, 175, 55, 255), anchor="mm")

    img.save(out_path)
    print(f"Created outro card: {out_path.name}")


# ----------------------------------------------------------------------
# 2. Sequence Structure Definition
# ----------------------------------------------------------------------

CHAPTERS = [
    {
        "act_id": "ACT I",
        "title": "Lisbon — The Departure",
        "sub": "July 8, 1497 | The Hermitage of Restelo & River Tagus",
        "folder": "episode-01-lisbon",
        "clips": [f"chapters/chapter-01-first-voyage/episode-01-lisbon/videos/CH01-S0{i}-motion-v1.mp4" for i in range(1, 9)],
        "transition_after": "production/exports/transitions/MAP-01-Lisbon-to-Atlantic.mp4",
        "transition_title": "Portolan Chart: Lisbon to Cape Verde & Atlantic",
    },
    {
        "act_id": "ACT II",
        "title": "The South Atlantic — Into the Unknown",
        "sub": "August–October 1497 | The Great Volta do Mar",
        "folder": "episode-02-atlantic",
        "clips": [f"chapters/chapter-01-first-voyage/episode-02-atlantic/videos/CH01-EP02-S0{i}-motion-v1.mp4" for i in range(1, 9)],
        "transition_after": "production/exports/transitions/MAP-02-Atlantic-to-Cape.mp4",
        "transition_title": "Portolan Chart: Atlantic Loop to Southern Africa",
    },
    {
        "act_id": "ACT III",
        "title": "The Devil's Sea — Rounding the Cape",
        "sub": "November–December 1497 | Cabo das Tormentas & Mossel Bay",
        "folder": "episode-03-cape",
        "clips": [f"chapters/chapter-01-first-voyage/episode-03-cape/videos/CH01-EP03-S0{i}-motion-v1.mp4" for i in range(1, 9)],
        "transition_after": "production/exports/transitions/MAP-03-Cape-to-East-Africa.mp4",
        "transition_title": "Portolan Chart: Rounding Cape of Good Hope to East Africa",
    },
    {
        "act_id": "ACT IV",
        "title": "East Africa — The Swahili Coast",
        "sub": "January–March 1498 | Mozambique Island & The Swahili World",
        "folder": "episode-04-east-africa",
        "clips": [f"chapters/chapter-01-first-voyage/episode-04-east-africa/videos/CH01-EP04-S0{i}-motion-v1.mp4" for i in range(1, 9)],
        "transition_after": "production/exports/transitions/MAP-04-Mozambique-to-Malindi.mp4",
        "transition_title": "Portolan Chart: Mozambique to Mombasa & Malindi",
    },
    {
        "act_id": "ACT V",
        "title": "Malindi — Pilot of the Monsoon",
        "sub": "April 1498 | Sultanate of Malindi & The Master Navigator",
        "folder": "episode-05-mombasa-malindi",
        "clips": [f"chapters/chapter-01-first-voyage/episode-05-mombasa-malindi/videos/CH01-EP05-S0{i}-motion-v1.mp4" for i in range(1, 9)],
        "transition_after": "production/exports/transitions/MAP-05-Malindi-to-Arabian-Sea.mp4",
        "transition_title": "Portolan Chart: Setting Sail into the Open Arabian Sea",
    },
    {
        "act_id": "ACT VI",
        "title": "The Arabian Sea — Monsoon Crossing",
        "sub": "May 1498 | 23 Days Across the Open Ocean to Mount Delli",
        "folder": "episode-06-monsoon-crossing",
        "clips": [f"chapters/chapter-01-first-voyage/episode-06-monsoon-crossing/videos/CH01-EP06-S0{i}-motion-v1.mp4" for i in range(1, 9)],
        "transition_after": "production/exports/transitions/MAP-06-Arrival-at-Calicut.mp4",
        "transition_title": "Portolan Chart: Landfall at Kappad Beach & Calicut",
    },
    {
        "act_id": "ACT VII",
        "title": "Calicut — The Zamorin's Court",
        "sub": "May–June 1498 | Royal Audience in the City of Spices",
        "folder": "episode-07-calicut",
        "clips": [
            "chapters/chapter-01-first-voyage/episode-07-calicut/videos/ch01ep07sc01_20260911122346.mp4",
            "chapters/chapter-01-first-voyage/episode-07-calicut/videos/ch01ep07sc02_20260911122352.mp4",
            "chapters/chapter-01-first-voyage/episode-07-calicut/videos/ch01ep07sc03_20260911122352.mp4",
            "chapters/chapter-01-first-voyage/episode-07-calicut/videos/ch01ep07sc04_20260911122352.mp4",
            "chapters/chapter-01-first-voyage/episode-07-calicut/videos/ch01ep07sc05_20260911122352.mp4",
            "chapters/chapter-01-first-voyage/episode-07-calicut/videos/ch01ep07sc06_20260911122346.mp4",
            "chapters/chapter-01-first-voyage/episode-07-calicut/videos/ch01ep07sc07_20260911122351.mp4",
            "chapters/chapter-01-first-voyage/episode-07-calicut/videos/ch01ep07sc08_20260911122346.mp4",
        ],
        "transition_after": "production/exports/transitions/MAP-07-Calicut-to-Anjediva.mp4",
        "transition_title": "Portolan Chart: Escaping Calicut to Anjediva Island",
    },
    {
        "act_id": "ACT VIII",
        "title": "The Break with Calicut — Ambush & Escape",
        "sub": "August–October 1498 | Hostages, 70 War Boats & Gaspar da Gama",
        "folder": "episode-08-calicut-conflict",
        "clips": [
            "chapters/chapter-01-first-voyage/episode-08-calicut-conflict/videos/Man_writing_at_table_20260912124724.mp4",
            "chapters/chapter-01-first-voyage/episode-08-calicut-conflict/videos/Merchant_weighs_pepper_on_tablet_20260912124724.mp4",
            "chapters/chapter-01-first-voyage/episode-08-calicut-conflict/videos/Man_sets_down_pen_20260912124724.mp4",
            "chapters/chapter-01-first-voyage/episode-08-calicut-conflict/videos/Vasco_da_Gama_lowers_arm_20260912124724.mp4",
            "chapters/chapter-01-first-voyage/episode-08-calicut-conflict/videos/Dias_hands_olla_to_Vasco_20260912124724.mp4",
            "chapters/chapter-01-first-voyage/episode-08-calicut-conflict/videos/Storm_hits_Portuguese_fleet_20260912124724.mp4",
            "chapters/chapter-01-first-voyage/episode-08-calicut-conflict/videos/Workers_scraping_careened_ship_hull_20260912124724.mp4",
            "chapters/chapter-01-first-voyage/episode-08-calicut-conflict/videos/Gaspar_greets_men_on_shore_20260912124724.mp4",
        ],
        "transition_after": None,
        "transition_title": None,
    },
]


# ----------------------------------------------------------------------
# 3. Clip Normalization & Title Card Generation
# ----------------------------------------------------------------------

def render_opening_clip(title_png: pathlib.Path, bg_img: pathlib.Path, out_path: pathlib.Path):
    """Render 5.0s opening documentary sequence with title fade."""
    if out_path.exists() and out_path.stat().st_size > 500000:
        print(f"Opening clip already cached: {out_path.name}")
        return

    vf = (
        "[0:v]scale=2560:2560,zoompan=z='min(zoom+0.0006,1.15)':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d=150:s=1920x1080:fps=30[bg];"
        "[1:v]fade=t=in:st=0.5:d=1.0:alpha=1,fade=t=out:st=3.8:d=1.0:alpha=1[fg];"
        "[bg][fg]overlay=0:0[v]"
    )
    af = (
        "anoisesrc=d=5.0:c=pink:r=48000,lowpass=f=220,volume=0.35[swell];"
        "aevalsrc='0.04*sin(2*PI*55*t)':d=5.0:s=48000[drone];"
        "[swell][drone]amix=inputs=2,afade=t=in:st=0:d=1.5,afade=t=out:st=3.5:d=1.5,loudnorm=I=-20:TP=-1.5:LRA=11[a]"
    )

    cmd = [
        "ffmpeg", "-y",
        "-loop", "1", "-i", str(bg_img),
        "-loop", "1", "-i", str(title_png),
        "-filter_complex", f"{vf};{af}",
        "-map", "[v]", "-map", "[a]",
        "-c:v", "libx264", "-preset", "fast", "-crf", "18", "-pix_fmt", "yuv420p",
        "-c:a", "aac", "-b:a", "192k", "-ar", "48000", "-ac", "2",
        "-t", "5.0",
        str(out_path)
    ]
    res = subprocess.run(cmd, capture_output=True, text=True)
    if res.returncode != 0:
        raise RuntimeError(f"Failed to render opening: {res.stderr[-400:]}")
    print(f"Rendered opening clip: {out_path.name} ({out_path.stat().st_size // 1024} KB)")


def render_outro_clip(outro_png: pathlib.Path, bg_img: pathlib.Path, out_path: pathlib.Path):
    """Render 5.0s outro documentary sequence."""
    if out_path.exists() and out_path.stat().st_size > 500000:
        print(f"Outro clip already cached: {out_path.name}")
        return

    vf = (
        "[0:v]scale=2560:2560,zoompan=z='min(zoom+0.0006,1.15)':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d=150:s=1920x1080:fps=30[bg];"
        "[1:v]fade=t=in:st=0.5:d=1.0:alpha=1,fade=t=out:st=4.0:d=0.8:alpha=1[fg];"
        "[bg][fg]overlay=0:0,fade=t=out:st=4.2:d=0.8[v]"
    )
    af = (
        "anoisesrc=d=5.0:c=pink:r=48000,lowpass=f=220,volume=0.35[swell];"
        "aevalsrc='0.04*sin(2*PI*55*t)':d=5.0:s=48000[drone];"
        "[swell][drone]amix=inputs=2,afade=t=in:st=0:d=1.5,afade=t=out:st=3.5:d=1.5,loudnorm=I=-20:TP=-1.5:LRA=11[a]"
    )

    cmd = [
        "ffmpeg", "-y",
        "-loop", "1", "-i", str(bg_img),
        "-loop", "1", "-i", str(outro_png),
        "-filter_complex", f"{vf};{af}",
        "-map", "[v]", "-map", "[a]",
        "-c:v", "libx264", "-preset", "fast", "-crf", "18", "-pix_fmt", "yuv420p",
        "-c:a", "aac", "-b:a", "192k", "-ar", "48000", "-ac", "2",
        "-t", "5.0",
        str(out_path)
    ]
    res = subprocess.run(cmd, capture_output=True, text=True)
    if res.returncode != 0:
        raise RuntimeError(f"Failed to render outro: {res.stderr[-400:]}")
    print(f"Rendered outro clip: {out_path.name} ({out_path.stat().st_size // 1024} KB)")


def normalize_clip(in_path: pathlib.Path, out_path: pathlib.Path, overlay_png: pathlib.Path | None = None):
    """Normalize clip to 1080p, 30fps, 48kHz audio with loudnorm, optionally with overlay."""
    if out_path.exists() and out_path.stat().st_size > 200000:
        return

    if overlay_png and overlay_png.exists():
        vf = (
            f"[0:v]scale=1920:1080:flags=lanczos,fps=30[base];"
            f"[1:v]fade=t=in:st=1.0:d=0.8:alpha=1,fade=t=out:st=6.2:d=0.8:alpha=1[ol];"
            f"[base][ol]overlay=0:0:enable='between(t,1.0,7.0)'[v]"
        )
        cmd = [
            "ffmpeg", "-y",
            "-i", str(in_path),
            "-i", str(overlay_png),
            "-filter_complex", vf,
            "-map", "[v]", "-map", "0:a",
            "-af", "loudnorm=I=-20:TP=-1.5:LRA=11",
            "-c:v", "libx264", "-preset", "fast", "-crf", "18", "-pix_fmt", "yuv420p",
            "-c:a", "aac", "-b:a", "192k", "-ar", "48000", "-ac", "2",
            str(out_path)
        ]
    else:
        vf = "scale=1920:1080:flags=lanczos,fps=30"
        cmd = [
            "ffmpeg", "-y",
            "-i", str(in_path),
            "-vf", vf,
            "-af", "loudnorm=I=-20:TP=-1.5:LRA=11",
            "-c:v", "libx264", "-preset", "fast", "-crf", "18", "-pix_fmt", "yuv420p",
            "-c:a", "aac", "-b:a", "192k", "-ar", "48000", "-ac", "2",
            str(out_path)
        ]

    res = subprocess.run(cmd, capture_output=True, text=True)
    if res.returncode != 0:
        raise RuntimeError(f"Failed to normalize {in_path.name}: {res.stderr[-400:]}")
    print(f"  -> Normalized: {out_path.name} ({out_path.stat().st_size // 1024} KB)")


# ----------------------------------------------------------------------
# 4. Master Orchestration
# ----------------------------------------------------------------------

def get_duration(file_path: pathlib.Path) -> float:
    """Get accurate duration via ffprobe."""
    cmd = [
        "ffprobe", "-v", "error",
        "-show_entries", "format=duration",
        "-of", "default=noprint_wrappers=1:nokey=1",
        str(file_path)
    ]
    res = subprocess.run(cmd, capture_output=True, text=True)
    return float(res.stdout.strip())


def main():
    print("=" * 60)
    print("VASCO DA GAMA — OUTBOUND EXPEDITION 14-MINUTE SUPERCUT")
    print("OpenMontage & FFmpeg Master Assembly Pipeline")
    print("=" * 60)

    # 1. Create Overlays
    title_png = OVERLAYS_DIR / "OPENING_TITLE.png"
    outro_png = OVERLAYS_DIR / "OUTRO_CARD.png"
    create_title_card(title_png)
    create_outro_card(outro_png)

    lower_thirds = {}
    for ch in CHAPTERS:
        lt_path = OVERLAYS_DIR / f"{ch['act_id'].replace(' ', '_')}_lower_third.png"
        create_lower_third(ch["act_id"], ch["title"], ch["sub"], lt_path)
        lower_thirds[ch["act_id"]] = lt_path

    # 2. Render Opening & Outro
    opening_clip = CACHE_DIR / "000_OPENING_TITLE.mp4"
    bg_opening = ROOT / "chapters" / "chapter-01-first-voyage" / "episode-01-lisbon" / "images" / "CH01-S01-v1.png"
    render_opening_clip(title_png, bg_opening, opening_clip)

    outro_clip = CACHE_DIR / "999_OUTRO_CARD.mp4"
    bg_outro = ROOT / "chapters" / "chapter-01-first-voyage" / "episode-08-calicut-conflict" / "images" / "CH01-EP08-S08-v1.png"
    render_outro_clip(outro_png, bg_outro, outro_clip)

    # 3. Schedule all normalization jobs
    print("\nPreparing clip normalization queue...")
    norm_jobs = []
    ordered_clips_meta = []
    clip_counter = 1

    for ch in CHAPTERS:
        act_id = ch["act_id"]
        for idx, clip_rel in enumerate(ch["clips"], 1):
            clip_path = ROOT / clip_rel
            cached_clip = CACHE_DIR / f"{clip_counter:03d}_{act_id.replace(' ', '_')}_S{idx:02d}.mp4"
            ol = lower_thirds[act_id] if idx == 1 else None

            norm_jobs.append((clip_path, cached_clip, ol))
            ordered_clips_meta.append({
                "type": "scene",
                "act_id": act_id,
                "title": f"{act_id}: {ch['title']} (Scene {idx})",
                "act_title": f"{act_id}: {ch['title']}",
                "is_first_of_act": (idx == 1),
                "path": cached_clip
            })
            clip_counter += 1

        if ch["transition_after"]:
            trans_path = ROOT / ch["transition_after"]
            cached_trans = CACHE_DIR / f"{clip_counter:03d}_{act_id.replace(' ', '_')}_MAP.mp4"
            norm_jobs.append((trans_path, cached_trans, None))
            ordered_clips_meta.append({
                "type": "map",
                "act_id": act_id,
                "title": f"Route Map: {ch['transition_title']}",
                "act_title": f"Route Map: {ch['transition_title']}",
                "is_first_of_act": False,
                "path": cached_trans
            })
            clip_counter += 1

    print(f"Total normalization jobs queued: {len(norm_jobs)}")
    print("Normalizing all clips concurrently (4 worker threads)...")
    t_start_norm = time.time()

    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
        futures = [executor.submit(normalize_clip, job[0], job[1], job[2]) for job in norm_jobs]
        concurrent.futures.wait(futures)
        for f in futures:
            if f.exception():
                raise f.exception()

    t_end_norm = time.time()
    print(f"All {len(norm_jobs)} clips normalized successfully in {t_end_norm - t_start_norm:.1f}s!")

    # 4. Construct Concat Manifest & Accurate Timeline
    print("\nCalculating timestamps and building manifest...")
    concat_list = [opening_clip]
    timeline_log = []
    current_time = 0.0

    timeline_log.append({
        "timestamp_str": time.strftime("%M:%S", time.gmtime(current_time)),
        "seconds": round(current_time, 2),
        "title": "Documentary Prologue: The Mission to India",
    })
    current_time += get_duration(opening_clip)

    for item in ordered_clips_meta:
        clip_path = item["path"]
        clip_dur = get_duration(clip_path)

        # Record major chapter timestamps (first scene of each act or route map)
        if item["is_first_of_act"]:
            timeline_log.append({
                "timestamp_str": time.strftime("%M:%S", time.gmtime(current_time)),
                "seconds": round(current_time, 2),
                "title": item["act_title"],
            })
        elif item["type"] == "map":
            timeline_log.append({
                "timestamp_str": time.strftime("%M:%S", time.gmtime(current_time)),
                "seconds": round(current_time, 2),
                "title": item["title"],
            })

        concat_list.append(clip_path)
        current_time += clip_dur

    concat_list.append(outro_clip)
    timeline_log.append({
        "timestamp_str": time.strftime("%M:%S", time.gmtime(current_time)),
        "seconds": round(current_time, 2),
        "title": "Outro: The Return Voyage Ahead & Credits",
    })
    current_time += get_duration(outro_clip)

    print(f"Total documentary runtime: {current_time:.1f}s ({time.strftime('%M:%S', time.gmtime(current_time))})")

    # Write concat manifest
    manifest_file = CACHE_DIR / "concat_manifest.txt"
    with open(manifest_file, "w", encoding="utf-8") as f:
        for c in concat_list:
            f.write(f"file '{c.as_posix()}'\n")
    print(f"Wrote concat manifest ({len(concat_list)} clips): {manifest_file.name}")

    # 5. Execute Concat via FFmpeg
    print("\n============================================================")
    print("CONCATENATING ALL 73 CLIPS INTO MASTER SUPERCUT FILE")
    print("============================================================")

    cmd = [
        "ffmpeg", "-y",
        "-f", "concat",
        "-safe", "0",
        "-i", str(manifest_file),
        "-c", "copy",
        str(MASTER_OUTPUT)
    ]
    t0 = time.time()
    res = subprocess.run(cmd, capture_output=True, text=True)
    t1 = time.time()

    if res.returncode != 0:
        print(f"Concat failed: {res.stderr[-500:]}")
        sys.exit(1)

    print(f"\nCONCATENATION SUCCESSFUL in {t1 - t0:.1f}s!")
    print(f"Master file: {MASTER_OUTPUT}")
    print(f"Master size: {MASTER_OUTPUT.stat().st_size / (1024 * 1024):.2f} MB")

    # 6. Save Timestamps
    timestamps_path = ROOT / "production" / "supercut_ep01_08_timestamps.json"
    with open(timestamps_path, "w", encoding="utf-8") as f:
        json.dump(timeline_log, f, indent=2)
    print(f"Saved timestamps to {timestamps_path}")

    print("\n--- YOUTUBE CHAPTERS ---")
    for item in timeline_log:
        print(f"{item['timestamp_str']} — {item['title']}")


if __name__ == "__main__":
    main()
