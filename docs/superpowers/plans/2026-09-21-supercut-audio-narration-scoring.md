# Supercut Audio Narration & Historical Scoring Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Transform the 11-minute Outbound Expedition Supercut into a broadcast-standard historical documentary by adding ElevenLabs AI voiceover (British narrator), 5 historically grounded regional music suites, and dynamic sidechain audio ducking.

**Architecture:** A 4-stage modular audio pipeline: (1) extract verified journal voiceover scripts across all 64 scenes into a JSON manifest, (2) synthesize voice clips via ElevenLabs API with idempotency caching, (3) assemble 5 regional acoustic music suites, (4) mix 3-stem audio (VO + ducked music + foley) per scene and concatenate into the master 1080p MP4.

**Tech Stack:** Python 3.10+, FFmpeg (with `sidechaincompress`, `loudnorm`, `amix`), ElevenLabs REST API / `requests`, `PIL` (Pillow).

**Spec:** [`docs/superpowers/specs/2026-09-21-supercut-audio-narration-scoring-design.md`](file:///C:/Sagar/Projects/vasco-da-gama/docs/superpowers/specs/2026-09-21-supercut-audio-narration-scoring-design.md)

## Global Constraints
- Target video runtime: ~11:08 min (668.3s), 1080p Full HD @ 30fps.
- Voiceover engine: ElevenLabs API using `ELEVEN_LAB_API_KEY` from environment.
- Voice model: `eleven_multilingual_v2` with British narrator baritone (`George` / `JBFqnCBsd6RMkjVDRZzb`).
- Audio standard: EBU R128 loudness normalization (`loudnorm=I=-20:TP=-1.5:LRA=11`), 48kHz stereo AAC.
- Pacing: 1.0s silence pre-roll, 4.5–6.5s spoken voice, 2.5–3.5s trail-out music swell per 10s scene.
- Sidechain ducking: -7 dB music dip during speech, 300ms attack, 600ms release.

## Review Focus
1. Missing voiceover line in scene markdown -> Script extractor must fallback to documented scene description and log warning without crashing.
2. ElevenLabs API rate limits or timeout -> HTTP request wrapper must implement exponential backoff retry and cache completed MP3 files.
3. Voiceover duration exceeds 7.5 seconds -> Script validator must measure character/word count and flag over-length lines before synthesis.
4. Audio-video duration mismatch during remux -> Mixer must clamp scene audio strictly to the video clip's ffprobe duration (10.0s for scenes, 4.0s for maps).
5. Audio clipping or digital distortion -> Master mix must enforce `-1.5 dBTP` true peak limit via `loudnorm`.

---

### Task 1: Script Extraction & Manifest Generator

**Files:**
- Create: `production/tools/extract_scene_narration.py`
- Output: `production/audio/narration_manifest.json`
- Test: `tests/test_narration_manifest.py`

**Interfaces:**
- Consumes: Scene markdown files in `chapters/chapter-01-first-voyage/episode-01` through `episode-08`.
- Produces: `production/audio/narration_manifest.json` containing 64 entries with `act_id`, `scene_idx`, `scene_id`, `text`, `word_count`, `target_duration_sec`.

- [ ] **Step 1: Write test for script extraction**

```python
import json
import pathlib
import pytest

def test_manifest_structure_and_completeness():
    manifest_path = pathlib.Path("production/audio/narration_manifest.json")
    assert manifest_path.exists(), "Manifest file must exist"
    with open(manifest_path, "r", encoding="utf-8") as f:
        data = json.load(f)
    assert len(data) == 64, f"Expected 64 scenes, found {len(data)}"
    for item in data:
        assert "scene_id" in item
        assert "text" in item and len(item["text"]) > 10
        assert item["word_count"] >= 3, f"Line too short in {item['scene_id']}"
        assert item["word_count"] <= 35, f"Line too long for 10s window in {item['scene_id']}"
```

- [ ] **Step 2: Run test to verify it fails**

Run: `pytest tests/test_narration_manifest.py -v`
Expected: FAIL (manifest does not exist yet)

- [ ] **Step 3: Implement `extract_scene_narration.py`**

Create `production/tools/extract_scene_narration.py` to iterate through all 8 episodes, parse `## Narration & Voiceover Script` blocks, clean quotes, calculate word counts, and save to `production/audio/narration_manifest.json`.

- [ ] **Step 4: Run test to verify it passes**

Run: `python production/tools/extract_scene_narration.py && pytest tests/test_narration_manifest.py -v`
Expected: PASS with 64 verified scenes.

- [ ] **Step 5: Commit**

```bash
git add production/tools/extract_scene_narration.py production/audio/narration_manifest.json tests/test_narration_manifest.py
git commit -m "feat(audio): extract verified scene narration manifest for episodes 1-8"
```

---

### Task 2: ElevenLabs Voiceover Synthesizer with Caching

**Files:**
- Create: `production/tools/generate_elevenlabs_voiceover.py`
- Output: `production/audio/voiceover/ACT_I_S01_vo.mp3` through `ACT_VIII_S08_vo.mp3`
- Test: `tests/test_voiceover_generation.py`

**Interfaces:**
- Consumes: `production/audio/narration_manifest.json`, `os.environ["ELEVEN_LAB_API_KEY"]`.
- Produces: 64 dry narration MP3 files in `production/audio/voiceover/`.

- [ ] **Step 1: Write test for voiceover caching and audio properties**

```python
import pathlib
import subprocess
import pytest

def test_proof_of_concept_voiceover():
    s01_vo = pathlib.Path("production/audio/voiceover/ACT_I_S01_vo.mp3")
    assert s01_vo.exists(), "Act I Scene 1 voiceover must exist"
    assert s01_vo.stat().st_size > 5000, "Audio file should have valid size"

    cmd = ["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(s01_vo)]
    dur = float(subprocess.check_output(cmd).decode().strip())
    assert 2.0 <= dur <= 8.0, f"VO duration {dur}s outside expected 2-8s window"
```

- [ ] **Step 2: Run test to verify it fails**

Run: `pytest tests/test_voiceover_generation.py -v`
Expected: FAIL (voiceover files not yet generated)

- [ ] **Step 3: Implement `generate_elevenlabs_voiceover.py`**

Implement ElevenLabs API client using `requests`:
- API URL: `https://api.elevenlabs.io/v1/text-to-speech/JBFqnCBsd6RMkjVDRZzb`
- Model: `eleven_multilingual_v2`
- Voice settings: stability=0.55, similarity_boost=0.80
- Exponential backoff retry logic (3 retries).
- File caching check: skip if file exists.
- Supports `--limit N` flag for testing gates.

- [ ] **Step 4: Run Gate 1 proof-of-concept test**

Run: `python production/tools/generate_elevenlabs_voiceover.py --limit 2 && pytest tests/test_voiceover_generation.py -v`
Expected: PASS for proof-of-concept scenes.

- [ ] **Step 5: Run full batch generation for all 64 scenes**

Run: `python production/tools/generate_elevenlabs_voiceover.py --all`
Expected: 64/64 MP3 files generated in `production/audio/voiceover/`.

- [ ] **Step 6: Commit**

```bash
git add production/tools/generate_elevenlabs_voiceover.py tests/test_voiceover_generation.py
git commit -m "feat(audio): implement ElevenLabs voiceover generator with caching"
```

---

### Task 3: Thematic Music Suites & Foley Engine

**Files:**
- Create: `production/tools/generate_period_music_suites.py`
- Output: `production/audio/music/SUITE_1_LISBON_ATLANTIC.mp3` through `SUITE_5_CALICUT_AMBUSH.mp3` and `MAP_BRIDGE.mp3`
- Test: `tests/test_music_suites.py`

**Interfaces:**
- Consumes: None (procedural harmonic audio synthesis + period acoustic sample arrangement).
- Produces: 5 loopable continuous thematic music suites and 1 map bridge track in `production/audio/music/`.

- [ ] **Step 1: Write test for music suite existence and audio specs**

```python
import pathlib
import subprocess
import pytest

@pytest.mark.parametrize("suite_name", [
    "SUITE_1_LISBON_ATLANTIC.mp3",
    "SUITE_2_CAPE_STORMS.mp3",
    "SUITE_3_SWAHILI_COAST.mp3",
    "SUITE_4_MONSOON_CALICUT.mp3",
    "SUITE_5_CALICUT_AMBUSH.mp3",
    "MAP_BRIDGE.mp3",
])
def test_music_suites(suite_name):
    p = pathlib.Path(f"production/audio/music/{suite_name}")
    assert p.exists() and p.stat().st_size > 20000
    cmd = ["ffprobe", "-v", "error", "-show_entries", "stream=channels,sample_rate", "-of", "json", str(p)]
    info = subprocess.check_output(cmd).decode()
    assert "48000" in info or "44100" in info
```

- [ ] **Step 2: Run test to verify it fails**

Run: `pytest tests/test_music_suites.py -v`
Expected: FAIL (suites not yet created)

- [ ] **Step 3: Implement `generate_period_music_suites.py`**

Generate rich, authentic modal audio beds for all 5 suites using multi-oscillator acoustic synthesis and atmospheric layering via FFmpeg:
- Suite 1 (D-Dorian lute/viol progression + frame drum pulse)
- Suite 2 (D-minor contrabass tempest + low howling sub-bass)
- Suite 3 (Bayat/Hijaz oud and ney modal drone + daf percussion)
- Suite 4 (Raag Bhupali / Yaman bansuri flute tones + tanpura drone + mridangam)
- Suite 5 (Tense Kerala chenda battle rhythms + martial brass chords)
- Map Bridge (Atmospheric navigational lute cadence)

- [ ] **Step 4: Run test to verify it passes**

Run: `python production/tools/generate_period_music_suites.py && pytest tests/test_music_suites.py -v`
Expected: PASS across all 6 tracks.

- [ ] **Step 5: Commit**

```bash
git add production/tools/generate_period_music_suites.py tests/test_music_suites.py
git commit -m "feat(audio): generate 5 authentic historical music suites and transition cues"
```

---

### Task 4: Multi-Stem Scene Mixer with Dynamic Ducking

**Files:**
- Create: `production/tools/mix_scene_audio.py`
- Output: `production/exports/supercut_cache/` (updated audio for all 71 segments)
- Test: `tests/test_scene_audio_mixing.py`

**Interfaces:**
- Consumes: Voiceover clips (`ACT_X_Sxx_vo.mp3`), Music suites, Environmental foley.
- Produces: 3-stem mixed audio with sidechain ducking (-7 dB) and `loudnorm=I=-20` embedded into each cached segment.

- [ ] **Step 1: Write test for ducked scene audio**

```python
import pathlib
import subprocess
import pytest

def test_ducked_scene_audio():
    clip_path = pathlib.Path("production/exports/supercut_cache/001_ACT_I_S01.mp4")
    assert clip_path.exists()
    cmd = ["ffprobe", "-v", "error", "-show_entries", "stream=channels,sample_rate,codec_name", "-of", "csv=p=0", str(clip_path)]
    out = subprocess.check_output(cmd).decode().strip()
    assert "aac" in out and "48000" in out
```

- [ ] **Step 2: Run test on unmixed clip to verify baseline**

Run: `pytest tests/test_scene_audio_mixing.py -v`

- [ ] **Step 3: Implement `mix_scene_audio.py`**

Implement multi-track audio pipeline:
- Offset voiceover by 1.0s (`adelay=1000|1000`).
- Mix voiceover, music suite slice, and environmental foley.
- Apply dynamic ducking: `sidechaincompress=threshold=0.08:ratio=4:attack=300:release=600`.
- Apply mastering filter: `loudnorm=I=-20:TP=-1.5:LRA=11`.
- Replace audio track in cached MP4 file using `-c:v copy -c:a aac -b:a 192k`.

- [ ] **Step 4: Run proof-of-concept mix on Act I Scenes 1 & 2**

Run: `python production/tools/mix_scene_audio.py --limit 2`
Verify audio playback: voice is loud and clear, music ducks during speech and swells after.

- [ ] **Step 5: Batch-mix all 71 clips**

Run: `python production/tools/mix_scene_audio.py --all`
Expected: All 64 scenes and 7 map transitions updated with mastered audio.

- [ ] **Step 6: Commit**

```bash
git add production/tools/mix_scene_audio.py tests/test_scene_audio_mixing.py
git commit -m "feat(audio): implement multi-stem mixer with sidechain ducking and loudness mastering"
```

---

### Task 5: Master Concat, Verification & YouTube Packaging Update

**Files:**
- Modify: `production/tools/assemble_supercut_ep01_08.py`
- Output: `production/exports/Vasco-da-Gama-Outbound-Voyage-Supercut-v1.mp4`
- Test: `tests/test_master_video_integrity.py`

**Interfaces:**
- Consumes: All 73 voiced and scored cached clips.
- Produces: Final 11:08 master documentary MP4 and updated `supercut_launch_pack.md`.

- [ ] **Step 1: Write test for master video file integrity**

```python
import pathlib
import subprocess
import pytest

def test_master_supercut_integrity():
    master_path = pathlib.Path("production/exports/Vasco-da-Gama-Outbound-Voyage-Supercut-v1.mp4")
    assert master_path.exists()
    assert master_path.stat().st_size > 300 * 1024 * 1024, "File size must be > 300 MB"

    cmd = ["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(master_path)]
    dur = float(subprocess.check_output(cmd).decode().strip())
    assert 660 <= dur <= 675, f"Runtime {dur}s outside expected 11:00-11:15 range"
```

- [ ] **Step 2: Run test on existing video**

Run: `pytest tests/test_master_video_integrity.py -v`

- [ ] **Step 3: Execute master concatenation**

Run: `python production/tools/assemble_supercut_ep01_08.py`
Expected: Re-concatenates the master file in ~3 seconds using the updated, fully voiced and scored segments.

- [ ] **Step 4: Verify audio streams and loudness**

Run: `ffmpeg -i production/exports/Vasco-da-Gama-Outbound-Voyage-Supercut-v1.mp4 -af ebur128=framelog=verbose -f null -`
Expected: Integrated Loudness in range -19.5 to -20.5 LUFS, True Peak <= -1.5 dBTP.

- [ ] **Step 5: Commit**

```bash
git add production/tools/assemble_supercut_ep01_08.py tests/test_master_video_integrity.py
git commit -m "feat(master): compile fully voiced and scored 11-minute documentary supercut"
```
