"""Update all scene markdown records in scenes/ with Narration, Audio Tags, and Omni Flash prompts."""

import pathlib

SCENES_DIR = pathlib.Path(__file__).resolve().parent.parent.parent / "scenes"

SCENE_DATA = {
    "CH01-S01": {
        "narration": "In July 1497, four vessels gathered at Belém for a voyage into the ocean.",
        "delivery": "Measured documentary narrator; warm baritone, steady opening cadence.",
        "audio_tags": "[VOICEOVER: documentary narrator, warm baritone, natural cadence] [AMBIENCE: Tagus river water lap against stone quay, distant port murmur, seagulls] [FOLEY: heavy hemp rope dragging on stone, cask thuds, footsteps on timber gangplanks, creaking ships] [MUSIC: soft low strings, gentle frame drum pulse]",
        "omni_prompt": "Animate this historical painting as a restrained cinematic establishing shot of the Belém waterfront in July 1497. Tagus water laps gently against the quay, loose rope ends sway, sailcloth breathes in summer breeze, and workers make subtle loading gestures. Slow forward camera drift toward VASCO_01 and the four ships.",
    },
    "CH01-S02": {
        "narration": "Command lived in ropes, stores, sails, and the men who had to make them work.",
        "delivery": "Focused, practical mariner cadence; clear documentary delivery.",
        "audio_tags": "[VOICEOVER: documentary narrator, clear vocal delivery] [AMBIENCE: open river wind, water lap on hull] [FOLEY: footsteps on wooden deck planks, canvas snapping in wind, pulley creak, low indistinct work voices] [MUSIC: sustained viola, quiet woodwinds]",
        "omni_prompt": "Animate the deck-height readiness scene with subtle human gestures: checking rigging lines, sailcloth fluttering, pulleys swaying slightly. Slow lateral camera move across ropes and sailcloth, settling briefly on VASCO_01 and the senior officers.",
    },
    "CH01-S03": {
        "narration": "Water, food, rope, timber, and sailcloth became the expedition’s first measure of survival.",
        "delivery": "Weighty, deliberate pacing emphasizing logistical scale.",
        "audio_tags": "[VOICEOVER: documentary narrator, grounded cadence] [AMBIENCE: bustling river harbor] [FOLEY: heavy wooden barrels rolling, rope fibers straining under hoist, wood creaking, water sloshing in casks] [MUSIC: low weighty cello ostinato]",
        "omni_prompt": "Animate the supply loading with physical weight: rolling a wooden cask, a hoisted barrel settling, rope fibers tightening. Slow downward and forward tilt from supply ship hull toward foreground cargo with realistic depth parallax.",
    },
    "CH01-S04": {
        "narration": "Two large ships, a smaller vessel, and a supply ship formed one fragile moving system.",
        "delivery": "Spacious, contemplative tone observing fleet scale.",
        "audio_tags": "[VOICEOVER: documentary narrator, spacious delivery] [AMBIENCE: broadening river-to-sea wind, Tagus current] [FOLEY: four hulls cutting water, canvas filling with wind, distant harbor sounds fading] [MUSIC: open fifths in strings, soft french horn note]",
        "omni_prompt": "Animate the wide fleet view as a calm Tagus passage. Each sail responds naturally to the wind; hulls rise and fall on the same water system. Slow wide river glide from São Gabriel across São Rafael, Berrio, and the supply ship.",
    },
    "CH01-S05": {
        "narration": "On 8 July 1497, a released rope set the long voyage in motion.",
        "delivery": "Reverent, historic threshold delivery.",
        "audio_tags": "[VOICEOVER: documentary narrator, reverent tone] [AMBIENCE: open water surge, quay ambience receding] [FOLEY: wet mooring rope slapping water, bollard groaning, sail catching wind, water rushing along hull] [MUSIC: single low percussion pulse on release, rising strings]",
        "omni_prompt": "Animate the wet mooring rope as it slackens and slips from the timber bollard into the river with falling droplets. The hull begins slow forward motion; sails take wind. Low waterline camera tracking alongside the departing hull.",
    },
    "CH01-S06": {
        "narration": "Lisbon receded behind them as the fleet entered the Atlantic and turned toward the south.",
        "delivery": "Reflective, atmospheric pacing; receding perspective.",
        "audio_tags": "[VOICEOVER: documentary narrator, reflective tone] [AMBIENCE: open Atlantic sea breeze, seagulls thinning] [FOLEY: foaming stern wake, creaking stern timbers, wind whistling in hemp shrouds] [MUSIC: sparse bowed strings with long unresolved pedal note]",
        "omni_prompt": "Animate from the stern of São Gabriel as wake lengthens and Lisbon slowly recedes through atmospheric haze. Gentle stern sway, rigging vibration, small sail motion. Slow backward tracking shot widening toward open Atlantic.",
    },
    "CH01-S07": {
        "narration": "At night, the voyage became a discipline of listening—to water, timber, rope, and darkness.",
        "delivery": "Intimate, quiet delivery; documentary observation of night watch.",
        "audio_tags": "[VOICEOVER: documentary narrator, intimate whispered tone] [AMBIENCE: dark ocean night, rhythmic sea swell] [FOLEY: shielded oil lantern hiss, water rushing past planks, rhythmic deck creak, slow footsteps] [MUSIC: almost silent low sub-bass drone, distant bowed violin harmonic]",
        "omni_prompt": "Animate the first night watch with shielded lantern flicker reflecting on wet deck planks, slow cloud drift across stars, and subtle breathing posture shifts from sailors. Slow lantern-centered camera orbit with rack focus to distant fleet lights.",
    },
    "CH01-S08": {
        "narration": "The fleet took its southward course. The journey had begun.",
        "delivery": "Solemn, resolute closure for the departure chapter.",
        "audio_tags": "[VOICEOVER: documentary narrator, solemn resolution] [AMBIENCE: vast open Atlantic wind and swell] [FOLEY: four hulls cutting ocean swell, sail canvas pressurized in trade winds, rigging hum] [MUSIC: gentle orchestral swelling, resolving into wind and waves]",
        "omni_prompt": "Animate the high wide view as the four-vessel fleet sails a deliberate southbound course across the open Atlantic. Sails billow in coherent wind, hulls pitch gently, wakes trail naturally. Very slow aerial drift preserving fleet spacing.",
    },
    "CH01-EP02-S01": {
        "narration": "Past the familiar Iberian coast, the four ships found the ocean winds and settled into the long rhythm of open water.",
        "delivery": "Steady, observant documentary tone opening the Atlantic passage.",
        "audio_tags": "[VOICEOVER: documentary narrator, steady tone] [AMBIENCE: rolling Atlantic swell, steady trade wind] [FOLEY: water rushing along hull, hemp rigging singing, canvas breathing, distant seabirds] [MUSIC: low open strings, spacious violas]",
        "omni_prompt": "Animate this historical painting with slow forward deck drift from São Gabriel toward the rolling blue-grey horizon where the Iberian coast recedes. Four ships ride the rhythmic Atlantic swell in stable formation.",
    },
    "CH01-EP02-S02": {
        "narration": "Off the African coast, dense fog swallowed the horizon. For days, the fleet lost sight of itself in the grey Atlantic mist.",
        "delivery": "Muffled, tense cadence capturing maritime isolation.",
        "audio_tags": "[VOICEOVER: documentary narrator, quiet tense delivery] [AMBIENCE: thick damp sea-fog, muffled ocean swell] [FOLEY: condensation dripping from rigging onto planks, creak of heavy rudder, distant muffled bell or call] [MUSIC: near-silent low cello drone with dissonant harmonic]",
        "omni_prompt": "Animate the fog-bound deck of São Rafael with dense Atlantic sea-mist rolling in layered waves across damp masts and cordage. Paulo da Gama and crew peer into the grey void. Slow lateral track along the wet gunwale.",
    },
    "CH01-EP02-S03": {
        "narration": "Near the island of Sal, sails reappeared through the heat. The separated vessels found one another again across the calm.",
        "delivery": "Gentle, relieved tone; quiet resolution of reunion.",
        "audio_tags": "[VOICEOVER: documentary narrator, quiet relief] [AMBIENCE: calm tropical Atlantic, gentle water lap] [FOLEY: light air in canvas, faint shouts and hand signals echoing across water, rudder splash] [MUSIC: warm gentle string resolution, soft bowed melody]",
        "omni_prompt": "Animate calm Cape Verde waters near Ilha do Sal with subtle heat shimmer over the low island horizon. The four ships converge slowly across the glassy water with crew making signaling gestures. Slow horizontal drift.",
    },
    "CH01-EP02-S04": {
        "narration": "At São Thiago, the fleet took its final provisions: meat, fresh water, firewood, and fresh timber to repair strained spars.",
        "delivery": "Disciplined, industrious cadence reflecting provisioning.",
        "audio_tags": "[VOICEOVER: documentary narrator, grounded cadence] [AMBIENCE: tropical island bay, shore surf] [FOLEY: wooden adzes shaping timber, block and tackle creaking, heavy barrels thudding into hold, oar strokes] [MUSIC: weighty rhythmic cello and bass ostinato]",
        "omni_prompt": "Animate the anchorage at Santa Maria Bay on São Thiago with small shore boats ferrying water casks and firewood, while shipwrights refit a yard arm beside São Gabriel. Slow push-in toward harbor work under harsh island light.",
    },
    "CH01-EP02-S05": {
        "narration": "Two hundred leagues into the southern ocean, the captain-major’s main yard snapped. The armada halted in open water while the spar was secured.",
        "delivery": "Urgent, tense delivery conveying open-sea crisis.",
        "audio_tags": "[VOICEOVER: documentary narrator, dramatic urgency] [AMBIENCE: stormy southern ocean squalls, heavy rolling rollers] [FOLEY: sharp crack of splitting timber, groaning cordage, heavy canvas luffing in wind, spray hitting deck, sailors shouting work commands] [MUSIC: low pulsing timpani roll, dissonant low strings]",
        "omni_prompt": "Animate the open-sea crisis with São Gabriel lying to under reduced canvas while sailors lash and repair the broken main yard. The ship pitches heavily in ocean rollers with spray against bow. Swell-riding camera rocking with the deck.",
    },
    "CH01-EP02-S06": {
        "narration": "Far from any known coast, the ocean revealed its own life: migrating birds flying southeast, and whales rising in the deep swell.",
        "delivery": "Awe-filled, spacious documentary delivery.",
        "audio_tags": "[VOICEOVER: documentary narrator, awe-filled restraint] [AMBIENCE: immense open ocean, continuous trade wind] [FOLEY: deep whoosh of whale blowhole exhaling vapor, rhythmic bow-wave, solitary seabird cries] [MUSIC: sparse expansive high strings and soft woodwinds]",
        "omni_prompt": "Animate the solitary South Atlantic expanse beneath towering clouds. A whale surfaces at respectful distance exhaling vapor; coastal birds glide southeast overhead. Wide expansive pull-out emphasizing oceanic scale.",
    },
    "CH01-EP02-S07": {
        "narration": "By early November, floating weed and coastal birds appeared in the water—the first signs that the vast South Atlantic arc had brought them back toward land.",
        "delivery": "Measured, observant documentary narrator; intimate, reflective pacing.",
        "audio_tags": "[VOICEOVER: documentary narrator, warm baritone, clear vocal delivery] [AMBIENCE: deep South Atlantic swell, ocean wind, long wave wash] [FOLEY: heavy oak hull creak, floating gulf-weed scraping along wooden hull, wind in rigging, quiet murmurs of crew pointing at water] [MUSIC: suspended string pedal point, sustained cello harmonics, rising tension]",
        "omni_prompt": "Animate this historical painting with slow upward tilt from the floating gulf-weed drifting past the wooden hull to the crew's watchful, weathered faces on deck. Sails billow gently in the cold southern wind; ocean swell rolls with realistic fluid weight.",
    },
    "CH01-EP02-S08": {
        "narration": "On 4 November, ninety-six days after leaving Cape Verde, they sighted land. The armada dropped anchor in the Bay of St Helena to mend sails and prepare for the Cape.",
        "delivery": "Solemn, emotional resolution after months at sea.",
        "audio_tags": "[VOICEOVER: documentary narrator, solemn resolution] [AMBIENCE: calm bay waters, gentle shore surf, seabird colonies] [FOLEY: heavy iron anchor chain rattling through hawsehole with deep splash, oars creaking in rowlocks, lead line sounding splash] [MUSIC: rich warm resolution in full strings with french horn]",
        "omni_prompt": "Animate dawn landfall at Bay of St Helena with golden morning light over arid shoreline. A sounding boat rows ahead casting a lead line as the four ships maneuver to anchor. Low waterline forward glide following the boat.",
    },
}


def main():
    for scene_id, data in SCENE_DATA.items():
        file_path = SCENES_DIR / f"{scene_id}.md"
        if not file_path.exists():
            print(f"Skipping {file_path.name} (not found)")
            continue

        text = file_path.read_text(encoding="utf-8")

        # 1. Add/update Narration & Audio Direction section
        if "## Narration & Voiceover Script" not in text:
            narr_block = f"""## Narration & Voiceover Script

> "{data['narration']}"

* **Delivery:** {data['delivery']}
* **Classification:** [SOURCE] journal account; [CINEMATIC] documentary voiceover.

## Audio Direction & Sound Design

* **[AUDIO_TAGS]:** {data['audio_tags']}

"""
            text = text.replace("## Image Prompt", narr_block + "## Image Prompt")

        # 2. Add/update Image-to-Video Prompt (Google Omni Flash) section
        if "## Image-to-Video Prompt (Google Omni Flash)" not in text:
            omni_block = f"""## Image-to-Video Prompt (Google Omni Flash)

{data['omni_prompt']}

* **[VOICEOVER]:** "{data['narration']}"
* **[AUDIO_TAGS]:** {data['audio_tags']}

"""
            text = text.replace("## Animation Potential", omni_block + "## Animation Potential")

        file_path.write_text(text, encoding="utf-8")
        print(f"Updated scene: {file_path.name}")

    print("All scene files successfully updated with Narration, Audio Tags, and Omni Flash prompts!")


if __name__ == "__main__":
    main()
