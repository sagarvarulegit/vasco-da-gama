"""Generate still frames (v1) for Chapter 1 Episode 7 (Calicut: The Zamorin's Court) using visual-skills dramaturgy."""

import pathlib
import subprocess
import sys

PROJECT_ROOT = pathlib.Path(__file__).resolve().parent.parent.parent
IMAGES_EP07_DIR = PROJECT_ROOT / "chapters" / "chapter-01-first-voyage" / "episode-07-calicut" / "images"
PROMPT_GEN_SCRIPT = PROJECT_ROOT / "production" / "tools" / "gemini_image_generate.py"

EP07_PROMPTS = [
    {
        "id": "CH01-EP07-S01",
        "output": "CH01-EP07-S01-v1.png",
        "prompt": (
            "MASTER_STYLE_02. 35mm lens, eye-level medium shot, humid tropical midday light, 21 May 1498. "
            "Inside an open-sided coconut-timber warehouse on the Calicut beachfront, Malabar Coast, India. "
            "In the foreground, Portuguese convict scout NUNES_01 (gaunt, sun-scorched face, salt-stained linen shirt, rough wool trousers, wide astonished eyes) "
            "stands face-to-face with two wealthy Tunisian Moor merchants (MONCAIDE_01 circle) in flowing patterned silk kaftans and wrapped turbans, "
            "one merchant's hand frozen mid-gesture of disbelief. "
            "Around them, coarse jute sacks of black pepper split open to spill glossy peppercorns across the packed-earth floor, "
            "brass drinking cups glinting on a low teak table. "
            "Through the open wooden arches behind, a crowded beach market bustles under coconut palms with stacked timber and curious onlookers pressing closer. "
            "European historical oil painting, tactile jute, silk and sun-warmed wood, no text, no modern objects."
        ),
    },
    {
        "id": "CH01-EP07-S02",
        "output": "CH01-EP07-S02-v1.png",
        "prompt": (
            "MASTER_STYLE_02. 35mm lens, wide sunlit composition, golden morning light, 22 May 1498. "
            "On the quarterdeck of the weathered Portuguese flagship SHIP_SG01 riding at anchor off Calicut. "
            "In the center, MONCAIDE_01 (Tunisian Moor merchant in dark crimson silk tunic and white turban) stands with both arms flung triumphantly skyward, "
            "mouth open mid-proclamation. "
            "Around him, a dozen battle-hardened Portuguese mariners in salt-bleached canvas shirts drop to their knees on the scrubbed oak deck, "
            "hands clasped in prayer, tears cutting clean tracks through salt-caked beards. "
            "To one side, VASCO_01 (sun-darkened face, trimmed dark beard, worn dark velvet doublet) grips the oak rail, jaw locked with restrained emotion. "
            "Behind the ship, the calm blue roadstead stretches to the palm-fringed Kerala shoreline in morning haze. "
            "European historical oil painting, weathered oak grain, glistening tear tracks, sea breeze in rigging, no text, no modern vessels."
        ),
    },
    {
        "id": "CH01-EP07-S03",
        "output": "CH01-EP07-S03-v1.png",
        "prompt": (
            "MASTER_STYLE_02. 24mm wide-angle lens, dynamic street-level tracking composition, bright late-morning sunlight filtering through palm fronds, 28 May 1498. "
            "A narrow crowded street in Calicut, Malabar Coast: an elaborate covered palanquin of polished teak with crimson silk curtains sways on thick bamboo poles, "
            "carried by barefoot bearers, with VASCO_01 (weathered face, crimson velvet doublet, polished steel cuirass glinting) half-visible through the parted curtain. "
            "At the head of the escort strides CATUAL_01 (Malabar noble in fine white cotton mundu and gold-bordered shoulder cloth, gripping a tall silver staff of office). "
            "Flanking the palanquin, scores of athletic Nair warriors with bare oiled torsos, white dhotis and knotted topknots march with polished steel broadswords and round brass-studded bucklers, "
            "a curved bronze kombu horn raised mid-blast. "
            "Thousands of onlookers pack carved wooden balconies, clay-tile rooftops and street edges beneath swaying coconut palms. "
            "European historical oil painting, laterite dust in sunbeams, sweat on skin, creaking bamboo poles, no text, no modern structures."
        ),
    },
    {
        "id": "CH01-EP07-S04",
        "output": "CH01-EP07-S04-v1.png",
        "prompt": (
            "MASTER_STYLE_02. 35mm lens, low interior perspective, warm chiaroscuro oil-lamp glow against dark stone, 28 May 1498. "
            "Inside the vast granite mandapa of an ancient Kerala Hindu temple near Calicut: rows of intricately carved stone pillars recede into fragrant gloom, "
            "thousands of small bronze oil diyas flickering ontiered stands. "
            "In the center, VASCO_01 and three Portuguese officers in crimson velvet and steel kneel on the cold granite floor with bowed heads and folded hands, "
            "praying earnestly before a flower-garlanded sanctum doorway they mistake for a Christian altar. "
            "Beside them, bare-chested Brahmin priests wearing sacred white yajnopavita threads across their torsos lean in to press white sandalwood ash onto a sailor's forehead, "
            "one young sailor's eyes darting sideways in frightened doubt. "
            "Thick incense smoke coils through shafts of lamplight over sculpted multi-armed deities. "
            "European historical oil painting, dripping lamp oil, ash paste, cold stone under knees, no text, no modern items."
        ),
    },
    {
        "id": "CH01-EP07-S05",
        "output": "CH01-EP07-S05-v1.png",
        "prompt": (
            "MASTER_STYLE_02. 35mm lens, wide symmetrical composition, dusk lamplight in a vast stone hall, 28 May 1498. "
            "The royal audience hall of the Stone Palace of Calicut: dark polished laterite pillars, heavy hanging bronze oil chandeliers, polished plaster walls. "
            "On a raised dais, the ZAMORIN_01 (Samutiri Raja, powerful middle-aged Malabar king) reclines on a couch draped in deep green velvet, "
            "clad in sheer white Malabar muslin with woven gold kasavu borders, enormous emerald earrings the size of walnuts tugging his earlobes, "
            "fingers heavy with ruby and diamond rings, a pearl necklace cascading over his chest, a wad of betel leaf (paan) staining his lips red. "
            "A bare-chested royal page kneels holding a massive solid-gold spittoon and a brass tray of folded betel leaves. "
            "Before the dais, VASCO_01 in polished steel cuirass over dark crimson velvet bows deeply, both hands extending King Manuel's sealed parchment letter. "
            "Court nobles in white and gold line the shadowed walls. "
            "European historical oil painting, sandalwood haze, gleaming gold and gemstones, rustle of silk, no text, no fantasy crowns."
        ),
    },
    {
        "id": "CH01-EP07-S06",
        "output": "CH01-EP07-S06-v1.png",
        "prompt": (
            "MASTER_STYLE_02. 50mm lens, eye-level tense medium shot, cool morning light through a stone doorway, 29 May 1498. "
            "Inside a dim stone-walled palace warehouse in Calicut: pried-open wooden crates sprawl across the flagstone floor, "
            "displaying the meagre Portuguese gifts — folded rolls of coarse striped cloth, four red woolen caps, six cheap hammered-brass washbasins, "
            "two small wooden casks of butter with one lid knocked askew. "
            "Standing over the goods, wealthy Arab merchant factors in gold-threaded turbans and rich silk robes convulse with open mocking laughter, "
            "one clutching his belly, another flicking a strip of striped cloth dismissively between thumb and forefinger; "
            "beside them, Calicut royal ministers in white mundu exchange contemptuous sideways glances. "
            "In the shadowed background, VASCO_01 stands rigid with knuckles white around his sword hilt, face burning crimson with humiliation beneath his dark beard. "
            "European historical oil painting, clattering brass on stone, coarse wool texture, held-breath tension, no text, no modern plastics."
        ),
    },
    {
        "id": "CH01-EP07-S07",
        "output": "CH01-EP07-S07-v1.png",
        "prompt": (
            "MASTER_STYLE_02. 50mm lens, tight confrontational two-shot, stormy evening: cold blue lightning glare against warm bronze torchlight, 30 May 1498. "
            "The shadowed inner council room of the Zamorin's palace: the ZAMORIN_01 sits upright on a carved teak throne, stern and cold, "
            "one bejewelled hand raised mid-question, emerald earrings catching the torch flame. "
            "Behind the throne, two Arab merchant advisors in dark turbans lean in close, one whispering into the king's ear with a venomous sideways stare at the Portuguese. "
            "Opposite them, VASCO_01 stands resolute in dark doublet and breastplate, rainwater still dripping from his cloak hem, "
            "dark eyes locked on the king, right hand tight on his sword pommel. "
            "Through ornate stone lattice windows, white monsoon lightning forks over black clouds. "
            "European historical oil painting, rain gusts through lattice, dripping steel, held-breath silence between thunderclaps, no text, no cartoonish villainy."
        ),
    },
    {
        "id": "CH01-EP07-S08",
        "output": "CH01-EP07-S08-v1.png",
        "prompt": (
            "MASTER_STYLE_02. 24mm wide-angle lens, low dramatic night composition, torchlight slashing through monsoon rain, 31 May 1498. "
            "The coastal stone compound of Pandarani near Calicut: massive iron-studded teak gates boom shut in the foreground, "
            "a guard's hand slamming the heavy iron bolt home. "
            "Inside the flooded courtyard, VASCO_01 and thirteen Portuguese officers in soaked doublets and cuirasses cluster under a sagging palm-thatch awning, "
            "rain streaming from their beards, hands hovering over sword hilts. "
            "Ringing them, dozens of Malabar guards and Nair soldiers with drawn steel talwars and levelled matchlocks hold sputtering pitch torches that hiss and smoke in the downpour. "
            "Beyond the compound wall, the storm-black ocean heaves under lightning, where the distant silhouettes of SHIP_SG01 and SHIP_SR01 toss in crashing surf. "
            "European historical oil painting, sheeting rain through torch glare, wet iron and stone, crashing breakers, no text, no modern fences."
        ),
    },
    {
        "id": "CH01-EP07-Thumbnail",
        "output": "CH01-EP07-thumbnail-v1.png",
        "prompt": (
            "MASTER_STYLE_02. High-impact historical-painting YouTube thumbnail composition, no text inside the image. "
            "On the left, a powerful close-up of Portuguese commander VASCO_01: sun-darkened weathered face, trimmed dark beard beaded with rain, "
            "fierce dark eyes, polished steel cuirass over crimson velvet catching warm torchlight. "
            "On the right, the imposing ZAMORIN_01 of Calicut: deep brown skin, enormous walnut-sized emerald earrings, cascading pearl necklaces, "
            "white gold-bordered muslin, red betel-stained lips set in a cold stare. "
            "Between them in the middle distance, a glowing Kerala temple doorway ringed with bronze oil lamps and a covered crimson palanquin, "
            "with Portuguese carracks under full sail on a monsoon-grey sea behind. "
            "Extreme chiaroscuro contrast, vivid emerald, gold and crimson against dark monsoon tones, clean uncluttered layout, European historical oil painting, no text, no logos."
        ),
    },
]


def main():
    IMAGES_EP07_DIR.mkdir(parents=True, exist_ok=True)

    for item in EP07_PROMPTS:
        out_path = IMAGES_EP07_DIR / item["output"]
        print(f"[{item['id']}] Generating still: {out_path.name}...")

        cmd = [
            sys.executable,
            str(PROMPT_GEN_SCRIPT),
            "--prompt",
            item["prompt"],
            "--output",
            str(out_path),
        ]

        res = subprocess.run(cmd, capture_output=True, text=True)
        if res.returncode != 0:
            print(f"FAILED {item['id']}: {res.stderr.strip()}", file=sys.stderr)
        else:
            print(f"SUCCESS {item['id']} -> {out_path.name} ({out_path.stat().st_size} bytes)")

    print("\nEpisode 7 Still Generation Complete.")


if __name__ == "__main__":
    main()
