# Episodes 1–8 Documentary Supercut Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Assemble, render, and package a continuous 13–15 minute cinematic historical animated documentary feature ("The Impossible Voyage: How Vasco da Gama Reached India") combining Episodes 1 through 8 to capture the 4,000 public watch hours needed for YouTube monetization.

**Architecture:** A unified Python/FFmpeg assembly pipeline (`production/tools/assemble_supercut_ep01_08.py`) that generates high-res 1080p motion clips for Episodes 1–6 using sub-pixel cinematic camera kinematics (`zoompan`), integrates the existing fully animated clips for Episodes 7 & 8, inserts animated Portolan transition maps between chapters, and stitches the entire 64-scene sequence with crossfades, layered maritime soundscapes, and synchronized documentary voiceovers into a single master MP4.

**Tech Stack:** Python 3.11, FFmpeg / FFprobe, Pillow (PIL), Google Omni Flash clips, existing canonical assets in `chapters/chapter-01-first-voyage/`.

**Spec:** [`production/supercut-ep01-ep08-outbound-documentary.md`](file:///C:/Sagar/Projects/vasco-da-gama/production/supercut-ep01-ep08-outbound-documentary.md) and [`AGENTS.md`](file:///C:/Sagar/Projects/vasco-da-gama/AGENTS.md) (Section 26).

---

## Global Constraints

- **Runtime Invariant:** Total duration MUST be between 12:00 and 15:30 minutes to qualify for YouTube Browse recommendation and creator-placed mid-roll ad slots.
- **Visual Style:** All visual elements MUST strictly conform to `MASTER_STYLE_02` (European historical painting realism, no modern elements, no CGI gloss).
- **Single-Version Policy:** Final master export MUST be named `Vasco-da-Gama-Outbound-Voyage-Supercut-v1.mp4` (no v2, v3).
- **Strict Audio Hygiene:** Dialogue and voiceover MUST be normalized (EBU R128 / -14 LUFS) to prevent distortion when transitioning between chapters.
- **Portolan Map Transitions:** Every chapter transition MUST include a 4.0-second Portolan route update using [`images/maps/portolan-chart-master.png`](file:///C:/Sagar/Projects/vasco-da-gama/images/maps/portolan-chart-master.png) to establish geographic continuity.

---

## Review Focus

1. **Clip Resolution & Aspect Ratio Parity:** Ensure clips from Episodes 1–6 (generated from stills) and Episodes 7–8 (Omni Flash MP4s) share exact 1920x1080 resolution, 30fps, and yuv420p pixel format to prevent concat failure.
2. **Audio Normalization Across Acts:** Ensure synthetic ambient beds (pink/white noise ocean swells) do not drown out spoken voiceover lines during crossfades.
3. **Transition Glitch Prevention:** Verify that `xfade` offsets are strictly calculated against cumulative duration to avoid black frames or frozen video.
4. **Mobile Thumbnail Test:** Ensure the Supercut master thumbnail text is legible at 10% display scale on mobile screens.
5. **Timestamp Precision:** Ensure timestamps in the YouTube description match video scene markers within ±1 second.

---

## Task Breakdown

### Task 1: Asset Audit & Motion Clip Generation for Episodes 1–6
**Files:**
- Create: `production/tools/generate_episodes_01_06_motion.py`
- Output: `chapters/chapter-01-first-voyage/episode-0#/videos/CH01-EP0#-S##-motion-v1.mp4`

- [ ] Inspect existing locked stills for EP01 through EP06 (48 stills total).
- [ ] Define cinematic camera kinematics per scene (push-in, lateral track, swell roll, pan) following `assemble_episode_video.py` standards.
- [ ] Implement `generate_episodes_01_06_motion.py` to batch render all 48 motion clips at 1080p, 30fps, 10.0s duration each.
- [ ] Verify each generated MP4 exists and has valid audio/video streams via `ffprobe`.

### Task 2: Portolan Map Animated Transition Cards
**Files:**
- Create: `production/tools/generate_map_transitions.py`
- Output: `production/exports/transitions/MAP-TRANSITION-EP01-TO-EP08.mp4` (7 transitions)

- [ ] Inspect `images/maps/portolan-chart-master.png` and `generate_route_maps.py`.
- [ ] Build 4.0-second animated pan/zoom route clips showing the fleet's progression:
  - Transition 1: Lisbon to Cape Verde
  - Transition 2: Cape Verde into the South Atlantic Arc
  - Transition 3: South Atlantic to Cape of Good Hope
  - Transition 4: Cape of Good Hope to Mozambique
  - Transition 5: Mozambique to Mombasa & Malindi
  - Transition 6: Malindi to Calicut (Arabian Sea Crossing)
  - Transition 7: Calicut to Anjediva
- [ ] Render map clips with subtle paper creak and maritime wave audio.

### Task 3: Master Concat & Audio Bed Assembly Script
**Files:**
- Create: `production/tools/assemble_supercut_ep01_08.py`
- Output: `production/exports/Vasco-da-Gama-Outbound-Voyage-Supercut-v1.mp4`

- [ ] Assemble the full EDL (Edit Decision List) combining:
  - Prologue (S01 Lisbon departure hook)
  - Episodes 1 to 6 motion clips (48 clips)
  - Map transitions (7 clips)
  - Episodes 7 & 8 Omni Flash animated clips (16 clips)
- [ ] Implement smooth 1.0-second crossfades (`xfade`) between adjacent scenes and chapter titles.
- [ ] Mix continuous dynamic audio: ambient swell + wind + cultural instrumentation (rabeca -> African drums -> bansuri/sitar -> artillery thunder) + normalized voiceover.
- [ ] Execute master render using FFmpeg (h.264 / aac / -crf 18 / faststart).
- [ ] Validate final runtime, audio levels (-14 LUFS), and video integrity.

### Task 4: High-CTR Master Thumbnail & YouTube Publishing Package
**Files:**
- Create: `production/tools/generate_supercut_thumbnail.py`
- Output: `production/exports/Vasco-da-Gama-Outbound-Voyage-Supercut-thumbnail-v1.png`
- Update: `production/supercut-ep01-ep08-outbound-documentary.md`

- [ ] Design the 3-Element Master Thumbnail:
  - Element 1: Vasco da Gama in command + São Gabriel surging under full sails.
  - Element 2: The coastline of India with emerald-draped Zamorin palace in background.
  - Element 3: Impact Yellow Headline: `THE IMPOSSIBLE VOYAGE` + Sub-badge: `FULL DOCUMENTARY (1497-1498)`.
- [ ] Render thumbnail at 1280x720 and test at 10% smartphone scale.
- [ ] Extract exact second-by-second timestamps from the rendered video into the description package.
- [ ] Finalize the 3 Mid-Roll ad timestamps for maximum retention and revenue.
