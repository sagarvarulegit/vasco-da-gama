"""Lock Chapter 1 Episode 3 (Cape of Good Hope) canonical stills (v2) and create lock manifest."""

import datetime
import hashlib
import pathlib

PROJECT_ROOT = pathlib.Path(__file__).resolve().parent.parent.parent
IMAGES_DIR = PROJECT_ROOT / "images" / "episode-03"
REVIEWS_DIR = PROJECT_ROOT / "production" / "reviews"
LOCKS_DIR = PROJECT_ROOT / "production" / "locks"
SCENES_DIR = PROJECT_ROOT / "scenes"
APPROVAL_LOG = PROJECT_ROOT / "production" / "approval-log.md"
STORYBOARDS_DIR = PROJECT_ROOT / "storyboards"

SCENES_LOCKED = [
    {
        "id": "CH01-EP03-S01",
        "title": "Careening and Wood Gathering at St Helena Bay",
        "date": "4–7 November 1497",
        "file": "CH01-EP03-S01-v2.png",
        "desc": "High-drama visceral scene: massive carrack heeled on sand spit, black pitch smoke, frantic barnacle scraping, Vasco roaring orders to armed sentries.",
    },
    {
        "id": "CH01-EP03-S02",
        "title": "First Encounter on the Strand",
        "date": "7–8 November 1497",
        "file": "CH01-EP03-S02-v2.png",
        "desc": "Breath-holding psychological standoff on windblown dunes: sand stinging faces, glinting brass hawk-bells, fingers hovering near daggers and fire-hardened spears.",
    },
    {
        "id": "CH01-EP03-S03",
        "title": "Skirmish on the Beach",
        "date": "10–12 November 1497",
        "file": "CH01-EP03-S03-v2.png",
        "desc": "Explosive surf battle: blood in foam, wooden spears raining down, Vasco wounded in thigh gripping the gunwale in fury, crossbow firing through spray.",
    },
    {
        "id": "CH01-EP03-S04",
        "title": "Battling the Cape Headwinds",
        "date": "18–20 November 1497",
        "file": "CH01-EP03-S04-v2.png",
        "desc": "Cataclysmic tempest at the Cape of Storms: 45-degree roll, colossal black wave towering over deck, lightning illuminating black Cape cliffs, Vasco defying the gale.",
    },
    {
        "id": "CH01-EP03-S05",
        "title": "Rounding the Cape of Good Hope",
        "date": "22 November 1497",
        "file": "CH01-EP03-S05-v2.png",
        "desc": "Glorious emotional triumph: golden god-rays bursting through black storm clouds, red Order of Christ crosses glowing, trumpets blaring, weeping sailors embracing.",
    },
    {
        "id": "CH01-EP03-S06",
        "title": "Music and Trade at Mossel Bay",
        "date": "25–27 November 1497",
        "file": "CH01-EP03-S06-v2.png",
        "desc": "Exuberant, swirling celebration on sand: hypnotic multi-part reed flutes, dust kicking up under stomping feet, scarlet caps bartered for a magnificent black ox.",
    },
    {
        "id": "CH01-EP03-S07",
        "title": "Breaking Up the Supply Ship",
        "date": "1–4 December 1497",
        "file": "CH01-EP03-S07-v2.png",
        "desc": "Haunting midnight sacrificial inferno: roaring orange flames engulfing charred oak ribs, swirling embers in starry sky, Vasco watching in somber resolve.",
    },
    {
        "id": "CH01-EP03-S08",
        "title": "Departure into the Unknown East",
        "date": "8 December 1497",
        "file": "CH01-EP03-S08-v2.png",
        "desc": "Monumental cinematic finale: three battle-scarred carracks slicing through radiant sunrise on deep blue Indian Ocean, African mountains receding into purple mist.",
    },
]


def sha256_file(p: pathlib.Path) -> str:
    h = hashlib.sha256()
    h.update(p.read_bytes())
    return h.hexdigest()


def main():
    today = datetime.datetime.now().strftime("%Y-%m-%d")
    manifest_rows = []

    # 1. Update Review Records to Approved Canonical
    for s in SCENES_LOCKED:
        img_path = IMAGES_DIR / s["file"]
        sha = sha256_file(img_path)
        manifest_rows.append((s["id"], s["title"], s["date"], s["file"], sha, s["desc"]))

        rev_text = f"""# Scene Review: {s['id']}

* **Title:** {s['title']}
* **Date:** {s['date']}
* **Canonical Image:** [`images/episode-03/{s['file']}`](../../images/episode-03/{s['file']})
* **SHA-256:** `{sha}`
* **Status:** APPROVED / CANONICAL — {today} (CH01-EP03-LOCK-v1)

---

## Visual & Historical Verification

* **Master Style:** `MASTER_STYLE_02` (High-drama European historical oil painting, textured chiaroscuro, cinematic depth)
* **Character Continuity:** `VASCO_01` in mid-voyage battle-tested state (dark unkempt beard, salt-stained wool, bandaged thigh wound in S03–S05).
* **Ship Continuity:** 
  - Scenes 01–06: 4-ship fleet (`SHIP_SG01`, `SR01`, `B01`, `ST01`).
  - Scene 07: Sacrificial burning of `SHIP_ST01` on sand spit.
  - Scene 08: 3-ship fleet entering Indian Ocean.
* **Scene Description:** {s['desc']}

---

## Audio & Narration Verification

* **[VOICEOVER]:** Scripted in `scenes/{s['id']}.md` and `prompts/CH01-EP03-image-to-video.md`.
* **[AUDIO_TAGS]:** Structured multi-track audio configured with `[VOICEOVER]`, `[AMBIENCE]`, `[FOLEY]`, and `[MUSIC]`.
"""
        rev_path = REVIEWS_DIR / f"{s['id']}-review.md"
        rev_path.write_text(rev_text, encoding="utf-8")

        # Update Scene File with Lock Status header
        scene_path = SCENES_DIR / f"{s['id']}.md"
        scene_text = scene_path.read_text(encoding="utf-8")
        header_tag = f"**Image status:** APPROVED / CANONICAL — [{s['file']}](../images/episode-03/{s['file']}), reviewed {today}\n**Lock status:** LOCKED / CANONICAL — CH01-EP03-LOCK-v1\n\n"
        if "**Image status:**" not in scene_text:
            scene_text = scene_text.replace("## Source Facts", header_tag + "## Source Facts")
            scene_path.write_text(scene_text, encoding="utf-8")

    # 2. Append to Approval Log
    log_entry = f"\n\n## {today} — Chapter 1 Episode 3 (Cape of Good Hope) Stills Canonical Approval (Option A)\n\n"
    log_entry += "Owner approved all eight dramatized `v2` candidate stills as canonical for Episode 3:\n\n"
    for sid, title, date, f, sha, _ in manifest_rows:
        log_entry += f"- **`{sid}`** ({title}): [`images/episode-03/{f}`](images/episode-03/{f}) — SHA-256: `{sha}`\n"

    app_text = APPROVAL_LOG.read_text(encoding="utf-8") if APPROVAL_LOG.exists() else "# Approval Log\n"
    APPROVAL_LOG.write_text(app_text + log_entry, encoding="utf-8")

    # 3. Create Episode 3 Lock Manifest
    lock_manifest = f"""# CH01-EP03-LOCK-v1 Manifest

**Episode:** `CH01-EP03 — Cape of Good Hope`  
**Lock Date:** {today}  
**Visual Style:** `MASTER_STYLE_02` (High-drama European historical oil painting)  
**Status:** CANONICAL STILLS LOCKED  

---

## Locked Canonical Frames

| Scene ID | Title | Date | File | SHA-256 Hash |
|---|---|---|---|---|
"""
    for sid, title, date, f, sha, _ in manifest_rows:
        lock_manifest += f"| **`{sid}`** | {title} | {date} | [`images/episode-03/{f}`](../../images/episode-03/{f}) | `{sha}` |\n"

    lock_manifest += """
---

## Continuity Rules & Post-Lock Protections

1. **Immutable Stills:** Locked frames under `images/episode-03/` must not be overwritten or modified without an explicit version increment (`v3`).
2. **Fleet Progression:**
   - S01–S06: Four vessels (`SHIP_SG01`, `SHIP_SR01`, `SHIP_B01`, `SHIP_ST01`).
   - S07: Planned destruction of `SHIP_ST01`.
   - S08+: Three vessels (`SHIP_SG01`, `SHIP_SR01`, `SHIP_B01`).
3. **Character Progression:** `VASCO_01` carries his bandaged leg wound sustained in St Helena Bay through the Cape rounding.
4. **Google Omni Flash Pipeline:** Video motion prompts are anchored directly to these locked stills.
"""
    lock_path = LOCKS_DIR / "CH01-EP03-lock-v1.md"
    lock_path.write_text(lock_manifest, encoding="utf-8")

    # 4. Assemble Episode 3 Storyboard
    sb_content = f"""# Storyboard — Chapter 1 Episode 3: Cape of Good Hope

**Lock Manifest:** [`production/locks/CH01-EP03-lock-v1.md`](../production/locks/CH01-EP03-lock-v1.md)  
**Visual Style:** `MASTER_STYLE_02` (High-Drama European Historical Oil Painting)  
**Date:** {today}

---

"""
    for sid, title, date, f, sha, desc in manifest_rows:
        sb_content += f"""## {sid} — {title}

* **Date:** {date}
* **Image:** ![{title}](../images/episode-03/{f})
* **Description:** {desc}
* **SHA-256:** `{sha}`

---

"""
    sb_path = STORYBOARDS_DIR / "CH01-EP03-storyboard.md"
    sb_path.write_text(sb_content, encoding="utf-8")

    print(f"Successfully locked Chapter 1 Episode 3 (CH01-EP03-LOCK-v1)!")


if __name__ == "__main__":
    main()
