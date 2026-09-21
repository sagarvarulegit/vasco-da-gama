# Project Understanding

This file acts as the persistent memory for AI agents working on this project. It contains high-level context, architectural decisions, and important constraints.

## Core Purpose
A historically grounded, visually continuous, immersive European-painting video docuseries reconstructing Vasco da Gama's first voyage to India (1497–1499). The channel goal is to produce prestige, monetizable YouTube documentary content (in the vein of *Fall of Civilizations*, *Shōgun*, *Black Sails*) supported by viral Shorts funnels, animated Portolan transition maps, and high-CTR algorithmic packaging.

- **Primary Source**: *A Journal of the First Voyage of Vasco da Gama, 1497–1499* (ed. E. G. Ravenstein, Hakluyt Society, 1898; Álvaro Velho account / *Roteiro*).
- **Core Narrative Philosophy**: The Indian Ocean was an already sophisticated, connected maritime world. The Portuguese arrival is not the "discovery" of an empty land, but a high-stakes cultural, economic, and human collision.

## Architecture & Tech Stack
- **Repository Structure**:
  - `reference/`: Master bibles for chronology ([`timeline.md`](file:///C:/Sagar/Projects/vasco-da-gama/reference/timeline.md)), sources ([`historical-sources.md`](file:///C:/Sagar/Projects/vasco-da-gama/reference/historical-sources.md)), visual style ([`visual-bible.md`](file:///C:/Sagar/Projects/vasco-da-gama/reference/visual-bible.md)), geography ([`geography.md`](file:///C:/Sagar/Projects/vasco-da-gama/reference/geography.md)), character & ship registries ([`reference/characters/`](file:///C:/Sagar/Projects/vasco-da-gama/reference/characters/), [`reference/ships/`](file:///C:/Sagar/Projects/vasco-da-gama/reference/ships/)), and the [`anachronism-watchlist.md`](file:///C:/Sagar/Projects/vasco-da-gama/reference/anachronism-watchlist.md).
  - `chapters/chapter-01-first-voyage/`: Unified directories for Episodes 01 through 11, each containing `scenes/`, `prompts/`, `storyboards/`, `images/`, `videos/`, and `production/` (`locks/`, `reviews/`).
  - `production/`: Master feature film blueprint, Shorts packs 01–04, [`approval-log.md`](file:///C:/Sagar/Projects/vasco-da-gama/production/approval-log.md), [`definition-of-done.md`](file:///C:/Sagar/Projects/vasco-da-gama/production/definition-of-done.md), and automation tooling in `production/tools/`.
- **Tooling & Generation Pipeline**:
  - `gemini_image_generate.py`: Generates still frames via Gemini image API (`gemini-2.5-flash-image`).
  - `lint_prompts.py`: Automated prompt validator enforcing MASTER_STYLE_02, camera lenses, and banning watchlist terms.
  - `verify_locks.py`: Validates SHA-256 hashes against lock manifests.
  - Video Generation: Google Omni Flash (and Veo) for 10.0s motion clips synchronized with ~18–20 word VO scripts.
  - Delivery Stack: Stills → Google Flow / Omni Flash → OpenMontage / Assembly → YouTube Studio (`Education` category, AI synthetic disclosure flagged).

## Key Conventions & Rules
- **Fact Classification**: Every scene item must be tagged as `[SOURCE]`, `[HISTORICAL]`, `[RECONSTRUCTION]`, or `[CINEMATIC]`. Never present reconstruction as source fact.
- **Permanent IDs**:
  - Characters: `VASCO_01`, `PAULO_01`, `COELHO_01`, `DIAS_01` (Bartolomeu Dias, outward leg only), `PILOT_01` (Malindi pilot / Gujarati), `DIOGO_01` (Diogo Dias, Calicut factor), `GASPAR_01` (Gaspar da Gama).
  - Ships: `SHIP_SG01` (*São Gabriel*), `SHIP_SR01` (*São Rafael* - burned at Malindi on return), `SHIP_B01` (*Bérrio*), `SHIP_ST01` (*Supply Ship* - broken up at Mossel Bay).
- **Master Styles**:
  - `MASTER_STYLE_01`: Benchmark graphic novel/controlled linework for early Chapter 1 Lisbon scenes.
  - `MASTER_STYLE_02`: Active standard — immersive European historical-painting realism, tenebrist/Rembrandt lighting, tactile textures, no modern CGI gloss.
- **Strict Single-Version Policy (`v1` only)**: Never create `v2`, `v3` filenames for images or lock files. Maintain canonical `v1` in-place (`CH01-EPxx-Sxx-v1.png`, `CH01-EPxx-lock-v1.md`).
- **The 3 Physical Details Law**: Banned empty adjectives (`cinematic`, `epic`, `masterpiece`). Every shot requires: (1) Environmental pressure, (2) Body micro-action, (3) Sound/visual anchor.
- **Definition of Done Gates**: (1) Ravenstein-verified scene records → (2) `lint_prompts.py` exits 0 → (3) Stills generated as `v1` → (4) Reviews in `production/reviews/` with SHA-256 → (5) Owner approval recorded in `production/approval-log.md` → (6) Registries updated → (7) Lock manifest verified via `verify_locks.py`.
- **Security**: Never expose, log, commit, or save `GEMINI_API_KEY` to disk.

## Ongoing Decisions & Discoveries
- **2026-08-24**: Shifted primary medium from comic illustration (`MASTER_STYLE_01`) to immersive European historical oil-painting docuseries (`MASTER_STYLE_02`).
- **2026-08-26**: Action dramatization implemented for Episode 3 (Cape of Good Hope); fleet supply ship `SHIP_ST01` dismantled and burned at Mossel Bay per account.
- **2026-09-02**: Episode 5 (Mombasa to Malindi) introduces Swahili coast maritime dynamics, night sabotage, and alliance with the Sultan of Malindi.
- **2026-09-08**: Voiceover timing rule established: Capped at 18–20 words (~8.3–9.2s read time) to match Google Omni Flash 10.0-second video clip limits.
- **2026-09-11**: Generated v1 stills for Episode 7 (Calicut & The Zamorin's Court); YouTube 3-element mobile thumbnail rules enforced.
- **2026-09-12**: Disambiguated `DIOGO_01` (Diogo Dias, ashore factor) from `DIAS_01` (Bartolomeu Dias). Created `reference/anachronism-watchlist.md` and `lint_prompts.py` after catching out-of-period guns, fabrics, and instruments. Locked Episodes 8 and 9 stills.
- **2026-09-13**: Enforced strict single-version `v1` naming mandate across the project. Approved EP10 S01 & S02 canonical stills under this policy.
- **2026-09-21**: Post-publish analytics audit of Episode 8 (`Ambushed in India`) revealed critical distribution bottleneck: 1:21 horizontal runtime falls into an algorithmic dead zone (suppressed Browse impressions at 44 total despite elite 72.8% retention / 0:59 AVD). Diagnosed passive/dark S01 thumbnail and Lisbon search term mismatch. Formulated immediate turnaround plan: high-contrast thumbnail, companion 9:16 Shorts funnel, and full 12–15 minute Documentary Supercut (Episodes 1–8) to drive 4,000 watch hours for monetization.
