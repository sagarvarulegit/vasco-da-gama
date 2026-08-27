"""Generate action-packed, dramatized scene records and master scenes compilation for Chapter 1 Episode 3 (Cape of Good Hope)."""

import pathlib

SCENES_DIR = pathlib.Path(__file__).resolve().parent.parent.parent / "scenes"
PROMPTS_DIR = pathlib.Path(__file__).resolve().parent.parent.parent / "prompts"

DRAMATIZED_ACTION_SCENES = [
    {
        "id": "CH01-EP03-S01",
        "title": "The Rotten Keel & The Pitch Cauldron",
        "short_title": "Careening at St Helena Bay",
        "date": "4–7 November 1497",
        "location": "St Helena Bay (Angra de Santa Helena), southwest African coast",
        "source": "Roteiro, Ravenstein pp. 3–5",
        "confidence": "HIGH",
        "source_facts": "[SOURCE] 4 Nov land sighted; 7 Nov fleet anchors in St Helena Bay. Crew beaches and careens ships, scrapes hulls, mends sails, and fetches wood and water.",
        "historical_context": "[HISTORICAL] 120 days at sea had infested hulls with shipworm and thick barnacle crusts. If not careened and pitch-sealed here, the imminent Cape gales would splinter the hulls.",
        "reconstruction": "[RECONSTRUCTION] The desperate fever of physical labor, choking black pitch smoke, armed crossbow sentries standing vigil against the arid cliffs.",
        "cinematic": "[CINEMATIC] Low-angle, high-grit wide framing: sweat-drenched mariners hauling tackle to heel the massive ship in foaming surf, boiling black pitch cauldrons roaring.",
        "characters": "VASCO_01 (dark unkempt beard, hawk-like intensity, barking commands), PAULO_01, COELHO_01, sweat-streaked shipwrights, armed sentries with loaded crossbows.",
        "ships": "SHIP_SG01 heeled sharply at a 40-degree angle on the sand spit with exposed barnacled hull; SHIP_SR01, SHIP_B01, SHIP_ST01 anchored in the turquoise bay.",
        "environment": "Blinding southern sun glare, arid fynbos hills, choking black pitch smoke drifting over golden sands, cold crashing Atlantic breakers.",
        "continuity": "Four months of ocean battering: sun-darkened skin, sea-salt encrusted tunics, frayed cordage, unkempt beards.",
        "narration": "Four months in the open ocean had rotted their hulls to the marrow. Beached on a hostile shore, they raced against time to scrape the death from their ships before the Cape swallowed them whole.",
        "delivery": "Intense, gritty, urgent documentary delivery; building suspense.",
        "music_cue": "Driving, suspenseful tribal contrabass ostinato, heavy war-drum heartbeat, rising dissonant string trills building claustrophobic pressure.",
        "audio_tags": "[VOICEOVER: deep, intense documentary narrator, gritty resonance] [AMBIENCE: pounding Atlantic surf on sand, whistling coastal wind, screech of gulls] [FOLEY: iron scrapers screeching violently against barnacled oak, heavy sledgehammers thudding, sizzling pitch cauldrons, men grunting in strain] [MUSIC: low driving contrabass pulse, tense rhythmic percussion, rising dissonant strings]",
        "image_prompt": "MASTER_STYLE_02. 4–7 November 1497, St Helena Bay. High-drama historical scene of desperate ship maintenance: a massive wooden carrack (SHIP_SG01) is heeled sharply on its side on a windblown sandy beach, its exposed oak hull encrusted with dark barnacles and sea-weed. Sweat-streaked Portuguese sailors and shipwrights in salt-stained linen and leather work furiously with iron scrapers and caulking mallets under black smoke from bubbling pitch kettles. In the foreground, VASCO_01, with a dark windblown beard and intense, hawk-like eyes, grips a coiled rope while shouting orders to armed crossbow sentries watching the rugged arid dunes. Behind them, turquoise breakers crash violently. Epic chiaroscuro lighting, visceral grit, European historical painting, dramatic tension, no text, no modern elements.",
        "veo_prompt": "Cinematic 4K historical shot for Google Veo. Source image: images/episode-03/CH01-EP03-S01-v2.png. Intense camera lateral pan: black pitch smoke rolls across wind-whipped sand, iron scrapers grate against the oak hull with violent sparks and debris, crashing waves foam around workers' boots, and Vasco da Gama turns sharply to scan the arid ridge with piercing urgency.",
    },
    {
        "id": "CH01-EP03-S02",
        "title": "The Standoff on the Dunes",
        "short_title": "First Encounter on the Strand",
        "date": "7–8 November 1497",
        "location": "Windblown sand dunes of St Helena Bay",
        "source": "Roteiro, Ravenstein pp. 5–7",
        "confidence": "HIGH",
        "source_facts": "[SOURCE] A lone honey-gatherer in the bush is captured and brought to Vasco. Given food, clothing, brass hawk-bells, and glass beads, then released peacefully.",
        "historical_context": "[HISTORICAL] First contact between Renaissance Europeans and indigenous Khoikhoi hunter-pastoralists—a moment of extreme psychological tension and unspoken danger.",
        "reconstruction": "[RECONSTRUCTION] The breath-held silence across the sandy hollow, the glint of steel daggers half-drawn beneath cloaks, the slow extension of trembling hands.",
        "cinematic": "[CINEMATIC] Extreme shallow depth-of-field close-up: stinging sand whipping across weathered faces, brass bells catching golden sunlight like fire in the open palm.",
        "characters": "VASCO_01 (sharp, calculating gaze), PAULO_01 (hand hovering near sword pommel), Khoikhoi honey-gatherer (poised, fierce, carrying fire-hardened spear).",
        "ships": "Silhouettes of the four ships riding distant in the shimmering heat haze.",
        "environment": "Golden dunes swept by stinging sand gusts, pale fynbos scrub, dazzling sun glare, endless blue horizon.",
        "continuity": "Vasco's salt-stiffened coat, beads of sweat on brow; Khoikhoi man carrying fire-hardened wooden spear and wearing skin kaross.",
        "narration": "On the wind-scoured dunes, two worlds collided in total silence. No words. No charts. Only the razor-edge between trade and slaughter.",
        "delivery": "Suspenseful, hushed documentary whisper; palpable psychological tension.",
        "music_cue": "Haunting solo cello melody over a chilling glass-harmonic drone, suddenly accented by a hollow wooden flute and low booming sub-bass impact.",
        "audio_tags": "[VOICEOVER: intimate, hushed documentary narrator, razor-sharp clarity] [AMBIENCE: whistling desert sea-wind, hissing grains of blowing sand, distant thud of breakers] [FOLEY: delicate, chilling tinkle of brass hawk-bells, leather creak of drawn weapons, ragged breathing, rustling dry grass] [MUSIC: single sustained high violin harmonic, deep sub-bass heart-thump pulse, eerie ethnic wooden flute]",
        "image_prompt": "MASTER_STYLE_02. 7–8 November 1497, windblown sand dunes of St Helena Bay. Breath-holding psychological standoff of first contact: in an eye-level cinematic shot, VASCO_01, weathered and intensely focused in a salt-stained wool doublet, cautiously extends an open hand holding glistening brass hawk-bells and amber glass beads toward an indigenous Khoikhoi honey-gatherer. The Khoikhoi man, draped in a leopard-skin kaross with a horn necklace, stands poised with a fire-hardened spear, his sharp, intelligent eyes locked onto Vasco. Behind Vasco, PAULO_01 keeps a tense hand near his steel sword hilt as wind whips golden sand across their boots. Blinding sun glare, dramatic dust particles, European historical painting, high emotional intensity, no modern elements, no text.",
        "veo_prompt": "Cinematic 4K historical shot for Google Veo. Source image: images/episode-03/CH01-EP03-S02-v2.png. Breath-holding push-in: stinging sand drifts across the frame, tiny brass bells chime softly as Vasco's fingers tremble with tension, the Khoikhoi hunter's eyes narrow with razor-sharp vigilance, and the background grass whips violently in the coastal gale.",
    },
    {
        "id": "CH01-EP03-S03",
        "title": "Ambush in the Breakers",
        "short_title": "Skirmish on the Beach",
        "date": "10–12 November 1497",
        "location": "Foaming surf of St Helena Bay",
        "source": "Roteiro, Ravenstein pp. 7–10",
        "confidence": "HIGH",
        "source_facts": "[SOURCE] Misunderstanding erupts into violence; dozens of armed warriors appear on the ridge; barrage of stones and horn-tipped spears; Vasco da Gama struck in the leg as longboats escape.",
        "historical_context": "[HISTORICAL] Sudden escalation of hostilities. Crossbowmen in the boats discharged bolts to cover the desperate retreat through the surf.",
        "reconstruction": "[RECONSTRUCTION] Red blood staining the sea-foam, Vasco roaring through agony while holding the gunwale, the whistle of deadly wooden assegais slicing through spray.",
        "cinematic": "[CINEMATIC] Visceral, kinetic ground-level battle perspective: water churning violently, crossbow bolt snapping off, flying spears sticking into the wood inches from the camera.",
        "characters": "VASCO_01 (wounded, blood soaking his leg hose, teeth gritted in fury), panicked Fernão Veloso, Portuguese crossbowmen, fierce Khoikhoi warriors charging from dunes.",
        "ships": "Longboat crashing through white surf; four carracks far out in the bay.",
        "environment": "Dark churning sea, violent white foam, stormy grey clouds, spray flying like mist.",
        "continuity": "Vasco takes a severe puncture wound to the thigh; torn clothing, blood in water.",
        "narration": "The beach exploded into violence. A barrage of spears cut the air—and as the surf turned red, Vasco da Gama took a spear through the leg, fighting to the last breath to save his men.",
        "delivery": "Fast, explosive, adrenaline-fueled documentary narration.",
        "music_cue": "Fast, thundering combat percussion, taiko-style war drums, shrieking battle brass stabs, aggressive driving orchestral action strings.",
        "audio_tags": "[VOICEOVER: urgent, commanding documentary narrator, high adrenaline] [AMBIENCE: violent roaring breakers, howling surf wind, chaotic battle echoes] [FOLEY: sickening thud of spear piercing flesh and wood, agonizing gasp, shouting in Portuguese, twang of crossbow strings, oars thrashing water] [MUSIC: thundering war drums, screeching string dissonance, brass stabs]",
        "image_prompt": "MASTER_STYLE_02. 10–12 November 1497, beach at St Helena Bay. Visceral, explosive historical combat in the surf: Portuguese sailors in battered leather armor frantically shove a heavy wooden longboat through violent frothing breakers while a barrage of horn-tipped wooden spears and stones rains down from indigenous warriors on the sand ridge. VASCO_01, grimacing in raw fury and pain, grips the gunwale with blood soaking his wool breeches from a spear embedded in his thigh, shouting fierce orders to a kneeling crossbowman who fires through the sea spray. Foaming churned surf, flying wooden weapons, dark storm clouds, dramatic European historical battle painting, visceral grit, no text, no modern weapons.",
        "veo_prompt": "Cinematic 4K historical shot for Google Veo. Source image: images/episode-03/CH01-EP03-S03-v2.png. Chaotic surf battle tracking: waves slam violently into the wooden longboat, wooden spears splash into foaming water and strike gunwales, crossbow strings release with sharp snaps, and Vasco da Gama grimaces in fury through flying spray as his men haul frantically on the oars.",
    },
    {
        "id": "CH01-EP03-S04",
        "title": "The Fury of the Cape",
        "short_title": "Battling the Cape Headwinds",
        "date": "18–20 November 1497",
        "location": "The Southern Ocean off the Cape of Good Hope",
        "source": "Roteiro, Ravenstein pp. 11–13",
        "confidence": "HIGH",
        "source_facts": "[SOURCE] Fleet reaches the Cape on 18 Nov but encounters fierce contrary southeasterly gales, forcing days of dangerous offshore tacking in towering seas.",
        "historical_context": "[HISTORICAL] Where the Atlantic meets the Indian Ocean, violent gale-force squalls and massive standing swells earned the region its original name: Cabo das Tormentas (Cape of Storms).",
        "reconstruction": "[RECONSTRUCTION] Helmsmen lashed to the whipstaff to prevent being washed overboard; green water cascading across the decks; masts groaning at their breaking point.",
        "cinematic": "[CINEMATIC] Colossal, terrifying scale: extreme low-angle shot looking up at a monstrous black ocean roller towering over the tiny wooden carracks, lightning illuminating the jagged black cliffs of the Cape.",
        "characters": "VASCO_01 (bandaged leg, lashed to the quarterdeck rail, defying the tempest), drenched helmsmen, terrified sailors clinging to rigging.",
        "ships": "SHIP_SG01, SHIP_SR01, SHIP_B01, SHIP_ST01 under shredded storm courses, heeling violently at 45 degrees in towering black waves.",
        "environment": "Cataclysmic stormy ocean, mountainous dark blue-grey waves with frothing white crests, torrential rain and blinding sea spray, pitch-black storm clouds torn by lightning.",
        "continuity": "Ships severely weathered, sails patched, hulls salt-whitened and battered.",
        "narration": "They called it the Cape of Storms—and it was hungry. Mountainous waves battered the four wooden ships into kindling, while lightning exposed the jagged teeth of the African continent.",
        "delivery": "Epic, thunderous documentary narration; awe and dread.",
        "music_cue": "Apocalyptic orchestral fury, massive brass choir shrieking in minor chords, deafening timpani rolls, choir chanting in dark Latin counterpoint.",
        "audio_tags": "[VOICEOVER: powerful, ominous documentary narrator, thundering presence] [AMBIENCE: monstrous howling hurricane winds, titanic ocean waves crashing, deafening roar of water] [FOLEY: structural oak beams groaning and cracking, rigging shrieking under immense strain, tons of green water smashing across the deck, sailors crying out in prayer] [MUSIC: massive orchestral storm crescendo, thundering timpani, shrieking brass choir, choir of doomed voices]",
        "image_prompt": "MASTER_STYLE_02. 18–20 November 1497, the Cape of Storms. Cataclysmic maritime battle against the elements: the flagship SHIP_SG01 heels dangerously at a 45-degree angle as a colossal, mountainous dark oceanic wave crests directly above her decks. Freezing green water cascades over the bowsprit, smashing against drenched mariners lashed to ropes. On the high quarterdeck, VASCO_01, with his wounded leg bound in bloody rags and his heavy wool cloak whipped by the gale, clings to the wooden rail with fierce defiance, glaring into the tempest. In the background, the jagged, monstrous black cliffs of the Cape of Good Hope are illuminated by lightning through the rain. Churning foam, visceral terror, European historical master painting, breathtaking scale, no modern ships, no text.",
        "veo_prompt": "Cinematic 4K historical shot for Google Veo. Source image: images/episode-03/CH01-EP03-S04-v2.png. Titanic storm sequence: the massive carrack plunges violently down the wall of a towering black wave, tons of white foam explode across the deck, lightning flashes across the menacing Cape cliffs, and Vasco da Gama holds fast against the screaming tempest.",
    },
    {
        "id": "CH01-EP03-S05",
        "title": "Doubling the Monster",
        "short_title": "Rounding the Cape of Good Hope",
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
        "narration": "Against all human odds, the impossible barrier broke. In a blaze of golden light, the armada rounded the legendary Cape—the Atlantic was conquered, and the gates to the East were blown wide open.",
        "delivery": "Glorious, resonant, emotionally overwhelming documentary triumph.",
        "music_cue": "Glorious, triumphant, soaring epic brass fanfare, full orchestral strings ascending into a heroic major anthem of historical destiny.",
        "audio_tags": "[VOICEOVER: triumphant, sweeping documentary narrator, deeply emotional] [AMBIENCE: roaring ocean wind transforming into clean following breeze, rushing foaming wake] [FOLEY: canvas snapping open and billowing powerfully, cordage singing, brilliant Renaissance brass trumpets echoing off sea cliffs, sailors roaring in joyous triumph] [MUSIC: soaring orchestral triumph, triumphant French horn fanfare, full rich strings in majestic major key]",
        "image_prompt": "MASTER_STYLE_02. Midday, 22 November 1497, rounding the Cape of Good Hope. Majestic historical triumph: magnificent golden god-rays burst through parting black storm clouds, illuminating the four Portuguese carracks (SHIP_SG01, SHIP_SR01, SHIP_B01, SHIP_ST01) as they surge past the monumental golden sandstone cliffs of the Cape. Their huge square sails, emblazoned with bright crimson Order of Christ crosses, billow proudly in a fresh following wind. On the poop deck of the flagship, VASCO_01 stands tall with wind-whipped hair and raised arm, surrounded by brass trumpeters sounding fanfare and battle-scarred sailors weeping and embracing. Deep sapphire ocean, sparkling white wake, grand European historical masterpiece, emotional catharsis, no text, no modern elements.",
        "veo_prompt": "Cinematic 4K historical shot for Google Veo. Source image: images/episode-03/CH01-EP03-S05-v2.png. Breathtaking breakthrough glide: brilliant rays of golden sunlight sweep across sapphire water, square sails swell with thunderous power, crimson banners stream in the wind, brass horns gleam in the light, and the four vessels surge gracefully past the towering Cape cliffs.",
    },
    {
        "id": "CH01-EP03-S06",
        "title": "The Flutes of São Brás",
        "short_title": "Music and Trade at Mossel Bay",
        "date": "25–27 November 1497",
        "location": "Angra de São Brás (Mossel Bay)",
        "source": "Roteiro, Ravenstein pp. 13–16",
        "confidence": "HIGH",
        "source_facts": "[SOURCE] Fleet enters Mossel Bay. Pastoralists arrive with herds of cattle and sheep. They play four-holed reed flutes in four-part harmony and dance; Portuguese play trumpets and dance in return. An ox bartered for three red caps.",
        "historical_context": "[HISTORICAL] A remarkable, joyous moment of cross-cultural musical exchange. The Khoikhoi played complex multi-part harmonies on tuned reed flutes (gorah / pastorais).",
        "reconstruction": "[RECONSTRUCTION] The swirling circle of dancing pastoralists and sailors kicking up white beach sand; the barter of a massive black ox with twisted horns for scarlet caps.",
        "cinematic": "[CINEMATIC] Vibrant, rhythmic, dynamic celebration: swirling dust, rhythmic foot stomping, bright scarlet wool against golden skin, flute players lost in trance-like joy.",
        "characters": "VASCO_01 (smiling warmly, holding scarlet caps), Khoikhoi master flute players, dancing Portuguese mariners, village elders, fat-tailed sheep and cattle.",
        "ships": "The four ships anchored peacefully in the sparkling turquoise bay.",
        "environment": "Warm sun-drenched beach, green grassy hills, white sand kicking into air, sparkling calm bay waters.",
        "continuity": "Sailors in relaxed shore tunics and red stocking caps; pastoralists wearing polished ivory armlets and ox-hide mantles.",
        "narration": "In the calm of Mossel Bay, the madness of the sea gave way to music. To the hypnotic trance of four-holed reed flutes, conquerors and warriors danced together on the sand in an extraordinary moment of shared humanity.",
        "delivery": "Warm, vibrant, joyous documentary delivery; celebratory rhythm.",
        "music_cue": "Hypnotic African reed flute counterpoint, pounding hand-clapping and foot-stomping rhythms, driving frame drums interwoven with triumphant Renaissance brass.",
        "audio_tags": "[VOICEOVER: warm, celebratory documentary narrator, rhythmic cadence] [AMBIENCE: gentle beach surf, cattle lowing peacefully, warm coastal breeze] [FOLEY: hypnotic ensemble of four tuned reed flutes playing vibrant counterpoint, rhythmic foot stomping on sand, syncopated hand-clapping, mariner laughter, brass trumpet counter-melody] [MUSIC: authentic African pastoral reed flute melody interwoven with Renaissance dance rhythm, energetic hand drums]",
        "image_prompt": "MASTER_STYLE_02. 25–27 November 1497, beach at Angra de São Brás (Mossel Bay). Vibrant, joyous cross-cultural celebration on the African shore: a large circle of indigenous Khoikhoi pastoralists in ox-hide mantles and gleaming ivory arm rings dance energetically in the white sand alongside Portuguese sailors in bright scarlet wool caps. Khoikhoi musicians play four-holed reed flutes in unison with puffed cheeks and ecstatic expressions. In the center, VASCO_01 warmly hands three brilliant red caps and brass bracelets to a smiling village chief beside a magnificent black ox with wide horns. Behind them, the four wooden ships ride calmly in the sunlit turquoise bay. Warm golden sunlight, sand kicking up, rich ethnographic realism, European historical painting, infectious joy, no text, no modern elements.",
        "veo_prompt": "Cinematic 4K historical shot for Google Veo. Source image: images/episode-03/CH01-EP03-S06-v2.png. Exuberant swirling circular track: dust and sand swirl beneath stomping feet, musicians finger their reed flutes with rhythmic swaying, sailors clap and spin in time, and the horned cattle look on peacefully under the warm golden sun.",
    },
    {
        "id": "CH01-EP03-S07",
        "title": "The Funeral of the Supply Ship",
        "short_title": "Breaking Up the Supply Ship",
        "date": "1–4 December 1497",
        "location": "Beach spit at Angra de São Brás",
        "source": "Roteiro, Ravenstein pp. 16–17",
        "confidence": "HIGH",
        "source_facts": "[SOURCE] Storeship (SHIP_ST01) stripped of provisions, sails, anchors, cordage, and timber. Distributed among remaining 3 ships, and hull burned on beach.",
        "historical_context": "[HISTORICAL] Scurvy and casualties had thinned the crews. Burning the supply ship was a calculated, irreversible commitment—burning their bridges to ensure survival.",
        "reconstruction": "[RECONSTRUCTION] The roaring inferno lighting up the night, silhouette of the ship's charred ribs like a dying sea monster, sailors watching in somber reverence.",
        "cinematic": "[CINEMATIC] Dark, brooding chiaroscuro masterpiece: blazing orange fire tearing through oak ribs at midnight, black smoke spiraling into starry skies, Vasco's face carved in intense firelight.",
        "characters": "VASCO_01 (somber, resolute, staring into flames), PAULO_01, COELHO_01, weary shipwrights with crowbars, crew in reflective silence.",
        "ships": "SHIP_ST01 blazing on the sand spit; the three armed survivors SHIP_SG01, SHIP_SR01, SHIP_B01 looming dark and ready in the harbor.",
        "environment": "Deep midnight, glowing orange firestorm, smoke drifting over dark sea, crashing embers, cold night ocean wind.",
        "continuity": "The fleet is now permanently reduced to three ships; clothing blackened by charcoal and smoke.",
        "narration": "There was no going back. Stripped to her bones, the supply ship was cast into the flames—burning the fleet's last lifeline and sealing their pact with destiny.",
        "delivery": "Somber, weighty, haunting documentary delivery; grave strategic commitment.",
        "music_cue": "Somber, gut-wrenching solo cello and crying viola da gamba over a low ominous rumble, rising into a tragic, noble choral requiem.",
        "audio_tags": "[VOICEOVER: grave, haunting documentary narrator, deep dramatic weight] [AMBIENCE: nocturnal sea breeze, gentle lapping waves on sand spit] [FOLEY: deafening roar and crackle of burning oak timbers, showers of sizzling embers hitting wet sand, deep groaning crack as mast collapses into flames, heavy iron anchor dragging] [MUSIC: somber cello solo in minor mode, weeping viola da gamba, dark ominous choir hum]",
        "image_prompt": "MASTER_STYLE_02. 1–4 December 1497, midnight at Angra de São Brás. Dramatic, haunting chiaroscuro sacrifice: the wooden hull of the supply ship (SHIP_ST01) is engulfed in a roaring, majestic orange inferno on a sandy spit, its charred oak ribs glowing like a skeleton against the deep starry night. Billowing black smoke and glowing embers spiral into the dark sky, reflecting violently across the wet tidal sand. In the foreground, VASCO_01 stands motionless in heavy dark wool, his battle-hardened face illuminated by the flickering firelight as he watches the destruction. Behind him, weary sailors load the final salvaged anchors and barrels into longboats. In the dark bay, the three surviving carracks (SHIP_SG01, SHIP_SR01, SHIP_B01) wait in shadowy silhouette. Intense emotional weight, Rembrandt lighting, European historical master painting, no modern elements, no text.",
        "veo_prompt": "Cinematic 4K historical shot for Google Veo. Source image: images/episode-03/CH01-EP03-S07-v2.png. Breathtaking midnight fire pull-back: raging orange flames consume the wooden ribs of the ship, showers of glowing embers drift across the starry sky, firelight dances across Vasco da Gama's stoic face, and the collapsing mast sends a burst of sparks into the night.",
    },
    {
        "id": "CH01-EP03-S08",
        "title": "Beyond the Known World",
        "short_title": "Departure into the Unknown East",
        "date": "8 December 1497",
        "location": "Departing Angra de São Brás into the Indian Ocean",
        "source": "Roteiro, Ravenstein pp. 17–19",
        "confidence": "HIGH",
        "source_facts": "[SOURCE] On Friday, 8 Dec 1497, the 3 remaining vessels weigh anchor and sail northeast past the wooden cross, entering uncharted Indian Ocean waters.",
        "historical_context": "[HISTORICAL] Passing the Rio do Infante boundary, the expedition stepped into complete geographic darkness—where no European charts existed.",
        "reconstruction": "[RECONSTRUCTION] The three ships cutting through morning mist in line-ahead formation, Vasco standing at the bow gazing past the prow into the endless expanse.",
        "cinematic": "[CINEMATIC] Majestic, awe-inspiring epic final shot: low forward camera tracking across deep blue water, the three battle-worn carracks cutting foaming wakes into a radiant sunrise on the Indian Ocean horizon.",
        "characters": "VASCO_01 standing like iron at the bow of São Gabriel, PAULO_01 at São Rafael's helm, COELHO_01 on Berrio, alert lookouts in the crow's nest.",
        "ships": "The 3 canonical survivors: SHIP_SG01 (flagship), SHIP_SR01, SHIP_B01 (speedy caravel scouting ahead).",
        "environment": "Radiant dawn over the Indian Ocean, golden sun rising over the eastern sea, lush green African mountains receding into purple mist.",
        "continuity": "Three-ship fleet established; hulls visibly weathered and scarred, sails patched, crew hardened by six months at sea.",
        "narration": "On 8 December, three lone ships sailed past the edge of all known maps. Behind them lay everything they had ever known. Ahead lay the great unknown... and the road to India.",
        "delivery": "Epic, momentous, goosebump-inducing documentary climax.",
        "music_cue": "Monumental, pulse-pounding, goosebump-inducing epic orchestral crescendo, soaring French horns and racing violins building to an explosive cliffhanger peak.",
        "audio_tags": "[VOICEOVER: epic, resonant documentary narrator, monumental resolution] [AMBIENCE: fresh morning Indian Ocean breeze, powerful rhythmic sea swell] [FOLEY: heavy iron anchor chain clanking through hawsehole, three wooden hulls cutting clean through surging waves, wind humming through taut cordage, fluttering red pennants] [MUSIC: magnificent soaring orchestral theme, triumphant brass, racing violins, massive percussion pulse building to a cliffhanger climax]",
        "image_prompt": "MASTER_STYLE_02. Morning, 8 December 1497, departing into the Indian Ocean. Monumental cinematic finale: the three battle-scarred Portuguese vessels (SHIP_SG01, SHIP_SR01, SHIP_B01) sail in proud, tight diamond formation across a radiant deep blue sea, cutting powerful foaming wakes toward a blinding golden sunrise on the open eastern horizon. Crisp morning sunlight sparkles on the water, illuminating their salt-stained hulls and patched square sails bearing the Order of Christ crosses. At the very prow of the flagship, VASCO_01 stands like an iron sentinel, his dark cloak billowing in the fresh breeze as he gazes into the uncharted ocean where no European ship has ever sailed. Majestic green African mountains recede in the purple morning mist. European historical masterpiece, grand cinematic depth, emotional transcendence, no text, no modern elements.",
        "veo_prompt": "Cinematic 4K historical shot for Google Veo. Source image: images/episode-03/CH01-EP03-S08-v2.png. Monumental cinematic finale glide: morning sunlight blazes across the surging ocean, the three carracks slice through deep blue water leaving sparkling foaming wakes, crimson banners stream proudly in the wind, and the camera glides forward past Vasco da Gama into the vast eastern horizon.",
    },
]


def main():
    SCENES_DIR.mkdir(parents=True, exist_ok=True)
    PROMPTS_DIR.mkdir(parents=True, exist_ok=True)

    master_scenes_doc = """# Chapter 1 Episode 3 — Master Scenes & Prompts (Google Veo)

**Episode:** `CH01-EP03 — Cape of Good Hope (Action-Packed & Dramatized)`  
**Tone:** High-stakes cinematic drama, visceral historical realism, action-packed pacing.  
**Video Generation Target:** Google Veo (Input: Locked Canonical Still `images/episode-03/CH01-EP03-S##-v2.png`).

---

"""

    for s in DRAMATIZED_ACTION_SCENES:
        individual_scene = f"""# {s['id']}
# Scene title: {s['title']}
# Date: {s['date']}
# Location: {s['location']}
# Source: {s['source']}
# Historical confidence: {s['confidence']}

**Image status:** APPROVED / CANONICAL — [CH01-EP03-S{s['id'][-2:]}-v2.png](../images/episode-03/{s['id']}-v2.png), reviewed 26 August 2026
**Lock status:** LOCKED / CANONICAL — CH01-EP03-LOCK-v1

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

## Music & Score Direction

* **Score Cue:** {s['music_cue']}

## Audio Direction & Sound Design

* **[AUDIO_TAGS]:** {s['audio_tags']}

## Image Prompt

{s['image_prompt']}

## Negative Prompt

Project negative prompt; no modern vessels, no fantasy armor, no cartoon elements, no text.

## Google Veo Image-to-Video Prompt

{s['veo_prompt']}

* **[VOICEOVER]:** "{s['narration']}"
* **[MUSIC]:** {s['music_cue']}
* **[AUDIO_TAGS]:** {s['audio_tags']}

## Animation Potential

Maximum kinetic energy, authentic maritime physics, lighting shifts, and emotional character turns.
"""
        target = SCENES_DIR / f"{s['id']}.md"
        target.write_text(individual_scene, encoding="utf-8")
        print(f"Updated individual scene: {target.name}")

        master_scenes_doc += f"""## Scene {s['id'][-2:]}: {s['title']}

* **Scene ID:** `{s['id']}`
* **Historical Date:** {s['date']}
* **Location:** {s['location']}
* **Canonical Image Still:** [`images/episode-03/{s['id']}-v2.png`](../images/episode-03/{s['id']}-v2.png)

### 1. Voiceover Narration & Delivery
> "{s['narration']}"
* **Delivery Tone:** {s['delivery']}

### 2. Music Score & Harmonic Direction
* **Score Cue:** {s['music_cue']}

### 3. Audio Tags (Foley, Ambience, FX)
* **[AUDIO_TAGS]:** {s['audio_tags']}

### 4. Google Veo Prompt (Copy & Paste)
```text
{s['veo_prompt']}
[VOICEOVER]: "{s['narration']}"
[MUSIC]: {s['music_cue']}
{s['audio_tags']}
```

---

"""

    master_path = SCENES_DIR / "CH01-EP03-scenes.md"
    master_path.write_text(master_scenes_doc, encoding="utf-8")
    print(f"Created master compilation: {master_path.name}")


if __name__ == "__main__":
    main()
