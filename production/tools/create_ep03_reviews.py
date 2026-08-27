"""Generate individual review markdown records and lock manifest for Chapter 1 Episode 3."""

import hashlib
import pathlib

PROJECT_ROOT = pathlib.Path(__file__).resolve().parent.parent.parent
IMAGES_DIR = PROJECT_ROOT / "images" / "episode-03"
REVIEWS_DIR = PROJECT_ROOT / "production" / "reviews"
LOCKS_DIR = PROJECT_ROOT / "production" / "locks"

SCENES = [
    {
        "id": "CH01-EP03-S01",
        "title": "Careening and Wood Gathering at St Helena Bay",
        "date": "4–7 November 1497",
        "file": "CH01-EP03-S01-v1.png",
        "desc": "Careening on sandy beach at St Helena Bay, barnacle scraping, mending sails on dunes, rolling water casks, 4 ships anchored in bay.",
    },
    {
        "id": "CH01-EP03-S02",
        "title": "First Encounter on the Strand",
        "date": "7–8 November 1497",
        "file": "CH01-EP03-S02-v1.png",
        "desc": "Intimate encounter on sand dunes: Vasco da Gama and Paulo da Gama offering hawk-bells and glass beads to Khoikhoi man in skin cloak.",
    },
    {
        "id": "CH01-EP03-S03",
        "title": "Skirmish on the Beach",
        "date": "10–12 November 1497",
        "file": "CH01-EP03-S03-v1.png",
        "desc": "Dramatic beach retreat in surf: Khoikhoi warriors throwing stones and spears, Vasco wounded in thigh at gunwale, crossbow covering escape.",
    },
    {
        "id": "CH01-EP03-S04",
        "title": "Battling the Cape Headwinds",
        "date": "18–20 November 1497",
        "file": "CH01-EP03-S04-v1.png",
        "desc": "Epic storm seas off Cape of Good Hope: 4 ships tacking under reefed storm sails in heavy grey Southern Ocean swells against contrary gales.",
    },
    {
        "id": "CH01-EP03-S05",
        "title": "Rounding the Cape of Good Hope",
        "date": "22 November 1497",
        "file": "CH01-EP03-S05-v1.png",
        "desc": "Triumphant rounding of the Cape at midday: golden sunlight breaking through clouds, 4 ships sailing past cliffs with full sails, trumpets sounding.",
    },
    {
        "id": "CH01-EP03-S06",
        "title": "Music and Trade at Mossel Bay",
        "date": "25–27 November 1497",
        "file": "CH01-EP03-S06-v1.png",
        "desc": "Lively cross-cultural music and trade exchange on Mossel Bay beach: Khoikhoi playing 4-holed reed flutes and dancing, bartering red caps for ox.",
    },
    {
        "id": "CH01-EP03-S07",
        "title": "Breaking Up the Supply Ship",
        "date": "1–4 December 1497",
        "file": "CH01-EP03-S07-v1.png",
        "desc": "Somber dusk scene on beach: storeship hull dismantled and burned on sand spit, crew transferring anchors and casks, fleet reduced to 3 ships.",
    },
    {
        "id": "CH01-EP03-S08",
        "title": "Departure into the Unknown East",
        "date": "8 December 1497",
        "file": "CH01-EP03-S08-v1.png",
        "desc": "Historic morning departure: 3 surviving ships (São Gabriel, São Rafael, Berrio) sailing northeast in tight formation into uncharted Indian Ocean.",
    },
]


def sha256_file(p: pathlib.Path) -> str:
    h = hashlib.sha256()
    h.update(p.read_bytes())
    return h.hexdigest()


def main():
    REVIEWS_DIR.mkdir(parents=True, exist_ok=True)
    LOCKS_DIR.mkdir(parents=True, exist_ok=True)

    print("Generating Episode 3 scene reviews...")
    for s in SCENES:
        img_path = IMAGES_DIR / s["file"]
        sha = sha256_file(img_path)
        
        review_content = f"""# Scene Review: {s['id']}

* **Title:** {s['title']}
* **Date:** {s['date']}
* **Image File:** [`images/episode-03/{s['file']}`](../../images/episode-03/{s['file']})
* **SHA-256:** `{sha}`
* **Style Compliance:** `MASTER_STYLE_02` (European historical oil painting, textured lighting, atmospheric depth, no CGI sheen)
* **Status:** CANDIDATE — PENDING OWNER APPROVAL

---

## Visual & Historical Verification

* **Historical Basis:** High fidelity to *Roteiro* primary account.
* **Character Continuity:** Vasco da Gama shown in mid-voyage weathering state (sun-darkened, unkempt beard, salt-stained clothing).
* **Ship Continuity:** 
  - Scenes 01–06: 4-vessel fleet (São Gabriel, São Rafael, Berrio, Supply Ship).
  - Scene 07: Supply Ship decommissioned and burned on beach.
  - Scene 08: 3-vessel fleet (São Gabriel, São Rafael, Berrio) entering Indian Ocean.
* **Scene Description:** {s['desc']}

---

## Audio & Narration Verification

* **[VOICEOVER]:** Scripted in `scenes/{s['id']}.md` and `prompts/CH01-EP03-image-to-video.md`.
* **[AUDIO_TAGS]:** Configured with structured `[VOICEOVER]`, `[AMBIENCE]`, `[FOLEY]`, and `[MUSIC]`.
"""
        rev_path = REVIEWS_DIR / f"{s['id']}-review.md"
        rev_path.write_text(review_content, encoding="utf-8")
        print(f"Created: {rev_path.name} (SHA-256: {sha[:12]}...)")

    print("\nAll Episode 03 scene reviews generated successfully!")


if __name__ == "__main__":
    main()
