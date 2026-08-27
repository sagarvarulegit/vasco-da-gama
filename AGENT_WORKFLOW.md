# AI Agent Handoff Workflow

This document is the operating manual for any AI coding or production agent
continuing the Vasco da Gama — First Voyage project. Follow it together with
`AGENTS.md`; `AGENTS.md` is the authority when there is a conflict.

The goal is to produce historically grounded, visually continuous, immersive
European-painting episodes that can later be turned into image-to-video clips.
The audience should feel present on the voyage, while the project must never
present Portuguese arrival as the discovery of an empty or waiting world.

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
6. Generate one scene at a time when approval is the requested workflow. If the
   owner explicitly requests a batch, generate the batch but leave every frame
   individually reviewable and unlocked.
7. Never overwrite a generated or approved asset. Create `v2`, `v3`, etc., and
   record why the revision exists.
8. Never expose, print, commit, or write `GEMINI_API_KEY` to disk.
9. An image is not canonical until the project owner approves it and a review
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

Batch generation is allowed only when explicitly requested. Batch generation
does not bypass per-scene review or approval.


## 9. Image-to-video prompt authoring (Google Omni Flash)

For each approved still, create a prompt containing:

- The exact source still (`images/episode-##/...`) and scene ID
- Camera movement (slow push, lateral drift, stern glide, etc.)
- Only physically plausible motion for sails, rigging, water, smoke, animals,
  and human gestures
- A 10-second beat structure matching Google Omni Flash clip generation
- Voiceover language and tone, clearly marked as narration/reconstruction
- Music, ambience, and sound effects (rigging, waves, gulls, timber, wind)
- Negative motion constraints: no ship morphing, face drift, extra people,
  modern sounds, subtitles, logos, or invented dialogue presented as fact

Narration should be based on the journal/account or explicitly labeled as a
dramatic reconstruction. Never describe the surviving account as Vasco's
personal diary.

## 10. Current project state

- Chapter 1 Episode 1 (`CH01-EP01 — Lisbon: The Departure`): Complete, locked, assembled video deliverable ready.
- Chapter 1 Episode 2 (`CH01-EP02 — Atlantic: Into the Unknown`): Complete, locked (`CH01-EP02-LOCK-v1`), all 8 motion clips and assembled master video ready.
- Next production gate: Chapter 1 Episode 3 (`CH01-EP03 — Cape of Good Hope`).


Always verify the actual filesystem and Git status before relying on this
snapshot; the document is a handoff aid, not a substitute for inspection.

## 11. Safe continuation checklist

Before handing work back:

- No secret values appear in files, logs, prompts, or output.
- Every new image has a scene ID and version suffix.
- Every generated candidate has a review file or is clearly marked non-canonical.
- Every approval is recorded with a date and hash.
- No locked asset was overwritten.
- Scene chronology and geographic movement remain plausible.
- The next action is written in the relevant episode documentation.

The expected agent behavior is: inspect, research, author, generate, review,
report, obtain approval, lock, and only then move to the next production gate.
