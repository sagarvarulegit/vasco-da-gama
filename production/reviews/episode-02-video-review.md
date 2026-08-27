# Episode 02 Video Deliverable Review

**Episode ID:** `CH01-EP02 — Atlantic: Into the Unknown`  
**Master Video:** [`videos/episode-02/Vasco-Da-Gama-CH01-EP02-v1.mp4`](../../videos/episode-02/Vasco-Da-Gama-CH01-EP02-v1.mp4)  
**Review Date:** 26 August 2026  
**Status:** VIDEO PASS / ASSEMBLED DELIVERABLE COMPLETE

---

## 1. Container & Technical Specifications

* **File Path:** `videos/episode-02/Vasco-Da-Gama-CH01-EP02-v1.mp4`
* **Resolution:** 1920×1080 (16:9 Full HD)
* **Frame Rate:** 30 fps (progressive)
* **Duration:** 71.60 seconds (1 minute 11.6 seconds)
* **Video Stream:** H.264 / AVC (`High` profile, CRF 18, ~4.88 Mbps)
* **Audio Stream:** AAC LC, 44.1 kHz, ~118 kbps
* **Pixel Format:** `yuv420p`
* **Multiplexing / Faststart:** Enabled (`+faststart`) for instant streaming playback

---

## 2. Motion Clip Sequence Breakdown

Each 10-second shot is generated from the corresponding locked canonical still with dedicated sub-pixel camera kinematics:

| Shot | Scene ID | Title | Input Still | Motion Clip | Kinematics & Direction |
|---|---|---|---|---|---|
| **01** | `CH01-EP02-S01` | *Open Water After Lisbon* | `CH01-EP02-S01-v2.png` | `CH01-EP02-S01-motion-v1.mp4` | Slow forward push across deck of *São Gabriel* into the open ocean swell. |
| **02** | `CH01-EP02-S02` | *Fog and Separation* | `CH01-EP02-S02-v1.png` | `CH01-EP02-S02-motion-v1.mp4` | Slow lateral track through rolling Atlantic sea-fog on *São Rafael*. |
| **03** | `CH01-EP02-S03` | *Sal and Reunion* | `CH01-EP02-S03-v2.png` | `CH01-EP02-S03-motion-v1.mp4` | Shimmering horizontal drift across calm water as four ships converge. |
| **04** | `CH01-EP02-S04` | *São Thiago Stores & Repairs* | `CH01-EP02-S04-v1.png` | `CH01-EP02-S04-motion-v1.mp4` | Slow push toward harbor loading and yard carpentry work. |
| **05** | `CH01-EP02-S05` | *The Broken Main Yard* | `CH01-EP02-S05-v2.png` | `CH01-EP02-S05-motion-v1.mp4` | Dynamic swell oscillation and zoom on the broken spar. |
| **06** | `CH01-EP02-S06` | *Birds & Whale in Open Sea* | `CH01-EP02-S06-v2.png` | `CH01-EP02-S06-motion-v1.mp4` | Wide expansive pull-out revealing the vast sea, breaching whale, and birds. |
| **07** | `CH01-EP02-S07` | *Signs of Land* | `CH01-EP02-S07-v1.png` | `CH01-EP02-S07-motion-v1.mp4` | Subtle upward tilt from floating weed up to the crew's watchful faces. |
| **08** | `CH01-EP02-S08` | *Landfall Before St Helena* | `CH01-EP02-S08-v1.png` | `CH01-EP02-S08-motion-v1.mp4` | Waterline forward glide following the sounding boat toward St Helena Bay. |

---

## 3. Visual & Narrative Continuity Review

* **Style Integrity:** All clips maintain the `MASTER_STYLE_02` European historical oil-painting aesthetic.
* **Transitions:** 1.2-second cross-dissolves (`xfade=transition=fade`) eliminate jarring cuts and create a painterly documentary pacing.
* **Fleet Silhouette:** Exactly four vessels remain legible throughout the Atlantic crossing sequence.
* **Soundscape:** Layered multi-channel ocean atmosphere (pink noise lowpass swell, bandpass rigging wind, low harmonic modal drone) mixed with smooth 2.0s head/tail fades.

---

## 4. Deliverables Checklist

- [x] All 8 individual motion clips generated under `videos/episode-02/`
- [x] Master stitched video exported to `videos/episode-02/Vasco-Da-Gama-CH01-EP02-v1.mp4`
- [x] Video blueprint created: [`production/episode-02-atlantic-blueprint.md`](../episode-02-atlantic-blueprint.md)
- [x] Image-to-video prompt pack finalized: [`prompts/CH01-EP02-image-to-video.md`](../../prompts/CH01-EP02-image-to-video.md)
- [x] Storyboard assembly complete: [`storyboards/CH01-EP02-storyboard.md`](../../storyboards/CH01-EP02-storyboard.md)
