# Emmeloord Vrijbaan

A small 3D open-world game in the browser, set in the centre of Emmeloord (Noordoostpolder, the Netherlands). Walk across De Deel, get into any car, and drive the ring road around the Poldertoren.

## Play

Open `index.html` in a desktop browser. No build step is needed; Three.js (r128) loads from cdnjs. To serve it locally:

```sh
python3 -m http.server 8000
# then open http://localhost:8000
```

## Controls

| Key | Action |
| --- | --- |
| W A S D / arrow keys | Walk, or drive when in a car |
| E | Get in or out of a car (you can also borrow a car from traffic) |
| Shift | Sprint |
| Space | Jump, or handbrake when driving |
| Mouse | Click or drag to look around, scroll to zoom |
| H | Horn |
| R | Back to De Deel |
| M | Sound on/off |

## What's in town

- The Poldertoren (1959): brick shaft, visitor platform, open carillon crown with bells, clocks that show your local time, and a carillon tune when you are nearby.
- De Deel with market stalls, bikes and benches; shops along Lange Nering and Korte Nering; Lange and Korte Achterzijde.
- A ring road with traffic, and Lemsterweg, Urkerweg, Marknesserweg and Espelerlaan leading out to tulip fields, farms and wind turbines.
- A canal with a bridge, a park with a pond, and 12 orange polder coins to find.

The street layout is a simplified approximation of the real town; side streets, buildings and shop names are invented.
