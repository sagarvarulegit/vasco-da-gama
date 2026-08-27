"""Generate dramatized still frames (v2) for Chapter 1 Episode 3 (Cape of Good Hope)."""

import os
import pathlib
import subprocess
import sys

PROJECT_ROOT = pathlib.Path(__file__).resolve().parent.parent.parent
IMAGES_EP03_DIR = PROJECT_ROOT / "images" / "episode-03"
PROMPT_GEN_SCRIPT = PROJECT_ROOT / "production" / "tools" / "gemini_image_generate.py"

PROMPTS_V2 = [
    {
        "id": "CH01-EP03-S01",
        "output": "CH01-EP03-S01-v2.png",
        "prompt": "MASTER_STYLE_02. 4–7 November 1497, St Helena Bay. High-drama historical scene of desperate ship maintenance: a massive wooden carrack (SHIP_SG01) is heeled sharply on its side on a windblown sandy beach, its exposed oak hull encrusted with dark barnacles and sea-weed. Sweat-streaked Portuguese sailors and shipwrights in salt-stained linen and leather work furiously with iron scrapers and caulking mallets under black smoke from bubbling pitch kettles. In the foreground, VASCO_01, with a dark windblown beard and intense, hawk-like eyes, grips a coiled rope while shouting orders to armed crossbow sentries watching the rugged arid dunes. Behind them, turquoise breakers crash violently. Epic chiaroscuro lighting, visceral grit, European historical painting, dramatic tension, no text, no modern elements."
    },
    {
        "id": "CH01-EP03-S02",
        "output": "CH01-EP03-S02-v2.png",
        "prompt": "MASTER_STYLE_02. 7–8 November 1497, windblown sand dunes of St Helena Bay. Breath-holding psychological standoff of first contact: in an eye-level cinematic shot, VASCO_01, weathered and intensely focused in a salt-stained wool doublet, cautiously extends an open hand holding glistening brass hawk-bells and amber glass beads toward an indigenous Khoikhoi honey-gatherer. The Khoikhoi man, draped in a leopard-skin kaross with a horn necklace, stands poised with a fire-hardened spear, his sharp, intelligent eyes locked onto Vasco. Behind Vasco, PAULO_01 keeps a tense hand near his steel sword hilt as wind whips golden sand across their boots. Blinding sun glare, dramatic dust particles, European historical painting, high emotional intensity, no modern elements, no text."
    },
    {
        "id": "CH01-EP03-S03",
        "output": "CH01-EP03-S03-v2.png",
        "prompt": "MASTER_STYLE_02. 10–12 November 1497, beach at St Helena Bay. Visceral, explosive historical combat in the surf: Portuguese sailors in battered leather armor frantically shove a heavy wooden longboat through violent frothing breakers while a barrage of horn-tipped wooden spears and stones rains down from indigenous warriors on the sand ridge. VASCO_01, grimacing in raw fury and pain, grips the gunwale with blood soaking his wool breeches from a spear embedded in his thigh, shouting fierce orders to a kneeling crossbowman who fires through the sea spray. Foaming churned surf, flying wooden weapons, dark storm clouds, dramatic European historical battle painting, visceral grit, no text, no modern weapons."
    },
    {
        "id": "CH01-EP03-S04",
        "output": "CH01-EP03-S04-v2.png",
        "prompt": "MASTER_STYLE_02. 18–20 November 1497, the Cape of Storms. Cataclysmic maritime battle against the elements: the flagship SHIP_SG01 heels dangerously at a 45-degree angle as a colossal, mountainous dark oceanic wave crests directly above her decks. Freezing green water cascades over the bowsprit, smashing against drenched mariners lashed to ropes. On the high quarterdeck, VASCO_01, with his wounded leg bound in bloody rags and his heavy wool cloak whipped by the gale, clings to the wooden rail with fierce defiance, glaring into the tempest. In the background, the jagged, monstrous black cliffs of the Cape of Good Hope are illuminated by lightning through the rain. Churning foam, visceral terror, European historical master painting, breathtaking scale, no modern ships, no text."
    },
    {
        "id": "CH01-EP03-S05",
        "output": "CH01-EP03-S05-v2.png",
        "prompt": "MASTER_STYLE_02. Midday, 22 November 1497, rounding the Cape of Good Hope. Majestic historical triumph: magnificent golden god-rays burst through parting black storm clouds, illuminating the four Portuguese carracks (SHIP_SG01, SHIP_SR01, SHIP_B01, SHIP_ST01) as they surge past the monumental golden sandstone cliffs of the Cape. Their huge square sails, emblazoned with bright crimson Order of Christ crosses, billow proudly in a fresh following wind. On the poop deck of the flagship, VASCO_01 stands tall with wind-whipped hair and raised arm, surrounded by brass trumpeters sounding fanfare and battle-scarred sailors weeping and embracing. Deep sapphire ocean, sparkling white wake, grand European historical masterpiece, emotional catharsis, no text, no modern elements."
    },
    {
        "id": "CH01-EP03-S06",
        "output": "CH01-EP03-S06-v2.png",
        "prompt": "MASTER_STYLE_02. 25–27 November 1497, beach at Angra de São Brás (Mossel Bay). Vibrant, joyous cross-cultural celebration on the African shore: a large circle of indigenous Khoikhoi pastoralists in ox-hide mantles and gleaming ivory arm rings dance energetically in the white sand alongside Portuguese sailors in bright scarlet wool caps. Khoikhoi musicians play four-holed reed flutes in unison with puffed cheeks and ecstatic expressions. In the center, VASCO_01 warmly hands three brilliant red caps and brass bracelets to a smiling village chief beside a magnificent black ox with wide horns. Behind them, the four wooden ships ride calmly in the sunlit turquoise bay. Warm golden sunlight, sand kicking up, rich ethnographic realism, European historical painting, infectious joy, no text, no modern elements."
    },
    {
        "id": "CH01-EP03-S07",
        "output": "CH01-EP03-S07-v2.png",
        "prompt": "MASTER_STYLE_02. 1–4 December 1497, midnight at Angra de São Brás. Dramatic, haunting chiaroscuro sacrifice: the wooden hull of the supply ship (SHIP_ST01) is engulfed in a roaring, majestic orange inferno on a sandy spit, its charred oak ribs glowing like a skeleton against the deep starry night. Billowing black smoke and glowing embers spiral into the dark sky, reflecting violently across the wet tidal sand. In the foreground, VASCO_01 stands motionless in heavy dark wool, his battle-hardened face illuminated by the flickering firelight as he watches the destruction. Behind him, weary sailors load the final salvaged anchors and barrels into longboats. In the dark bay, the three surviving carracks (SHIP_SG01, SHIP_SR01, SHIP_B01) wait in shadowy silhouette. Intense emotional weight, Rembrandt lighting, European historical master painting, no modern elements, no text."
    },
    {
        "id": "CH01-EP03-S08",
        "output": "CH01-EP03-S08-v2.png",
        "prompt": "MASTER_STYLE_02. Morning, 8 December 1497, departing into the Indian Ocean. Monumental cinematic finale: the three battle-scarred Portuguese vessels (SHIP_SG01, SHIP_SR01, SHIP_B01) sail in proud, tight diamond formation across a radiant deep blue sea, cutting powerful foaming wakes toward a blinding golden sunrise on the open eastern horizon. Crisp morning sunlight sparkles on the water, illuminating their salt-stained hulls and patched square sails bearing the Order of Christ crosses. At the very prow of the flagship, VASCO_01 stands like an iron sentinel, his dark cloak billowing in the fresh breeze as he gazes into the uncharted ocean where no European ship has ever sailed. Majestic green African mountains recede in the purple morning mist. European historical masterpiece, grand cinematic depth, emotional transcendence, no text, no modern elements."
    },
]


def main():
    IMAGES_EP03_DIR.mkdir(parents=True, exist_ok=True)

    for item in PROMPTS_V2:
        out_path = IMAGES_EP03_DIR / item["output"]
        if out_path.exists() and out_path.stat().st_size > 0:
            print(f"Skipping existing still: {item['output']} ({out_path.stat().st_size} bytes)")
            continue

        print(f"\nGenerating {item['id']} -> {item['output']}...")
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
            print(f"Failed to generate {item['output']}:\n{res.stderr}", file=sys.stderr)
        else:
            print(f"Successfully generated: {item['output']}")

    print("\nEpisode 03 v2 stills generation pass completed.")


if __name__ == "__main__":
    main()
