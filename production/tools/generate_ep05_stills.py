"""Generate still frames (v1) for Chapter 1 Episode 5 (Mombasa to Malindi) using visual-skills dramaturgy."""

import os
import pathlib
import subprocess
import sys

PROJECT_ROOT = pathlib.Path(__file__).resolve().parent.parent.parent
IMAGES_EP05_DIR = PROJECT_ROOT / "chapters" / "chapter-01-first-voyage" / "episode-05-mombasa-malindi" / "images"
PROMPT_GEN_SCRIPT = PROJECT_ROOT / "production" / "tools" / "gemini_image_generate.py"

EP05_PROMPTS = [
    {
        "id": "CH01-EP05-S01",
        "output": "CH01-EP05-S01-v1.png",
        "prompt": (
            "MASTER_STYLE_02. 24mm wide angle, dynamic low water-level shot, harsh equatorial midday light, 5 April 1498. "
            "The Shoals of São Rafael off East Africa. The Portuguese three-masted carrack SHIP_SR01 sits stranded at a slight angle on a sunlit coral shelf in crystal-clear turquoise shallows. "
            "In the foreground, half a dozen sunburned Portuguese mariners in rolled canvas trousers wade waist-deep in the sparkling water, straining with raw physical effort to haul a thick dripping hemp kedge cable. "
            "On the tilted wooden ship deck, PAULO_01 leans over the oak bulwark shouting commands. In the deep blue distance, SHIP_SG01 rides at anchor. "
            "European historical oil painting, immense tactile detail, chiaroscuro sunlight, no text, no modern boats."
        )
    },
    {
        "id": "CH01-EP05-S02",
        "output": "CH01-EP05-S02-v1.png",
        "prompt": (
            "MASTER_STYLE_02. 35mm lens, wide cinematic view, clear morning tropical sunlight, 7 April 1498. "
            "The Roadstead of Mombasa. On the quarterdeck of the weathered Portuguese flagship SHIP_SG01, VASCO_01 stands beside COELHO_01, looking with guarded suspicion toward the formidable island city. "
            "Below the wooden hull in the emerald sea, a traditional Swahili sewn dhow (zambuco) with lateen sail rests alongside; Swahili men in white linen tunics and turbans hold up woven baskets filled with bright oranges and sugar cane. "
            "In the background across the water, the gleaming whitewashed coral-stone ramparts and minarets of Mombasa rise proudly against a deep blue sky. "
            "European historical oil painting, immense depth, rich textures of oak and silk, no text, no modern structures."
        )
    },
    {
        "id": "CH01-EP05-S03",
        "output": "CH01-EP05-S03-v1.png",
        "prompt": (
            "MASTER_STYLE_02. 50mm portrait lens, eye-level atmospheric interior shot, warm chiaroscuro lighting, 8 April 1498. "
            "Inside a wealthy Gujarati merchant's house in Mombasa. In the center, two wealthy Indian merchants in fine draped cream cotton robes and intricately wrapped turbans burn sweet sandalwood incense from brass censers before a decorated stone niche containing an ornate painted devotional icon. "
            "On the left, two rugged Portuguese convicts (degredados) in tattered canvas doublets and wool trousers stand in awe, one crossing himself with dirt-stained hands. "
            "In the background, ornate carved Swahili wooden archways lead to a sunlit coral-stone courtyard. "
            "European historical oil painting, delicate incense smoke in sunbeams, deep psychological nuance, no modern items."
        )
    },
    {
        "id": "CH01-EP05-S04",
        "output": "CH01-EP05-S04-v1.png",
        "prompt": (
            "MASTER_STYLE_02. 28mm wide angle, dynamic high-speed action composition, overcast dramatic tropical daylight, 10 April 1498. "
            "The harbor mouth of Mombasa. On the deck of the Portuguese flagship SHIP_SG01, total chaos erupts as sails flap wildly and a massive iron anchor plunges with explosive spray into the churning green sea. "
            "In the foreground, two Swahili men in white turbans and tunics leap frantically over the wooden ship rail into the swirling water below. "
            "On the quarterdeck, VASCO_01 grips his sword hilt, shouting furious commands to his crew who are frantically securing lines. "
            "In the background, churning coral reef breakers and the fortified white walls of Mombasa. "
            "European historical oil painting, incredible kinetic motion, splashing sea spray, chiaroscuro contrast, no text."
        )
    },
    {
        "id": "CH01-EP05-S05",
        "output": "CH01-EP05-S05-v1.png",
        "prompt": (
            "MASTER_STYLE_02. 35mm lens, intense nocturnal chiaroscuro composition, flickering torchlight and charcoal brazier glow, 11 April 1498. "
            "Night on the deck of the Portuguese flagship SHIP_SG01. In the foreground, VASCO_01 stands with a ruthless, determined expression, his face lit by the orange glow of a roaring iron brazier. "
            "Nearby, a captured Moorish prisoner is bound to a wooden capstan, while a Portuguese sailor holds a smoking iron ladle. "
            "In the background on the bulwarks, alert Portuguese watchmen hold torches and matchlocks over the side, staring into the pitch-black sea where moonlight glints on fleeing ripples. "
            "European historical oil painting, Rembrandt-like dramatic lighting, intense psychological realism, no text."
        )
    },
    {
        "id": "CH01-EP05-S06",
        "output": "CH01-EP05-S06-v1.png",
        "prompt": (
            "MASTER_STYLE_02. 24mm wide panoramic shot, luminous morning sunlight, 15 April 1498 (Easter Sunday). "
            "The open roadstead of Malindi on the East African coast. In the foreground, the weathered Portuguese carracks SHIP_SG01 and SHIP_SR01 ride at anchor in crystal-clear turquoise waters. "
            "On the poop deck of the flagship, VASCO_01 and PAULO_01 stand together looking toward the shore. "
            "In the water around the ships, Swahili wooden outriggers and dhows approach peacefully, their crews offering baskets of green ginger, cloves, and fresh sheep. "
            "In the background, the beautiful white coral-stone city of Malindi stretches along a pristine golden beach backed by lush emerald palm forests. "
            "European historical oil painting, breathtaking atmospheric depth, vibrant tropical color palette, no text."
        )
    },
    {
        "id": "CH01-EP05-S07",
        "output": "CH01-EP05-S07-v1.png",
        "prompt": (
            "MASTER_STYLE_02. 35mm lens, eye-level water shot, vibrant tropical midday light, 18 April 1498. "
            "The lagoon of Malindi. A historic diplomatic summit on the water: On the right, the regal Sultan of Malindi sits in a fine wooden royal barge on a cushioned bronze chair beneath an ornate crimson damask parasol; he is dressed in rich damask robes and a gold-embroidered white turban, flanked by attendants blowing long carved ivory horns (siwa). "
            "On the left, in an armed Portuguese longboat, VASCO_01 stands tall in a crimson velvet doublet and dark cap, bowing respectfully with hand on heart. "
            "In the background across the sparkling turquoise water, Portuguese ships fire celebratory white smoke salutes before the white stone city of Malindi. "
            "European historical oil painting, magnificent pageantry, exquisite textile details, no text."
        )
    },
    {
        "id": "CH01-EP05-S08",
        "output": "CH01-EP05-S08-v1.png",
        "prompt": (
            "MASTER_STYLE_02. 35mm lens, dynamic three-quarter composition, vibrant sunny daylight, 24 April 1498. "
            "On the quarterdeck of the Portuguese flagship SHIP_SG01 standing out to sea from Malindi. "
            "In the center, PILOT_01—a dignified Indian Gujarati master navigator in fine draped cream cotton robes and a wrapped turban—stands calmly holding a traditional wooden kamal instrument, sighting the horizon while pointing east into the open ocean. "
            "Beside him, VASCO_01 stands with his dark hair and cloak whipped by the powerful monsoon wind, looking with intense anticipation toward the eastern horizon. "
            "In the background on a green coastal headland, the white stone Padrão de São Rafael stands proud, as the massive square sails bearing crimson Order of Christ crosses billow under full wind. "
            "European historical oil painting, immense sense of motion and discovery, no text."
        )
    },
    {
        "id": "CH01-EP05-Thumbnail",
        "output": "CH01-EP05-thumbnail-v1.png",
        "prompt": (
            "MASTER_STYLE_02. 35mm lens, high-impact cinematic YouTube thumbnail composition, 16:9 aspect ratio, vibrant tropical morning sunlight. "
            "On the left, a powerful close-up of Portuguese explorer VASCO_01, his weather-beaten sun-bronzed face and dark windblown beard showing intense determination. "
            "In the center, a dignified Indian Gujarati master navigator (PILOT_01) in fine cream linen turban and robes holds a traditional wooden kamal celestial instrument up to his eye, pointing his hand toward the open ocean. "
            "On the right, the massive dark wooden Portuguese flagship SHIP_SG01 surges under full billowing white sails with bold crimson crosses across deep blue foaming waves, past a white stone pillar on a green tropical headland. "
            "European historical oil painting, immense dramatic contrast, vivid colors, no text, no logos."
        )
    },
]


def main():
    IMAGES_EP05_DIR.mkdir(parents=True, exist_ok=True)

    for item in EP05_PROMPTS:
        out_path = IMAGES_EP05_DIR / item["output"]
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

    print("\nEpisode 5 Still Generation Complete.")


if __name__ == "__main__":
    main()
