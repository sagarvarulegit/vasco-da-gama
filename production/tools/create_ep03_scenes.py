"""Generate production-ready scene markdown files for Chapter 1 Episode 3 (Cape of Good Hope)."""

import pathlib

SCENES_DIR = pathlib.Path(__file__).resolve().parent.parent.parent / "scenes"

SCENES_EP03 = [
    {
        "id": "CH01-EP03-S01",
        "title": "Careening and Wood Gathering at St Helena Bay",
        "date": "4–7 November 1497",
        "location": "St Helena Bay (Angra de Santa Helena), southwest African coast",
        "source": "Roteiro, Ravenstein pp. 3–5; Hakluyt Society 1898",
        "confidence": "HIGH",
        "source_facts": "[SOURCE] On 4 November land is sighted; on 7 November the fleet anchors in St Helena Bay. The crew careens the ships on the beach, mends sails, and gathers firewood and fresh water from the river.",
        "historical_context": "[HISTORICAL] Four months at sea in warm and cold currents fouled hulls with algae and barnacles. Beaching or heeling ships at low tide to scrape weed and tar planking was critical maintenance before rounding the Cape.",
        "reconstruction": "[RECONSTRUCTION] The specific placement of longboats, caulking braziers with pitch, sailmakers working on sand dunes, and armed watch posts.",
        "cinematic": "[CINEMATIC] Low wide angle capturing the industry of the landing camp against the sweeping arid landscape.",
        "characters": "VASCO_01, PAULO_01, COELHO_01, carpenters, caulkers, sailmakers, armed sentries.",
        "ships": "SHIP_SG01, SHIP_SR01, SHIP_B01, SHIP_ST01 anchored close inshore; longboats ferrying casks and timber.",
        "environment": "Arid southwest African coast, fynbos vegetation, broad sandy beach, calm turquoise bay waters, bright Southern Hemisphere spring sunlight.",
        "continuity": "Four months of sea exposure visible: sun-darkened skin, sea-salt encrusted tunics, salt-bleached wooden masts, frayed cordage.",
        "narration": "In the sheltered waters of St Helena Bay, the armada grounded its hulls on the sand to scrape barnacles, mend worn sails, and replenish fresh water.",
        "delivery": "Measured, observant documentary narrator; calm and practical tone.",
        "audio_tags": "[VOICEOVER: documentary narrator, warm baritone, steady cadence] [AMBIENCE: gentle coastal surf on sand, cry of kelp gulls, dry Atlantic shore breeze] [FOLEY: iron scrapers grating on oak hull planks, rhythmic wood sawing, water splashing into casks, caulking mallet tapping] [MUSIC: soft low cello drone, Renaissance lute arpeggio in minor mode]",
        "image_prompt": "MASTER_STYLE_02. 4–7 November 1497, St Helena Bay on the southwest African coast. Working beach encampment under bright southern spring sun: Portuguese crew and shipwrights careen a wooden ship hull on the sandy shore, scraping barnacles, while sailmakers repair heavy canvas sails on the dunes and sailors roll water casks from a freshwater spring. VASCO_01, sun-weathered with dark beard in practical maritime wool tunic, stands near the water observing the work with his officers. In the calm turquoise bay, the four ships SHIP_SG01, SHIP_SR01, SHIP_B01, SHIP_ST01 ride quietly at anchor. Arid African coastal scrub, rolling sandy dunes, realism, European historical painting, fine texture, no text, no modern elements.",
        "negative_prompt": "Modern clothing, modern tools, fantasy armor, tropical palm trees, steamships, later 17th century galleons, glossy CGI, modern typography, fantasy elements.",
        "omni_prompt": "Animate this historical painting with a slow cinematic lateral pan across the working shore camp: caulkers scrape barnacles with rhythmic strokes, woodsmoke drifts from pitch braziers, water sloshes in rolling casks, and sailmakers pull cordage on the dunes. In the background, four wooden carracks sway gently on the calm turquoise bay.",
        "vo_line": "In the sheltered waters of St Helena Bay, the armada grounded its hulls on the sand to scrape barnacles, mend worn sails, and replenish fresh water.",
        "animation_potential": "Excellent for wide panoramic drift: woodsmoke drift, water lap on hull, caulker motion, sailcloth billowing gently."
    },
    {
        "id": "CH01-EP03-S02",
        "title": "First Encounter on the Strand",
        "date": "7–8 November 1497",
        "location": "Dunes of St Helena Bay",
        "source": "Roteiro, Ravenstein pp. 5–7",
        "confidence": "HIGH",
        "source_facts": "[SOURCE] A local inhabitant gathering honey in the bushes is captured and brought aboard São Gabriel. He is fed, given clothing, brass hawk-bells, glass beads, and released back ashore peacefully.",
        "historical_context": "[HISTORICAL] The inhabitants were indigenous Khoikhoi / pastoralist-hunter-gatherers of the southwestern Cape, wearing skin cloaks, bone/horn ornaments, and carrying fire-hardened wood-pointed spears.",
        "reconstruction": "[RECONSTRUCTION] The cautious body language, initial hesitation on the dunes, and the presentation of small trade objects in the open palm.",
        "cinematic": "[CINEMATIC] Intimate eye-level encounter on the windblown sand, emphasizing mutual curiosity rather than hostility.",
        "characters": "VASCO_01, PAULO_01, indigenous Khoikhoi man in skin cloak, Portuguese mariners.",
        "ships": "SHIP_SG01 visible in the bay background.",
        "environment": "Low rolling dunes, dry fynbos bushes, bright sun, sandy wind, open blue sky.",
        "continuity": "Vasco wears practical salt-stained mariner jerkin; indigenous man carries wooden gathering stick and skin cloak.",
        "narration": "On the dunes, the Portuguese made their first contact with the southern coast's inhabitants, exchanging small brass bells and glass beads.",
        "delivery": "Intrigued, measured documentary delivery; respectful curiosity.",
        "audio_tags": "[VOICEOVER: documentary narrator, clear and reflective] [AMBIENCE: wind rustling dry coastal scrub, distant ocean surf, bird calls] [FOLEY: tinkling small brass hawk-bells, rustling dry brush, soft footsteps on sand, light linen flap] [MUSIC: quiet bowed viola, sparse wooden flute melody, delicate modal harmony]",
        "image_prompt": "MASTER_STYLE_02. 7–8 November 1497, sand dunes of St Helena Bay. Intimate historical encounter on the strand: VASCO_01 and PAULO_01 stand cautiously in weathered 15th-century Portuguese maritime attire, offering shiny small brass hawk-bells and coloured glass beads in an outstretched palm to an indigenous Khoikhoi hunter-gatherer wearing a traditional animal skin cloak (kaross) and bone necklace. Dry fynbos shrubs, golden sand dunes, soft sea breeze, brilliant southern ocean light, European historical painting aesthetic, human dignity, historical accuracy, no modern elements, no text.",
        "negative_prompt": "Stereotypical Hollywood savage tropes, modern clothes, modern beads, tropical jungle, cartoonish expressions, fantasy weapons, text, watermarks.",
        "omni_prompt": "Animate the quiet encounter on the dunes with subtle camera drift: the brass bells gleam in the sun, dry coastal grass sways in the sea breeze, and Vasco extends his open palm with calm, measured gestures as the indigenous man observes with watchful dignity.",
        "vo_line": "On the dunes, the Portuguese made their first contact with the southern coast's inhabitants, exchanging small brass bells and glass beads.",
        "animation_potential": "Subtle character interaction, grass swaying, wind across dunes, glinting brass bells."
    },
    {
        "id": "CH01-EP03-S03",
        "title": "Skirmish on the Beach",
        "date": "10–12 November 1497",
        "location": "Shore of St Helena Bay",
        "source": "Roteiro, Ravenstein pp. 7–10",
        "confidence": "HIGH",
        "source_facts": "[SOURCE] Fernão Veloso returns hastily from an excursion into the hills; dozens of locals appear on the ridge; misunderstandings turn to conflict. Stones and wooden assegais with horn tips are thrown; Vasco da Gama is wounded in the leg/thigh by a spear as the boats push off.",
        "historical_context": "[HISTORICAL] Cultural misunderstanding and suspicion over intentions quickly escalated into armed confrontation. Crossbows were discharged from the longboats to cover the retreat.",
        "reconstruction": "[RECONSTRUCTION] The chaotic surf zone, splashes around the longboat, Vasco clutching his wounded thigh while directing the retreat.",
        "cinematic": "[CINEMATIC] Dynamic action framed from waterline: surging surf, flying spears, crew hauling oars in foam.",
        "characters": "VASCO_01 (wounded in leg), Fernão Veloso (running in panic), crossbowmen, boat crew, Khoikhoi warriors.",
        "ships": "Portuguese longboats in surf; four main ships riding at anchor in distant bay.",
        "environment": "Choppy breaking surf, overcast windy coastal sky, kicked-up sand, frothing white water.",
        "continuity": "Vasco da Gama wounded in thigh; clothing showing battle tear and blood stain on wool hose.",
        "narration": "Mistrust broke the fragile peace. In a sudden skirmish on the strand, spears were thrown, and the captain-major was struck in the leg as the boats pushed off.",
        "delivery": "Urgent, dramatic documentary delivery; controlled intensity.",
        "audio_tags": "[VOICEOVER: documentary narrator, urgent dramatic delivery] [AMBIENCE: roaring breaking surf, gusting coastal wind] [FOLEY: splashing water, shouting men, thud of wooden spears hitting wet sand and gunwale, crossbow latch release, frantic oar strokes] [MUSIC: fast tense frame drum rhythm, driving low strings, dissonant brass accents]",
        "image_prompt": "MASTER_STYLE_02. 10–12 November 1497, beach at St Helena Bay. Dramatic historical skirmish in the surf: Portuguese mariners in leather jerkins and steel helmets hastily shove a wooden longboat off the foaming shoreline while indigenous Khoikhoi warriors on the low sand ridge throw stones and horn-tipped wooden spears. VASCO_01, grimacing with a spear wound in his thigh, leans against the boat gunwale while steadying his men; a crossbowman fires toward the ridge to cover the escape. Splashing white sea spray, churning sand, dark windblown clouds, European historical battle painting, dynamic realism, no modern weapons, no text.",
        "negative_prompt": "Modern firearms, cannons, fantasy armor, blood-gore exploitation, cartoon motion, superhero poses, 19th-century colonial soldiers, text.",
        "omni_prompt": "Animate the tense beach retreat with dynamic surf motion: waves crash violently against the longboat, spears strike the wet sand and splash water, oars dig furiously into foaming sea, and Vasco da Gama braces against the gunwale directing his crew through the spray.",
        "vo_line": "Mistrust broke the fragile peace. In a sudden skirmish on the strand, spears were thrown, and the captain-major was struck in the leg as the boats pushed off.",
        "animation_potential": "High kinetic energy: foaming breakers, flying spears, splashing oars, wind whipping hair and canvas."
    },
    {
        "id": "CH01-EP03-S04",
        "title": "Battling the Cape Headwinds",
        "date": "18–20 November 1497",
        "location": "Open ocean approaching the Cape of Good Hope",
        "source": "Roteiro, Ravenstein pp. 11–13",
        "confidence": "HIGH",
        "source_facts": "[SOURCE] The fleet leaves St Helena on 16 November. On 18 November the Cape of Good Hope is sighted, but severe contrary winds force the ships to tack repeatedly out to sea for days.",
        "historical_context": "[HISTORICAL] The meeting of the South Atlantic and Agulhas ocean currents creates massive standing swells, rogue waves, and fierce southeasterly gale winds that tested the wooden hulls to their limits.",
        "reconstruction": "[RECONSTRUCTION] The severe rolling of São Gabriel under storm canvas, salt encrustation on rigging, lookouts lashed to mast shrouds.",
        "cinematic": "[CINEMATIC] Epic wide sea shot showing the four tiny wooden ships battling towering dark grey ocean rollers against the distant silhouette of the Cape promontory.",
        "characters": "VASCO_01 (wrapped in heavy wool cloak with bandaged leg), helmsmen, deckhands fighting the ropes.",
        "ships": "SHIP_SG01, SHIP_SR01, SHIP_B01, SHIP_ST01 under double-reefed courses, pitching deeply in heavy seas.",
        "environment": "Violent dark grey Southern Ocean swell, howling cold wind, white-capped wave crests, towering rocky Cape cliffs visible through sea spray.",
        "continuity": "Ships show heavy salt stains and patched sails; crew wearing heavy wool storm hoods and oilcloths.",
        "narration": "For days, the fleet fought heavy contrary gales offshore, tacking repeatedly into the cold, turbulent swells of the southern ocean.",
        "delivery": "Weighty, dramatic documentary tone capturing the maritime struggle.",
        "audio_tags": "[VOICEOVER: documentary narrator, solemn and powerful] [AMBIENCE: howling gale-force wind, deep crashing ocean swells, freezing sea spray] [FOLEY: heavy oak timbers groaning and twisting, ropes whistling under violent tension, canvas snapping, water cascading across deck] [MUSIC: churning contrabass ostinato, heavy orchestral brass swells, deep timpani rolls]",
        "image_prompt": "MASTER_STYLE_02. 18–20 November 1497, off the Cape of Good Hope. Dramatic maritime struggle in heavy seas: the four Portuguese ships SHIP_SG01, SHIP_SR01, SHIP_B01, SHIP_ST01 battle enormous dark grey oceanic swell and contrary gales off the towering, jagged promontory of the Cape. Heavy white spray crashes over the bow of São Gabriel as she tacks under reefed storm sails; sailors fight the helm and rigging in cold sea wind. Dark storm clouds, churning foam, epic European historical maritime painting, realistic fluid physics, no text, no modern elements.",
        "negative_prompt": "Calm seas, sunny tropical sky, modern ships, steam vessels, fantasy monsters, oversized waves, cartoon lighting, text.",
        "omni_prompt": "Animate the ships pitching heavily in immense Southern Ocean rollers: foaming wave crests break over the bow, heavy canvas strains in the howling gale, and the distant rugged Cape headland looms through grey ocean mist.",
        "vo_line": "For days, the fleet fought heavy contrary gales offshore, tacking repeatedly into the cold, turbulent swells of the southern ocean.",
        "animation_potential": "Magnificent storm kinetics: pitching wooden hulls, cascading water on deck, whipping cordage, churning swell."
    },
    {
        "id": "CH01-EP03-S05",
        "title": "Rounding the Cape of Good Hope",
        "date": "22 November 1497",
        "location": "Cape of Good Hope (Cabo da Boa Esperança)",
        "source": "Roteiro, Ravenstein p. 13",
        "confidence": "HIGH",
        "source_facts": "[SOURCE] On Wednesday, 22 November at midday, the fleet doubles the Cape of Good Hope with a favorable wind and sounds their trumpets in celebration.",
        "historical_context": "[HISTORICAL] Passing the Cape of Good Hope marked the successful completion of the Atlantic leg and entry into the southern passage toward the Indian Ocean.",
        "reconstruction": "[RECONSTRUCTION] The sunlight breaking through clouds, trumpeters sounding brass fanfares from the poop deck, crew cheering and embracing on deck.",
        "cinematic": "[CINEMATIC] Heroic wide establishing shot of the four carracks sailing abreast past the legendary cliffs in golden sunlight.",
        "characters": "VASCO_01 standing tall at the quarterdeck rail, PAULO_01, COELHO_01, trumpeters, rejoicing crew.",
        "ships": "SHIP_SG01, SHIP_SR01, SHIP_B01, SHIP_ST01 sailing with full square sails and Order of Christ red crosses illuminated.",
        "environment": "Golden sunlight breaking through clearing storm clouds, deep blue sparkling sea, towering sandstone cliffs of the Cape of Good Hope bathed in light.",
        "continuity": "Vasco da Gama visibly relieved, leg bandaged; ships weathered but triumphant with banners flying.",
        "narration": "On Wednesday, 22 November, the wind shifted. With sails full, the four ships rounded the legendary Cape and entered the passage eastward.",
        "delivery": "Triumphant, solemn documentary delivery; momentous historical milestone.",
        "audio_tags": "[VOICEOVER: documentary narrator, triumphant and resonant] [AMBIENCE: powerful open sea wind, rhythmic rushing wake] [FOLEY: wind filling heavy canvas sails with deep billow, cordage singing, water hissing past hull, distant brass trumpet fanfares echoing across water, crew cheering] [MUSIC: soaring Renaissance strings, noble brass choir fanfare, warm major resolution]",
        "image_prompt": "MASTER_STYLE_02. 22 November 1497, midday, rounding the Cape of Good Hope. Triumphant historical maritime scene: the four Portuguese vessels SHIP_SG01, SHIP_SR01, SHIP_B01, SHIP_ST01 sail proudly past the towering sandstone cliffs of the Cape of Good Hope with square sails fully billowing in a fresh following wind. Golden sunlight breaks through parting storm clouds, illuminating the deep blue ocean and the red Order of Christ crosses on the white sails. On the poop deck of São Gabriel, VASCO_01 and his officers gaze eastward while trumpeters sound brass fanfares. European historical painting, grand cinematic composition, authentic textures, no text, no modern elements.",
        "negative_prompt": "Storm destruction, sunken ships, modern cruise liners, fantasy castle on cliffs, text, watermark, cartoon colors.",
        "omni_prompt": "Animate the historic rounding of the Cape: golden sunlight shafts sweep across the deep blue water, square sails swell with powerful following wind, red banners flutter proudly, and the four carracks glide gracefully past the towering Cape cliffs.",
        "vo_line": "On Wednesday, 22 November, the wind shifted. With sails full, the four ships rounded the legendary Cape and entered the passage eastward.",
        "animation_potential": "Stunning cinematic glide: billowing sails, breaking sun rays on water, proud banner flutter, sweeping cliff perspective."
    },
    {
        "id": "CH01-EP03-S06",
        "title": "Music and Trade at Mossel Bay",
        "date": "25–27 November 1497",
        "location": "Angra de São Brás (Mossel Bay)",
        "source": "Roteiro, Ravenstein pp. 13–16",
        "confidence": "HIGH",
        "source_facts": "[SOURCE] The fleet enters Angra de São Brás on 25 November. Local Khoikhoi pastoralists arrive with herds of cattle and sheep. They play four-holed reed flutes in harmony and dance; the Portuguese play trumpets and dance in return. Trade is conducted: an ox is bartered for three red caps.",
        "historical_context": "[HISTORICAL] The encounter at Mossel Bay was one of the earliest recorded cross-cultural musical exchanges between Europeans and Southern African pastoralists.",
        "reconstruction": "[RECONSTRUCTION] The circular gathering on the sandy beach, pastoralists playing reed flutes (*pastorais*), Portuguese sailors joining in rhythm, trading red wool caps for a fat black ox.",
        "cinematic": "[CINEMATIC] Warm, humanizing mid-shot emphasizing the joyful, harmonious rhythm of the musical exchange.",
        "characters": "VASCO_01, Khoikhoi musicians and pastoralists with reed flutes, Portuguese trumpeters and dancing sailors, cattle.",
        "ships": "The four ships anchored in the calm natural harbor of Mossel Bay in background.",
        "environment": "Sunny coastal bay, lush green and golden grassy hills, white sandy beach, grazing cattle, warm afternoon glow.",
        "continuity": "Portuguese crew in relaxed shore state; local pastoralists wearing leather mantles, ivory bracelets, and shell ornaments.",
        "narration": "At the Bay of São Brás, trade began with the pastoralists of the coast—bartering red caps for livestock to the sound of four-holed reed flutes.",
        "delivery": "Lively, warm documentary tone; celebration of human connection.",
        "audio_tags": "[VOICEOVER: documentary narrator, warm and engaging] [AMBIENCE: sunlit coastal bay, cattle lowing softly, gentle beach surf] [FOLEY: four-holed reed flutes playing in rhythmic harmony, hand clapping, shuffling footsteps on sand, brass trumpet counter-melody, mariner laughter] [MUSIC: authentic modal reed flute pastoral tune with syncopated hand drums]",
        "image_prompt": "MASTER_STYLE_02. 25–27 November 1497, beach at Angra de São Brás (Mossel Bay). Harmonious cross-cultural musical and trade exchange on the African shore: indigenous Khoikhoi pastoralists in leather mantles and ivory arm rings play four-holed reed flutes in unison while dancing on the white sand beside their herd of horned cattle. Portuguese sailors in red caps and linen shirts dance alongside them, while VASCO_01 barters bright red wool caps and brass bracelets with a village elder for a fat ox. In the background, the four wooden ships ride peacefully in the sun-drenched bay. Warm golden lighting, rich human detail, European historical painting, authentic ethnography, no modern elements, no text.",
        "negative_prompt": "Stereotypical savage tropes, modern clothing, modern brass instruments, tropical palms, fantasy elements, text, cartoon style.",
        "omni_prompt": "Animate the lively musical exchange on the beach: pastoralists play reed flutes with rhythmic foot stomping on the sand, Portuguese sailors clap and step in time, cattle shift peacefully, and gentle surf laps the shore under golden afternoon light.",
        "vo_line": "At the Bay of São Brás, trade began with the pastoralists of the coast—bartering red caps for livestock to the sound of four-holed reed flutes.",
        "animation_potential": "Vibrant human motion: flute playing, rhythmic dancing, clapping, cattle tail swish, calm bay reflections."
    },
    {
        "id": "CH01-EP03-S07",
        "title": "Breaking Up the Supply Ship",
        "date": "1–4 December 1497",
        "location": "Beach at Angra de São Brás",
        "source": "Roteiro, Ravenstein pp. 16–17",
        "confidence": "HIGH",
        "source_facts": "[SOURCE] As planned before departure, the storeship (SHIP_ST01) is broken up at São Brás. Her provisions, spare sails, anchors, cordage, and timber are distributed into São Gabriel, São Rafael, and Berrio, and the remaining hull is burned.",
        "historical_context": "[HISTORICAL] The storeship's purpose was to sustain the fleet through the Atlantic arc. Now lightened by consumption and with crew numbers reduced by sickness, consolidating into three armed fighting ships was sound maritime strategy.",
        "reconstruction": "[RECONSTRUCTION] Shipwrights stripping oak planks with crowbars, hauling iron anchors into longboats, the crackling bonfire of the stranded hull on the sand spit.",
        "cinematic": "[CINEMATIC] Somber dusk scene with the glowing silhouette of the burning storeship framing Vasco and his men as they prepare for the uncharted Indian Ocean.",
        "characters": "VASCO_01, PAULO_01, COELHO_01, shipwrights, heavily laden crew hauling crates and anchors.",
        "ships": "SHIP_ST01 dismantled and burning on beach sandbar; SHIP_SG01, SHIP_SR01, SHIP_B01 riding loaded and ready in harbor.",
        "environment": "Dusk over Mossel Bay, glowing orange flames against indigo twilight sky, smoke drifting over water, tide receding.",
        "continuity": "Fleet reduced permanently from four ships to three; crew wearing worn, utilitarian clothing.",
        "narration": "Having transferred its remaining stores into the other three vessels, the supply ship was stripped and burned on the beach—the fleet now pared down to three war-tested ships.",
        "delivery": "Solemn, pragmatic documentary delivery; momentous strategic sacrifice.",
        "audio_tags": "[VOICEOVER: documentary narrator, solemn and resonant] [AMBIENCE: evening sea breeze, rhythmic gentle tide] [FOLEY: heavy oak timber cracking under iron prybars, heavy anchor dragging across gravel, crackle and roar of burning wooden hull, sizzling hiss in wet sand] [MUSIC: somber sustained cello pedal point, reflective minor melody in viola da gamba]",
        "image_prompt": "MASTER_STYLE_02. 1–4 December 1497, dusk at Angra de São Brás. Strategic dismantling and burning of the storeship: the hull of SHIP_ST01 sits beached on a sandy spit, partially dismantled and engulfed in crackling orange fire as smoke rises into the indigo twilight sky. In the foreground, weary Portuguese sailors and shipwrights heave heavy iron anchors, spare sailcloth rolls, and food barrels into longboats to transfer to the remaining three carracks. VASCO_01 stands on the beach watching the blaze with resolute expression. In the bay, SHIP_SG01, SHIP_SR01, and SHIP_B01 wait fully laden. Dramatic firelight and twilight contrast, European historical painting, emotional weight, no text, no modern elements.",
        "negative_prompt": "Accidental shipwreck disaster, fantasy magic fire, modern fire extinguishers, cartoon flames, modern clothes, text.",
        "omni_prompt": "Animate the dramatic dusk scene on the beach: orange flames and smoke lick the oak ribs of the burning supply ship, embers drift into the evening sky, sailors haul heavy crates across the wet sand, and firelight flickers across Vasco da Gama's weathered face.",
        "vo_line": "Having transferred its remaining stores into the other three vessels, the supply ship was stripped and burned on the beach—the fleet now pared down to three war-tested ships.",
        "animation_potential": "Breathtaking lighting kinetics: flickering firelight, rising smoke and embers, reflection of flames on wet sand and tidal pools."
    },
    {
        "id": "CH01-EP03-S08",
        "title": "Departure into the Unknown East",
        "date": "8 December 1497",
        "location": "Departing Angra de São Brás heading northeast along the coast",
        "source": "Roteiro, Ravenstein pp. 17–19",
        "confidence": "HIGH",
        "source_facts": "[SOURCE] On Friday, 8 December 1497, the three remaining ships weigh anchor and stand out to sea, navigating northeast past the headland where a wooden cross had been erected, entering the waters of the Indian Ocean.",
        "historical_context": "[HISTORICAL] Scurvy was beginning to manifest among the crew as they sailed beyond the furthest point reached by Bartolomeu Dias (Rio do Infante), entering waters never before sailed by European ships.",
        "reconstruction": "[RECONSTRUCTION] The three ships sailing tightly together in diamond line-ahead formation, lookout on the bowsprit, morning mist lifting over the rugged green hills of the Garden Route / Wild Coast.",
        "cinematic": "[CINEMATIC] Majestic forward tracking shot over the sea looking toward the endless eastern horizon.",
        "characters": "VASCO_01 at the forward rail of São Gabriel, PAULO_01 on São Rafael, COELHO_01 on Berrio, alert lookouts.",
        "ships": "The 3 canonical surviving ships: SHIP_SG01 (flagship), SHIP_SR01, SHIP_B01 (swift caravel leading slightly).",
        "environment": "Crisp morning sea light, fresh breeze, green lush African hills falling away to the west, vast sparkling Indian Ocean expanding to the east.",
        "continuity": "Three-ship fleet canon established for all subsequent chapters; vessels look heavily weathered, hulls darkened, sails patched.",
        "narration": "On 8 December, the three surviving ships weighed anchor and stood out to sea, pressing northeast into waters no European fleet had ever navigated.",
        "delivery": "Momentous, forward-looking documentary delivery; profound sense of departure into the unknown.",
        "audio_tags": "[VOICEOVER: documentary narrator, momentous and resolute] [AMBIENCE: fresh morning sea wind, rhythmic rushing waves] [FOLEY: heavy iron anchor chain clanking through hawsehole, three wooden hulls cutting clean through water, wind whistling through taut hemp shrouds, fluttering pennants] [MUSIC: expansive modal maritime theme, soaring cello and violin melody, building sense of destiny]",
        "image_prompt": "MASTER_STYLE_02. 8 December 1497, morning, departing Angra de São Brás. Historic departure into the uncharted Indian Ocean: the three surviving Portuguese vessels SHIP_SG01, SHIP_SR01, and SHIP_B01 sail in proud tight formation across a sparkling, deep blue sea, heading northeast along the rugged green African coastline. Crisp morning sunlight glints off the water and illuminates the weathered hulls and patched sails. VASCO_01 stands at the bow of the flagship São Gabriel, looking forward into the open horizon where no European ship has ever sailed. European historical maritime painting, grand atmospheric depth, fine realism, no text, no modern elements.",
        "negative_prompt": "Four ships (supply ship is gone), modern vessels, tropical fantasy islands, cartoon colors, text, watermarks.",
        "omni_prompt": "Animate the three ships sailing boldly into the Indian Ocean: morning sunlight sparkles on the rolling waves, three wooden hulls slice through the water leaving clean foaming wakes, and the lush African coastline recedes on the left as the camera tracks toward the open eastern horizon.",
        "vo_line": "On 8 December, the three surviving ships weighed anchor and stood out to sea, pressing northeast into waters no European fleet had ever navigated.",
        "animation_potential": "Magnificent sweeping motion: three-vessel fleet wake formation, sparkling sea reflections, morning sun flare, forward tracking drift."
    },
]


def main():
    SCENES_DIR.mkdir(parents=True, exist_ok=True)

    for s in SCENES_EP03:
        content = f"""# {s['id']}
# Scene title: {s['title']}
# Date: {s['date']}
# Location: {s['location']}
# Source: {s['source']}
# Historical confidence: {s['confidence']}

## Source Facts

{s['source_facts']}

## Historical Context

{s['historical_context']}

## Reconstruction

{s['reconstruction']}

## Cinematic Interpretation

{s['cinematic']}

## Characters

{s['characters']}

## Ships

{s['ships']}

## Environment

{s['environment']}

## Continuity Requirements

{s['continuity']}

## Narration & Voiceover Script

> "{s['narration']}"

* **Delivery:** {s['delivery']}
* **Classification:** [SOURCE] journal account; [CINEMATIC] documentary voiceover.

## Audio Direction & Sound Design

* **[AUDIO_TAGS]:** {s['audio_tags']}

## Image Prompt

{s['image_prompt']}

## Negative Prompt

{s['negative_prompt']}

## Image-to-Video Prompt (Google Omni Flash)

{s['omni_prompt']}

* **[VOICEOVER]:** "{s['vo_line']}"
* **[AUDIO_TAGS]:** {s['audio_tags']}

## Animation Potential

{s['animation_potential']}
"""
        target = SCENES_DIR / f"{s['id']}.md"
        target.write_text(content, encoding="utf-8")
        print(f"Created: {target.name}")

    print("\nAll Episode 03 scene files generated successfully!")


if __name__ == "__main__":
    main()
