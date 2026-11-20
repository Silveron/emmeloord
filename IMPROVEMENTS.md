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
