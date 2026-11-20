# Emmeloord Vrijbaan: improvement log

Each daily run adds an entry at the top: the plan, what was done (title, category, outcome), problems found, and ideas for the next run.

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
