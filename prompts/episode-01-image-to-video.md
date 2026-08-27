# Episode 01 — Image-to-Video Prompt Pack

**Use:** One prompt per approved Chapter 1 scene image.  
**Models:** Model-agnostic prompts suitable for image-to-video systems such as Veo or comparable tools.  
**Default shot length:** 10 seconds per scene; extend only with a controlled loop or hold.  
**Style:** MASTER_STYLE_02.  
**Core rule:** The input image is the canonical visual anchor. Animate motion into the image; do not redesign it.

## Global instruction for every shot

Use the supplied scene image as the exact visual reference. Preserve the identity, face, beard, age, clothing, body proportions, ship silhouettes, mast arrangement, sail arrangement, architecture, cargo, lighting direction, palette, and historical period shown in the source image. Add only physically plausible environmental motion and restrained camera movement. No new characters, no new ships, no object substitutions, no costume changes, no text, no logos, no watermark, no modern elements, no fantasy motion, no exaggerated cinematic destruction. Keep MASTER_STYLE_02: immersive European historical painting with naturalistic oil-paint texture, atmospheric depth, and realistic motion.

## Global audio instruction

Generate restrained, historically grounded audio with each 10-second clip. Voiceover should sound like an intimate documentary narrator, never a modern character speaking as Vasco. Keep the line concise, naturally paced, and beneath no other sound. Use diegetic sound prominently—water, timber, rope, canvas, footsteps, birds, wind, and labor. Music should be sparse orchestral atmosphere rather than trailer music, and remain beneath the voice and environmental sound. No invented dialogue, modern sound effects, lyrics, or recognizable copyrighted melody.

## CH01-S01 — The Armada Is Assembled

**Input:** `images/episode-01/CH01-S01-v1.png`  
**Duration:** 10 seconds  
**Prompt:**

> Animate this still image as a restrained cinematic establishing shot of the Belém waterfront in early July 1497. Make the Tagus water move gently against the quay, gulls cross slowly in the distance, loose rope ends sway, sailcloth breathes in the summer breeze, and dock workers make small believable loading motions. Add a very slow forward camera drift toward VASCO_01 and the four ships, with subtle depth parallax between foreground cargo, workers, water, and background vessels. Preserve all faces, clothing, ship identities, architecture, and composition exactly. European historical painting, natural motion, no new objects, no dialogue text.

**Voiceover:** “In July 1497, four vessels gathered at Belém for a voyage into the ocean.”  
**Sound:** Tagus water, gulls, rope drag, cask knocks, distant port voices, timber creak.  
**Music:** Barely audible low strings and soft frame-drum pulse; curious, spacious, not triumphant.

## CH01-S02 — Command Before the River

**Input:** `images/episode-01/CH01-S02-v1.png`  
**Duration:** 10 seconds  
**Prompt:**

> Animate the deck-height readiness scene with small human gestures only: a hand checks a rope, canvas flutters, a pulley sways slightly, and the four officers make restrained head and eye movements as they inspect the working deck. Add a slow lateral camera move across the rope and sailcloth, settling briefly on VASCO_01 without changing his face or clothing. Keep SHIP_SG01 and the background fleet stable; preserve the late-fifteenth-century Tagus light and painterly texture. No invented speaking mouths, no new tools, no modern instruments, no costume or identity drift.

**Voiceover:** “Command lived in ropes, stores, sails, and the men who had to make them work.”  
**Sound:** Footsteps on planks, canvas snap, pulley creak, low indistinct practical voices.  
**Music:** Sustained viola and muted woodwind breath, almost documentary-quiet.

## CH01-S03 — Cargo and Water

**Input:** `images/episode-01/CH01-S03-v1.png`  
**Duration:** 10 seconds  
**Prompt:**

> Animate the supply-loading scene through physical weight: workers roll one cask a short distance, a hoisted barrel settles gently, rope fibers tighten, loose sailcloth shifts, and water ripples beside the hull. Use a slow downward-and-forward camera move from the SHIP_ST01 hull toward the foreground cargo, with subtle parallax. Preserve every worker, cask, timber bundle, rope coil, ship silhouette, and background waterfront exactly. Motion must remain laborious and realistic, not frantic. No extra cargo, no modern packaging, no object morphing, no text.

**Voiceover:** “Water, food, rope, timber, and sailcloth became the expedition’s first measure of survival.”  
**Sound:** Rolling barrels, wood strain, footsteps, cask thuds, rope fibers tightening, water slosh.  
**Music:** Low cello ostinato, slow and weighty, fading beneath the cargo sounds.

## CH01-S04 — The Four Silhouettes

**Input:** `images/episode-01/CH01-S04-v1.png`  
**Duration:** 10 seconds  
**Prompt:**

> Animate the wide fleet view as a calm Tagus passage. Let each sail respond subtly to one shared wind, make the four hulls rise and fall gently on the same water system, and add small wakes behind the moving vessels. Use a slow wide river glide from SHIP_SG01 across SHIP_SR01, SHIP_B01, and SHIP_ST01 while preserving their relative sizes and positions. Keep the Lisbon shoreline stable with only atmospheric haze and water movement. No ship redesign, no extra vessels, no modern naval formation, no dramatic storm.

**Voiceover:** “Two large ships, a smaller vessel, and a supply ship formed one fragile moving system.”  
**Sound:** Wind broadening, sailcloth filling, water against four hulls, harbor ambience receding.  
**Music:** Open fifths in strings and soft horn; widening scale without heroic fanfare.

## CH01-S05 — Casting Off

**Input:** `images/episode-01/CH01-S05-v1.png`  
**Duration:** 10 seconds  
**Prompt:**

> Animate the wet mooring rope as it slackens and slips from the timber bollard, with droplets falling and a small splash in the Tagus. The nearby hull begins a slow believable movement; sails take a little wind; distant ships shift only slightly. Use a low waterline camera move following the rope toward the departing fleet. Preserve VASCO_01’s practical clothing, all ship structures, shore workers, and the warm summer light. No sudden launch, no celebration effects, no modern flags, no object replacement.

**Voiceover:** “On 8 July 1497, a released rope set the long voyage in motion.”  
**Sound:** Rope slap, bollard creak, water surge, sail snap, shore voices receding.  
**Music:** One low pulse at release, followed by restrained rising strings.

## CH01-S06 — Belém Falls Behind

**Input:** `images/episode-01/CH01-S06-v1.png`  
**Duration:** 10 seconds  
**Prompt:**

> Animate from the stern of SHIP_SG01 as the wake lengthens and Lisbon slowly recedes through atmospheric haze. Add gentle stern movement, rigging vibration, small sail response, and distant fleet motion while keeping the horizon stable. Use a slow backward-looking tracking shot that widens toward open Atlantic water. Preserve the settled late-fifteenth-century shoreline, all ship silhouettes, VASCO_01’s small scale, and natural light exactly. No modern skyline, no map graphics, no sudden geographic jump, no conquest imagery.

**Voiceover:** “Lisbon receded behind them as the fleet entered the Atlantic and turned toward the south.”  
**Sound:** Stern wake, creaking wood, wind through rigging, gulls thinning into open-water ambience.  
**Music:** Sparse bowed strings with a long unresolved note; leave space for the wake.

## CH01-S07 — First Watch

**Input:** `images/episode-01/CH01-S07-v1.png`  
**Duration:** 10 seconds  
**Prompt:**

> Animate this first-night watch with a gentle shielded-lantern flicker reflected on wet planks, slow cloud movement across the stars, slight rigging sway, and subtle breathing or posture shifts from the sailors. Add a restrained lantern-centered camera orbit and a very slow rack of attention from the deck to the distant fleet lights. Preserve VASCO_01’s face, beard, clothing, the dark Atlantic, and the exact ship deck. No supernatural glow, no lightning, no modern lights, no exaggerated fear, no speaking mouths.

**Voiceover:** “At night, the voyage became a discipline of listening—to water, timber, rope, and darkness.”  
**Sound:** Lantern hiss, night water, rigging strain, low footsteps, occasional wood knock.  
**Music:** Almost silent low drone with a single distant bowed note; sea remains dominant.

## CH01-S08 — Southward Course

**Input:** `images/episode-01/CH01-S08-v1.png`  
**Duration:** 10 seconds  
**Prompt:**

> Animate the high wide view as the four-vessel fleet sails a deliberate southbound course across the open Atlantic. Make sails billow in one coherent wind, hulls pitch gently, wakes trail naturally, and cloud shadows move slowly across the water. Use a very slow aerial drift that preserves the fleet’s spacing and never becomes a modern map or drone spectacle. Keep all four ship identities and proportions stable, with no new damage or weathering. End on a quiet hold over the open water, preserving the European historical-painting look.

**Voiceover:** “The fleet took its southward course. The journey had begun.”  
**Sound:** Wind and sea broaden, coherent sail pressure, wakes, distant rigging creaks.  
**Music:** Gentle orchestral lift, resolving back into wind and water before the end card.

## Episode-level negative prompt

No face drift, age change, beard change, costume change, ship morphing, mast changes, sail redesign, extra ships, disappearing crew, duplicated people, modern objects, modern architecture, plastic, fantasy weather, supernatural lighting, impossible camera movement, CGI gloss, cartoon motion, comic-panel transitions, subtitles inside the image, logos, watermarks, or unhistorical dramatic events.

## Assembly note

Use the same approved still as the first and last frame of each shot where the model allows it. Crossfade or cut between shots according to [episode-01-lisbon-blueprint.md](../production/episode-01-lisbon-blueprint.md). Keep generated video clips versioned separately from the locked stills, using names such as `CH01-EP01-S01-motion-v1.mp4`.
