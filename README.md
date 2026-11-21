# Emmeloord Vrijbaan

A small 3D open-world game in the browser, set in the centre of Emmeloord (Noordoostpolder, the Netherlands). Walk across De Deel, get into any car, and drive the real streets around the Poldertoren.

## Play

Open `index.html` in a browser (desktop or phone). No build step is needed; Three.js (r128) loads from cdnjs. To serve it locally:

```sh
python3 -m http.server 8000
# then open http://localhost:8000
```

## Controls

| Key | Action |
| --- | --- |
| W A S D / arrow keys | Walk, or drive when in a car |
| E | Get in or out of a car (you can also borrow a car from traffic), or start a job at a job marker |
| Shift | Sprint |
| Space | Jump, or handbrake when driving |
| Mouse | Click or drag to look around, scroll to zoom |
| H | Horn |
| G | Call a tow truck when your car is wrecked (€60, takes it to the garage) |
| R | Back to De Deel |
| T | Skip one hour (day/night) |
| M | Sound on/off |
| N | Music on/off |
| P / Esc | Pause (also the II button) |

### Phone and tablet

Turn the phone sideways. Put your left thumb anywhere on the left side for a joystick (walk, or steer and accelerate in a car; push it all the way to run). Drag with your right thumb to look around. Buttons: **CAR** (get in/out), **JUMP/BRAKE** and **HORN**. You can also tap the "Get in" prompt.

## Speed cameras

The four polder roads have an 80 km/h limit (red-ringed signs where they leave the ring road). Speed cameras (*flitspalen*) on each of them flash and fine you €50, or €120 above 110 km/h.

## Car damage

Hard crashes into walls, trees or other cars damage the car you drive (the bar under the speedometer). Above half damage smoke pours from the bonnet; badly damaged cars lose speed, and a wrecked car only limps along. The garage repairs it (the price depends on the damage). You can see it too: from 40% the bonnet is dented, from 75% the front is crumpled, the paint dull and the headlights broken. A wrecked car far from the garage can be towed there (G, or the pause menu on a phone) for €60.

## Achievements

23 achievements (first coin, every job, the tower lift, the Ferris wheel, 150 km/h, losing the police, a night out at 3 AM, the Thursday market, and more). A gold message pops up when you earn one; the full list is in the pause menu under **Achievements**.

## Saving

Coins, cash, your best lap and the time of day are saved in your browser automatically. The start screen then offers **Continue** or **New game**.

## Jobs

Coloured light beams mark three jobs (also shown on the minimap). Stand or drive into one and press **E** (or tap the prompt):

- **Parcel delivery** (blue, on De Deel): pick up a parcel at a real shop in the centre and deliver it to an address on a real street. Works on foot or by car.
- **Polder taxi** (yellow, north of De Deel): pick up a passenger and drive them home, sometimes far out into the polder. Stop at the marker to let them in and out.
- **Centrum time trial** (pink): one lap around the centre (Korte Dreef, Espelerlaan, Koningin Julianastraat, Noordzijde, Smedingplein, Lange Dreef) through all the gates before the timer runs out. Your best lap is remembered.

Finishing faster pays more cash. **R** cancels a job.

## What's in town

- **Poldertoren lift**: walk to the tower door facing De Deel and press **E** to ride the lift up to the viewing platform at 43.4 m. Walk around the gallery with A/D (or the joystick), drag to look, press E to go back down.
- **Carillon**: from 08:00 to 22:00 the tower's bells play a short tune on every full hour and then strike the hour. You hear it from about 700 m away.
- The Poldertoren (1959, 65 m to the top of the weather vane): octagonal brick shaft with white concrete ribs and bands, the glass case with the turning figures (mammoth, caveman, cog ship, pioneer, combine harvester, factory) above the door facing De Deel, four clocks that show the game time, the visitor platform and the open crown with its 48-bell carillon.
- De Deel with market stalls, bikes and benches; shops along Lange Nering and Korte Nering; Lange and Korte Achterzijde.
- Cyclists riding the ring roads (they ring their bell if you block the way).
- A ring road with traffic, and Lemsterweg, Urkerweg, Marknesserweg and Espelerlaan leading out to tulip fields, farms and wind turbines.
- Polder weather: rain showers roll in now and then, with grey skies, falling rain and the sound of it.
- A day and night cycle (one real second is one game minute): sunsets, stars, lit windows, street lamps and headlights.
- A canal with a bridge, a park with a pond, and 12 orange polder coins to find.
- Background music: "Emmeloord, Vrijbaan" (made by Ron with Suno, `music.mp3`), looping quietly under the game sounds from the start menu on. **N** or the pause menu turns it off; the choice is saved.

Streets, squares, parking, water, parks, building footprints, shops, trees and street lamps come from OpenStreetMap (© OpenStreetMap contributors, ODbL, https://www.openstreetmap.org/copyright), for about 1.8 by 1.5 km around the Poldertoren. Building heights, facades, colours and the polder outside the town are approximated.
