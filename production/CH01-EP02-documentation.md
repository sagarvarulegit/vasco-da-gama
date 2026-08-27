# CH01-EP02 Production Documentation

## Episode identity

- **Project:** Vasco da Gama — First Voyage
- **Story chapter:** CH01 — The first-voyage Atlantic passage
- **Episode:** CH01-EP02 — Atlantic: Open Water
- **Primary historical source:** the surviving first-voyage journal/account, traditionally associated with Álvaro Velho; English translation/editing by E. G. Ravenstein (Hakluyt Society, 1898)
- **Active visual style:** `MASTER_STYLE_02` — immersive European historical painting
- **Image model:** Gemini API `gemini-2.5-flash-image`
- **Generation wrapper:** `production/tools/gemini_image_generate.py`

## Historical scope

This episode follows the fleet from its departure near Lisbon through the
Atlantic passage and the approach to the Bay of St Helena. The chronology is
based on the surviving voyage account. Daily deck activity, exact weather,
camera position, and individual gestures are marked as reconstruction or
cinematic interpretation in the scene files; they are not presented as direct
journal quotations.

## Scene slate

| Scene | Title | Date / place | Status |
|---|---|---|---|
| CH01-EP02-S01 | Open Water After Lisbon | 10–15 Jul 1497, Atlantic west of Iberia | **Approved & locked (v2)** |
| CH01-EP02-S02 | Fog and Separation | 16–17 Jul, near Rio do Ouro | **Approved & locked (v1)** |
| CH01-EP02-S03 | Sal and Reunion | 22–26 Jul, Cape Verde / Ilha do Sal | **Approved & locked (v2)** |
| CH01-EP02-S04 | São Thiago Stores and Repairs | 27 Jul, São Thiago | **Approved & locked (v1)** |
| CH01-EP02-S05 | The Broken Main Yard | 18 Aug, southern Atlantic | **Approved & locked (v2)** |
| CH01-EP02-S06 | Birds and Whale in the Open Sea | 22 Aug, southern Atlantic | **Approved & locked (v2)** |
| CH01-EP02-S07 | Signs of Land | Late Oct–1 Nov, approaching southern Africa | **Approved & locked (v1)** |
| CH01-EP02-S08 | Landfall Before St Helena | 4–8 Nov, southwest Africa | **Approved & locked (v1)** |

## Continuity anchors

- `VASCO_01` begins the episode in his maintained departure appearance. Do not
  introduce mid-voyage beard growth, sun-darkening, or exhaustion until later
  scenes justify it.
- The fleet contains four recurring vessels: `SHIP_SG01` São Gabriel,
  `SHIP_SR01` São Rafael, `SHIP_B01` Berrio, and `SHIP_ST01` supply ship.
- `CH01-EP02-S01` establishes the four-vessel formation. No additional ship,
  boat, or skiff should appear unless a scene explicitly requires it.
- No Cape landmark, southern-African coastal wear, or main-yard damage should
  appear before its designated scene.

## Image generation procedure

1. Read the scene file and prompt pack.
2. Preserve the scene's source/reconstruction/cinematic classification.
3. Generate one frame with the Gemini wrapper using `GEMINI_API_KEY` from the
   environment; never write the key to disk.
4. Inspect the rendered image for historical accuracy, ship count, character
   continuity, geography, and style.
5. If a continuity defect is found, create a new version rather than silently
   overwriting the prior image.
6. Record the review and obtain explicit project-owner approval.
7. Record the SHA-256 hash in the episode lock manifest.

## Current locked assets

All eight scenes (S01–S08) are approved and canonical under `CH01-EP02-LOCK-v1`. SHA-256 hashes are recorded in [CH01-EP02-lock-v1.md](locks/CH01-EP02-lock-v1.md).

## Approval gate

Complete. All eight scenes have individual review records, approved canonical versions, and verified SHA-256 hashes in the lock manifest.

## Next production action

1. Assemble the Chapter 1 Episode 2 storyboard and continuity sheet (`storyboards/CH01-EP02-storyboard.md`).
2. Finalize the Episode 2 video blueprint and image-to-video prompt pack (`prompts/CH01-EP02-image-to-video.md`).
3. Generate motion clips / animatics and assemble the episode video deliverable under `videos/episode-02/`.

