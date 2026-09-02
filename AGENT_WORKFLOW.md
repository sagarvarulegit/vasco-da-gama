# AI Agent Handoff Workflow

This document is the operating manual for any AI coding or production agent
continuing the Vasco da Gama — First Voyage project. Follow it together with
`AGENTS.md`; `AGENTS.md` is the authority when there is a conflict.

The goal is to produce historically grounded, visually continuous, immersive
European-painting episodes that feel like a binge-worthy prestige streaming series
(e.g., *Shōgun*, *Black Sails*, *Fall of Civilizations*). The audience should feel
personally present on the deck with the crew, experiencing human survival, fear,
awe, and cultural collision, while never presenting Portuguese arrival as the
discovery of an empty world.

## 0. Executive Producer & AI Director Operating Model

The series operates on a studio production structure:

* **Executive Producer / Studio Head (You)**:
  - Establishes the overarching vision, strategic goals, and target audience standards.
  - Greenlights production gates, approves key budgets/milestones, and gives final sign-off.
  - Reviews final episode deliverables and steers publishing strategy.

* **Director, Screenwriter & Lead Filmmaker (AI Agent / Antigravity)**:
  - Takes full creative and technical ownership of directing every scene, shot, and cut.
  - Directs camera language (focal lengths, motivated moves), lighting, blocking, and dramaturgy.
  - Drives visual continuity (characters, ships, historical costumes, aging progression).
  - Crafts the screenplay from primary historical accounts (*Roteiro*) with strict source discipline.
  - Leads audio direction (voiceover tone, 3D foley, period score) and edits the final master video.
  - Packages and optimizes releases for maximum algorithmic growth and retention.

## 1. Non-negotiable rules

1. Read `AGENTS.md` before changing project files.
2. Treat the surviving first-voyage journal/account, Ravenstein's 1898 edition,
   and the project's research notes as the historical backbone.
3. Separate every scene into `[SOURCE]`, `[HISTORICAL]`, `[RECONSTRUCTION]`, and
   `[CINEMATIC]` material. Never turn a reconstruction into a source fact.
4. Preserve permanent IDs: `VASCO_01`, `PAULO_01`, `COELHO_01`, `DIAS_01`,
   `PILOT_01`; and `SHIP_SG01`, `SHIP_SR01`, `SHIP_B01`, `SHIP_ST01`.
5. Use `MASTER_STYLE_02` for new immersive European historical-painting work.
   `MASTER_STYLE_01` is the protected earlier benchmark for the locked Chapter
   1 Lisbon set.
6. Enforce `visual-skills` dramaturgy: no empty placeholder adjectives (`cinematic`, `epic`, `masterpiece`). Every shot must have 3 physical details (environmental pressure, body micro-action, sound anchor).
7. Generate one scene at a time when approval is the requested workflow. If the
   owner explicitly requests a batch, generate the batch but leave every frame
   individually reviewable and unlocked.
8. Never overwrite a generated or approved asset. Create `v2`, `v3`, etc., and
   record why the revision exists.
9. Never expose, print, commit, or write `GEMINI_API_KEY` to disk.
10. An image is not canonical until the project owner approves it and a review
   record plus SHA-256 hash are recorded.

## 2. Start-of-task checklist

Before doing production work:

```powershell
Get-Content AGENTS.md
git status --short
Get-ChildItem -Recurse -File | Select-Object -ExpandProperty FullName
```

Then inspect the relevant files:

- `reference/timeline.md` for chronology
- `reference/historical-sources.md` for source quality
- `reference/visual-bible.md` and `reference/style-history.md` for style
- `reference/characters/` for face, clothing, age, and personality continuity
- `reference/ships/` for hull, mast, sail, and damage continuity
- `scenes/` for the scene record being produced
- `prompts/` for image and image-to-video prompt packs
- `production/reviews/`, `production/approval-log.md`, and `production/locks/`
  for what is approved and protected

Do not assume a scene is approved because an image file exists.

## 3. Repository map

| Directory | Purpose |
|---|---|
| `reference/` | Canonical historical, geographic, style, character, and ship references |
| `chapters/` | Chapter and episode scope, outlines, and status |
| `scenes/` | One source-grounded Markdown record per scene |
| `prompts/` | Image prompts, image-to-video prompts, narration, music, and sound direction |
| `images/` | Generated stills, approved thumbnails, and non-canonical tests |
| `storyboards/` | Panel order, continuity sheets, and visual sequence maps |
| `production/` | Reviews, approval logs, locks, blueprints, tools, and export notes |
| `videos/` | Final or versioned assembled episode videos |
| `research/` | Additional source extracts and uncertainty notes |

## 4. Naming and versioning

Use zero-padded IDs:

- Episode: `CH01-EP02`
- Scene: `CH01-EP02-S03`
- Still: `images/episode-02/CH01-EP02-S03-v1.png`
- Review: `production/reviews/CH01-EP02-S03-review.md`
- Motion clip: `videos/episode-02/CH01-EP02-S03-motion-v1.mp4`
- Episode video: `videos/episode-02/Vasco-Da-Gama-CH01-EP02-v1.mp4`
- Thumbnail: `images/episode-02/CH01-EP02-thumbnail-v1.png`
- Lock manifest: `production/locks/CH01-EP02-lock-v1.md`

Existing names are compatibility-sensitive. Do not rename old Chapter 1
assets merely to make them match the newer convention.

## 5. How to author a scene

Create `scenes/CH01-EP##-S##.md` with these mandatory sections:

```markdown
# CH01-EP##-S##
# Scene title
# Date
# Location
# Source
# Historical confidence

## Source Facts
## Historical Context
## Reconstruction
## Cinematic Interpretation
## Characters
## Ships
## Environment
## Continuity Requirements
## Narration & Voiceover Script
## Audio Direction & Sound Design ([AUDIO_TAGS])
## Image Prompt
## Negative Prompt
## Image-to-Video Prompt (Google Omni Flash)
## Animation Potential
```

The scene must establish date, location, source basis, confidence, characters,
ships, environmental conditions, narration line, structured audio tags, and what is known versus reconstructed. Use
the primary account for chronology. Use broader historical research for ports,
clothing, maritime practice, and local cultures. If uncertain, say so.


### Scene prompt formula

Every image prompt should be self-contained and include:

```text
MASTER_STYLE_02.
Date and historically appropriate location.
Character IDs and appearance state.
Ship IDs and continuity descriptions.
Late-fifteenth-century clothing, tools, materials, and environment.
Lighting, camera position, composition, emotional tone, and scale.
Historical restrictions and no-text requirements.
```

The negative prompt must exclude modern objects, modern ships, later weapons,
fantasy armor, pirate stereotypes, glossy CGI, anachronistic architecture,
extra vessels, generated labels, logos, watermarks, and unsupported spectacle.

## 6. How to generate images with Gemini

The working API key is a Gemini API key. It is not a Vertex Imagen `:predict`
credential. Use the repository wrapper, which calls the Gemini image model and
decodes the returned PNG:

```powershell
python production/tools/gemini_image_generate.py `
  --prompt "<complete scene-specific prompt>" `
  --output images/episode-02/CH01-EP02-S03-v1.png
```

Or use a UTF-8 prompt file:

```powershell
python production/tools/gemini_image_generate.py `
  --prompt-file prompts/CH01-EP02-S03-gemini.txt `
  --output images/episode-02/CH01-EP02-S03-v1.png
```

The default model is `gemini-2.5-flash-image`. Set `GEMINI_IMAGE_MODEL` or use
`--model` only after confirming that the model is available to the key. Do not
replace this path with a Vertex endpoint unless the owner supplies the required
Google Cloud project and OAuth/service-account setup.

The wrapper handles HTTP errors, missing image data, output-directory creation,
and base64 decoding. It does not create approval records automatically.

## 7. Image review protocol

After generation, inspect the image visually and compare it to the scene file
and canonical references. Check:

- Character face, age, beard, clothing, and physical condition
- Ship count, hull silhouette, masts, sails, flags, and localized damage
- Date, route, coast, climate, vegetation, and architecture
- Source fact versus reconstruction labeling
- No extra boats, modern objects, labels, text, logos, or watermarks
- Image-to-video suitability: clear subject, stable geometry, no impossible
  anatomy, and plausible motion affordances

If defective, generate a new version with a more specific constraint. Keep the
rejected version and explain the defect in the review file. Example review:

```markdown
# CH01-EP02-S03 Review

## Versions
- v1 rejected: generated a fifth vessel and visible labels.
- v2 candidate: corrected vessel count; still needs approval.

## Historical review
...

## Continuity review
...

## Status
Ready for project-owner approval. Not locked.
```

When the owner approves, update the review with the approval date and SHA-256:

```powershell
(Get-FileHash images/episode-02/CH01-EP02-S03-v2.png -Algorithm SHA256).Hash
```

Then append the event to `production/approval-log.md` and add the asset/hash to
the episode lock manifest. Approval is explicit; do not infer it from silence.

## 8. Episode workflow

For each episode, follow this order:

1. Confirm episode scope and historical dates in `chapters/` and the outline.
2. Create or update all scene records.
3. Build the image prompt pack in `prompts/`.
4. Generate stills with the Gemini wrapper.
5. Review each still and create its individual review file.
6. Present candidate images to the owner for approval.
7. Record approvals and hashes; update the lock manifest.
8. Assemble the storyboard and continuity sheet only from approved frames.
9. Write image-to-video prompts for each approved frame tailored for the Google Omni Flash model.
10. Generate motion clips using Google Omni Flash (or comparable engine),
    then review voiceover, music, sound, motion, and historical continuity.
11. Assemble the episode video under `videos/episode-##/` and document the
    export settings, source frames, and version.
12. Generate animated 15th-century Portolan nautical route maps for episode
    transitions and geography orientation using `production/tools/generate_route_maps.py`.
13. Author the YouTube Publishing Package and Shorts Funnel (high-CTR standalone
    titles, 3-element mobile thumbnail specs, SEO metadata, and 9:16 vertical shorts).

Batch generation is allowed only when explicitly requested. Batch generation
does not bypass per-scene review or approval.


## 9. Cinematic Dramaturgy & Image-to-Video Authoring (`visual-skills`)

All scene design and video prompt generation must adhere to the `visual-skills`
framework located in `.agents/skills/video` and `.agents/skills/image`.

### 1. The Core Scene Formula
Every scene must define five structural elements before generating prompts:
```text
Scene = Hero's Desire + Obstacle + Space Geometry + Controlled Gaze + Editing Rhythm
```
* **Desire:** What does the character want right now in this exact second?
* **Obstacle:** What blocks them (fear, rot, distance, armed defenders, language barrier)?
* **Space Geometry:** Who holds the power position? Where is the threat, and where is escape?
* **Controlled Gaze:** Exactly where the viewer's eye is forced to look (one focal point per shot).
* **Editing Rhythm:** The shot length ladder (e.g. wide 3.5s $\rightarrow$ medium 3.5s $\rightarrow$ macro 3.0s).

### 2. The 3 Physical Details Law (Banning Empty Adjectives)
* **Banned Words:** Never use `cinematic`, `epic`, `masterpiece`, `stunning`, `dramatic lighting`, `intense moment`.
* **The 3 Mandatory Details per Shot:**
  1. *Environmental Pressure:* A concrete physical fact carrying the emotion (choking tallow smoke, pitch-black hold, blinding coral sun glare, salt encrustation).
  2. *Body Micro-Action:* The emotion translated into the human body (jaw locking rigid, knuckles whitening on sword hilt, trembling hand dabbing vinegar, hollow eyes scanning horizon).
  3. *Sound / Visual Anchor:* A sensory motif hook (metallic CLANG of caulking mallets, tinny jingle of brass bells on oak, whistling arrow through dawn mist).

### 3. Walter Murch's Rule of Six (Editing Priority)
When structuring multi-shot sequences or cuts, adhere to Walter Murch's hierarchy:
1. **Emotion (51%)**: Does the cut honor the emotional truth of the moment?
2. **Story (23%)**: Does the cut advance the story or reveal character?
3. **Rhythm (10%)**: Does the cut fall on the musical cadence of the scene?
4. **Eye-trace (7%)**: Where is the viewer's gaze at the cut?
5. **2D Screen Plane (5%)**: Does the cut preserve left-to-right vector consistency?
6. **3D Physical Space (4%)**: Does the cut respect the physical geography?

### 4. David Fincher Camera Motivation
* The camera never moves without a reason.
* Every pan, crane, tracking shot, or push-in must answer: **"What changed?"** (e.g., the camera pushes in the exact frame the Sheikh turns away in disgust). If nothing changed, keep the camera static.

### 5. Multi-Layer Sound Design Standard (4-Layer Audio)
Sound represents 50% of the emotional weight. Every scene specifies:
* **Layer 1 — Voiceover:** Intimate, deep documentary narrator speaking as a witness.
* **Layer 2 — Spatial Foley:** Tangible physical actions (creaking hull oak, clanking mallets, sloshing bilge water).
* **Layer 3 — Environmental Ambience:** Multi-channel atmospheric beds (howling trade winds, tropical cicadas, distant Adhan call).
* **Layer 4 — Authentic Period Music:** Period instrumentation (oud, nay, daf drums, Portuguese vihuela, bowed cellos).

---

Every completed episode deliverable must include an optimized publishing package
in `production/episode-##-youtube-package.md` designed to overcome the YouTube
cold-start problem and maximize recommendation CTR and viewer retention.

### 1. Standalone Curiosity-First Title Formula
- **Rule**: Never lead titles with serialized codenames like `(Ep. 3)` or `CH01-EP02`. Cold viewers avoid clicking serialized episodes.
- **Mobile limit**: The first 45–50 characters must contain the core emotional hook, life-or-death stakes, or curiosity gap before truncation.
- **Formula**: `[High-Stakes Hook / Curiosity Question] | [Broad Search Topic] ([Year])`
- *Example*: `The Deadly Monster Wave That Almost Ended Vasco da Gama (1497)`

### 2. The 3-Element High-CTR Thumbnail Rule
Every thumbnail must be verified for clarity at mobile scale (120×68 px) and follow the 3-element composition:
1. **Hero Subject**: High-contrast focal point (extreme emotional facial expression or a ship tilted in violent peril).
2. **Immediate Threat/Environment**: Dramatic contextual backdrop (50-foot rogue wave, midnight flames, coastal spear ambush).
3. **Bold Text Hook**: 2–4 high-impact words in bold yellow/white with heavy dark stroke/shadow (e.g., `POINT OF NO RETURN`, `NO ESCAPE`, `LOST 96 DAYS`).

### 3. Mandatory 9:16 Shorts Funnel
For every long-form episode, produce **at least 2 vertical (9:16) 30–60 second action Shorts**:
- Highlight peak dramatic beats (e.g., the St Helena spear attack, snapped main yard, supply ship burning).
- Fast pacing with bold animated captions.
- Explicitly configure YouTube Studio's **"Related Video"** picker on each Short to link directly to the parent long-form episode.

### 4. Search & Evergreen SEO Metadata
- The first 2 lines of the description must contain high-volume search phrases (`Vasco da Gama voyage to India`, `Age of Discovery`, `Cape of Good Hope 1497`).
- Include structured chapter timestamps, primary source citations, and an engaging pinned comment question.

### 5. Cold Open Retention Rule (First 15 Seconds)
- Jump directly into high-stakes narration or visual tension within the first 0–15 seconds.
- Strictly avoid slow channel logo animations, animated intro bumpers, or dead silence before the hook.

## 11. Current project state

- Chapter 1 Episode 1 (`CH01-EP01 — Lisbon: The Departure`): Complete, locked, assembled video deliverable ready.
- Chapter 1 Episode 2 (`CH01-EP02 — Atlantic: Into the Unknown`): Complete, locked (`CH01-EP02-LOCK-v1`), all 8 motion clips and assembled master video ready.
- Chapter 1 Episode 3 (`CH01-EP03 — Cape of Good Hope`): Complete, locked (`CH01-EP03-LOCK-v1`), all 8 motion clips and assembled master video ready.
- Next production gate: Chapter 1 Episode 4 (`CH01-EP04 — East Africa & Mozambique Channel`).


Always verify the actual filesystem and Git status before relying on this
snapshot; the document is a handoff aid, not a substitute for inspection.

## 12. Safe continuation checklist

Before handing work back:

- No secret values appear in files, logs, prompts, or output.
- Every new image has a scene ID and version suffix.
- Every generated candidate has a review file or is clearly marked non-canonical.
- Every approval is recorded with a date and hash.
- No locked asset was overwritten.
- Scene chronology and geographic movement remain plausible.
- The next action is written in the relevant episode documentation.
- The YouTube publishing package adheres to Section 10 standards.

The expected agent behavior is: inspect, research, author, generate, review,
report, obtain approval, lock, package for publishing, and only then move to the next production gate.
