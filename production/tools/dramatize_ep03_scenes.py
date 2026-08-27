"""Generate high-drama, cinematic scene records for Chapter 1 Episode 3 (Cape of Good Hope)."""

import pathlib

SCENES_DIR = pathlib.Path(__file__).resolve().parent.parent.parent / "scenes"

DRAMATIZED_SCENES = [
    {
        "id": "CH01-EP03-S01",
        "title": "Careening and Wood Gathering at St Helena Bay",
        "date": "4–7 November 1497",
        "location": "St Helena Bay (Angra de Santa Helena), southwest African coast",
        "source": "Roteiro, Ravenstein pp. 3–5",
        "confidence": "HIGH",
        "source_facts": "[SOURCE] On 4 November land is sighted; on 7 November the fleet anchors in St Helena Bay. The crew careens the ships on the beach, mends sails, and gathers firewood and fresh water from the river.",
        "historical_context": "[HISTORICAL] Four grueling months at sea had fouled hulls with dense barnacles and sea-rot. Unless the hulls were scraped and pitch-caulked here, the impending gales of the Cape would drag them under.",
        "reconstruction": "[RECONSTRUCTION] The feverish physical exhaustion, steam rising from boiling pitch cauldrons, armed lookouts scanning the arid ridges.",
        "cinematic": "[CINEMATIC] Low dramatic wide-angle shot showing sweat-drenched, salt-encrusted sailors hauling ropes to heel a massive ship on the sand, black smoke from pitch kettles billowing against a harsh sunlit sky.",
        "characters": "VASCO_01 (tense, watchful, coordinating refit), PAULO_01, COELHO_01, exhausted shipwrights, caulkers, armed crossbow sentries.",
        "ships": "SHIP_SG01 heeled dramatically on the sand spit with exposed barnacle-encrusted keel; SHIP_SR01, SHIP_B01, SHIP_ST01 in the turquoise bay.",
        "environment": "Blinding southern sun, arid fynbos hills, harsh sea glare, black smoke drifting across golden sand, cold Atlantic breakers.",
        "continuity": "Four months of ocean battering: sun-blackened skin, salt-whitened woolens, frayed cordage, unkempt beards.",
        "narration": "Four months in the open ocean had rotted their hulls and pushed the crew to the brink of collapse. On the barren sands of St Helena Bay, they raced against time to scrape the rot before the Cape claimed them.",
        "delivery": "Intense, gritty, urgent documentary delivery; building suspense.",
        "audio_tags": "[VOICEOVER: deep, intense documentary narrator, gritty resonance] [AMBIENCE: pounding Atlantic surf on sand, whistling coastal wind, screech of gulls] [FOLEY: iron scrapers screeching violently against barnacled oak, heavy sledgehammers thudding, sizzling pitch cauldrons, men grunting in strain] [MUSIC: low driving contrabass pulse, tense rhythmic percussion, rising dissonant strings]",
        "image_prompt": "MASTER_STYLE_02. 4–7 November 1497, St Helena Bay. High-drama historical scene of desperate ship maintenance: a massive wooden carrack (SHIP_SG01) is heeled sharply on its side on a windblown sandy beach, its exposed oak hull encrusted with dark barnacles and sea-weed. Sweat-streaked Portuguese sailors and shipwrights in salt-stained linen and leather work furiously with iron scrapers and caulking mallets under black smoke from bubbling pitch kettles. In the foreground, VASCO_01, with a dark windblown beard and intense, hawk-like eyes, grips a coiled rope while shouting orders to armed crossbow sentries watching the rugged arid dunes. Behind them, turquoise breakers crash violently. Epic chiaroscuro lighting, visceral grit, European historical painting, dramatic tension, no text, no modern elements.",
        "negative_prompt": "Peaceful tropical vacation, modern tools, clean pristine clothes, fantasy armor, steamships, cartoon colors, text.",
        "omni_prompt": "Animate the high-stakes beach repair with intense cinematic motion: black pitch smoke rolls across the wind-whipped sand, iron scrapers grate against the oak hull with violent sparks and debris, crashing waves foam around the workers' boots, and Vasco da Gama turns sharply to scan the arid ridge with piercing urgency.",
        "vo_line": "Four months in the open ocean had rotted their hulls and pushed the crew to the brink of collapse. On the barren sands of St Helena Bay, they raced against time to scrape the rot before the Cape claimed them.",
        "animation_potential": "Maximum kinetic grit: billowing smoke, flying sea-spray, rhythmic scraping labor, tense character turns."
    },
    {
        "id": "CH01-EP03-S02",
        "title": "First Encounter on the Strand",
        "date": "7–8 November 1497",
        "location": "Windblown dunes of St Helena Bay",
        "source": "Roteiro, Ravenstein pp. 5–7",
        "confidence": "HIGH",
        "source_facts": "[SOURCE] A lone inhabitant gathering honey in the scrub is captured and brought to Vasco da Gama. He is fed, given clothing, brass hawk-bells, and glass beads, and released with tokens of goodwill.",
        "historical_context": "[HISTORICAL] The first meeting between Renaissance Europe and the indigenous Khoikhoi people—a moment charged with extreme caution, cultural shock, and unspoken tension.",
        "reconstruction": "[RECONSTRUCTION] The breath-held silence across the sandy hollow, the glint of steel daggers partially concealed, the slow extension of trembling hands.",
        "cinematic": "[CINEMATIC] High-tension eye-level close framing: extreme shallow depth of field, wind-blown sand stinging faces, golden brass bells glinting like fire in the palm.",
        "characters": "VASCO_01 (sharp, calculating gaze), PAULO_01 (hand resting near sword hilt), indigenous Khoikhoi honey-gatherer (poised, fiercely observant, wrapped in skin kaross).",
        "ships": "Silhouettes of the four ships riding distant in the shimmering bay.",
        "environment": "Golden dunes swept by stinging sand gusts, pale fynbos scrub, dazzling sun glare, endless blue horizon.",
        "continuity": "Vasco's salt-stiffened coat, beads of sweat on brow; Khoikhoi man carrying fire-hardened wooden digging stick and horn pendant.",
        "narration": "In the silence of the dunes, two alien worlds stood face to face. With daggers concealed and spears at the ready, the first contact was forged in the glint of brass and glass.",
        "delivery": "Suspenseful, hushed documentary whisper; palpable psychological tension.",
        "audio_tags": "[VOICEOVER: intimate, hushed documentary narrator, razor-sharp clarity] [AMBIENCE: whistling desert sea-wind, hissing grains of blowing sand, distant thud of breakers] [FOLEY: delicate, chilling tinkle of brass hawk-bells, leather creak of drawn weapons, ragged breathing, rustling dry grass] [MUSIC: single sustained high violin harmonic, deep sub-bass heart-thump pulse, eerie ethnic wooden flute]",
        "image_prompt": "MASTER_STYLE_02. 7–8 November 1497, windblown sand dunes of St Helena Bay. Breath-holding psychological standoff of first contact: in an eye-level cinematic shot, VASCO_01, weathered and intensely focused in a salt-stained wool doublet, cautiously extends an open hand holding glistening brass hawk-bells and amber glass beads toward an indigenous Khoikhoi honey-gatherer. The Khoikhoi man, draped in a leopard-skin kaross with a horn necklace, stands poised with a fire-hardened spear, his sharp, intelligent eyes locked onto Vasco. Behind Vasco, PAULO_01 keeps a tense hand near his steel sword hilt as wind whips golden sand across their boots. Blinding sun glare, dramatic dust particles, European historical painting, high emotional intensity, no modern elements, no text.",
        "negative_prompt": "Hollywood stereotypes, modern clothes, peaceful smiles, cartoon graphics, fantasy weapons, text, blur.",
        "omni_prompt": "Animate the breathtaking standoff: stinging sand drifts across the frame, the tiny brass bells chime softly as Vasco's fingers tremble with tension, the Khoikhoi hunter's eyes narrow with razor-sharp vigilance, and the background grass whips violently in the coastal gale.",
        "vo_line": "In the silence of the dunes, two alien worlds stood face to face. With daggers concealed and spears at the ready, the first contact was forged in the glint of brass and glass.",
        "animation_potential": "Masterclass in subtle tension: sand drift, glinting brass, tense facial twitches, blowing skin cloaks."
    },
    {
        "id": "CH01-EP03-S03",
        "title": "Skirmish on the Beach",
        "date": "10–12 November 1497",
        "location": "Foaming surf of St Helena Bay",
        "source": "Roteiro, Ravenstein pp. 7–10",
        "confidence": "HIGH",
        "source_facts": "[SOURCE] Cultural misunderstanding turns to violence; dozens of armed warriors appear on the ridge; stones and horn-tipped spears rain down; Vasco da Gama is struck and wounded in the leg as the longboats fight to escape.",
        "historical_context": "[HISTORICAL] Fear and misinterpretation of gestures triggered an ambush. Crossbowmen in the boats fired into the melee to prevent the entire landing party from being overrun.",
        "reconstruction": "[RECONSTRUCTION] Red blood staining the sea-foam, Vasco roaring through agony while holding the gunwale, the whistle of deadly wooden assegais slicing through spray.",
        "cinematic": "[CINEMATIC] Visceral, kinetic ground-level battle perspective: water churning violently, crossbow bolt snapping off, flying spears sticking into the wood inches from the camera.",
        "characters": "VASCO_01 (wounded, blood soaking his leg hose, teeth gritted in fury), panicked Fernão Veloso, Portuguese crossbowmen, fierce Khoikhoi warriors charging from dunes.",
        "ships": "Longboat crashing through white surf; four carracks far out in the bay.",
        "environment": "Dark churning sea, violent white foam, stormy grey clouds, spray flying like mist.",
        "continuity": "Vasco takes a severe puncture wound to the thigh; torn clothing, blood in water.",
        "narration": "The fragile peace shattered into blood. From the dunes, a barrage of spears rained upon the shore—and as the longboat pushed into the churning surf, a horn-tipped spear struck the captain-major.",
        "delivery": "Fast, explosive, adrenaline-fueled documentary narration.",
        "audio_tags": "[VOICEOVER: urgent, commanding documentary narrator, high adrenaline] [AMBIENCE: violent roaring breakers, howling surf wind, chaotic battle echoes] [FOLEY: sickening thud of spear piercing flesh and wood, agonizing gasp, shouting in Portuguese, twang of crossbow strings, oars thrashing water] [MUSIC: thundering war drums, screeching string dissonance, brass stabs]",
        "image_prompt": "MASTER_STYLE_02. 10–12 November 1497, beach at St Helena Bay. Visceral, explosive historical combat in the surf: Portuguese sailors in battered leather armor frantically shove a heavy wooden longboat through violent frothing breakers while a barrage of horn-tipped wooden spears and stones rains down from indigenous warriors on the sand ridge. VASCO_01, grimacing in raw fury and pain, grips the gunwale with blood soaking his wool breeches from a spear embedded in his thigh, shouting fierce orders to a kneeling crossbowman who fires through the sea spray. Foaming churned surf, flying wooden weapons, dark storm clouds, dramatic European historical battle painting, visceral grit, no text, no modern weapons.",
        "negative_prompt": "Guns, muskets, modern boats, fantasy magic, clean clothes, cartoon blood, peaceful scenes, text.",
        "omni_prompt": "Animate the chaotic surf battle: waves slam violently into the wooden longboat, wooden spears splash into the foaming sea and strike the gunwales, crossbow strings release with sharp snaps, and Vasco da Gama grimaces in fury through flying spray as his men haul frantically on the oars.",
        "vo_line": "The fragile peace shattered into blood. From the dunes, a barrage of spears rained upon the shore—and as the longboat pushed into the churning surf, a horn-tipped spear struck the captain-major.",
        "animation_potential": "Maximum combat kinetic energy: churning foam, flying projectiles, water explosions, raw human struggle."
    },
    {
        "id": "CH01-EP03-S04",
        "title": "Battling the Cape Headwinds",
        "date": "18–20 November 1497",
        "location": "The Southern Ocean off the Cape of Good Hope",
        "source": "Roteiro, Ravenstein pp. 11–13",
        "confidence": "HIGH",
        "source_facts": "[SOURCE] Departing St Helena on 16 November, the fleet reaches the Cape on 18 November but encounters fierce contrary southeasterly gales, forcing days of dangerous offshore tacking in towering seas.",
        "historical_context": "[HISTORICAL] Where the Atlantic meets the Indian Ocean, violent gale-force squalls and massive standing swells earned the region its original name: *Cabo das Tormentas* (Cape of Storms).",
        "reconstruction": "[RECONSTRUCTION] Helmsmen lashed to the whipstaff to prevent being washed overboard; green water cascading across the decks; masts groaning at their breaking point.",
        "cinematic": "[CINEMATIC] Colossal, terrifying scale: extreme low-angle shot looking up at a monstrous black ocean roller towering over the tiny wooden carracks, lightning illuminating the jagged black cliffs of the Cape.",
        "characters": "VASCO_01 (bandaged leg, lashed to the quarterdeck rail, defying the tempest), drenched helmsmen, terrified sailors clinging to rigging.",
        "ships": "SHIP_SG01, SHIP_SR01, SHIP_B01, SHIP_ST01 under shredded storm courses, heeling violently at 45 degrees in towering black waves.",
        "environment": "Cataclysmic stormy ocean, mountainous dark blue-grey waves with frothing white crests, torrential rain and blinding sea spray, pitch-black storm clouds torn by lightning.",
        "continuity": "Ships severely weathered, sails patched, hulls salt-whitened and battered.",
        "narration": "Off the edge of the known world, the ocean unleashed its fury. For six agonizing days, the four fragile hulls fought against the colossal swells of the Cape of Storms, where one mistake meant watery death.",
        "delivery": "Epic, thunderous documentary narration; awe and dread.",
        "audio_tags": "[VOICEOVER: powerful, ominous documentary narrator, thundering presence] [AMBIENCE: monstrous howling hurricane winds, titanic ocean waves crashing, deafening roar of water] [FOLEY: structural oak beams groaning and cracking, rigging shrieking under immense strain, tons of green water smashing across the deck, sailors crying out in prayer] [MUSIC: massive orchestral storm crescendo, thundering timpani, shrieking brass choir, choir of doomed voices]",
        "image_prompt": "MASTER_STYLE_02. 18–20 November 1497, the Cape of Storms. Cataclysmic maritime battle against the elements: the flagship SHIP_SG01 heels dangerously at a 45-degree angle as a colossal, mountainous dark oceanic wave crests directly above her decks. Freezing green water cascades over the bowsprit, smashing against drenched mariners lashed to ropes. On the high quarterdeck, VASCO_01, with his wounded leg bound in bloody rags and his heavy wool cloak whipped by the gale, clings to the wooden rail with fierce defiance, glaring into the tempest. In the background, the jagged, monstrous black cliffs of the Cape of Good Hope are illuminated by lightning through the rain. Churning foam, visceral terror, European historical master painting, breathtaking scale, no modern ships, no text.",
        "negative_prompt": "Calm water, sunny skies, steamships, fantasy sea monsters, cartoon storm, modern oil rigs, text.",
        "omni_prompt": "Animate the titanic storm sequence: the massive carrack plunges violently down the wall of a towering black wave, tons of white foam explode across the deck, lightning flashes across the menacing Cape cliffs, and Vasco da Gama holds fast against the screaming tempest.",
        "vo_line": "Off the edge of the known world, the ocean unleashed its fury. For six agonizing days, the four fragile hulls fought against the colossal swells of the Cape of Storms, where one mistake meant watery death.",
        "animation_potential": "Industry-defining fluid storm animation: pitching hull, cascading green water, lightning flashes, howling gale."
    },
    {
        "id": "CH01-EP03-S05",
        "title": "Rounding the Cape of Good Hope",
        "date": "22 November 1497",
        "location": "Cape of Good Hope (Cabo da Boa Esperança)",
        "source": "Roteiro, Ravenstein p. 13",
        "confidence": "HIGH",
        "source_facts": "[SOURCE] On Wednesday, 22 November at midday, the wind shifts to the northwest. With full sails and sounding trumpets, the armada doubles the Cape of Good Hope.",
        "historical_context": "[HISTORICAL] The psychological climax of the voyage: conquering the geographic barrier that had stopped Portuguese exploration for a decade.",
        "reconstruction": "[RECONSTRUCTION] Tears of relief streaming down salt-encrusted faces; brass trumpeters leaning over the poop rail; red Order of Christ crosses blazing in sunlight.",
        "cinematic": "[CINEMATIC] Epic, breathtaking breakthrough shot: golden shafts of sunlight piercing black clouds, lighting up the sapphire ocean as the four ships surge abreast past the colossal golden cliffs of the Cape.",
        "characters": "VASCO_01 (triumphant, hand raised toward the horizon), PAULO_01, COELHO_01, trumpeters sounding brass horns, weeping crew embracing on deck.",
        "ships": "All four ships SHIP_SG01, SHIP_SR01, SHIP_B01, SHIP_ST01 in glorious line-abreast formation with crimson Order of Christ crosses glowing.",
        "environment": "Dramatic parting storm clouds, brilliant golden god rays, deep sparkling ultramarine ocean, towering sandstone Cape cliffs radiating warm orange light.",
        "continuity": "Exhaustion turning into euphoric triumph; bandaged limbs, wind-tattered banners.",
        "narration": "On Wednesday, 22 November, the impossible barrier broke. In a flood of golden light, the armada doubled the legendary Cape—the Atlantic was behind them, and the Indian Ocean lay open.",
        "delivery": "Glorious, resonant, emotionally overwhelming documentary triumph.",
        "audio_tags": "[VOICEOVER: triumphant, sweeping documentary narrator, deeply emotional] [AMBIENCE: roaring ocean wind transforming into clean following breeze, rushing foaming wake] [FOLEY: canvas snapping open and billowing powerfully, cordage singing, brilliant Renaissance brass trumpets echoing off sea cliffs, sailors roaring in joyous triumph] [MUSIC: soaring orchestral triumph, triumphant French horn fanfare, full rich strings in majestic major key]",
        "image_prompt": "MASTER_STYLE_02. Midday, 22 November 1497, rounding the Cape of Good Hope. Majestic historical triumph: magnificent golden god-rays burst through parting black storm clouds, illuminating the four Portuguese carracks (SHIP_SG01, SHIP_SR01, SHIP_B01, SHIP_ST01) as they surge past the monumental golden sandstone cliffs of the Cape. Their huge square sails, emblazoned with bright crimson Order of Christ crosses, billow proudly in a fresh following wind. On the poop deck of the flagship, VASCO_01 stands tall with wind-whipped hair and raised arm, surrounded by brass trumpeters sounding fanfare and battle-scarred sailors weeping and embracing. Deep sapphire ocean, sparkling white wake, grand European historical masterpiece, emotional catharsis, no text, no modern elements.",
        "negative_prompt": "Modern cruise ships, modern flags, fantasy architecture, cartoon colors, text, watermark.",
        "omni_prompt": "Animate the breathtaking triumph: brilliant rays of sunlight sweep across the sapphire water, square sails swell with thunderous power, crimson banners stream in the wind, brass horns gleam in the light, and the four vessels surge gracefully past the towering Cape cliffs.",
        "vo_line": "On Wednesday, 22 November, the impossible barrier broke. In a flood of golden light, the armada doubled the legendary Cape—the Atlantic was behind them, and the Indian Ocean lay open.",
        "animation_potential": "Epic emotional breakthrough: moving sunbeams, billowing canvas, banner flutter, soaring cliff perspective."
    },
    {
        "id": "CH01-EP03-S06",
        "title": "Music and Trade at Mossel Bay",
        "date": "25–27 November 1497",
        "location": "Angra de São Brás (Mossel Bay)",
        "source": "Roteiro, Ravenstein pp. 13–16",
        "confidence": "HIGH",
        "source_facts": "[SOURCE] The fleet enters Angra de São Brás. Pastoralists arrive with herds of cattle and sheep. They play four-holed reed flutes in four-part harmony and dance; the Portuguese play trumpets and dance in return. Trade: an ox bartered for three red caps.",
        "historical_context": "[HISTORICAL] A remarkable, joyous moment of cross-cultural musical exchange. The Khoikhoi played complex multi-part harmonies on tuned reed flutes (*gorah / pastorais*).",
        "reconstruction": "[RECONSTRUCTION] The swirling circle of dancing pastoralists and sailors kicking up white beach sand; the barter of a massive black ox with twisted horns for scarlet caps.",
        "cinematic": "[CINEMATIC] Vibrant, rhythmic, dynamic celebration: swirling dust, rhythmic foot stomping, bright scarlet wool against golden skin, flute players lost in trance-like joy.",
        "characters": "VASCO_01 (smiling warmly, holding scarlet caps), Khoikhoi master flute players, dancing Portuguese mariners, village elders, fat-tailed sheep and cattle.",
        "ships": "The four ships anchored peacefully in the sparkling turquoise bay.",
        "environment": "Warm sun-drenched beach, green grassy hills, white sand kicking into air, sparkling calm bay waters.",
        "continuity": "Sailors in relaxed shore tunics and red stocking caps; pastoralists wearing polished ivory armlets and ox-hide mantles.",
        "narration": "At Mossel Bay, the tension of the voyage dissolved into music. To the hypnotic rhythm of four-holed reed flutes, Portuguese mariners and Khoikhoi pastoralists danced together on the sand in an extraordinary moment of shared humanity.",
        "delivery": "Warm, vibrant, joyous documentary delivery; celebratory rhythm.",
        "audio_tags": "[VOICEOVER: warm, celebratory documentary narrator, rhythmic cadence] [AMBIENCE: gentle beach surf, cattle lowing peacefully, warm coastal breeze] [FOLEY: hypnotic ensemble of four tuned reed flutes playing vibrant counterpoint, rhythmic foot stomping on sand, syncopated hand-clapping, mariner laughter, brass trumpet counter-melody] [MUSIC: authentic African pastoral reed flute melody interwoven with Renaissance dance rhythm, energetic hand drums]",
        "image_prompt": "MASTER_STYLE_02. 25–27 November 1497, beach at Angra de São Brás (Mossel Bay). Vibrant, joyous cross-cultural celebration on the African shore: a large circle of indigenous Khoikhoi pastoralists in ox-hide mantles and gleaming ivory arm rings dance energetically in the white sand alongside Portuguese sailors in bright scarlet wool caps. Khoikhoi musicians play four-holed reed flutes in unison with puffed cheeks and ecstatic expressions. In the center, VASCO_01 warmly hands three brilliant red caps and brass bracelets to a smiling village chief beside a magnificent black ox with wide horns. Behind them, the four wooden ships ride calmly in the sunlit turquoise bay. Warm golden sunlight, sand kicking up, rich ethnographic realism, European historical painting, infectious joy, no text, no modern elements.",
        "negative_prompt": "Stereotypical savage tropes, modern instruments, tropical palms, cartoon expressions, modern clothing, text.",
        "omni_prompt": "Animate the exuberant dance circle: dust and sand swirl beneath stomping feet, musicians finger their reed flutes with rhythmic swaying, sailors clap and spin in time, and the horned cattle look on peacefully under the warm golden sun.",
        "vo_line": "At Mossel Bay, the tension of the voyage dissolved into music. To the hypnotic rhythm of four-holed reed flutes, Portuguese mariners and Khoikhoi pastoralists danced together on the sand in an extraordinary moment of shared humanity.",
        "animation_potential": "Vibrant choreographic motion: energetic dancing, swirling dust, flute finger movements, cattle shifting."
    },
    {
        "id": "CH01-EP03-S07",
        "title": "Breaking Up the Supply Ship",
        "date": "1–4 December 1497",
        "location": "Beach spit at Angra de São Brás",
        "source": "Roteiro, Ravenstein pp. 16–17",
        "confidence": "HIGH",
        "source_facts": "[SOURCE] The storeship (SHIP_ST01) is stripped of all provisions, sails, anchors, cordage, and timber. Her stores are distributed among São Gabriel, São Rafael, and Berrio, and her hull is burned on the beach.",
        "historical_context": "[HISTORICAL] Scurvy and casualties had thinned the crews. Burning the supply ship was a calculated, irreversible commitment—burning their bridges to ensure the survival of the remaining three fighting ships.",
        "reconstruction": "[RECONSTRUCTION] The roaring inferno lighting up the night, silhouette of the ship's charred ribs like a dying sea monster, sailors watching in somber reverence.",
        "cinematic": "[CINEMATIC] Dark, brooding chiaroscuro masterpiece: blazing orange fire tearing through oak ribs at midnight, black smoke spiraling into starry skies, Vasco's face carved in intense firelight.",
        "characters": "VASCO_01 (somber, resolute, staring into flames), PAULO_01, COELHO_01, weary shipwrights with crowbars, crew in reflective silence.",
        "ships": "SHIP_ST01 blazing on the sand spit; the three armed survivors SHIP_SG01, SHIP_SR01, SHIP_B01 looming dark and ready in the harbor.",
        "environment": "Deep midnight, glowing orange firestorm, smoke drifting over dark sea, crashing embers, cold night ocean wind.",
        "continuity": "The fleet is now permanently reduced to three ships; clothing blackened by charcoal and smoke.",
        "narration": "To survive the unknown ahead, a sacrifice was demanded. Stripped to her bones, the supply ship was set ablaze on the sands—burning the armada’s lifeline and leaving three lone ships with no choice but victory or death.",
        "delivery": "Somber, weighty, haunting documentary delivery; grave strategic commitment.",
        "audio_tags": "[VOICEOVER: grave, haunting documentary narrator, deep dramatic weight] [AMBIENCE: nocturnal sea breeze, gentle lapping waves on sand spit] [FOLEY: deafening roar and crackle of burning oak timbers, showers of sizzling embers hitting wet sand, deep groaning crack as mast collapses into flames, heavy iron anchor dragging] [MUSIC: somber cello solo in minor mode, weeping viola da gamba, dark ominous choir hum]",
        "image_prompt": "MASTER_STYLE_02. 1–4 December 1497, midnight at Angra de São Brás. Dramatic, haunting chiaroscuro sacrifice: the wooden hull of the supply ship (SHIP_ST01) is engulfed in a roaring, majestic orange inferno on a sandy spit, its charred oak ribs glowing like a skeleton against the deep starry night. Billowing black smoke and glowing embers spiral into the dark sky, reflecting violently across the wet tidal sand. In the foreground, VASCO_01 stands motionless in heavy dark wool, his battle-hardened face illuminated by the flickering firelight as he watches the destruction. Behind him, weary sailors load the final salvaged anchors and barrels into longboats. In the dark bay, the three surviving carracks (SHIP_SG01, SHIP_SR01, SHIP_B01) wait in shadowy silhouette. Intense emotional weight, Rembrandt lighting, European historical master painting, no modern elements, no text.",
        "negative_prompt": "Accidental shipwreck, fantasy magic fire, cartoon flames, modern firefighters, modern clothes, text.",
        "omni_prompt": "Animate the breathtaking midnight fire: raging orange flames consume the wooden ribs of the ship, showers of glowing embers drift across the starry sky, firelight dances across Vasco da Gama's stoic face, and the collapsing mast sends a burst of sparks into the night.",
        "vo_line": "To survive the unknown ahead, a sacrifice was demanded. Stripped to her bones, the supply ship was set ablaze on the sands—burning the armada’s lifeline and leaving three lone ships with no choice but victory or death.",
        "animation_potential": "Spectacular lighting and fluid fire physics: licking flames, drifting embers, glowing reflections on wet sand."
    },
    {
        "id": "CH01-EP03-S08",
        "title": "Departure into the Unknown East",
        "date": "8 December 1497",
        "location": "Departing Angra de São Brás into the Indian Ocean",
        "source": "Roteiro, Ravenstein pp. 17–19",
        "confidence": "HIGH",
        "source_facts": "[SOURCE] On Friday, 8 December 1497, the three remaining vessels weigh anchor and stand out to sea, sailing northeast past the wooden cross erected on the hill, pushing beyond the limits of all prior navigation.",
        "historical_context": "[HISTORICAL] Passing the Rio do Infante boundary, the expedition stepped into complete geographic darkness—where no European charts existed.",
        "reconstruction": "[RECONSTRUCTION] The three ships cutting through morning mist in line-ahead formation, Vasco standing at the bow gazing past the prow into the endless expanse.",
        "cinematic": "[CINEMATIC] Majestic, awe-inspiring epic final shot: low forward camera tracking across deep blue water, the three battle-worn carracks cutting foaming wakes into a radiant sunrise on the Indian Ocean horizon.",
        "characters": "VASCO_01 standing like iron at the bow of São Gabriel, PAULO_01 at São Rafael's helm, COELHO_01 on Berrio, alert lookouts in the crow's nest.",
        "ships": "The 3 canonical survivors: SHIP_SG01 (flagship), SHIP_SR01, SHIP_B01 (speedy caravel scouting ahead).",
        "environment": "Radiant dawn over the Indian Ocean, golden sun rising over the eastern sea, lush green African mountains receding into purple mist.",
        "continuity": "Three-ship fleet established; hulls visibly weathered and scarred, sails patched, crew hardened by six months at sea.",
        "narration": "On 8 December, the three surviving ships weighed anchor and stood out to sea. Behind them lay Africa and the Atlantic. Ahead lay thousands of leagues of uncharted ocean, and the destiny of nations.",
        "delivery": "Epic, momentous, goosebump-inducing documentary climax.",
        "audio_tags": "[VOICEOVER: epic, resonant documentary narrator, monumental resolution] [AMBIENCE: fresh morning Indian Ocean breeze, powerful rhythmic sea swell] [FOLEY: heavy iron anchor chain clanking through hawsehole, three wooden hulls cutting clean through surging waves, wind humming through taut cordage, fluttering red pennants] [MUSIC: magnificent soaring orchestral theme, triumphant brass, racing violins, massive percussion pulse building to a cliffhanger climax]",
        "image_prompt": "MASTER_STYLE_02. Morning, 8 December 1497, departing into the Indian Ocean. Monumental cinematic finale: the three battle-scarred Portuguese vessels (SHIP_SG01, SHIP_SR01, SHIP_B01) sail in proud, tight diamond formation across a radiant deep blue sea, cutting powerful foaming wakes toward a blinding golden sunrise on the open eastern horizon. Crisp morning sunlight sparkles on the water, illuminating their salt-stained hulls and patched square sails bearing the Order of Christ crosses. At the very prow of the flagship, VASCO_01 stands like an iron sentinel, his dark cloak billowing in the fresh breeze as he gazes into the uncharted ocean where no European ship has ever sailed. Majestic green African mountains recede in the purple morning mist. European historical masterpiece, grand cinematic depth, emotional transcendence, no text, no modern elements.",
        "negative_prompt": "Four ships (supply ship is gone), modern vessels, fantasy islands, cartoon colors, text, watermark.",
        "omni_prompt": "Animate the breathtaking finale: morning sunlight blazes across the surging ocean, the three carracks slice through deep blue water leaving sparkling foaming wakes, crimson banners stream proudly in the wind, and the camera glides forward past Vasco da Gama into the vast eastern horizon.",
        "vo_line": "On 8 December, the three surviving ships weighed anchor and stood out to sea. Behind them lay Africa and the Atlantic. Ahead lay thousands of leagues of uncharted ocean, and the destiny of nations.",
        "animation_potential": "Masterpiece camera glide: sparkling ocean surface, cutting bow wakes, streaming pennants, soaring epic horizon."
    },
]


def main():
    SCENES_DIR.mkdir(parents=True, exist_ok=True)

    for s in DRAMATIZED_SCENES:
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
* **Classification:** [SOURCE] journal account; [CINEMATIC] dramatized documentary voiceover.

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
        print(f"Updated Dramatized Scene: {target.name}")

    print("\nAll Episode 03 scene records dramatized successfully!")


if __name__ == "__main__":
    main()
