# Emmeloord Vrijbaan: improvement log

Each daily run adds an entry at the top: the plan, what was done (title, category, outcome), problems found, and ideas for the next run.

## 2026-11-25 (run 06:45)

### Plan (prioritized)
No open bugs except the one the 01:17 run noticed (the leaf blower worker standing behind the tree trunk). Its "next ideas" list is the base:

1. **Leaf blower polish** (bug): the worker blows from the open side of the heap, away from the tree trunk, and the nozzle points at the leaves.
2. **Festive lights over the shopping streets** (graphics): in winter strings of warm fairy lights hang across the real shopping streets of the centre (OSM street lines), glowing from dusk.
3. **Ice chairs on the frozen canal** (content): parents push toddlers on wooden ice chairs ("ijsstoel") among the skaters.
4. Conkers under chestnut trees were checked: the 6,328 OSM trees round Emmeloord carry no genus/species tags, so there is no real place for chestnut trees; skipped.
5. **Performance**: merge loose meshes near De Deel if time allows.

### Done
- **Leaf blower polish** (bug): each heap now remembers the tree it lies under. The worker blows from the open side of the heap, at least 1.6 m from the trunk, walks up from that side and sweeps the nozzle over the leaves. Tested on 6 heaps: worker 2.1-2.3 m from the heap and 3.7-4.1 m from the trunk every time.
- **Festive lights** (graphics): in winter, 54 strings with about 2,100 warm white bulbs hang in shallow loops across the shopping streets of the centre (the OSM lines of Lange Nering, Kerksteeg, Smallegang, Luifelsteeg, De Schalm and de Deel), every 11 m, tied to the house fronts on both sides about 5 m up (only where there are buildings on both sides, 5-24 m apart). Every third string has short hanging drops, others alternate warm white and gold bulbs. One Points mesh with a twinkle shader and one line mesh (2 draw calls). Small and pale by day, glowing from dusk.
- **Ice chairs** (content): two parents on skates push a toddler along the frozen canals on a wooden ice chair (runners curled up at the front, seat, back, sides, push bar). Arms reach forward to the bar, gentler sway, no falls, and they turn round earlier so the chair stays on the ice.
- **Seasonal day length** (graphics/realism): sunrise and sunset follow the season as in Emmeloord (winter about 08:33-16:51, autumn 07:42-18:24, spring 06:36-20:24, summer 05:36-21:54), the sun stays lower in winter (longer shadows) and the moon rises after sunset. A new game in winter starts at 09:30 so it does not begin in the dark. Winter afternoons now end in dusk under the festive lights.
- **README** updated for all of these.

### Report for Ron
This run (06:45) added 4 improvements, each tested in headless Chromium (no console errors; walking, getting into a car and driving off, the worker on 6 heaps, the lights at 13:00, 16:54 and 21:00, two ice chairs on the canal) and pushed straight to `main`:
- The leaf blower worker no longer stands behind the tree trunk.
- In winter there are fairy lights across the shopping streets of the centre.
- Parents push toddlers on wooden ice chairs on the frozen canals.
- Days are short in winter and long in summer, like in real Emmeloord.

Screenshots in the project files under `runs/`: `2026-11-25b-festive-lights.png` (Lange Nering at 21:00 with loops of warm lights over the street), `2026-11-25b-winter-dusk-lights.png` (the same street at 16:54 on a winter afternoon, pink dusk sky), `2026-11-25b-ice-chair.png` (a parent in a woolly hat pushing a toddler on a red-brown ice chair).

Problems: none found. Note that the fixed screenshot spot `deel-dusk` (19:36) in `tools/shots.js` is now night in autumn and winter because the sun sets earlier; use about 18:00 (autumn) or 16:40 (winter) for a dusk shot. Conkers could not be added: the OSM trees round Emmeloord have no species tags, so there are no real chestnut trees to place them under.

### Next ideas (for the next run)
1. Let the player rent and push an ice chair at the skate rack (or sit in one and be pushed).
2. Some snow on the festive light wires and the shop awnings after a snowfall.
3. A late-night/early-morning winter mood: frost on car windscreens before sunrise (scrape it off before driving).
4. Performance: measure draw calls per object at De Deel and merge what is loose.
5. Check the times of the school run and the skaters against the new short winter days.

## 2026-11-25 (run 01:17)

### Plan (prioritized)
No open bugs except the one the 11:52 run noticed. Its "next ideas" list is the base:

1. **Culvert bridge slab** (bug/graphics): the dark slab on top of small culvert bridges (Rietstraat over the canal); give them a proper deck edge and railing.
2. **Frost breath** (graphics): small puffs at the mouth of people (and the player) on cold mornings and in winter.
3. **Street sweeper** (content/gameplay): in autumn a small municipal sweeper drives the streets near you and clears leaf heaps.
4. **Snowballs and tree crowns** (bug): snowballs fly through crowns; let them hit and shake a bit of snow off.
5. **Puddles with leaves / conkers** (content): if time allows.
6. **Performance**: merge loose meshes near De Deel if time allows.

### Done
- **Black embankments by culvert bridges** (bug/graphics): the "dark slab" was two things. The grass embankments on the raised culvert bridges were nearly black, because the grass photo tint was multiplied once per map tile when several tile meshes share one material (the embankment material got it dozens of times). `applyPhotoTextures` now treats each material once (the last slot for a material still wins, as before). The railing was one solid 1 m dark plate; it is now an open railing with a top, middle and bottom rail and posts about every 1.6 m.
- **Frost breath** (graphics): on cold days (all winter, autumn before 10:00 and after 18:00 with a fainter breath around those hours, spring before 08:00) you and the people within 18 m of the camera breathe out small clouds of mist every 3 to 4 s (faster when sprinting or skating). One Points mesh with a soft-sprite shader, 160 puffs at most; darker at night.
- **Leaf blower worker** (content/sound): kick a heap of leaves over and a few seconds later (3 in 4 times, at most once every 40 s) a council worker in a yellow hi-vis jacket walks up from about 18 m away with a leaf blower. For 7 s the leaves swirl in from round about while the heap grows back, with a procedural two-stroke whine that fades with distance; sometimes they grumble ("Not again..."). Then they walk off.
- **Snowballs and tree crowns** (bug): snowballs now stop in the crown of a round street tree, with a soft thump and a little shower of snow falling from the branches.
- **README** updated (frost breath, leaf blower, tree crowns).

### Report for Ron
This run (01:17) added 4 improvements, each tested in headless Chromium (no console errors; walking, the bridge from two sides, frost breath at 08:12 in winter, a kicked heap with the worker blowing it back, a snowball into a tree crown) and pushed straight to `main`:
- The black wedges and dark slab at the small culvert bridges (Rietstraat) are gone: the grass beside them is green again and the bridges have open railings.
- Frost breath on cold days for you and the people round you.
- A council worker with a leaf blower comes to tidy up a heap you kicked over.
- Snowballs no longer fly through tree crowns.

Screenshots in the project files under `runs/`: `2026-11-25-culvert-bridge.png` (the Rietstraat culvert bridge with green banks and an open blue railing), `2026-11-25-frost-breath.png` (the player at De Deel on a winter morning with a small puff of mist at the mouth), `2026-11-25-leaf-blower.png` (a worker in a yellow jacket by a tree, leaves swirling round the heap, bubble "Not again...").

Problems: the worker sometimes stands behind the tree trunk while blowing. The bug with the grass tint may have darkened other shared grass materials in the past too; they all look normal now. The session restarted once mid-run, no work was lost.

### Next ideas (for the next run)
1. Leaf blower polish: keep the worker on the open side of the heap (away from the trunk) and point the nozzle at the heap.
2. Puddles with floating leaves after rain in autumn; conkers (kastanjes) under the chestnut trees to pick up.
3. Sledge or ice chair ("ijsstoel") on the frozen canal.
4. Breath for horses/dogs if any, and steam from manholes on cold mornings.
5. Performance: merge the remaining loose meshes near De Deel (bus stop signs, lamp glow planes).

## 2026-11-24 (run 11:52)

### Plan (prioritized)
No open bugs were left by the 06:45 run. Its "next ideas" list is the base for this run:

1. **Ice race with rivals** (gameplay): two skaters (in racing suits) race you round the flags, with a 3-2-1 countdown, and you finish 1st, 2nd or 3rd (a bonus and a new achievement for winning).
2. **Thin ice near bridges** (gameplay/sound): close to a bridge the ice is thin: it creaks and cracks, a warning shows, and if you stay you break through to your knees and have to scramble out.
3. **Snowmen and snowballs** (content/gameplay): when snow lies, children build snowmen on lawns, and you can throw snowballs at people (they react).
4. **Performance** (performance): merge more static meshes in the centre (dark glass of bus shelters and shop fronts, lamp glow planes).
5. Leftovers if there is time: a sledge or ice chair, polish.

### Done
- **Ice race with rivals** (gameplay): Sjoerd (red racing suit) and Femke (blue) line up beside you at the stall. A 3-2-1 countdown holds everyone still, then they race round the flags: they push off like the other skaters, slow down for each turn, swing round the stall and keep a light rubber band with you (about 0.8 m/s either way). You finish 1st, 2nd or 3rd; winning pays a €20 prize and the new achievement "Fastest on the ice". Normal pushing (8 m/s) usually gets you 3rd; sprinting with Shift wins. Racers wear no winter coats.
- **Thin ice by the bridges** (gameplay/sound/graphics): beside every bridge over a frozen canal the ice is darker (one mesh with vertex alpha on a 1 m grid over the ice only, about 7000 cells town-wide, built in about 0.3 s the first time the canals freeze). Stand on it and it creaks and cracks with a warning; stay about 3 s (gliding fast buys time) and you go through up to your knees, leaving a black hole with broken plates of ice (it stays for 3 minutes). Walk to the edge of the hole to scramble out. People nearby shout. New achievement "Wet feet".
- **Snowmen and snowballs** (content/gameplay/sound): once the snow lies thick, about 26 snowmen stand on lawns round town (carrot nose, coal eyes, stick arms, a hat, a bucket or a scarf; one mesh each), built while you are not looking and sagging as the snow melts. Throw snowballs with **Q** (on phones the HORN button turns into THROW on foot): they lock on to someone near your aim, fly in an arc, splat in a puff of snow and stop at walls and trees. People shout ("Right in the neck!"), skaters wobble, and children (and about a third of the grown-ups) throw one back. New achievement "Snowball fight" (hit five people). 34 achievements in total.
- **README** updated: Q key, rivals, thin ice, snowmen.
- **Performance** (performance): only cars within 26 m of the camera (and your own) cast wheel shadows, and only people within 28 m (40 m on High) cast a shadow. At De Deel this cuts draw calls from about 906 to 801 per frame, with no visible change.
- **Children's snowball fights** (content): on snowy days children near you throw snowballs at each other (and now and then at a grown-up), with a shout when one hits.
- **Autumn leaves** (graphics/gameplay/sound): it is autumn in the game right now (the season follows the calendar), so this one shows straight away. Leaves flutter down from the street trees round you (up to 170 on High, one instanced mesh, more in gusts) and lie on the ground for a few seconds. About 60 heaps of raked leaves lie under trees along the streets (one instanced mesh); walk, cycle or drive through one and 40 leaves fly up with a rustle, and it is raked up again out of sight a few minutes later. New achievement "Leaf kicker" (35 in total).

### Report for Ron
This run (11:52) added 7 improvements, each tested in headless Chromium (no console errors; walking, driving, the ice race with rivals from countdown to finish, breaking through thin ice and climbing out, throwing snowballs and the throw-back, kicking a leaf heap, all scripted and checked with screenshots) and pushed straight to `main`:
- Ice race against two rival skaters, Sjoerd and Femke, with a 3-2-1 countdown, 1st/2nd/3rd place and a €20 prize for winning.
- Thin ice beside the bridges: darker ice that creaks and cracks; stay too long and you go through to your knees and must climb out.
- Snowmen on the lawns when snow lies, and snowball fights: throw with **Q** (THROW button on phones); people shout, children throw back and have fights of their own.
- Autumn (the season you see now): falling leaves and heaps of leaves you can kick through.
- Fewer shadow draw calls near De Deel (about 12% fewer draw calls there).
- 4 new achievements (35 in total); README updated.

Screenshots in the project files under `runs/`: `2026-11-24c-ice-race-rivals.png` (you in orange between Sjoerd in red and Femke in blue on the ice by the koek-en-zopie stall, "Get ready… 3"), `2026-11-24c-thin-ice.png` (the player knee-deep in a black hole in the ice with broken plates round it, beside a bridge), `2026-11-24c-thin-ice-patch.png` (the darker thin ice at the end of a canal by a bridge), `2026-11-24c-snowball-snowman.png` (a snowman with a carrot nose and scarf on a snowy square, a man shouting "Right in the neck!"), `2026-11-24c-leaf-heap.png` and `2026-11-24c-leaf-kick.png` (a heap of leaves under a street tree, then the leaves flying up).

Problems: none open. The winter things (ice, snow, snowmen) only show when the season is winter; with the season on Auto that starts on 1 December, until then pick Winter in the pause menu. The large dark slab on top of some small culvert bridges (seen while testing thin ice at Rietstraat) is not new and still looks odd; worth a look. Snowballs fly through tree crowns (they only stop at trunks and walls).

### Next ideas (for the next run)
1. Check the dark slab on top of small culvert bridges (Rietstraat over the canal) and give it a proper deck and railing.
2. More autumn: puddles with floating leaves, a leaf blower man or a street sweeper truck clearing the heaps, conkers (kastanjes) to pick up.
3. Sledge or ice chair ("ijsstoel") on the frozen canal: push a child over the ice.
4. Frost breath for people on cold winter mornings (small puffs at the mouth).
5. More performance: merge the remaining loose meshes near De Deel (bus stop signs, lamp glow planes).

## 2026-11-24 (run 06:45)

### Plan (prioritized)
No open bugs were left by the 01:17 run. Its "next ideas" list is the base for this run:

1. **Skates to rent** (gameplay/graphics/sound): a skate rack beside the koek-en-zopie stall. Rent skates (€5) and you skate on the ice: faster, a proper skating stride and lean, blades on your feet, the scrape of the blades. Blades on the skaters' feet too.
2. **Falling over on the ice** (gameplay): turn too sharply at speed on the ice (more easily without skates) and you slip and fall, get up again after a moment.
3. **Ice race** (gameplay/content): a new timed job from the stall: skate round flags along the frozen canal and back before the time runs out.
4. **Fingers round the oliebol and the cup** (graphics): curl the player's fingers when eating and holding a cup of hot chocolate.
5. **Frost days** (content/seasons): freeze the canals after cold days, with a "the ice is open" message, if it fits without making the ice too rare.
6. Leftovers if there is time: phone performance (merge loose static meshes near De Deel), polish.

### Done
- **Skates to rent** (gameplay/graphics/sound): a skate rack with a "SKATES €5" sign stands beside the koek-en-zopie stall. Rent a pair with **E** (hand them back the same way). On the ice you skate: push off with W to about 8 m/s (11 with Shift), glide a long way when you let go, steer into the glide, lean forward with a slow stride and a sway, and the blades scrape on every push. On land you can only waddle ("klunen"). Steel blades are drawn under the feet of every skater (one instanced mesh). New achievement "Polder skater".
- **Falling over on the ice** (gameplay/sound): turn round sharply at speed on the ice (much harder on skates, and now and then when you skate fast close to the bank) and you slip: you tip over backwards, slide on your back for a moment, then get up. A thud, a toast ("Bambi on ice..."), and someone nearby laughs in a speech bubble. New achievement "Bambi on ice". The skaters on the canals also fall now and then and get up again.
- **Bug fix: job markers** (bug): the coloured rings and light beams of all jobs stood together at the map origin instead of at each job's start spot (since the first version). They now stand on their own spots.
- **Ice race** (gameplay/content): a new winter job (light blue marker on the ice beside the stall, level 1, needs rented skates). Skate to an orange flag at each end of the straight frozen canal (laid out along the canal from the stall, about 120 m each way) and back to the stall against the clock. The best time is saved. New achievement "Eleven towns, one canal" (31 in total). The job is hidden outside winter and does not count for "Jack of all trades".
- **Hot chocolate and fingers** (graphics/sound): after buying hot chocolate you carry a steaming paper cup in your right hand and take five sips (arm to mouth, a soft slurp). The hero's fingers now curl round the cup, the oliebol and the oliebollen bag (each joint set from its rest pose, restored when you let go).
- **Performance** (performance): the Poldertoren's gallery railing (56 bars and posts) and each clock's ring with its 12 hour marks are now single meshes: about 100 fewer draw calls (main and shadow pass) wherever the tower is in view, with the same look (checked side by side).
- **README** updated: skates, ice race, falling, the cup, 31 achievements.

### Report for Ron
This run (06:45) added 7 improvements, each tested in headless Chromium (no console errors; walking, driving, renting skates, skating, falling, the ice race from start to finish and the hot chocolate scripted and checked with screenshots) and pushed straight to `main`:
- Rent skates at the koek-en-zopie stall and skate on the frozen canals: fast, gliding, leaning forward, with blades on your feet.
- Turn too sharply on the ice and you fall on your back (people laugh). The other skaters fall now and then too.
- A new winter job, the Ice race: skate to the flags at both ends of the canal and back against the clock.
- Bug fix: the job markers (rings and light beams) now stand at their jobs; before, they all stood at one spot in the middle of town.
- Hot chocolate comes in a steaming cup you sip from, and the fingers close round what you hold.
- The Poldertoren is a bit cheaper to draw (about 100 fewer draw calls).

Screenshots in the project files under `runs/`: `2026-11-24b-skating.png` (the player gliding on the frozen canal beside the Poldertoren, leaning forward with blades on his shoes), `2026-11-24b-fall-on-ice.png` (the player flat on his back on the ice), `2026-11-24b-skate-rack.png` (the stall with the SKATES €5 rack), `2026-11-24b-ice-race.png` (the ice race with timer and the marker at the far end of the canal), `2026-11-24b-hot-chocolate.png` (sipping from the cup), `2026-11-24b-job-marker-fixed.png` (the yellow taxi job marker at its own spot).

Problems: none open. The ice race flags are thin and only show up from about 60 m; the light beam of the target marker shows the way from further. Frost days (ice only after a few cold days) were left out on purpose: with the ice tied to the winter season you always find it when you pick winter.

### Next ideas (for the next run)
1. A real ice race with rival skaters (two or three NPC skaters racing you, like the ring race).
2. Ice chair ("ijsstoel") or a sledge: push a child on a chair over the ice, or a sledge on a snowy slope.
3. Merge more static meshes in the centre: the glass of bus shelters and shop fronts near De Deel (about 26 dark glass meshes) and the lamp glow planes.
4. Thin ice near bridges: a crack sound and a warning, and you sink to your knees if you stay there.
5. Frost days as an option in the pause menu (ice after cold days) if Ron wants it.

## 2026-11-24 (run 01:17)

### Plan (prioritized)
No open bugs were left by the 11:52 run. Its "next ideas" list is the base for tonight:

1. **Real path to the college bike park** (content/bug): pupils now ride over the grass for the last 20 m. Use the OSM paths (ways 1360765716, 1360765715, 1314839838, 1314839805) from the end of Hendric Stevinlaan to the bike park, draw them as paving and let pupils follow them.
2. **Eating oliebollen** (gameplay/graphics): after buying a bag, the player eats them on the way (arm to mouth), with powdered sugar on the shirt for a while and a line from passers-by.
3. **Winter coats** (graphics/seasons): longer, darker coats over the shirt in winter, keeping the shirt colour known for the lost-child hints.
4. **More families** (gameplay/content): a dad with two children as a taxi fare, and children on a child seat on a parent's bike.
5. **Phone performance check** (performance/mobile): draw calls near crowds in winter (scarves, hats) at the phone quality level.
6. Leftovers if there is time: polish, sounds.

### Done
- **Real path to the college bike park** (content/bug): the paved paths from the end of Hendric Stevinlaan round the bike park are drawn from OSM (ways 1360765716, 1360765715, 1314839838, 1314839805), 2 m wide, with no grass through them. Pupils ride in and out along them instead of over the grass.
- **Eating oliebollen** (gameplay/graphics/sound): after buying a bag you carry it in your left hand and eat all six on the way, one every 4 to 7 s: the right arm brings an oliebol to the mouth (bones aimed in world space), a puff of powdered sugar falls and you hear a soft crunch. Your jacket is dusted with sugar for two minutes (rain washes it off faster) and people you pass say so ("You have got sugar all over you!").
- **Winter coats** (graphics/seasons): in winter 70% of the people wear a coat: the top and sleeves turn the coat colour (black, dark blue, brown, dark red, dark green, grey, beige, blue, red) and a hem hangs to mid-thigh. The lost child names the coat ("a brown coat") instead of the shirt. Rigged people now share one set of vertex buffers (only the colours differ per person), so the extra coat looks cost almost no memory.
- **Families** (gameplay/content): new taxi fare Mr de Boer with Daan and Fenna (by day). The two children wait beside him, bicker and chat from the back seat ("Daan started it!", "Dad, I need the toilet.") and walk home with him. Taxi fares now take any number of children. About one parent cyclist in four carries a toddler in a child seat on the carrier (home in bed at night).
- **Phone performance** (performance): measured draw calls on the Low setting near the De Deel car park: about 1110, of which about 420 were cars (shadow pass included). Parked and far cars now switch to their cheap far look at 44 m on Low and 70 m on Medium (88 m on High as before), and far cars also drop the lamp lenses and trim (the night glows stay). Result: about 950 draw calls there on Low. Winter wear adds about 50 to 70 draw calls in a crowd, which is fine.
- **Frozen canals** (graphics/gameplay/sound): in winter the canals freeze: pale grey-blue ice with cloudy patches and skate scratches (no ripples, weaker reflection), ducks stand on the ice, and by day up to seven skaters (two children) glide up and down the canals near you, leaning forward with long strides, some with their arms back; you hear the blades scrape. You can walk down the bank and slide over the ice (speed builds slowly and you keep gliding when you let go). New achievement "Natural ice" (28 in total).
- **Koek en zopie** (content): a little stall on the ice of the canal closest to the Poldertoren, with a striped roof, a pan of hot chocolate and a stall keeper. Buy hot chocolate with **E** for €2.

### Report for Ron
Tonight's run (01:17) added 7 improvements, each tested in headless Chromium (no console errors; walking, driving, the taxi ride with Mr de Boer, eating, sliding on the ice and the stall scripted and checked with screenshots) and pushed straight to `main`:
- The pupils ride to the college bike park along the real paved paths from OpenStreetMap.
- You eat your oliebollen on the way, and the powdered sugar on your jacket gets comments.
- People wear winter coats in winter.
- A dad with two bickering children as a taxi fare, and toddlers in child seats on parents' bikes.
- Phones: far and parked cars are cheaper to draw (about 15% fewer draw calls near the big car park).
- In winter the canals freeze: skaters, ducks on the ice, you can slide on it yourself, and there is a koek-en-zopie stall selling hot chocolate.

Screenshots in the project files under `runs/`: `2026-11-24-frozen-canal-skater.png` (a woman in a brown coat and red scarf skating on the frozen canal, more skaters in the distance), `2026-11-24-koek-en-zopie.png` (the player at the KOEK & ZOPIE stall on the ice), `2026-11-24-on-the-ice.png`, `2026-11-24-winter-coats.png`, `2026-11-24-eating-oliebollen.png`, `2026-11-24-taxi-dad-two-kids.png`, `2026-11-24-child-seat.png`, `2026-11-24-college-paths.png`.

Problems: none open. The canals freeze every day the season is winter (set by the calendar or the season button), not only on cold days. When eating, the hand is open (no finger pose). The player slides on the ice but there is no falling over yet. Cars cannot go onto the ice (they never could go into the canals).

### Next ideas (for the next run)
1. Frost days: freeze the canals only after a few cold days in winter (a frost counter), with a "the ice is open!" message, and thin ice near bridges.
2. Skating yourself: rent skates at the koek-en-zopie stall for a faster glide with a skating animation, and a small skating race along the canal (a new job).
3. Falling over on the ice when you turn too sharply at speed (a short stumble animation).
4. Curl the fingers round the oliebol and the hot chocolate cup when eating and drinking.
5. More performance on phones: merge the loose static meshes near De Deel (about 250 single meshes in view).

## 2026-11-23 (run 11:52)

### Plan (prioritized)
No open bugs were left by the 06:45 run. Its "next ideas" list is the base for this run:

1. **Slimmer build for women** (graphics/people): narrower shoulders by pulling the shoulder bones in after each animation update.
2. **Winter and autumn clothes** (graphics/seasons): scarves and woolly hats on people in winter, scarves on some in autumn, switched with the season.
3. **Bike rack at the Zuyderzee College** (gameplay/content): pupils park their bike in a rack by the drop-off kerb and walk in, instead of vanishing.
4. **Kermis snack stand queue** (content/sound): a few people queue at the snack stand while the kermis is open, with a frying sound when you are close.
5. **Parent and child taxi ride** (gameplay): a fare with two passengers, the child in the back.
6. Leftovers: polish, phone checks.

### Done
- **Slimmer build for women** (graphics/people): the walk clips animate the shoulder bones' positions, so after each animation update the shoulders of women and girls are pulled in towards the spine (16% narrower, chest and arms follow the skin). Also applied to seated poses.
- **Winter and autumn clothes** (graphics/seasons): every pedestrian gets a knitted scarf (neck bone) and about half a woolly hat with a bobble (head bone, not over a bun) in one matching colour. Winter: 80% wear them; autumn: 30% wear only the scarf; spring and summer: none. Switches with the season button straight away. Meshes are hidden when not worn, so no extra cost in summer.
- **Oliebollen queue** (content/sound): up to four fair-goers line up at the oliebollen stall while the kermis is open; every 6 to 11 s the one at the front orders (speech bubble when you are within 15 m: "A bag of oliebollen, please!"), walks off and someone else joins the back. Frying crackles come from the stall within 26 m.
- **Buy oliebollen yourself** (gameplay): at the counter press E to buy a bag for €3; jumping the queue earns a remark from the front of the line. New achievement "Powdered sugar" (27 in total).
- **Zuyderzee College bike park** (content/gameplay): at the real spot from OSM (way 1314839846, amenity=bicycle_parking, the courtyard south of the school building, x 378 to 417, z -644 to -658): grey paved floor, two rows of steel hoops (76 places, one draw call), a walkway to the door (OSM entrance node 12169881309) and 20 bikes on school days from 07:40 to 16:40 (one merged mesh). On the morning school run 80% of the pupils now ride via the end of Hendric Stevinlaan into the bike park, lock their bike in a free spot, and walk to the door. After school they walk back out, wheel the bike out and ride home. No grass blades poke through the paving.
- **Taxi: mum and child** (gameplay): new fare Mrs Jansen with her daughter Noor (only between 07:30 and 20:30). Noor waits beside her mum at the kerb, gets in the back, chats from the back seat ("Are we there yet?", "Can you honk? Please please please?") and walks home with her mum after the ride.

### Report for Ron
This lunchtime run (11:52) added 6 improvements, each tested in headless Chromium (no console errors; the people line-up, kermis queue, buying oliebollen, the bike park morning and afternoon and the mum-and-child taxi ride scripted and checked with screenshots) and pushed straight to `main`:
- Women have a slimmer build (narrower shoulders).
- In winter people wear scarves and woolly hats; in autumn some wear a scarf.
- At the kermis people queue for oliebollen, you hear the fat crackle, and you can buy a bag yourself (new achievement).
- The Zuyderzee College has its bike park at the real OpenStreetMap spot: pupils park their bike there in the morning, walk in, and ride home after school.
- New taxi passengers: a mum with her daughter, who talks from the back seat.

Screenshots in the project files under `runs/`: `2026-11-23c-winter-scarves.png` (a row of people on De Deel in winter with scarves and woolly hats), `2026-11-23c-oliebollen-queue.png` (three people queueing at the oliebollen stall, "A bag of oliebollen, please!"), `2026-11-23c-college-bike-park.png` (the bike park behind the college with rows of hoops and parked bikes), `2026-11-23c-taxi-mum-and-child.png` (Mrs Jansen and Noor waiting in the taxi marker on De Deel).

Problems: none open. The scarves and hats are simple shapes (a ring and a cap), and the narrower shoulders are only a small change; women still share the man's body. The bike park is reached across the school grounds without a real path in the game data, so pupils ride over the grass for the last 20 m.

### Next ideas (for the next run)
1. A path from Hendric Stevinlaan to the bike park (OSM footway near x 432) drawn as paving, so pupils do not ride over grass.
2. Winter coats: darker, longer tops in winter (would need the shirt colour kept for the lost-child hints).
3. Eating the oliebollen: a short animation or powdered sugar on the player's shirt for a minute.
4. More families: a dad with two children on the taxi, children on the back seat of parents' bikes (bakfiets).
5. Check performance on a phone with the extra scarves and hats in winter (draw calls near crowds).

## 2026-11-23 (run 06:45)

### Plan (prioritized)
No open bugs were left by the 01:17 run. Its "next ideas" list is the base for this morning:

1. **Women and girls** (graphics/people variety): the CC0 asset library has no Quaternius woman or child body (only chunky Kenney mini figures, which would clash with the style), so build a female look on the existing rig: long hair, ponytail or bob attached to the head bone, skirts and dresses on the hips, slightly slimmer build. Children get a larger head so they read as children, not small adults. Mums walk with children too; the lost child mission then talks about "mum" or "dad".
2. **Lost child hint** (gameplay): after a minute without finding the parent, their dot appears on the minimap.
3. **School run** (gameplay/content): on school-day mornings, pupils with backpacks cycle towards the Zuyderzee College (OSM way 1539834599).
4. **Kermis night life** (content): fair-goers walk home from the kermis after the rides close at 23:30.
5. **Phone portrait check** (mobile/bugs): speech bubble and chat on a portrait phone.
6. Leftovers if there is time: ambient sounds, small polish.

### Done
- **Women and girls** (graphics/people variety): the CC0 library in the npm package has no realistic woman or child body (only chunky Kenney mini figures), so the female look is built on the existing Quaternius rig. About 46% of the people are now women or girls, with one of four hair styles (long, ponytail, bob, bun) on the head bone and, for half of them, a skirt or a dress (skirt in the shirt colour) on the hips bone. Children have a 1.22x head so they read as children. Taxi passengers match their names (Mrs Bakker has a grey bun and a skirt, Sanne and Lotte have ponytails, the men are men), and a street hailer is always given a passenger of the same sex. Extra cost: one or two draw calls per woman, only while she is near the camera.
- **Lost child can look for mum** (gameplay): the child now asks for mum or dad depending on the parent ("Take Sem to mum: a woman in a yellow shirt near Lange Nering"), dresses are called dresses.
- **Lost child hint** (gameplay): after a minute the child remembers ("Wait, I think I saw my dad over there!") and the parent shows as a pink dot on the minimap.
- **School run** (gameplay/content): on school days from 07:18 to 08:33, 7 pupils with backpacks (teen size, coloured backpacks on the torso bone) start out of sight near the player and cycle to the Zuyderzee College drop-off kerb (OSM way 1539834599) along the GPS road graph, keeping right. After school (14:54 to 16:24) they ride home, away from the college.
- **Kermis closing time** (content): at 23:30 the 12 fair visitors no longer vanish; they walk to the nearer end of the stall lane and then home into town, and some say something as you pass ("I still taste the oliebollen.", "Same time next year!").
- **Portrait phones** (mobile/bug): on a 390 px wide phone the place name ran under the coins/cash/time panel. Now the coins label is shortened to "Coins", the labels are tighter and long street names end in "..."; messages sit below the minimap instead of over it. Checked at 390x844 and 360x740; desktop and sideways phones are unchanged.
- **Sounds** (sound): gulls call over the open polder by day, and the Zuyderzee College bell rings at 08:30 and 15:00 on school days when you are within about 350 m.

### Report for Ron
This morning's run (06:45) added 7 improvements, each tested in headless Chromium (no console errors; walking and driving scripted, the lost child, school run, kermis closing and the bell checked with scripts and screenshots) and pushed straight to `main`:
- Women and girls in town: long hair, ponytails, bobs and buns, skirts and dresses. Children have bigger heads so they look like children.
- The lost child can be looking for mum, and after a minute the parent shows as a pink dot on the minimap.
- School run: on school-day mornings pupils with backpacks cycle to the Zuyderzee College, and they ride home after school.
- When the kermis closes at 23:30 the visitors walk home through town instead of disappearing.
- Portrait phone fix: the place name no longer overlaps the coins and cash panel.
- Gulls over the polder, and the school bell at the college.

Screenshots in the project files under `runs/`: `2026-11-23b-women-girls.png` (seven people on the Kettingplein: a woman in a blue dress with a blonde ponytail, a woman with long hair, a bob, a girl in a yellow dress, a boy and two men), `2026-11-23b-school-run.png` (a pupil with a yellow backpack cycling on Koningin Julianastraat at 07:36), `2026-11-23b-kermis-home.png` (fair-goers walking home at night, "I still taste the oliebollen."), `2026-11-23b-phone-portrait.png`.

Problems: none open. The women share the man's body (only hair and skirt differ, no different build), and skirts are rigid, so legs can poke through them a little when walking fast. Headless play runs at a few frames per second, so the school run and kermis were sped up by script.

### Next ideas (for the next run)
1. A slimmer build for women (narrower shoulders by scaling the shoulder bones) and a few more clothes: trousers in other colours, coats in autumn and winter.
2. Bike parking at the Zuyderzee College: pupils lock their bike in a rack and walk in, instead of vanishing after 25 s.
3. A taxi ride for a parent with a child (two passengers, the child in the back).
4. More kermis night life: a queue at the snack stand with the sound of frying, and a short announcer line at the rides.
5. Seasonal clothes: scarves and coats when the season is winter.

## 2026-11-23 (run 01:17)

### Plan (prioritized)
No open bugs were left by the 06:45 run. Its "next ideas" list is the base for tonight:

1. **Tower facts in the lift** (content): short checked facts appear on the lift display on the way up (water tank, the 48 bells, gallery height).
2. **New taxi passengers** (gameplay/content): a student to the Zuyderzee College (position from OSM) and a late-night ride home from the kermis on De Deel.
3. **People variety** (graphics): children and elderly people among the pedestrians (smaller bodies, slower walk, grey hair), different walking speeds.
4. **Honk reactions** (gameplay/sound): people you honk at say something or shake their head, cyclists ring their bell back.
5. **Phone check** (mobile/bugs): the pause menu with the taxi stats on a small sideways phone.
6. Leftovers if there is time: more ambient sounds, small polish.

### Done
- **Tower facts in the lift** (content): the lift display shows four facts on the way up (finished 1959 as the water tower of the Noordoostpolder, 48-bell carillon, 65.3 m to the top, gallery at 43.4 m), all from the plaque facts checked in the last run. The ride up now takes 11 s instead of 5 s so the facts can be read; the ride down stays 5 s.
- **New taxi passengers** (gameplay/content): Lotte, a pupil who missed her bus, on school-day mornings (07:00 to 11:00) to the Zuyderzee College. Drop-off is the kerb of Professor ter Veenstraat along the north edge of the school grounds, OSM way 1539834599 (amenity=school, name=Zuyderzee College, polygon x 330 to 427, z -540 to -661 in game metres). Kevin, a kermis-goer with a giant banana, is picked up beside the fair on De Deel late at night (21:00 to 02:00) on kermis weekends. Passengers are now chosen by time of day (pickFare).
- **People variety** (graphics): about 1 in 5 pedestrians is elderly (grey or white hair, muted clothes, slower walk, slight stoop via the Abdomen bone), and 7 adults walk with a child at their side (scaled 0.55 to 0.7, brightly dressed, stride length scaled so feet do not slide). Children are home between 21:00 and 07:00.
- **Honk reactions** (gameplay/sound): the nearest pedestrian within 12 m calls something back in a speech bubble ("Hey!", "Watch it!", "Hello to you too!"), a cyclist nearby rings their bell back, taxi passengers comment on honking. New achievement "Polder trumpet" (honk five times in a row in town).
- **Pause menu on sideways phones** (mobile/bug): on a 667x375 phone the "New game" and "Achievements" buttons were cut off below the screen. The pause card is now wider and flatter on short screens (five stat columns, smaller buttons) and everything fits.
- **Lost child** (gameplay): by day, while you walk around without a job, a child who lost their dad sometimes stands crying nearby ("Daddy?"). Walk up to them: they name the colour of dad's shirt and the street, then follow you. Bring them to dad (he waits where they lost him) for €25, 30 XP and the achievement "Found you!" (26 achievements in total). Driving off or taking a job ends it; the child runs back to dad.

### Report for Ron
Tonight's run (01:17) added 7 improvements, each tested in headless Chromium (no console errors; walking, driving, the new taxi rides, honking and the lost-child mission scripted; screenshots checked) and pushed straight to `main`:
- Two new taxi passengers: a pupil late for the Zuyderzee College (real OSM spot) on school mornings, and a kermis-goer going home late at night.
- The Poldertoren lift shows tower facts on the way up.
- More varied people: elderly people with grey hair who walk slower, and children walking beside their parents (home in bed at night).
- Honking gets a reaction: speech bubbles, cyclists ring back, passengers comment.
- New mini-mission: help a lost child find their dad.
- Pause menu fixed on small sideways phones (buttons were cut off).

Screenshots in the project files under `runs/`: `2026-11-23-lost-child.png` (a dad in a blue shirt waving "There you are!" on Lange Nering), `2026-11-23-people-variety.png` (a parent with a child and a grey-haired man on Lange Nering), `2026-11-23-honk-bubble.png` ("Hey!" bubble), `2026-11-23-lift-facts.png`, `2026-11-23-phone-pause.png`.

Problems: none open. All people still use the same CC0 male body, so "dad" is always a man and children are scaled-down adults; a real child or female model would look better. Headless play still runs at a few frames per second, so the missions were driven by script.

### Next ideas (for the next run)
1. A second CC0 body (woman, child) for people variety, so children and mums look right (check the npm asset library for Quaternius characters).
2. A minimap hint for the lost child mission after a minute (dad's dot appears) if the player cannot find him.
3. School run: on school-day mornings, children with backpacks cycling towards the real school spots in OSM.
4. More kermis night life: queue at the snack stand, people walking home from the fair after 23:30.
5. Check the speech bubble and chat on a phone in portrait mode.

## 2026-11-22 (run 06:45)

### Plan (prioritized)
The 01:17 run left one known bug: rigged people who hail a taxi stand still in their beam (only the simple fallback people wave). That comes first, then the leftover taxi and delivery ideas.

1. **Wave for rigged people** (bug/graphics): street hailers raise and wave an arm on the real characters too; passengers wave goodbye at the drop-off.
2. **Special taxi rides** (gameplay/content): a rush ride to the medical centre (real OSM position) with a tight time limit, and a tourist who wants to pass the Poldertoren first (an extra GPS step).
3. **Parcel recipients** (gameplay/content): someone comes out to the kerb when you arrive with a parcel, takes it, and you hear a signature/scanner beep.
4. **Taxi stats** (gameplay): rides, average stars, best tip and money earned in the pause menu, saved.
5. **Poldertoren plaque** (content): a plaque by the tower door with facts checked in OSM.
6. Leftovers if there is time: people variety, more passenger lines, phone check of new UI.

### Done
- **Waving for rigged people** (bug/graphics): the real characters can now wave (the right arm bones are aimed in world space, so it works whatever the rig's bone axes are). Street hailers wave in their yellow beam.
- **Passengers walk home, parcel recipients come out** (gameplay/content): at the drop-off the passenger gets out, waves goodbye and walks to their front door. With a parcel the doorbell rings, a resident walks to you, the scanner beeps, they say a line ("Is it the new coffee machine? Brilliant.") and go back inside.
- **Special taxi rides** (gameplay/content): Mr Smit cut his thumb cutting onions and needs a rush ride to the Dokter J.H. Jansencentrum, Urkerweg 1 (OSM node 2719213291, amenity=clinic): tight time limit, fare x1.5, he likes it fast. Mr Visser the tourist now asks to pass the Poldertoren first (extra GPS step on De Deel; a happy line and half a star when you do).
- **Taxi stats** (gameplay): rides, average rating, best fare and taxi takings in the pause menu, saved.
- **Poldertoren plaque** (content): bronze plaque beside the tower door. Facts checked against OSM way 266435887 and its Wikipedia article: finished 1959, 65.3 m, water tower, 48-bell carillon, visitor gallery at 43.4 m (the OSM height tag is the gallery height). Walk up to it to read it.
- **Passers-by wave hello** (gameplay/graphics): when you walk right past a pedestrian, now and then they turn and wave.

### Report for Ron
This morning's run (06:45) added 6 improvements, each tested in headless Chromium (no console errors; walking, driving and full taxi and parcel jobs scripted; screenshots checked) and pushed straight to `main`:
- People wave properly now: taxi hailers raise and wave an arm, and passers-by sometimes wave hello.
- Taxi passengers wave goodbye and walk to their door; parcel customers come out after the doorbell.
- Two special taxi rides: a rush to the medical centre on the Urkerweg (real OSM spot) and a tourist who wants to see the Poldertoren first.
- Taxi stats in the pause menu.
- A bronze plaque by the tower door with checked facts (1959, 65.3 m, 48 bells).

Screenshots in the project files under `runs/`: `2026-11-22b-wave-hello.png` (a man in a blue shirt waving at the player on the kermis lot by De Deel), `2026-11-22b-hail-wave.png` (taxi hailer waving in a yellow beam on Smeden), `2026-11-22b-taxi-stats.png` (pause menu with taxi rides, rating, best fare), `2026-11-22b-plaque.png`.

Problems: the README said the tower is from 1959 while OSM says start_date 1957; Wikipedia gives 1959 as finished, so the plaque says 1959. Headless play runs at about 1 frame per second, so animations were checked with state values plus a few screenshots.

### Next ideas (for the next run)
1. People variety (graphics plan): more CC0 bodies, children and elderly.
2. More passengers and special rides (late-night ride home from the kermis, a student to the Zuyderzee College at its OSM spot).
3. A honk reaction: pedestrians look round or step back when you honk near them.
4. Phone check of the larger pause stats grid on a small sideways phone.
5. Tower facts in the lift ride (gallery at 43.4 m, the 48 bells) shown on the way up.

## 2026-11-22 (run 01:17)

### Plan (prioritized)
No open bugs were logged after the graphics run. A quick play at the start view (walk, try a car) gave no console errors. This run goes back to gameplay and content after two days of graphics work, using the leftover ideas from earlier runs.

1. **Taxi passengers with a story** (gameplay/content): each passenger has a name and a few original lines of chat shown as subtitles during the ride; the fare follows the real driving distance of the GPS route; crashes and wild driving cost tip, and the drop-off shows a star rating.
2. **Show the delivery house** (gameplay/graphics): a floating house-number plate and a glowing door light at the real address you deliver to, so you know which house it is.
3. **Cheaper far people** (performance): people far away are hidden or animated less often, to save draw calls and CPU in busy views.
4. **Phone check** (mobile/bugs): look at the pause menu tow button, mission box and the new subtitles on a sideways phone.
5. **Small sound pass** (sound): a door/seat sound when a passenger gets in or out, an indicator tick when steering at low speed.
6. **Next leftovers** if there is time: more polder content, Poldertoren plaque, people variety.

### Done
- **Taxi passengers with a story** (gameplay/content): six original passengers (Mrs Bakker, Daan the late student, Sanne the nurse, Mr De Vries the farmer, Yusuf with eggs in his shopping, Mr Visser the tourist). They greet you, chat as subtitles during the ride, react to crashes and to speeding over 72 km/h (Daan likes it fast and complains when you crawl). The ride ends with a 1 to 5 star rating that scales the fare (70% to 110%). Fare and time limit follow the real GPS driving route. New achievement "Five stars" (24 in total).
- **House-number plate** (gameplay/graphics): parcel, taxi and pizza jobs show a floating plate with the number and street above the real house you deliver to, on top of its roof, readable from a distance and seen through other buildings.
- **Far people hidden** (performance): pedestrians further than 120/160/210 m (Low/Medium/High) from the camera are hidden and not animated; in the busy test views 19 to 41 of 72 people are drawn instead of 62.
- **Phone layout** (mobile/bug): on a sideways phone the job box ran under the coins/cash panel; it now sits right of the place name. The new chat subtitles and the tow button in the pause menu were checked on a sideways phone.
- **Sounds** (sound): car doors, a starter motor when you get in (a soft chime for the electric Volt E), the delivery van beeps when reversing, a little chatter blip when a passenger talks.
- **Street hails** (gameplay): from level 2, while you drive around without a job, someone at the kerb ahead now and then waves for a taxi (yellow beam, yellow dot on the minimap). Stop next to them and the taxi ride starts right there.

### Report for Ron
Tonight's run (01:17) added 6 improvements, each tested in headless Chromium (no console errors, walking/driving and the job checked with a script, screenshots looked right) and pushed straight to `main`; GitHub Pages deploys succeeded.
- Taxi passengers are now characters who talk during the ride, react to crashes and speeding, and give you 1 to 5 stars that change the fare.
- A house-number plate floats over the house you deliver to.
- People sometimes wave for a taxi at the kerb while you drive: stop next to them to start a ride.
- Far-away pedestrians are hidden, which saves draw calls in busy views.
- Sideways phones: the job box no longer covers the coins and cash.
- New sounds: car doors, starter motor, van reversing beep.

Screenshots in the project files under `runs/`: `2026-11-22-house-plate.png` (plate "21-01 De Deel" above the shops on De Deel), `2026-11-22-taxi-hail.png` (a person in a yellow beam on Smeden waving for a taxi), `2026-11-22-phone-taxi-chat.png` (sideways phone with Yusuf talking about the Thursday market).

Problems: the waving arm only shows on the simple fallback people; the rigged characters stand still in their beam (needs a wave animation on the rig). Draw-call numbers in the headless tests are noisy while tiles stream in, so the people saving is counted in people drawn, not exact calls. Every play test still runs at 3 to 5 fps in the cloud, so long drives are simulated with teleports.

### Next ideas (for the next run)
1. A wave pose for rigged people (hailing passengers, people greeting you).
2. More passenger lines and a few special rides (rush to the Medisch Centrum, a tourist who wants to see the Poldertoren first: a detour step).
3. Parcel recipients: someone opens the door when you arrive; signature sound.
4. Daily taxi stats in the pause menu (rides, average stars, best tip).
5. People variety (graphics plan): more CC0 bodies, children and elderly.
6. Poldertoren plaque with facts checked from OSM/Wikipedia.

## 2026-11-21 (realistic graphics plan, phases 0 to 10)

Ron approved the whole plan in `docs/GRAPHICS_PLAN.md` ("ok lets go I accept everything"). Each phase was pushed live separately.

### Done
- **Phase 0, measuring stick** (tools): `tools/shots.js` takes screenshots at fixed real spots and records draw calls and triangles per spot, so each phase can be compared before and after.
- **Phase 1, colours** (graphics): flat colours and vertex colours are treated as sRGB, so pale surfaces no longer glow; dark materials (trunks, poles, lions) were re-tuned.
- **Phase 2, engine** (graphics): Three.js r128 → r159, vendored in `assets/lib` (no CDN). It brings built-in colour management; the High post chain does its own ACES tone mapping.
- **Phase 3, streets** (graphics/content, OSM): kerbs along streets with `kerb` data inside built-up areas, pavements raised 12.5 cm, klinker streets from OSM `surface`, shark teeth and zebra crossings at OSM give-way and crossing points, and OSM bollards, bins, street cabinets, lowered kerbs and hedges.
- **Phase 4, heights** (graphics/gameplay): bridges and viaducts get deck heights from OSM bridge/layer tags; for example, the A6 runs 6.5 m up over the Marknesserweg and Zwolse Vaart with ramps at 3.5 %, on piers with guard rails and grass embankments. Cars drive up the ramps. Canals are sunken 1.1 m with sloped grass and mud banks (stencil holes in the ground).
- **Phase 5, buildings** (graphics, 3D BAG): measured eave height, ridge height, roof type and ridge direction from the 3D BAG (TU Delft, CC BY 4.0) for 12,015 of 12,705 buildings, matched by BAG id (`tools/bag3d.py`). Pitched roofs only where the 3D BAG measured them, in their real direction. L-shaped houses get one roof with raised gable walls.
- **Phase 6, grass** (graphics): tufts of grass blades within 13 m (Medium) or 24 m (High), swaying in the wind and fading out at the edge.
- **Phase 7, light and shadow** (graphics): the shadow box is pushed ahead of the camera and snapped to shadow texels (no shimmer), soft contact shadows run along every wall, and rough surfaces lose most of their sun sheen.
- **Phase 8, water and rain** (graphics): canals have a PBR water surface with Fresnel sky reflections, two ripple layers and rain rings. On High the canal mirrors the town (planar reflection). Streets get wet with rain and dry over a few minutes, and puddles in low spots become mirror-like.
- **Phase 9, vehicles** (graphics): car paint has a clear coat, and the lower body is dulled by road dirt (more when wet). Parked bikes and cyclists are now Dutch city bikes (omafiets) with mudguards, chain guard, carrier, lamp and reflector.
- **Phase 10, sky and horizon** (graphics/content): cloud shadows drift east over town with the clouds, on Medium and High. The invented rows of wind turbines are replaced by the one turbine OSM has near the map (node 1617174216, south of town).

### Problems / notes
- **Fixed a long-standing bug:** the first frame could get a negative time step, which put a layer of "snow" on every lawn and roof at startup. That was the real cause of the pale mint lawns, and it also made earlier screenshot comparisons unreliable. Time steps are now never negative.
- High is heavier when a canal is in view (the scene is drawn twice); the reflection only renders when water is ahead, at half resolution, out to 350 m.
- Not done, waiting for Ron's photos: era facade styles from OSM `start_date`, roof tile colours per street, and bus liveries.
- Not done (large): temporal anti-aliasing, a colour grade (LUT) matched to the drone video, and near-camera 3D tree models and impostors.

## 2026-11-21 (whole town)

Ron asked to build all of Emmeloord, not only the centre.

### Done
- **Whole town from OpenStreetMap** (content): the map region grew from 1.8 x 1.5 km to 5.1 x 5.3 km (x -2150..2950, z -2400..2950): all residential neighbourhoods, the Havens te Emmeloord / 1e and 2e Industriehaven, De Munt and De Gilden, the zonnepark. 12,700 buildings (was 4,500), 22,000 road pieces, 13,000 OSM trees, 7,400 street lamps. Converter: `tools/convert.py` with `REGION=-2150,2950,-2400,2950`; it now also writes built-up landuse (minimap), neighbourhood names (OSM place nodes) and named business parks.
- **Real addresses for the whole town** (`tools/gen_addr.py`): 15,000 OSM addresses, every second number in the centre and every third elsewhere (6,177 kept). Taxi rides now often go across town and pay by distance.
- **Neighbourhood names** (gameplay): the location box shows Emmelhage, Revelsant-Zuid, Bos en Gaard, De Munt etc. (nearest OSM place, or inside the named business park polygon).
- **Performance** (phones): ground layers and polder fields are split into 500-600 m tiles, buildings keep their 300 m tiles; every tile is distance-culled (`DCULL`/`VIEWD`, per quality level and the fog). Buildings beyond 260/400/560 m (Low/Medium/High) switch to a one-colour version without textures (one draw call per tile). Lamps are in 500 m chunks. The camera far plane follows the fog (sky dome and stars scale with it) so cars, people and signs across town aren't drawn. Minimap is drawn in 512 m tiles on demand (a single 7 km canvas is too big for phones). Start view on Medium: 463 draw calls / 0.90 M triangles (was 440 / 0.92 M).
- **Traffic follows the player** (gameplay): AI cars and cyclists that end up more than 700/500 m away come back on a street near the player, out of sight; route choices stay around the player instead of the tower.
- Wind turbines moved to rows just outside the new town edge; clouds drift around the camera.

### Problems / notes
- JS heap after loading is about 290 MB (was 200 MB); load takes about 10% longer.
- The A6 and its interchanges are flat (no bridges/height), like all roads; the motorway ends at the region edge.

## 2026-11-21 (run 06:45)

### Plan (prioritized)
No open bugs were logged; two known problems from the 01:17 run come first. Playing at the start view confirms the tower plinth still glows white in the sun.

1. **Camera collision** (bug/controls): the camera no longer ends up inside buildings or tree crowns; it pulls in in front of walls and dips under crowns.
2. **Pale concrete too bright** (graphics/bug): tone down the tower plinth, lions and other pale concrete per material (less sky light, darker base colour), not the global lighting.
3. **Real addresses** (content): taxi, courier and pizza jobs name real street + house numbers from OSM (addr:street/addr:housenumber) of the building you drive to.
4. **Visible car damage + tow** (gameplay/graphics): a dented bonnet and a broken headlight on badly damaged cars; when wrecked far from the garage, a tow option brings the car there for a fee.
5. **Ambient sound** (sound): birds in the morning, soft wind, crickets at summer nights, all procedural Web Audio, quiet in the car.
6. **Performance** (phones): check draw calls in the busiest views and merge cheap static parts.

### Done
- **Camera collision** (bug/controls): the camera walks out from the player to its wanted spot and stops in front of the first wall (building footprints now carry their roof height). Under round street trees it dips below the crown instead of ending up in the leaves. Pulls in fast, eases back out.
- **Poldertoren concrete** (graphics/bug): the plinth, ledges and door surround were flat colours treated as linear light and glowed white in the sun; now sRGB-converted beige-grey concrete with less sky reflection.
- **Real addresses** (content): 6,000 OSM addresses (addr:street + addr:housenumber) within 950 m were fetched; every other house number per street is embedded (3,073, 39 KB). Parcel, taxi and pizza jobs pick a real address and stop at the kerb of its street in front of the house ("Deliver the parcel to Steenstraat 5").
- **Visible car damage + tow truck** (gameplay/graphics): from 40% the bonnet sags and one flank gets a dent, from 75% the front is crumpled, the paint dull and the headlights broken (per-car copy of the body, restored on repair or paint). A wrecked car more than 120 m from the garage can be towed there with G or the pause menu for €60.
- **GPS line on the minimap** (gameplay): replaced plan item 5 because birds, crickets, wind and rain sounds already exist. During a job, a Dijkstra route over the OSM road graph to the next target is drawn in the job colour; one-way streets count when driving; it re-routes when you leave the line.
- **Cheaper far cars** (performance): measured the busiest view (Kettingplein looking west, Medium): ~1,400 draw calls, of which each car costs ~13. Cars over ~85 m away now swap their 4 spinning wheels, trim and plates for one merged wheel mesh: 1,411 → 1,170 calls in that view (-17%).
- **Camera vs tree trunks** (bug/controls): the camera also stops for street tree trunks, staying at least 1.7 m behind the hero (a trunk right behind you is then culled from inside instead of filling the screen). The hero is hidden only when a wall pushes the camera into their head.

### Report for Ron
Today's run (06:45) added 7 improvements, each tested in headless Chromium (no console errors, walking/driving checked, screenshots looked right) and pushed straight to `main` (GitHub Pages deploys succeed):
- The camera no longer looks through buildings or sits inside tree crowns and trunks.
- The white glowing Poldertoren plinth is now matt beige-grey concrete.
- Parcel, taxi and pizza jobs go to real house numbers from OpenStreetMap ("Deliver the parcel to Steenstraat 5").
- A GPS line on the minimap shows the way during a job, following one-way streets in a car.
- Damaged cars look damaged: dented, then crumpled bonnet, dull paint, broken headlights.
- A wrecked car can be towed to the garage with G (or the pause menu on a phone) for €60.
- Far-away cars are cheaper to draw (about 17% fewer draw calls in the busiest view).

Screenshots in the project files under `runs/`: `2026-11-21b-car-damage.png` (yellow car with a sagging, crumpled front, dark headlights and smoke on De Deel), `2026-11-21b-towed-to-garage.png` (the wrecked car parked on the garage forecourt beside the orange marker), `2026-11-21b-gps-minimap.png`, `2026-11-21b-tower-concrete.png`.

Problems: plan item 5 (ambient sound) was skipped because birds, crickets, wind and rain sounds already exist; the GPS line replaced it. Flat-coloured materials across the game are still treated as linear colours, which is why pale surfaces (garage forecourt, lamp posts) look washed out; only the tower was fixed. Address sample: every other house number per street is in the game, so some numbers never come up.

### Next ideas (for the next run)
1. Fix the colour handling of flat-coloured materials globally (`lm()` and vertex colours to sRGB), checked against Ron's photos, carefully because it changes the whole look.
2. Show the house you deliver to: a small glowing door marker or house number sign at the address.
3. More performance: people (rigged characters cost one draw call each, ~65 in busy views) could use a cheaper far version; merge building chunks per area.
4. Taxi passengers with short lines of chat, and fares that depend on the real driving distance of the GPS route.
5. More tower content: opening hours, a plaque about the 1957 water tower.
6. Phone check of the new tow button in the pause menu.

## 2026-11-21 (run 01:17)

### Plan (prioritized)
No open bugs were logged. Left over from yesterday's plan: achievements and a Poldertoren lift ride. Playing found the concrete lions next to the tower look like glowing white blocks.

1. **Achievements** (gameplay): about 20 goals (first job, every vehicle, all polder coins, top of the tower, a kermis ride, escape the police, ...), a toast with a sound when one unlocks, a list in the pause menu, saved.
2. **Poldertoren lift ride** (content): walk to the door, press E, ride the lift up to the viewing platform at 43.4 m and look out over Emmeloord and the polder.
3. **Carillon** (sound): the tower's 48 bells play a short original tune every game hour, louder near the tower.
4. **Concrete lions** (graphics/bug): rounder, sculpted lions in matt concrete instead of bright white boxes.
5. **Car damage** (gameplay/graphics): crashes dent the car's health, smoke from the bonnet when it is badly hurt, slower when wrecked, repair at the garage for cash.
6. **Performance** (phones): look at draw calls and merge static street furniture where it is cheap to do.

### Done
- **Achievements** (gameplay): 23 goals (first coin, all coins, first job, 10 jobs, every kind of job, beat the rival, tower lift, Ferris wheel, bike + scooter + tractor, borrow a car, 150 km/h, flitspaal, lose the police, pulled over, buy a car, new paint, level 5, out at 3 AM, caught in a shower, the Thursday market, 25 km driven, the carillon up close, a repair). Gold toast with a chime; list in the pause menu (Achievements button); saved; the start screen shows the count.
- **Poldertoren lift** (content): at the tower door facing De Deel press E. The screen goes dark with a metre counter while the lift goes up, then you stand on the visitor gallery at 43.4 m. Walk around the octagonal gallery (A/D or joystick), drag to look; E takes the lift down and you come out at the door.
- **Carillon** (sound): from 08:00 to 22:00 the bells play a short original tune on every full game hour and then strike the hour (bell partials: hum, prime, minor third, fifth, nominal). Heard up to about 700 m, softer inside a car.
- **De Leeuwen** (graphics/bug): the four concrete lions by the tower (OSM tourism=artwork, replicas by Marieke van Diemen, positions unchanged) were bright white boxes; now rounded lying lions with mane, paws and tail on low plinths, in darker matt concrete with less sky reflection.
- **Car damage** (gameplay/graphics): hard hits on walls, trees and other cars add damage (bar under the speedometer). From 50% smoke rises from the bonnet, from 75% it is dark and the car is slower, at 100% it is wrecked (45% power). Repair at the garage for about €1.20 per percent. Your own car's damage is saved.
- **Performance** (phones): the ~45 parked bikes are merged into one mesh: draw calls at the start view (Medium) 973 → 906. The rest is mostly large world chunks; further gains need building chunks merged per area.
- **Phone layout** (mobile/bug): on a sideways phone the pause card was taller than the screen; it now scrolls, so the achievements list is reachable. The speedometer overlapped the pause button; on short screens it now sits next to it.

### Report for Ron
Today's run (01:17) added 7 improvements, each tested in headless Chromium (no console errors, walking/driving checked, screenshots looked right) and pushed straight to `main`:
- 23 achievements with a gold pop-up and a list in the pause menu.
- Take the lift up the Poldertoren (E at the door facing De Deel) and walk around the gallery at 43.4 m.
- The tower carillon plays a short tune and strikes the hour on every full hour, 08:00-22:00.
- The four concrete lions (De Leeuwen) by the tower now look like lions instead of white blocks.
- Car damage: smoke from the bonnet, slower when wrecked, repair at the garage.
- Fewer draw calls (parked bikes merged) and two phone layout fixes.

Screenshots: `runs/2026-11-21-tower-gallery.png` (view from the gallery over De Deel with the kermis, the bus station and the polder wind turbines), `2026-11-21-achievement.png`, `2026-11-21-car-smoke.png` in the project files.

Problems: light concrete (tower plinth, lions) still looks very bright in sunshine; the sky lighting is strong on pale materials. Not changed globally because it affects the whole look. The camera can end up inside tree crowns when driving under street trees.

### Next ideas (for the next run)
1. Camera collision with tree crowns and buildings (pull the camera in).
2. Tone down the overall brightness of pale concrete/white surfaces (sky light strength), checked against Ron's photos.
3. Real house numbers from OSM (addr:housenumber) for taxi and pizza addresses.
4. Merge static world chunks per area for phones; check draw calls in the busiest views.
5. Visible dents or a crumpled bonnet on damaged cars; tow truck if wrecked far from the garage.
6. More tower content: the turning figures explained when you look at them, opening hours.

## 2026-11-20 (real map + Poldertoren)

Ron asked for the roads and squares to match the real town and for a more accurate Poldertoren.

### Done
- **Real street map** (content): roads, cycle paths, footpaths, De Deel and other squares, parking lots, canals, parks, building footprints, shops, trees and lamps now come from OpenStreetMap (about 1.8 x 1.5 km around the tower), stored compactly in the page (`EMM_DATA` / `EMM_BIN`). Google Street View was not reachable from the build environment, so OSM is the source.
- **Traffic and people on the real network** (gameplay): AI cars and cyclists follow the real road graph (right-hand lanes, pick turns by road size); parked cars stand in real parking bays; pedestrians walk on the squares and the Nering.
- **Jobs on real streets** (gameplay): parcels are picked up at real shops and delivered to named streets; the taxi uses real addresses; the ring road time trial became the Centrum time trial (19 gates).
- **Poldertoren** (graphics): octagon taken from the OSM footprint, finer brick, white concrete corner ribs and bands, window slits, the glass figure case with rotating figures facing De Deel, clocks on four faces, platform at about 43 m, open bell chamber with 48 bells, roof, lantern, spire and weather vane at about 65-70 m.
- Building collisions use the real footprints; canals push you out (except on bridges).

### Problems / notes
- The scene is heavier (about 600k triangles). Software rendering in the test browser runs slower than before; real GPUs should be fine, and adaptive quality still applies.
- Building heights, colours and facade details are approximated (OSM has few heights here).

### Ideas for next run
- Building heights from AHN (Dutch elevation data) or BAG.
- Real house numbers for taxi addresses.

## 2026-11-20 (run 1)

### Plan (prioritized)
No IMPROVEMENTS.md existed yet and no known bugs were logged, so this run starts with the biggest gaps found while playing:

1. **Mobile / touch controls** (mobile): the start screen says "needs a keyboard". Add an on-screen joystick, look-drag, and buttons (car, jump/brake, horn) so it plays on phones.
2. **Day/night cycle** (graphics): game clock with sunrise/sunset sky colours, sun moving, street lamps, lit windows, car headlights at night.
3. **Missions** (gameplay): pickup/delivery jobs from shops on the Nering and a ring-road time trial, with a reward counter.
4. **Better sound** (sound): richer procedural engine (two detuned oscillators + noise), tyre squeal when sliding/handbraking, ambient wind and birds by day.
5. **Save progress** (content): remember collected coins and mission records in localStorage.
6. **Pause menu** (controls): Esc/P pauses, shows controls, resume.
7. **Traffic on the radial roads** and simple pedestrians crossing at De Deel (gameplay).
8. **Performance**: adaptive pixel ratio when frame rate is low; lighter shadows on phones.

### Done
- **Touch controls** (mobile): floating left-thumb joystick (analog walk speed, sprint at full push; throttle/brake/steer in a car), right-thumb look, CAR / JUMP-BRAKE / HORN buttons, tappable "Get in" prompt, HUD rearranged on touch screens. Also fixed a bug: on a phone held sideways the start card was taller than the screen and the Start button could not be reached; the card now scrolls and is compact on short screens.
- **Day/night cycle** (graphics): game clock (1 real second = 1 game minute, starts 08:30), moving sun/moon, sky and fog colours for day, sunset and night, stars, warm lit windows in houses and shops, glowing street lamps with light pools, headlight beams on every car plus a real spotlight for your own car. Tower clocks and HUD follow game time. New key **T** skips one hour.
- **Jobs / missions** (gameplay): three job markers with light beams and minimap dots. Parcel delivery (on foot or by car), Polder taxi (pick up a passenger who stands waiting, drive them home, must stop to let them in/out) and a Ring road time trial (18 gates, 2 min limit, best lap kept). Objective panel with countdown, cash counter in the HUD, pay goes up the faster you finish. E / tap starts a job; R cancels.
- **Procedural sound** (sound): new engine with gears and revs (two detuned saws, sub-octave, rumble noise, filter opens on throttle), tyre squeal on handbrake turns and hard cornering, wind (louder in the open polder and at speed), footsteps (harder on paving), birds by day and crickets at night, a crunchier crash. M now mutes everything at once.
- **Save + pause** (content/controls): progress (coins, cash, best lap, time of day, sound setting) saved in localStorage on every coin/job and every 15 s; start screen shows Continue / New game with a summary. Pause with P, Esc or the II button (also auto-pauses when the tab is hidden); pause card shows stats, sound toggle and New game.
- **Polder traffic** (gameplay): 8 extra cars drive out and back on Lemsterweg, Espelerlaan, Urkerweg and Marknesserweg (right-hand lanes, U-turn at both ends, faster rural speed).
- **Adaptive quality** (performance): pixel ratio drops step by step (down to 0.6) when the frame rate is below ~38 fps and goes back up when there is headroom; phones use a 1024 shadow map and a lower pixel ratio cap.
- **Job direction arrow** (gameplay/UI): the job panel now has an arrow that points to the next marker relative to the camera, plus the distance; toasts move down so they no longer cover the job panel.
- **Rain showers** (graphics/sound): random showers (about every few game hours), 2200 rain streaks that follow the camera, grey sky, darker clouds, thicker fog, dimmer sun, rain hiss (louder in a car), no birdsong while it rains, toast "A polder shower rolls in."
- **Cyclists** (content): 10 cyclists ride along the edge of the inner and outer ring roads in both directions, pedalling, leaning into turns, braking for cars, people and each other, and ringing their bell when you block them. Traffic now brakes for cyclists too.
- **Speed cameras** (gameplay/content): 80 km/h signs where the four polder roads leave the ring and a *flitspaal* on each road; speeding gives a white flash, a click and a €50 fine (€120 above 110 km/h). Finding all 12 polder coins now pays a €250 bonus (the old message also showed a wrong total time after a reload).
- **Portrait phone layout** (mobile/bug): on a phone held upright the job panel covered the coins/cash/time panel. Narrow screens now get compact top panels and the job panel sits under them, between the minimap and the pause button.
- **Horn reaction** (gameplay): pedestrians within 14 m jump out of the way when you sound your horn.

### Report for Ron
Today's run (the first one) added 13 improvements to Emmeloord Vrijbaan, each tested in headless Chromium (no console errors, walking and driving checked, screenshots looked right) and pushed to `main` straight away:

- The game now works on phones: joystick, look-drag and buttons, plus fixes so the Start button and HUD fit on small screens.
- Day and night: sunsets, stars, lit windows, street lamps and headlights. Press T to skip an hour.
- Three jobs: parcel delivery, polder taxi and a ring road time trial, with cash, a timer and a direction arrow.
- Much better sound: a revving engine with gears, tyre squeal, wind, rain, footsteps, birds and crickets.
- Progress is saved (coins, cash, best lap), with Continue / New game and a pause menu (P, Esc or the II button).
- More life in town: traffic on the four polder roads, 10 cyclists who ring their bell, pedestrians who jump aside when you honk.
- Rain showers now and then, and speed cameras (flitspalen) with 80 km/h signs on the polder roads.
- Automatic quality drop on slow devices.

**Screenshot:** dusk at 19:36 on the street north of De Deel, driving the orange car on a taxi job. Windows glow warm, the headlights light the road, the sky is orange-pink behind the Poldertoren, and the job panel at the top shows "Pick up the passenger…", a 1:20 countdown and an arrow with 110 m.

**Problems:** none open. Testing runs in a software renderer at only a few frames per second, so driving feel and real frame rate on a phone still need a check by hand. Audio was checked for errors, but I could not listen to it.

### Next ideas (for the next run)
1. Play-test the jobs on a real phone and tune times/pay; add a job "level" that gets harder.
2. Traffic lights or give-way behaviour at the ring road junctions; AI cars sometimes bunch up at corners.
3. Real wet-road look in rain (darker, shinier asphalt, spray behind cars).
4. More Emmeloord landmarks: the water tower, a church, the Smeding / bus station area, a harbour on the vaart.
5. Simple car damage (dents/smoke) and a garage to repair for cash.
6. More collectibles or achievements (e.g. visit every street, top of the Poldertoren via a lift).
7. Spot the Dutch bike lanes: red fietspad strips along the ring road for the cyclists.
8. Performance: merge the people/car parts into fewer meshes; check draw calls on phones.

## 2026-11-20 — Graphics upgrade (Ron: "less blocky, more realistic")
- PBR materials everywhere, ACES tone mapping, sky dome with sun disc and halo, image-based lighting from the sky (cars and glass reflect it).
- Facades: 2x2 atlases per style so neighbouring windows differ; Dutch brick bond, rollaag lintels, framed windows with transoms, sills, curtains/blinds; normal maps for relief. Separate plain-brick gables. Night glow follows the same layout.
- Roofs: pantile texture with relief, white fascia boards and gutters, ridge caps, chimneys; dark plinths along walls.
- Ground: herringbone klinkers, 30 cm pavement tiles, asphalt with patches and cracks, finer grass.
- Cars: rounded extruded bodies (car and van), glass cabin, metallic paint, spoked rims, bumpers, mirrors, yellow Dutch plates, soft contact shadow.
- People: rounded heads, torsos and limbs; trees: lumpy clustered crowns with fake ambient occlusion.
- Performance: trees split into 150 m chunks (hidden out of view, shadows only nearby, simpler crowns beyond 320 m).
- Lantern street lamps, tapered turbine blades.
- Not touched: road layout and the Poldertoren (another thread is rebuilding those).

## 2026-11-20 — Graphics round 2 (Ron: "even more realistic")
- Graphics setting Low / Medium / High in the pause menu, saved. Phones start on Medium, laptops on High; if frames stay slow at the lowest resolution the game steps down by itself (only when the player has not picked a level).
- High: post-processing chain (screen-space ambient occlusion from the depth buffer, bloom, colour grading, vignette, FXAA) and a 4096 shadow map.
- Billboard clouds with shaded undersides, tinted by time of day and rain.
- Wet streets in rain: asphalt, klinkers and paving get darker and glossy.
- Plinths, white fascia boards and gutters on the OpenStreetMap buildings; less neon grass.
- Note: some views in town draw 2,000+ objects per frame (before this change too); merging street furniture and people would help phones.

## 2026-11-20 — Graphics round 3 (Ron: "another step further")
- Photographed skies (CC0 Poly Haven puresky HDRIs: partly cloudy, sunset, overcast) on the sky dome by day, blended by time of day and rain and turned so the sun lines up; image-based lighting and reflections use the same sky; fog takes the photo's horizon colour. Night still uses the gradient sky with stars.
- Photo textures with normal maps (CC0 Poly Haven, in `assets/`, credits in `assets/CREDITS.md`): red, dark and buff brick on facades and gables (windows drawn on top), herringbone klinkers, asphalt, pavement tiles, grass, roof tiles. Loaded in the background on Medium and High; Low keeps the procedural textures. About 2.6 MB in total.
- Draw calls: people 15 → 5 meshes, cars 24 → 11 meshes, night-only light pools and beams skipped by day. A busy street on a phone went from ~2,700 to ~1,500 draw calls.
- Unreal Engine was asked about; the game stays in the browser (Three.js) so it keeps working on the GitHub Pages link and phones.
- Ideas next: real CC0 glTF car and tree models, a few photo shop fronts, roughness maps for wet-road puddles.

## 2026-11-20 — Graphics round 4: real animated characters

- Pedestrians, cyclists and taxi passengers are now a rigged, animated CC0 human (Quaternius "Man"): idle, walk and run clips, with the gait driven by distance walked so feet don't slide. Each person is recoloured per vertex and merged into one skinned mesh, so a pedestrian is still one draw call. People more than 70 m away animate at a quarter of the rate.
- The player is the CC0 Quaternius "Adventurer" (backpack removed), recoloured to the old orange top and dark jeans. It uses idle, walk and run.
- Cyclists use the sitting pose, leaning forward with hands on the bars.
- The models load after the game starts (`loadRigs`, `assets/models/*.glb`, loader in `assets/lib/`). Until they arrive, or if they fail, the old procedural people stay.
- CC0 cars and trees (Kenney) were tried and not used, because they look more toy-like than the current ones.
- Phone street view: 275 → 312 draw calls.

## 2026-11-20 — Matching Ron's drone video ("Emmeloord van Boven")

- Poldertoren rebuilt to match the footage: dark brown brick all the way up, no white ribs or bands, three rows of narrow slits per face, dark clock faces with gold hands, a brick belfry with louvred openings, a dark gallery rail, a green copper roof and a golden ball and vane.
- Houses with an almost rectangular footprint now get pitched roofs (about 2,100 more). Roof colours are mostly dark grey concrete tiles.
- Street trees: tall trunks with limbs and loose crowns made of alpha-tested leaf cards. Far chunks use fewer cards.
- More dark brown brick on houses, darker canal water, darker grass, closer haze, and slightly less saturation on High.
- Phone street view: 312 → 336 draw calls.

## 2026-11-20 — More animation

- Car suspension: the body rolls in turns, the nose dips when braking and the car squats when pulling away (a damped spring in `syncCar`).
- Trees sway in the wind (a vertex shader on the crowns, each tree with its own phase). The wind is stronger in rain.
- The canal water has moving ripples (an animated normal map).
- Flocks of birds circle the Poldertoren and the town. All the birds are one dynamic mesh with flapping wings.
- The player leans into turns and holds a mid-stride pose while jumping.

## 2026-11-20: De Deel, buses, 't Voorhuys and the fountain (Ron's photos)
- **Brown klinkers** on the big car park beside the Poldertoren, aisles included (no centre lines there); the bays are filled with parked cars, drawn as instanced meshes so they cost a few draw calls in total.
- **Bus station** (the lot right beside the tower, platforms A to G): asphalt, raised platforms with kerbs, three 12 m city buses parked at platforms with doors to the platform, a glass shelter on platform B. Buses are solid but do not drive yet.
- **Hotel 't Voorhuys** stands where OpenStreetMap has it (way 266435940, De Deel 20): on the south front of its block at the entrance of the Lange Nering, in front of the rest of that block: buff brick, hipped dark roof, curved glass conservatory with an orange canopy and white slanted posts, lighter annex with three flags, terrace with parasols and box-ball planters, lit "'t Voorhuys" lettering, warm uplights and lit windows at night.
- **Polderfontein** (splash fountain, OSM way 902694671, 2020) at its real spot on De Deel in front of the hotel: octagon of wet stone in herringbone klinkers with 22 jets that pulse and take turns in three groups.

## 2026-11-20: plan steps "better cars" and "a living town"
- **Car lights**: every driven car now has glowing head lights and tail lights at dusk and night (seen only from the side they face), bright brake lights whenever a car slows down or waits (day and night), and blinking orange indicators when cars turn at junctions. All glows are one instanced mesh.
- **Rain spray**: cars faster than about 16 km/h throw up spray from their tyres on wet roads (one shared particle system).
- **Café terraces**: OSM cafés, restaurants, ice cream shops and snack bars within 700 m get a terrace of tables, chairs and parasols in front of the shop (merged into a few meshes, solid).
- **Bus station**: people wait on the platforms A to G.
- **Ducks**: small groups of ducks paddle on the canals near the centre, turning away from the banks and avoiding bridges (two instanced meshes).

## 2026-11-20: plan steps "weather and seasons" and "landmarks"
- **Morning mist**: on about half the days, mist lies over the polder from about 05:00 and burns off by 10:00 (fog closes in to ~110 m, the sky and sun fade).
- **Wind gusts**: the trees sway harder in gusts that come and go.
- **Seasons** (pause menu, "Season: Auto" follows the calendar): spring has thinner, fresher crowns like the drone video, autumn turns the leaves yellow-brown and thins them a little, winter has bare trees, frosty grass, and showers fall as snow that settles on grass and roofs and melts afterwards.
- **Churches from OSM**: Heilige Michaëlkerk, De Rank, Nieuw Jeruzalemkerk and De Hoeksteen now have church buildings on their real footprints (brick with tall narrow windows) and a bell tower with a copper spire and a golden cross on the corner nearest the street. Their names show when you are there. The tower heights and looks are approximations.
- The harbour (1e Industriehaven) lies just outside the mapped area, so it is not in the game yet.

## 2026-11-20: plan step "traffic that behaves"
- **Buses drive their real lines** (routes from OpenStreetMap relations): one bus runs 71 and 77 in a loop (in from Zwolle, out to Lemmer, in from Lemmer, out to Zwolle), a second runs the 315 Qliner to and from Groningen, a third rides the 71/77 loop half a lap behind. They keep right, brake for corners, leave from and return to the platforms at the bus station, and stop at the real stops on their way (Kettingstraat, Lange Dreef, Begraafplaats) with the indicator on. The display shows the line and where the bus goes. Buses wait for traffic, people and red lights, and are solid. You can't borrow a bus.
- **Bus stop signs** (blue H) at the real stops.
- **Traffic lights** at the 24 signals OpenStreetMap marks on the town's roads (Korte Dreef, Lange Dreef/Nagelerstraat, Urkerweg, Kettingstraat, Boslaan and others). Each faces the traffic it controls and has a white stop line. Crossing streets take turns (green 14 s, amber 3 s, a short all-red). AI cars and buses roll up to the stop line on red, queue behind each other without honking, and go on amber only when they are too close to stop.
- **Red-light camera**: drive through red and you are fined €90 (flash and sound, like the flitspaal).
- Draw calls at the phone start view: 524 (was 518 to 538).

## 2026-11-20: bus 146, police, benches and the Thursday market
- **Bus 146 (Dronten)** now runs too, on its OpenStreetMap route, stopping at Smeden and Zuyderzee College. Buses only hop between two platforms of the bus station when you can't see them.
- **Police**: after a flitspaal or red-light fine, a police car (white with blue and yellow blocks, flashing blue lights, two-tone siren) comes after you along the streets. Stop next to it and you are pulled over (€150 ticket); get more than about 330 m away for a few seconds and you lose them.
- **Days of the week**: the clock shows the day (it starts on today's real weekday and moves on at midnight).
- **Thursday market on the Kettingplein**, the real market day, place and hours (08:00 to 14:30, source: Visit Flevoland): two rows of stalls with striped awnings and crates of fruit and vegetables, and extra shoppers. Stalls stand from 07:30 to 15:00 game time.
- **People on benches** near the centre (up to 14, sitting, facing the street).
- Draw calls at the phone start view: 518.

## 2026-11-20: plan step "a reason to keep playing" (career and garage)
- **Career**: jobs give XP equal to their pay, polder coins give 25 XP. Ten levels (150, 400, 800, 1400, ... XP); the level and a progress bar sit in the HUD. Each level adds 5% to job pay. The taxi job unlocks at level 2. Old saves start with XP equal to their cash.
- **Garage** at the real car dealer hall OpenStreetMap shows by the Nagelerstraat (forecourt on the north side, Meeuwenkant): showroom windows lit at night, a GARAGE sign and totem, cars for sale on the forecourt, a white dot on the minimap. Walk or drive onto the orange ring and press E.
- **Cars to own**: Polder Hatch (your first car), Bezorgbus delivery van (€450, level 2, parcel jobs pay 25% more), Flevo GT (€1600, level 4, rear wing, 169 km/h), Volt E (€2700, level 6, fastest off the line). Bought cars are kept; switch between them in the garage. Your car waits on the forecourt.
- **Upgrades** per car, three steps each: engine (top speed), turbo (acceleration), sport tyres (grip), unlocked by level. **Paint** in ten colours (€40).
- Everything (XP, cars, upgrades, paint) is saved in the browser.

## 2026-11-20: plan step "more jobs and the kermis"
- **New vehicles** you can ride any time (walk up and press E): a courier bike at the real bike racks on De Deel, a red pizza scooter outside pizzeria Casareccia (OpenStreetMap: cuisine=pizza, Korte Achterzijde) and a farm tractor with a trailer on the Marknesserweg just outside town. Bikes and scooters lean into corners, the tractor's trailer swings wide in turns. Each has its own speed, grip, lights and engine sound (the bike is silent). Left somewhere, they go back to their spot when you are not looking.
- **Bike courier** (level 1): three envelopes to shops in the centre, pedestrian streets included.
- **Pizza delivery** (level 2): two hot pizzas from Casareccia to addresses around town.
- **Potato harvest** (level 3): drive the tractor to the potato field on the Marknesserweg, load up, and bring the harvest to a farm with a barn and silo on the Nagelerweg. (The field and farm are not real places; the roads are.)
- **Ring race** (level 4, by car): a black sports car with a yellow stripe races you once around the ring through every gate, after a 3-2-1 countdown. It keeps right, overtakes slow traffic and is a red dot on the minimap. Beat it for €200; best race time is saved.
- **Kermis on De Deel** (in 2026 the real Emmeloord kermis is back on De Deel, source: Omroep Flevoland): every Friday to Sunday it stands on the east half of the big car park (the parked cars make way), and the rides turn from 12:00 to 23:30. A Ferris wheel (22 m, 12 gondolas that stay level), a carousel with horses going up and down under a striped canopy, a swing ride whose seats fly out as it speeds up, bumper cars bumping around under a roof, 13 stalls (oliebollen, suikerspin, schiettent, poffertjes, loterij, patat, grijpkraan, ballentent, nougat), an entrance arch, string lights across the lane that glow at night, visitors, and a fairground organ waltz (an original tune) you hear when you come close.
- **Ride the Ferris wheel**: walk to the front of the wheel while the kermis is open and press E (€4) for one round with a view over Emmeloord; drag to look around.
- Draw calls at the phone start view: 547 while the kermis stands (it is visible from the start), 518 on weekdays.
