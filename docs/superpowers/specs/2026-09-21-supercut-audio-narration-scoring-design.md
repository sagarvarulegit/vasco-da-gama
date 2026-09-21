# Vasco da Gama — Outbound Expedition (Episodes 1–8)
## Audio Production & Documentary Scoring Specification

**Document ID:** `SPEC-2026-09-21-AUDIO-SCORING-V1`  
**Date:** 2026-09-21  
**Project:** Vasco da Gama — First Voyage Historical Documentary  
**Target Video Asset:** `production/exports/Vasco-da-Gama-Outbound-Voyage-Supercut-v1.mp4`  
**Target Duration:** ~11:08 min (668.3s)  
**Primary Source:** *A Journal of the First Voyage of Vasco da Gama, 1497–1499* (ed. E. G. Ravenstein, Hakluyt Society, 1898)  

---

## 1. Executive Summary

This design specification upgrades the Outbound Expedition Supercut (Episodes 1–8) from a silent visual montage into a fully voiced, musically scored, broadcast-standard historical documentary. The system integrates:
1. **High-Fidelity AI Voiceover** via ElevenLabs using a classic British documentary baritone narrator reading verified primary-source journal lines across all 64 narrative scenes.
2. **Historically Grounded Period Musical Score** progressing across 5 regional suites (Portuguese Renaissance lute/viol -> Cape storm drones -> Swahili coast oud/ney -> Malabar bansuri/mridangam -> Calicut naval battle chenda drums).
3. **Multi-Track Audio Ducking & Mastering** via FFmpeg dynamic sidechain ducking (-7 dB music dip during speech) and EBU R128 loudness normalization (-20 LUFS).

---

## 2. Voiceover Pipeline Architecture (ElevenLabs)

### 2.1 Voice Persona & Model Configuration
* **Engine:** ElevenLabs API (`ELEVEN_LAB_API_KEY` from environment).
* **Model:** `eleven_multilingual_v2`.
* **Voice ID:** Classic British Documentary Baritone (`George` - `JBFqnCBsd6RMkjVDRZzb` or `Brian` - `nPczCjzI2devNBz1zQrb`).
* **Voice Settings:**
  * Stability: `0.55` (consistent dignified delivery without emotional runaway)
  * Similarity Boost: `0.80` (rich resonance and crisp baritone clarity)
  * Style Exaggeration: `0.00` (neutral, authoritative documentary pacing)
  * Speaker Boost: `True`

### 2.2 Script Extraction & Scene Synchronization
* **Source Corpus:** Existing markdown records in `chapters/chapter-01-first-voyage/episode-01` through `episode-08` (`CH01-S01.md` through `CH01-EP08-scenes.md`).
* **Extraction Pattern:** Lines under `## Narration & Voiceover Script` (e.g. `> "..."`).
* **Scene Timing Profile (10.0-second scene window)**:
  * `0.0s – 1.0s`: Visual opening + music & foley establishment (silence on VO stem).
  * `1.0s – 7.0s`: Spoken voiceover line (duration target: 4.5 to 6.0 seconds, approx. 12–22 words at 135 words/minute).
  * `7.0s – 10.0s`: Voice trailing cushion; music swells before the visual cut.
* **Storage & Idempotency**:
  * Output directory: `production/audio/voiceover/`
  * Naming: `{ACT_ID}_S{IDX:02d}_vo.mp3` (e.g., `ACT_I_S01_vo.mp3` through `ACT_VIII_S08_vo.mp3`).
  * Checksum/cache check: Files already generated will not be re-requested, preserving API quota.

---

## 3. Musical Scoring & Thematic Suites

### 3.1 Regional Acoustic Progression
To convey the expedition crossing through distinct 15th-century maritime worlds, the score is divided into 5 thematic regional suites:

1. **Suite 1: Lisbon & Atlantic Ocean (Acts I & II)**
   * *Acoustic Elements*: Portuguese Renaissance lute, viola da gamba/rabeca, gentle frame drum pulse.
   * *Dramatic Function*: Solemn royal mission, vast Atlantic solitude, determination.
2. **Suite 2: Cape of Storms (Act III)**
   * *Acoustic Elements*: Bowed contrabass drones, ominous brass pads, low sea swells.
   * *Dramatic Function*: Peril, brutal Antarctic gales, rounding the continent.
3. **Suite 3: The Swahili Coast (Acts IV & V — Mozambique, Mombasa, Malindi)**
   * *Acoustic Elements*: Arabic oud, ney wooden flute, riqq/daf frame percussion.
   * *Dramatic Function*: Bustling medieval Islamic trade ports, shifting loyalties, discovery of the monsoon pilot.
4. **Suite 4: The Monsoon Crossing & Calicut Arrival (Acts VI & VII)**
   * *Acoustic Elements*: Classical Indian bansuri flute, meditative tanpura drone, mridangam rhythm.
   * *Dramatic Function*: 23-day sprint across open ocean, awe-inspiring landfall, grand royal audience before the Zamorin.
5. **Suite 5: The Ambush & Great Escape (Act VIII)**
   * *Acoustic Elements*: Urgent Kerala temple chenda drums, martial brass accents, resolving into solitary lute at Anjediva.
   * *Dramatic Function*: Hostage standoff, 70 war vessels swarming the harbor, thunderstorm escape, quiet recovery at Anjediva.
6. **Route Map Transitions (MAP-01 to MAP-07)**:
   * *Acoustic Elements*: Short, elegant navigational lute/string chords bridging the narrative acts.

### 3.2 Dynamic Sidechain Audio Ducking
* **Filter Configuration**:
  ```text
  [music][vo]sidechaincompress=threshold=0.08:ratio=4:attack=300:release=600[ducked_music]
  ```
* **Effect**:
  * Voiceover active -> Music ducks automatically by **-7 dB**.
  * Voiceover finishes / Scene transitions -> Music seamlessly swells back to 0 dB relative level.

---

## 4. Audio Mastering & Master Export Pipeline

### 4.1 Multi-Track Stem Hierarchy
For every scene, 3 discrete audio stems are balanced:
* **Stem 1 (Voiceover)**: Centered, dry, high-intelligibility broadcast speech (`volume=1.0`).
* **Stem 2 (Sound Effects & Foley)**: Ambient sea swell, rigging creak, harbor murmur (`volume=0.35`).
* **Stem 3 (Thematic Score)**: Ducked music bed (`volume=0.65` base, dropping to `0.28` during speech).

### 4.2 Broadcast Loudness Standard (EBU R128)
* Final mix passes through an automated FFmpeg filter:
  `loudnorm=I=-20:TP=-1.5:LRA=11`
* **Output Specs**: Stereo, 48,000 Hz, 192 kbps AAC.

### 4.3 Master Concat Integration
* The newly voiced and scored audio stems are remuxed with each normalized 1080p video clip in `production/exports/supercut_cache/`.
* Concat demuxer writes the master documentary:
  `production/exports/Vasco-da-Gama-Outbound-Voyage-Supercut-v1.mp4`.

---

## 5. Implementation Roadmap & Testing Gates

1. **Gate 1: Proof of Concept Test (Act I Scene 1 & 2)**
   - Extract script lines for CH01-S01 and CH01-S02.
   - Generate ElevenLabs audio for both scenes.
   - Mix with Suite 1 music and test ducking filter.
   - Verify balance and pacing.
2. **Gate 2: Batch Generation of All 64 Voiceover Clips**
   - Extract all 64 scene narration lines from markdown.
   - Batch request ElevenLabs audio with retry handling and rate limiting.
   - Validate that each voice clip is under 7.5 seconds.
3. **Gate 3: Score Arrangement & Multi-Track Mixing**
   - Place music stems and ambience for Acts I through VIII.
   - Run FFmpeg multi-stem mix across all 71 scene/map clips.
4. **Gate 4: Master Assembly & Verification**
   - Concatenate all 73 clips into the master 11-minute MP4.
   - Verify loudness profile (-20 LUFS) and stream synchronization.
