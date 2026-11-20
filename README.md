# Emmeloord Vrijbaan

A small 3D open-world game in the browser, set in the centre of Emmeloord (Noordoostpolder, the Netherlands). Walk across De Deel, get into any car, and drive the ring road around the Poldertoren.

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
| R | Back to De Deel |
| T | Skip one hour (day/night) |
| M | Sound on/off |
| P / Esc | Pause (also the II button) |

### Phone and tablet

Turn the phone sideways. Put your left thumb anywhere on the left side for a joystick (walk, or steer and accelerate in a car; push it all the way to run). Drag with your right thumb to look around. Buttons: **CAR** (get in/out), **JUMP/BRAKE** and **HORN**. You can also tap the "Get in" prompt.

## Saving

Coins, cash, your best lap and the time of day are saved in your browser automatically. The start screen then offers **Continue** or **New game**.

## Jobs

Coloured light beams mark three jobs (also shown on the minimap). Stand or drive into one and press **E** (or tap the prompt):

- **Parcel delivery** (blue, on De Deel): pick up a parcel at a shop on the Nering and deliver it to an address in town. Works on foot or by car.
- **Polder taxi** (yellow, north of De Deel): pick up a passenger and drive them home, sometimes far out into the polder. Stop at the marker to let them in and out.
- **Ring road time trial** (pink, on the Ringweg): one lap through all the gates before the timer runs out. Your best lap is remembered.

Finishing faster pays more cash. **R** cancels a job.

## What's in town

- The Poldertoren (1959): brick shaft, visitor platform, open carillon crown with bells, clocks that show the game time, and a carillon tune when you are nearby.
- De Deel with market stalls, bikes and benches; shops along Lange Nering and Korte Nering; Lange and Korte Achterzijde.
- Cyclists riding the ring roads (they ring their bell if you block the way), and a ring road with traffic, and Lemsterweg, Urkerweg, Marknesserweg and Espelerlaan leading out to tulip fields, farms and wind turbines.
- Polder weather: rain showers roll in now and then, with grey skies, falling rain and the sound of it.
- A day and night cycle (one real second is one game minute): sunsets, stars, lit windows, street lamps and headlights.
- A canal with a bridge, a park with a pond, and 12 orange polder coins to find.

The street layout is a simplified approximation of the real town; side streets, buildings and shop names are invented.
