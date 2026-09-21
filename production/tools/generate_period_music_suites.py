"""Generate 5 authentic historical music suites + map bridge track.

Uses multi-oscillator acoustic synthesis and harmonic layering via FFmpeg:
- Suite 1: Lisbon & Atlantic (D-Dorian lute/viol resonance + frame drum pulse)
- Suite 2: Cape of Storms (Contrabass drone + tempest sub-bass + gale winds)
- Suite 3: Swahili Coast (Bayat/Hijaz modal oud/ney drones + daf percussion)
- Suite 4: Monsoon Crossing & Calicut (Bansuri flute harmonics + tanpura drone + mridangam)
- Suite 5: Naval Ambush & Escape (Chenda battle rhythm + martial brass chords)
- Map Bridge: Portolan chart navigational lute arpeggio
"""

from __future__ import annotations

import pathlib
import subprocess
import sys
import time

ROOT = pathlib.Path(r"C:\Sagar\Projects\vasco-da-gama")
MUSIC_DIR = ROOT / "production" / "audio" / "music"
MUSIC_DIR.mkdir(parents=True, exist_ok=True)


def generate_suite_1(out_path: pathlib.Path, dur: float = 90.0):
    """Suite 1: Lisbon & Atlantic (D-Dorian Lute & Viols)."""
    # Lute fundamental (146.83 Hz D3, 220 Hz A3, 293.66 Hz D4, 349.23 Hz F4)
    filt = (
        f"aevalsrc='0.08*sin(2*PI*146.83*t)*exp(-3*mod(t,2.0)) + "
        f"0.06*sin(2*PI*220.00*t)*exp(-2.5*mod(t+0.5,2.0)) + "
        f"0.05*sin(2*PI*293.66*t)*exp(-2.0*mod(t+1.0,2.0)) + "
        f"0.04*sin(2*PI*349.23*t)*exp(-2.2*mod(t+1.5,2.0))':d={dur}:s=48000[lute];"
        f"aevalsrc='0.05*sin(2*PI*73.42*t) + 0.03*sin(2*PI*110.0*t)':d={dur}:s=48000,lowpass=f=240[viol];"
        f"anoisesrc=d={dur}:c=pink:r=48000,lowpass=f=120,volume=0.25[drum_sub];"
        f"aevalsrc='0.35*exp(-18*mod(t,1.5))':d={dur}:s=48000[drum_env];"
        f"[drum_sub][drum_env]amultiply[drum];"
        f"[lute][viol][drum]amix=inputs=3,afade=t=in:st=0:d=2.0,afade=t=out:st={dur-3.0:.1f}:d=3.0,"
        f"aecho=0.8:0.88:40|70:0.35|0.25[out]"
    )
    cmd = ["ffmpeg", "-y", "-filter_complex", filt, "-map", "[out]", "-c:a", "libmp3lame", "-b:a", "192k", str(out_path)]
    subprocess.check_call(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    print(f"Generated Suite 1: {out_path.name}")


def generate_suite_2(out_path: pathlib.Path, dur: float = 90.0):
    """Suite 2: Cape of Storms (Contrabass Drone & Tempest)."""
    filt = (
        f"aevalsrc='0.09*sin(2*PI*36.71*t) + 0.06*sin(2*PI*55.0*t) + 0.04*sin(2*PI*110.0*t)':d={dur}:s=48000[bass];"
        f"anoisesrc=d={dur}:c=pink:r=48000,lowpass=f=160,volume=0.55[surge];"
        f"anoisesrc=d={dur}:c=white:r=48000,bandpass=f=1200:w=800,volume=0.18[gale];"
        f"aevalsrc='0.03*sin(2*PI*440*t+sin(2*PI*0.3*t)*20)*exp(-0.2*mod(t,6))':d={dur}:s=48000[shiver];"
        f"[bass][surge][gale][shiver]amix=inputs=4,afade=t=in:st=0:d=2.5,afade=t=out:st={dur-3.0:.1f}:d=3.0[out]"
    )
    cmd = ["ffmpeg", "-y", "-filter_complex", filt, "-map", "[out]", "-c:a", "libmp3lame", "-b:a", "192k", str(out_path)]
    subprocess.check_call(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    print(f"Generated Suite 2: {out_path.name}")


def generate_suite_3(out_path: pathlib.Path, dur: float = 90.0):
    """Suite 3: Swahili Coast (Arabic Oud & Ney Modal)."""
    filt = (
        f"aevalsrc='0.07*sin(2*PI*196.00*t)*exp(-2.8*mod(t,1.33)) + "
        f"0.06*sin(2*PI*246.94*t)*exp(-2.8*mod(t+0.33,1.33)) + "
        f"0.05*sin(2*PI*293.66*t)*exp(-2.5*mod(t+0.66,1.33))':d={dur}:s=48000[oud];"
        f"aevalsrc='0.05*sin(2*PI*392.00*t+sin(2*PI*4*t)*6) + 0.03*sin(2*PI*440.0*t)':d={dur}:s=48000,lowpass=f=900[ney];"
        f"anoisesrc=d={dur}:c=pink:r=48000,bandpass=f=350:w=200,volume=0.25[daf_raw];"
        f"aevalsrc='0.4*exp(-22*mod(t,0.66))':d={dur}:s=48000[daf_env];"
        f"[daf_raw][daf_env]amultiply[daf];"
        f"[oud][ney][daf]amix=inputs=3,afade=t=in:st=0:d=2.0,afade=t=out:st={dur-3.0:.1f}:d=3.0,"
        f"aecho=0.8:0.85:50|90:0.3|0.2[out]"
    )
    cmd = ["ffmpeg", "-y", "-filter_complex", filt, "-map", "[out]", "-c:a", "libmp3lame", "-b:a", "192k", str(out_path)]
    subprocess.check_call(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    print(f"Generated Suite 3: {out_path.name}")


def generate_suite_4(out_path: pathlib.Path, dur: float = 90.0):
    """Suite 4: Monsoon & Calicut (Bansuri & Tanpura Drone)."""
    filt = (
        f"aevalsrc='0.06*sin(2*PI*110.0*t) + 0.04*sin(2*PI*164.81*t) + 0.03*sin(2*PI*220.0*t)':d={dur}:s=48000[tanpura];"
        f"aevalsrc='0.06*sin(2*PI*329.63*t+sin(2*PI*3*t)*5)*exp(-0.8*mod(t,3.0)) + "
        f"0.05*sin(2*PI*369.99*t)*exp(-0.8*mod(t+1.0,3.0)) + "
        f"0.04*sin(2*PI*440.00*t)*exp(-0.8*mod(t+2.0,3.0))':d={dur}:s=48000[bansuri];"
        f"anoisesrc=d={dur}:c=pink:r=48000,lowpass=f=200,volume=0.30[mrid_sub];"
        f"aevalsrc='0.35*exp(-14*mod(t,0.85))':d={dur}:s=48000[mrid_env];"
        f"[mrid_sub][mrid_env]amultiply[mrid];"
        f"[tanpura][bansuri][mrid]amix=inputs=3,afade=t=in:st=0:d=2.5,afade=t=out:st={dur-3.0:.1f}:d=3.0,"
        f"aecho=0.8:0.9:60|120:0.35|0.25[out]"
    )
    cmd = ["ffmpeg", "-y", "-filter_complex", filt, "-map", "[out]", "-c:a", "libmp3lame", "-b:a", "192k", str(out_path)]
    subprocess.check_call(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    print(f"Generated Suite 4: {out_path.name}")


def generate_suite_5(out_path: pathlib.Path, dur: float = 90.0):
    """Suite 5: Ambush & Great Escape (Chenda Battle Percussion)."""
    filt = (
        f"anoisesrc=d={dur}:c=pink:r=48000,bandpass=f=450:w=300,volume=0.45[chenda_raw];"
        f"aevalsrc='0.5*exp(-25*mod(t,0.35)) + 0.3*exp(-25*mod(t+0.175,0.35))':d={dur}:s=48000[chenda_env];"
        f"[chenda_raw][chenda_env]amultiply[chenda];"
        f"aevalsrc='0.08*sin(2*PI*98.00*t) + 0.06*sin(2*PI*146.83*t) + 0.05*sin(2*PI*196.0*t)':d={dur}:s=48000[brass];"
        f"aevalsrc='0.04*sin(2*PI*392*t)*sin(2*PI*6*t)':d={dur}:s=48000[tremolo];"
        f"[chenda][brass][tremolo]amix=inputs=3,afade=t=in:st=0:d=1.5,afade=t=out:st={dur-3.0:.1f}:d=3.0[out]"
    )
    cmd = ["ffmpeg", "-y", "-filter_complex", filt, "-map", "[out]", "-c:a", "libmp3lame", "-b:a", "192k", str(out_path)]
    subprocess.check_call(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    print(f"Generated Suite 5: {out_path.name}")


def generate_map_bridge(out_path: pathlib.Path, dur: float = 10.0):
    """Map Bridge: Portolan Navigational Chords."""
    filt = (
        f"aevalsrc='0.08*sin(2*PI*220.0*t)*exp(-2*mod(t,1.8)) + 0.06*sin(2*PI*277.18*t)*exp(-2*mod(t+0.4,1.8)) + "
        f"0.05*sin(2*PI*329.63*t)*exp(-2*mod(t+0.8,1.8)) + 0.04*sin(2*PI*440.0*t)*exp(-1.5*mod(t+1.2,1.8))':d={dur}:s=48000[lute];"
        f"anoisesrc=d={dur}:c=pink:r=48000,lowpass=f=280,volume=0.25[breeze];"
        f"[lute][breeze]amix=inputs=2,afade=t=in:st=0:d=0.8,afade=t=out:st={dur-1.2:.1f}:d=1.2,"
        f"aecho=0.8:0.88:50|100:0.3|0.2[out]"
    )
    cmd = ["ffmpeg", "-y", "-filter_complex", filt, "-map", "[out]", "-c:a", "libmp3lame", "-b:a", "192k", str(out_path)]
    subprocess.check_call(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    print(f"Generated Map Bridge: {out_path.name}")


def main():
    print("=" * 60)
    print("GENERATING 5 HISTORICAL PERIOD MUSIC SUITES + TRANSITIONS")
    print("=" * 60)
    t0 = time.time()
    generate_suite_1(MUSIC_DIR / "SUITE_1_LISBON_ATLANTIC.mp3")
    generate_suite_2(MUSIC_DIR / "SUITE_2_CAPE_STORMS.mp3")
    generate_suite_3(MUSIC_DIR / "SUITE_3_SWAHILI_COAST.mp3")
    generate_suite_4(MUSIC_DIR / "SUITE_4_MONSOON_CALICUT.mp3")
    generate_suite_5(MUSIC_DIR / "SUITE_5_CALICUT_AMBUSH.mp3")
    generate_map_bridge(MUSIC_DIR / "MAP_BRIDGE.mp3")
    t1 = time.time()
    print("=" * 60)
    print(f"All 6 musical suites generated in {t1 - t0:.1f}s!")
    print(f"Output directory: {MUSIC_DIR}")
    print("=" * 60)


if __name__ == "__main__":
    main()
