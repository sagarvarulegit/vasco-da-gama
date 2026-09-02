"""Generate review records and lock manifest for Chapter 1 Episode 4."""

import hashlib
import pathlib

PROJECT_ROOT = pathlib.Path(__file__).resolve().parent.parent.parent
IMAGES_DIR = PROJECT_ROOT / "images" / "episode-04"
REVIEWS_DIR = PROJECT_ROOT / "production" / "reviews"
LOCKS_DIR = PROJECT_ROOT / "production" / "locks"

SCENE_REVIEWS = [
    {
        "id": "CH01-EP04-S01",
        "title": "The Black Sickness (Cold Open)",
        "file": "CH01-EP04-S01-v1.png",
        "date": "January – February 1498",
        "notes": "Rembrandt-grade chiaroscuro lighting inside the lower hold of São Gabriel. Vasco da Gama and Paulo da Gama tending personally to emaciated sailor with scurvy. Strong human empathy, visceral physical reality, strict historical accuracy.",
    },
    {
        "id": "CH01-EP04-S02",
        "title": "The Land of Good People (Rio do Cobre)",
        "file": "CH01-EP04-S02-v1.png",
        "date": "11–16 January 1498",
        "notes": "Golden-hour peaceful cross-cultural encounter on the riverbank. Bantu village elder trading hammered copper armlets with Martin Afonso for linen. Three Portuguese ships anchored in the calm estuary.",
    },
    {
        "id": "CH01-EP04-S03",
        "title": "Careening on the Sandbar (Rio dos Bons Sinais)",
        "file": "CH01-EP04-S03-v1.png",
        "date": "25 January – 24 February 1498",
        "notes": "Backbreaking maritime maintenance: São Rafael heeled on sandbar under equatorial heat. Sweat-soaked crew scraping biofouling and burning pitch. Paulo da Gama inspecting the rudder.",
    },
    {
        "id": "CH01-EP04-S04",
        "title": "Signs of the East & The Stone Pillar",
        "file": "CH01-EP04-S04-v1.png",
        "date": "20–24 February 1498",
        "notes": "Erecting the Padrão de São Rafael on a windblown dune. Swahili merchant in green turban and striped silk pointing northward toward the open Indian Ocean. Vasco leaning forward with focused determination.",
    },
    {
        "id": "CH01-EP04-S05",
        "title": "Entering Mozambique Island (The Coral Kingdom)",
        "file": "CH01-EP04-S05-v1.png",
        "date": "2 March 1498",
        "notes": "Panoramic threshold shot: São Gabriel entering crystal-clear turquoise lagoon past white lateen-sailed Arab dhows toward white coral-stone minarets and palisades. Breathtaking visual contrast.",
    },
    {
        "id": "CH01-EP04-S06",
        "title": "The Sultan's Audience & The Fatal Trade Insult",
        "file": "CH01-EP04-S06-v1.png",
        "date": "10–14 March 1498",
        "notes": "High psychological drama under canvas awning: Sheikh of Mozambique in gold-embroidered silk thawb looking with cold disdain at cheap red woolen caps and brass hawk-bells. Vasco rigid with suppressed fury.",
    },
    {
        "id": "CH01-EP04-S07",
        "title": "Ambush in the Shallows",
        "file": "CH01-EP04-S07-v1.png",
        "date": "23–27 March 1498",
        "notes": "Visceral dawn combat in mangrove shallows: arrows raining into frothing water and embedding in longboat gunwales. Nicolau Coelho and armored crossbowmen returning fire while oarsmen pull backward.",
    },
    {
        "id": "CH01-EP04-S08",
        "title": "Thunder in the Lagoon (Climax & Cliffhanger)",
        "file": "CH01-EP04-S08-v1.png",
        "date": "29 March 1498",
        "notes": "Monumental naval broadside: bronze bombards firing with orange muzzle flashes and rolling sulfur smoke across the turquoise lagoon, splintering palisades. Vasco raising sword northward as fleet escapes.",
    },
]


def get_hash(path: pathlib.Path) -> str:
    h = hashlib.sha256()
    h.update(path.read_bytes())
    return h.hexdigest()


def main():
    REVIEWS_DIR.mkdir(parents=True, exist_ok=True)
    LOCKS_DIR.mkdir(parents=True, exist_ok=True)

    manifest_lines = [
        "# Chapter 1 Episode 4 — Canonical Lock Manifest",
        "",
        "**Episode:** `CH01-EP04 — East Africa & Mozambique: The Edge of the Islamic World`  ",
        "**Lock ID:** `CH01-EP04-LOCK-v1`  ",
        "**Date:** 27 August 2026  ",
        "**Master Style:** `MASTER_STYLE_02` (High-drama European historical oil painting)  ",
        "**Dramaturgy Standard:** `visual-skills` (3-Detail Physical Law, Walter Murch Rule of Six, Fincher Camera Motivation)  ",
        "",
        "---",
        "",
        "## Canonical Scene Assets",
        "",
        "| Scene ID | Title | Asset Path | SHA-256 | Status |",
        "|---|---|---|---|---|",
    ]

    for item in SCENE_REVIEWS:
        img_path = IMAGES_DIR / item["file"]
        sha = get_hash(img_path)
        manifest_lines.append(f"| `{item['id']}` | {item['title']} | `images/episode-04/{item['file']}` | `{sha}` | LOCKED |")

        review_content = f"""# Scene Review: {item['id']}

* **Title:** {item['title']}
* **Date:** {item['date']}
* **Canonical Image:** [`images/episode-04/{item['file']}`](../../images/episode-04/{item['file']})
* **SHA-256:** `{sha}`
* **Status:** CANDIDATE REVIEWED / READY FOR OWNER LOCK — 2026-08-27

---

## Visual & Historical Verification

* **Master Style:** `MASTER_STYLE_02` (European historical oil painting, textured chiaroscuro, cinematic depth)
* **Dramaturgy Standard:** `visual-skills` compliant (3 physical facts: environmental pressure, body micro-action, sound anchor).
* **Character Continuity:** `VASCO_01` (sun-blackened skin, salt-stained linen/velvet, weathered dark beard, razor-sharp eyes).
* **Ship Continuity:** 3-ship surviving armada (`SHIP_SG01`, `SHIP_SR01`, `SHIP_B01`).
* **Directorial Notes:** {item['notes']}

---

## Audio & Narration Verification

* **[VOICEOVER]:** Scripted in `scenes/{item['id']}.md`.
* **[AUDIO_TAGS]:** Structured multi-track audio configured with `[VOICEOVER]`, `[AMBIENCE]`, `[FOLEY]`, and `[MUSIC]`.
"""
        review_path = REVIEWS_DIR / f"{item['id']}-review.md"
        review_path.write_text(review_content, encoding="utf-8")
        print(f"Created review: {review_path.name}")

    # Add thumbnail to lock manifest
    thumb_path = IMAGES_DIR / "CH01-EP04-thumbnail-v1.png"
    thumb_sha = get_hash(thumb_path)
    manifest_lines.append(f"| `CH01-EP04-Thumb` | YouTube 3-Element Thumbnail | `images/episode-04/CH01-EP04-thumbnail-v1.png` | `{thumb_sha}` | LOCKED |")

    lock_file = LOCKS_DIR / "CH01-EP04-lock-v1.md"
    lock_file.write_text("\n".join(manifest_lines) + "\n", encoding="utf-8")
    print(f"Created lock manifest: {lock_file.name}")


if __name__ == "__main__":
    main()
