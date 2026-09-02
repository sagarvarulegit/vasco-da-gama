"""Generate still frames (v1) for Chapter 1 Episode 4 (East Africa & Mozambique) using visual-skills dramaturgy."""

import os
import pathlib
import subprocess
import sys

PROJECT_ROOT = pathlib.Path(__file__).resolve().parent.parent.parent
IMAGES_EP04_DIR = PROJECT_ROOT / "images" / "episode-04"
PROMPT_GEN_SCRIPT = PROJECT_ROOT / "production" / "tools" / "gemini_image_generate.py"

EP04_PROMPTS = [
    {
        "id": "CH01-EP04-S01",
        "output": "CH01-EP04-S01-v1.png",
        "prompt": (
            "MASTER_STYLE_02. 35mm lens, eye-level composition, January 1498. "
            "Interior lower hold of 15th-century Portuguese flagship (SHIP_SG01). "
            "Chiaroscuro lighting from a single swinging brass oil lamp casting amber light across curved dark oak hull ribs and moldering canvas sacks. "
            "In the center, VASCO_01 (weathered, sun-blackened skin, rough dark beard, salt-stained linen shirt with sleeves rolled up) kneels over an emaciated sailor whose face is pale and swollen with dark purple gums. "
            "Vasco's knuckles are white as he carefully applies a vinegar-soaked linen cloth to the sailor's mouth. "
            "Beside him, PAULO_01 holds a dented brass water basin. "
            "Dust motes and humidity drift through a narrow vertical ray of sunlight from the deck hatch above. "
            "Tactile historical textures of rough wet oak, rusted iron bolts, and coarse linen. "
            "15th-century Portuguese maritime reality, no text, no modern equipment."
        )
    },
    {
        "id": "CH01-EP04-S02",
        "output": "CH01-EP04-S02-v1.png",
        "prompt": (
            "MASTER_STYLE_02. 28mm wide lens, low-angle golden-hour composition, 11 January 1498. "
            "Rio do Cobre (Southeast Africa). Lush sub-tropical river mouth with golden sandbanks and tall coconut palms. "
            "In the foreground, a tall, dignified Bantu village elder with woven hair and an ivory-handled dagger sheath extends a heavy hammered copper bangle toward Portuguese interpreter Martin Afonso, who offers a bolt of white linen cloth with both hands. "
            "In the midground, Portuguese sailors in salt-stained linen shirts smile as they fill wooden casks from clay water urns carried by villagers. "
            "In the turquoise estuary background, three weather-stained Portuguese naus (SHIP_SG01, SHIP_SR01, SHIP_B01) rest quietly at anchor, their bleached sails furled. "
            "Warm amber sunlight casting long shadows across wet river sand. "
            "15th-century historical accuracy, dignified cultural encounter, no text, no modern objects."
        )
    },
    {
        "id": "CH01-EP04-S03",
        "output": "CH01-EP04-S03-v1.png",
        "prompt": (
            "MASTER_STYLE_02. 24mm wide-angle lens, low-angle ground-level shot, February 1498. "
            "Rio dos Bons Sinais (Zambezi Delta). High-noon blazing tropical sun illuminating a massive 15th-century wooden carrack (SHIP_SR01) heeled sharply at 35 degrees on a muddy river sandbank, propped up by heavy oak timber shores. "
            "In the foreground, Portuguese sailors and shipwrights, shirtless with dark sunburnt skin and glistening sweat, scrape thick green algae and dark barnacles from the exposed oak keel using curved iron blades. "
            "One caulker drives hemp oakum into a split hull seam with an iron mallet. "
            "Orange flames and thick black smoke billow from cast-iron cauldrons of boiling pitch on the wet mud. "
            "PAULO_01 stands ankle-deep in tidal water inspecting the rudder pintle, his linen shirt soaked with sweat and soot. "
            "In the distant background, mangrove trees shimmer under intense equatorial heat haze. "
            "Gritty historical realism, chiaroscuro lighting, no text, no modern machinery."
        )
    },
    {
        "id": "CH01-EP04-S04",
        "output": "CH01-EP04-S04-v1.png",
        "prompt": (
            "MASTER_STYLE_02. 35mm lens, low-angle dynamic composition, 24 February 1498. "
            "Promontory overlooking Rio dos Bons Sinais estuary. "
            "On a windblown sand dune, a tall, freshly carved white limestone pillar (Padrão de São Rafael) topped with the Portuguese royal coat of arms and an Order of Christ stone cross stands anchored into the sand. "
            "In the foreground, VASCO_01, his dark beard trimmed, wearing a worn dark blue wool doublet and leather boots, listens intently as a Swahili coastal trader draped in striped silk robes and a vibrant green satin turban points his outstretched arm northward across the sea. "
            "In the sparkling turquoise river mouth below, all three Portuguese ships (SHIP_SG01, SHIP_SR01, SHIP_B01) ride cleanly at anchor with newly caulked dark hulls. "
            "Crisp ocean sunlight glinting off white stone and sea foam. "
            "High historical fidelity, European oil painting tradition, no text, no modern objects."
        )
    },
    {
        "id": "CH01-EP04-S05",
        "output": "CH01-EP04-S05-v1.png",
        "prompt": (
            "MASTER_STYLE_02. 24mm wide-angle lens, elevated three-quarter view from quarterdeck, 2 March 1498. "
            "Mozambique Island coral lagoon. In crystal-clear turquoise and emerald waters, the dark weathered wooden flagship (SHIP_SG01, with cross-marked square sails) glides slowly into a bustling roadstead. "
            "In the immediate midground, sleek white lateen-rigged Arab dhows and sambuks, crewed by Swahili and Arab sailors in white cotton tunics and turbans, slice effortlessly through the turquoise swell. "
            "On the low sandy island in the background, white coral-stone buildings, domed mosques, and minarets gleam under a brilliant tropical sky fringed by coconut palms. "
            "On the flagship's deck, VASCO_01 and his officers lean against the wooden bulwark, looking on in silent astonishment. "
            "Crisp painterly chiaroscuro, luminous tropical water reflections, 15th-century historical accuracy, no text, no modern boats."
        )
    },
    {
        "id": "CH01-EP04-S06",
        "output": "CH01-EP04-S06-v1.png",
        "prompt": (
            "MASTER_STYLE_02. 50mm portrait lens, tight medium two-shot, March 1498. "
            "Quarterdeck of Portuguese flagship (SHIP_SG01) under a linen sunshade. "
            "In the center, the Sheikh of Mozambique—a distinguished Swahili-Arab nobleman in an opulent crimson silk robe woven with gold filigree and a silk turban with an ivory-hilted curved dagger—stares down with unmistakable haughty disdain at a coarse red woolen cap and cheap brass hawk-bells on a low oak table. "
            "Opposite him, VASCO_01 (weathered, sun-blackened face, intense dark beard, worn dark velvet doublet) stands rigid with pride and rising fury, his hand clamped white-knuckled around his sword hilt. "
            "Behind them, armored Portuguese soldiers with halberds and silk-robed Arab attendants exchange tense, suspicious glares. "
            "Rich Rembrandt chiaroscuro lighting, psychological tension, 15th-century historical reality, no text, no modern elements."
        )
    },
    {
        "id": "CH01-EP04-S07",
        "output": "CH01-EP04-S07-v1.png",
        "prompt": (
            "MASTER_STYLE_02. 28mm wide lens, low waterline angle, dawn light, 27 March 1498. "
            "Mangrove shallows on the mainland coast near Mozambique Island. "
            "Visceral, action-packed combat scene: two heavy wooden Portuguese longboats struggle in murky, knee-deep coastal shallows near tangled mangrove stilt-roots. "
            "Arrows and cane throwing-spears rain down from concealed archers behind wooden barricades on the shore, splashing water into the air and embedding into the boat's oak gunwales. "
            "In the lead boat, Nicolau Coelho in a rusted iron breastplate points his sword toward deep water while an armored Portuguese crossbowman crouches behind a wooden pavise shield and looses a steel quarrel into the trees. "
            "Oarsmen strain violently to pull the boat backward. Dawn mist is pierced by golden morning sunbeams. "
            "15th-century historical weapons and armor, gritty combat realism, no text, no modern weapons."
        )
    },
    {
        "id": "CH01-EP04-S08",
        "output": "CH01-EP04-S08-v1.png",
        "prompt": (
            "MASTER_STYLE_02. 35mm lens, dynamic three-quarter low angle, golden-hour light, 29 March 1498. "
            "Mozambique Island roadstead. A climactic naval broadside: the massive dark wooden hull of the Portuguese flagship (SHIP_SG01) unleashes a devastating cannonade. "
            "An intense orange muzzle flash bursts from a bronze bombard mounted on the ship bulwark, throwing thick, rolling clouds of white and gray sulfur smoke across the turquoise lagoon. "
            "Gunpowder sparks illuminate the deck planking. "
            "On the quarterdeck, VASCO_01 stands with his sword raised northward, his sun-darkened face and windblown dark hair framed by the rising smoke as his square sails, marked with crimson Order of Christ crosses, catch the wind. "
            "In the background across the water, wooden harbor palisades splinter as iron cannonballs impact the shoreline. "
            "European historical oil painting, immense scale, chiaroscuro battle lighting, no text, no modern steam vessels."
        )
    },
    {
        "id": "CH01-EP04-Thumbnail",
        "output": "CH01-EP04-thumbnail-v1.png",
        "prompt": (
            "MASTER_STYLE_02. High-impact cinematic YouTube thumbnail composition: "
            "in the left foreground, an intense close-up portrait of 15th-century Portuguese commander Vasco da Gama (VASCO_01), "
            "his face sun-scorched and battle-hardened with a rugged dark beard, fierce determined eyes, holding an unsheathed steel rapier catching dramatic orange firelight. "
            "In the right background, massive rolling clouds of white gunpowder smoke and brilliant orange cannon muzzle flashes erupt from the wooden hull of his caravel in a turquoise coral lagoon, with the white stone minarets of Mozambique Island silhouetted against rising black smoke. "
            "Extreme chiaroscuro contrast, dramatic tension, European historical oil painting, vibrant colors, clean uncluttered layout, no text inside the image."
        )
    },
]


def main():
    IMAGES_EP04_DIR.mkdir(parents=True, exist_ok=True)

    for item in EP04_PROMPTS:
        out_path = IMAGES_EP04_DIR / item["output"]
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

    print("\nEpisode 4 Still Generation Complete.")


if __name__ == "__main__":
    main()
