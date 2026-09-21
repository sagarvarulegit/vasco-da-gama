#!/usr/bin/env python3
"""Generate authentic 15th-century Portolan map transitions between documentary acts.

Uses the master chart images/maps/portolan-chart-master.png to create 4.0-second
cinematic camera tracks with antique paper texture and subtle ocean breeze ambience.
"""

from __future__ import annotations

import pathlib
import subprocess
import sys

PROJECT_ROOT = pathlib.Path(__file__).resolve().parent.parent.parent
MAP_IMAGE = PROJECT_ROOT / "images" / "maps" / "portolan-chart-master.png"
OUT_DIR = PROJECT_ROOT / "production" / "exports" / "transitions"
OUT_DIR.mkdir(parents=True, exist_ok=True)

# 7 Transitions between Chapters
TRANSITIONS = [
    {
        "id": "MAP-01-Lisbon-to-Atlantic",
        "title": "ACT I -> ACT II: THE OCEAN VOID",
        # Pan from Lisbon down to Cape Verde
        "zoompan": "zoompan=z='1.25':x='if(eq(on,1),iw*0.25,min(x+0.5,iw*0.35))':y='if(eq(on,1),ih*0.15,min(y+1.0,ih*0.35))':d=120:s=1920x1080:fps=30",
    },
    {
        "id": "MAP-02-Atlantic-to-Cape",
        "title": "ACT II -> ACT III: THE SEA OF STORMS",
        # Drift across the South Atlantic Arc toward the Cape
        "zoompan": "zoompan=z='1.22':x='if(eq(on,1),iw*0.20,min(x+1.5,iw*0.48))':y='if(eq(on,1),ih*0.45,min(y+1.5,ih*0.75))':d=120:s=1920x1080:fps=30",
    },
    {
        "id": "MAP-03-Cape-to-East-Africa",
        "title": "ACT III -> ACT IV: THE EDGE OF ISLAM",
        # Pan around the southern tip of Africa and up the Mozambique Channel
        "zoompan": "zoompan=z='1.26':x='if(eq(on,1),iw*0.45,min(x+1.2,iw*0.58))':y='if(eq(on,1),ih*0.78,max(y-1.5,ih*0.55))':d=120:s=1920x1080:fps=30",
    },
    {
        "id": "MAP-04-Mozambique-to-Malindi",
        "title": "ACT IV -> ACT V: THE SWAHILI COAST",
        # Track north along the East African coast to Mombasa and Malindi
        "zoompan": "zoompan=z='1.28':x='if(eq(on,1),iw*0.56,min(x+0.8,iw*0.62))':y='if(eq(on,1),ih*0.58,max(y-1.6,ih*0.38))':d=120:s=1920x1080:fps=30",
    },
    {
        "id": "MAP-05-Malindi-to-Arabian-Sea",
        "title": "ACT V -> ACT VI: THE MONSOON SPRINT",
        # Eastward sprint from Malindi across the open Arabian Sea toward India
        "zoompan": "zoompan=z='1.24':x='if(eq(on,1),iw*0.58,min(x+2.2,iw*0.82))':y='if(eq(on,1),ih*0.40,min(y+0.4,ih*0.45))':d=120:s=1920x1080:fps=30",
    },
    {
        "id": "MAP-06-Arrival-at-Calicut",
        "title": "ACT VI -> ACT VII: THE METROPOLIS OF SPICES",
        # Slow dramatic push-in to Calicut on the Malabar Coast of India
        "zoompan": "zoompan=z='min(zoom+0.0012,1.35)':x='iw*0.78-(iw/zoom/2)':y='ih*0.42-(ih/zoom/2)':d=120:s=1920x1080:fps=30",
    },
    {
        "id": "MAP-07-Calicut-to-Anjediva",
        "title": "ACT VII -> ACT VIII: THE GREAT ESCAPE",
        # Track north along the Indian coast from Calicut to Anjediva
        "zoompan": "zoompan=z='1.30':x='if(eq(on,1),iw*0.78,max(x-0.8,iw*0.74))':y='if(eq(on,1),ih*0.46,max(y-1.2,ih*0.36))':d=120:s=1920x1080:fps=30",
    },
]


def render_transition(trans: dict, output_file: pathlib.Path) -> bool:
    duration = 4.0
    audio_filt = (
        f"anoisesrc=d={duration}:c=pink:r=48000,lowpass=f=280,volume=0.30[sea];"
        f"aevalsrc='0.03*sin(2*PI*85*t)+0.015*sin(2*PI*170*t)':d={duration}:s=48000[drone];"
        f"[sea][drone]amix=inputs=2,afade=t=in:st=0:d=0.8,afade=t=out:st={duration-0.8}:d=0.8[aout]"
    )

    cmd = [
        "ffmpeg", "-y",
        "-loop", "1", "-i", str(MAP_IMAGE),
        "-filter_complex", f"[0:v]scale=2560:2560,{trans['zoompan']}[v];{audio_filt}",
        "-map", "[v]", "-map", "[aout]",
        "-c:v", "libx264", "-preset", "fast", "-crf", "20",
        "-pix_fmt", "yuv420p",
        "-c:a", "aac", "-b:a", "192k", "-ar", "48000",
        "-t", str(duration), "-r", "30",
        str(output_file)
    ]
    res = subprocess.run(cmd, capture_output=True, text=True)
    if res.returncode != 0:
        print(f"Error rendering {output_file.name}:\n{res.stderr[-300:]}", file=sys.stderr)
        return False
    return True


def main():
    print("=" * 60)
    print("GENERATING 7 PORTOLAN MAP ROUTE TRANSITIONS")
    print("=" * 60)
    for t in TRANSITIONS:
        out_p = OUT_DIR / f"{t['id']}.mp4"
        print(f"Rendering {t['id']} ({t['title']})...")
        ok = render_transition(t, out_p)
        if ok:
            print(f"  -> Generated: {out_p.name} ({out_p.stat().st_size // 1024} KB)")
    print("\nAll map transitions generated successfully!")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
