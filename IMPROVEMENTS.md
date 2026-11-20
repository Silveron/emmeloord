# Emmeloord Vrijbaan: improvement log

Each daily run adds an entry at the top: the plan, what was done (title, category, outcome), problems found, and ideas for the next run.

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
