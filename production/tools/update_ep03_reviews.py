"""Update Episode 3 scene reviews with v1 and dramatized v2 candidates and SHA-256 hashes."""

import hashlib
import pathlib

PROJECT_ROOT = pathlib.Path(__file__).resolve().parent.parent.parent
IMAGES_DIR = PROJECT_ROOT / "images" / "episode-03"
REVIEWS_DIR = PROJECT_ROOT / "production" / "reviews"

SCENES = [
    {
        "id": "CH01-EP03-S01",
        "title": "Careening and Wood Gathering at St Helena Bay",
        "date": "4–7 November 1497",
        "v1": "CH01-EP03-S01-v1.png",
        "v2": "CH01-EP03-S01-v2.png",
        "desc_v1": "Calm beach maintenance encampment at St Helena Bay.",
        "desc_v2": "High-drama visceral scene: massive carrack heeled on sand spit, black pitch smoke, frantic scraping of barnacles, Vasco roaring orders to armed sentries.",
    },
    {
        "id": "CH01-EP03-S02",
        "title": "First Encounter on the Strand",
        "date": "7–8 November 1497",
        "v1": "CH01-EP03-S02-v1.png",
        "v2": "CH01-EP03-S02-v2.png",
        "desc_v1": "Quiet encounter on dunes with hawk-bells and beads.",
        "desc_v2": "Breath-holding psychological standoff on windblown dunes: sand stinging faces, glinting brass bells, fingers hovering near daggers and fire-hardened spears.",
    },
    {
        "id": "CH01-EP03-S03",
        "title": "Skirmish on the Beach",
        "date": "10–12 November 1497",
        "v1": "CH01-EP03-S03-v1.png",
        "v2": "CH01-EP03-S02-v2.png",
        "desc_v1": "Surf retreat with spears falling into sand.",
        "desc_v2": "Explosive surf battle: blood in foam, wooden spears raining down, Vasco wounded in thigh gripping the gunwale in fury, crossbow firing through spray.",
    },
    {
        "id": "CH01-EP03-S04",
        "title": "Battling the Cape Headwinds",
        "date": "18–20 November 1497",
        "v1": "CH01-EP03-S04-v1.png",
        "v2": "CH01-EP03-S04-v2.png",
        "desc_v1": "Offshore tacking in heavy grey seas.",
        "desc_v2": "Cataclysmic tempest at the Cape of Storms: 45-degree roll, colossal black wave towering over deck, lightning illuminating black Cape cliffs, Vasco defying the gale.",
    },
    {
        "id": "CH01-EP03-S05",
        "title": "Rounding the Cape of Good Hope",
        "date": "22 November 1497",
        "v1": "CH01-EP03-S05-v1.png",
        "v2": "CH01-EP03-S05-v2.png",
        "desc_v1": "Midday rounding with four ships in formation.",
        "desc_v2": "Glorious emotional triumph: golden god-rays bursting through black storm clouds, red Order of Christ crosses glowing, trumpets blaring, weeping sailors embracing.",
    },
    {
        "id": "CH01-EP03-S06",
        "title": "Music and Trade at Mossel Bay",
        "date": "25–27 November 1497",
        "v1": "CH01-EP03-S06-v1.png",
        "v2": "CH01-EP03-S06-v2.png",
        "desc_v1": "Lively beach flute music and ox trade.",
        "desc_v2": "Exuberant, swirling celebration on sand: hypnotic multi-part reed flutes, dust kicking up under stomping feet, scarlet caps bartered for a magnificent black ox.",
    },
    {
        "id": "CH01-EP03-S07",
        "title": "Breaking Up the Supply Ship",
        "date": "1–4 December 1497",
        "v1": "CH01-EP03-S07-v1.png",
        "v2": "CH01-EP03-S07-v2.png",
        "desc_v1": "Dusk burning of supply ship on sand spit.",
        "desc_v2": "Haunting midnight sacrificial inferno: roaring orange flames engulfing charred oak ribs, swirling embers in starry sky, Vasco watching in somber resolve.",
    },
    {
        "id": "CH01-EP03-S08",
        "title": "Departure into the Unknown East",
        "date": "8 December 1497",
        "v1": "CH01-EP03-S08-v1.png",
        "v2": "CH01-EP03-S08-v2.png",
        "desc_v1": "Morning departure of three surviving vessels.",
        "desc_v2": "Monumental cinematic finale: three battle-scarred carracks slicing through radiant sunrise on deep blue Indian Ocean, African mountains receding into purple mist.",
    },
]


def sha256_file(p: pathlib.Path) -> str:
    h = hashlib.sha256()
    h.update(p.read_bytes())
    return h.hexdigest()


def main():
    REVIEWS_DIR.mkdir(parents=True, exist_ok=True)

    print("Updating Episode 3 reviews with v1 and dramatized v2...")
    for s in SCENES:
        p1 = IMAGES_DIR / s["v1"]
        p2 = IMAGES_DIR / s["v2"]
        sha1 = sha256_file(p1)
        sha2 = sha256_file(p2)

        content = f"""# Scene Review: {s['id']}

* **Title:** {s['title']}
* **Date:** {s['date']}
* **Status:** CANDIDATE REVIEW — PENDING SELECTION / APPROVAL

---

## Candidate Stills

### Option 1: Standard Version (`v1`)
* **Image File:** [`images/episode-03/{s['v1']}`](../../images/episode-03/{s['v1']})
* **SHA-256:** `{sha1}`
* **Description:** {s['desc_v1']}

### Option 2: Dramatized Version (`v2` — RECOMMENDED)
* **Image File:** [`images/episode-03/{s['v2']}`](../../images/episode-03/{s['v2']})
* **SHA-256:** `{sha2}`
* **Description:** {s['desc_v2']}

---

## Visual & Historical Verification

* **Master Style:** `MASTER_STYLE_02` (High-drama European historical oil painting, textured chiaroscuro, cinematic depth)
* **Character Continuity:** `VASCO_01` in mid-voyage battle-tested state (dark unkempt beard, salt-stained wool, bandaged thigh wound in S03–S05).
* **Ship Continuity:** 
  - Scenes 01–06: 4-ship fleet (`SHIP_SG01`, `SR01`, `B01`, `ST01`).
  - Scene 07: Sacrificial burning of `SHIP_ST01` on sand spit.
  - Scene 08: 3-ship fleet entering Indian Ocean.
* **Audio & Voiceover:** High-octane documentary script and multi-track `[AUDIO_TAGS]` in `scenes/{s['id']}.md`.
"""
        rev_path = REVIEWS_DIR / f"{s['id']}-review.md"
        rev_path.write_text(content, encoding="utf-8")
        print(f"Updated: {rev_path.name}")

    print("All review records updated.")


if __name__ == "__main__":
    main()
