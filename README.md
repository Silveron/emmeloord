# Emmeloord Vrijbaan

A small 3D open-world game in the browser, set in Emmeloord (Noordoostpolder, the Netherlands). Walk across De Deel, get into any car, and drive the real streets of the whole town: the Centrum around the Poldertoren, the residential neighbourhoods (Emmelhage, Revelsant, Espelervaart, De Erven, Bos en Gaard, De Zuidert, Waterland and more), the harbours and the business parks De Munt and De Gilden.

## Play

Open `index.html` in a browser (desktop or phone). No build step is needed; Three.js (r159) is included in `assets/lib/`. To serve it locally:

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
| Q | Throw a snowball (when snow lies in winter; on a phone the HORN button turns into THROW) |
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

37 achievements (pushing an ice chair, scraping a frozen windscreen, first coin, every job, the tower lift, the Ferris wheel, 150 km/h, losing the police, a night out at 3 AM, the Thursday market, and more). A gold message pops up when you earn one; the full list is in the pause menu under **Achievements**.

## Saving

Coins, cash, your best lap and the time of day are saved in your browser automatically. The start screen then offers **Continue** or **New game**.

## Jobs

When a job sends you to a real address, a house-number plate floats over that house, so you can see which door it is.

Coloured light beams mark the job start spots (also shown on the minimap). Stand or drive into one and press **E** (or tap the prompt): During a job a GPS line on the minimap shows the way along the streets (one-way streets respected when you drive), and deliveries go to real house numbers from OpenStreetMap.

- **Parcel delivery** (blue, on De Deel): pick up a parcel at a real shop in the centre and deliver it to an address on a real street. Works on foot or by car. At the address the doorbell rings and the resident comes out to collect it.
- **Polder taxi** (yellow, north of De Deel): pick up a passenger and drive them home, often to a real address on the other side of town. Stop at the marker to let them in and out. Each passenger is a character with their own lines (an elderly lady, a late worker, a nurse, a farmer, a man with eggs in his shopping, a tourist, a mum with her daughter in the back seat and a dad with two bickering children (by day); on school-day mornings a pupil late for the Zuyderzee College, and late at night on kermis weekends someone going home from the fair on De Deel); they chat during the ride and react to crashes and speeding (the student likes it fast). At the end they rate the ride with 1 to 5 stars, which changes the fare; the fare follows the real driving route. From level 2, people at the kerb sometimes wave for a taxi while you drive around (yellow beam and a yellow dot on the minimap): stop next to them and the ride starts right there. Some rides are special: Mr Smit has cut his thumb and needs a rush ride to the Dokter J.H. Jansencentrum on the Urkerweg (tight time, bigger fare), and Mr Visser the tourist wants to pass the Poldertoren first. Passengers wave goodbye and walk to their front door; taxi stats (rides, average rating, best fare, takings) are in the pause menu.
- **Centrum time trial** (pink): one lap around the centre (Korte Dreef, Espelerlaan, Koningin Julianastraat, Noordzijde, Smedingplein, Lange Dreef) through all the gates before the timer runs out. Your best lap is remembered.
- **Ice race** (light blue, winter only, on the ice beside the koek-en-zopie stall): with rented skates, skate to the orange flag at each end of the frozen canal and back to the stall before the timer runs out, against two rival skaters (Sjoerd and Femke) after a 3-2-1 countdown. Beat them both for a €20 prize. Your best time is remembered.

Finishing faster pays more cash. **R** cancels a job.

## What's in town

- **Tower plaque**: a bronze plaque beside the tower door; walk up to it to read about the tower.
- **Friendly town**: passers-by sometimes wave hello when you walk right past them. Men and women (long hair, ponytails, bobs, buns, skirts and dresses; in winter coats, scarves and woolly hats, in autumn some scarves), elderly people (grey hair, a slower walk) and parents with a child at their side. Honk (**H**) near people and the nearest one calls something back in a speech bubble; cyclists ring their bell, and taxi passengers have an opinion about it.
- **Lost child**: by day, while you walk around without a job, you may hear a child crying nearby. Walk up to them: they tell you what their mum or dad is wearing and the street where they got lost, then follow you. Find the parent for a small reward; after a minute the child remembers the way and the parent shows as a pink dot on the minimap.
- **Poldertoren lift**: walk to the tower door facing De Deel and press **E** to ride the lift up to the viewing platform at 43.4 m. The lift display shows tower facts on the way up. Walk around the gallery with A/D (or the joystick), drag to look, press E to go back down.
- **Carillon**: from 08:00 to 22:00 the tower's bells play a short tune on every full hour and then strike the hour. You hear it from about 700 m away.
- The Poldertoren (1959, 65 m to the top of the weather vane): octagonal brick shaft with white concrete ribs and bands, the glass case with the turning figures (mammoth, caveman, cog ship, pioneer, combine harvester, factory) above the door facing De Deel, four clocks that show the game time, the visitor platform and the open crown with its 48-bell carillon.
- De Deel with market stalls, bikes and benches; shops along Lange Nering and Korte Nering; Lange and Korte Achterzijde.
- Kermis weekends on De Deel: people queue at the oliebollen stall (you hear the fat crackle) and you can buy a bag yourself at the counter (**E**, €3). You eat all six on the way, and the powdered sugar on your jacket gets you a few remarks. When the rides close at 23:30 the visitors walk home into town, chatting about their night.
- Cyclists riding the ring roads (they ring their bell if you block the way); some parents carry a toddler in a child seat on the back. On school-day mornings pupils with backpacks cycle to the Zuyderzee College, ride along the school's paved paths into its bike park (both at their real OpenStreetMap spots behind the building), park and walk in; after school they walk back out and ride home. In the dark every bike has a white front lamp with a small pool of light on the road and a red rear light (in winter the morning school run is before sunrise).
- A ring road with traffic, and Lemsterweg, Urkerweg, Marknesserweg and Espelerlaan leading out to tulip fields, farms and wind turbines.
- Winter: the canals freeze over. People skate up and down by day (with steel blades on their feet; a few parents push a toddler along on a wooden ice chair), ducks stand on the ice, and you can walk down the bank and slide across. Turn round too sharply at speed and you slip and land on your back. On the canal closest to the Poldertoren a koek-en-zopie stall on the ice sells hot chocolate (**E**, €2; you carry the steaming cup and sip it), and the rack beside it rents skates (**E**, €5). On skates you push off with **W**, glide a long way, sprint with **Shift**, and on land you can only waddle ('klunen'). Hand them back at the rack. Keep away from the bridges: beside each bridge the ice is thin (darker patches). It creaks and cracks under you, and if you stay you go through up to your knees and have to scramble out.
- Autumn: leaves flutter down from the street trees round you (more when the wind gusts), and heaps of raked leaves lie under trees along the streets. Walk, cycle or drive through a heap and the leaves fly up with a rustle (they are raked up again later). A council worker with a leaf blower often comes to blow a kicked heap back together.
- Snow cover: after a snowfall lawns and roofs turn white, and so do pavements, footpaths and the klinker shopping streets (with trodden grey patches); the asphalt roads get patchy grey slush. On clear winter nights and mornings there is hoarfrost on the grass, verges and roofs, which melts in the first two hours after sunrise.
- Dressed for the weather: in winter the hero wears his orange top as a jacket with long sleeves, a blue scarf and a woolly hat; in autumn just the scarf.
- Snow: when snow lies thick, snowmen appear on lawns round town (they melt when it thaws). Throw snowballs with **Q**: people shout, and children and some grown-ups throw one back. Children also have snowball fights of their own by day. Snowballs that go into a tree crown shake a little snow off the branches.
- Tracks in the snow: walking leaves a trail of boot prints, driving leaves tyre tracks (they fade after a few minutes or when the snow melts), and footsteps crunch.
- Snowy days: snow lies on the bare branches of the street trees and on the Poldertoren's gallery and copper roof; parents pull a toddler through town on a wooden sledge; and on frosty days icicles hang from the eaves of the pitched roofs.
- Festive lights: in winter, strings of warm white fairy lights hang across the shopping streets of the centre (Lange Nering, Kerksteeg, Smallegang, Luifelsteeg, De Schalm and round de Deel), some with hanging drops. They twinkle softly and glow from dusk.
- Your own ice chair: with skates on, press **E** at the skate rack again to rent an ice chair (€3) with a toddler in it and push it round the frozen canal. Press **E** at the rack to hand it back.
- Frosted windscreens: on clear winter nights and mornings (from about 20:00 until an hour and a half after sunrise) parked cars have frost on their windows. Walk up to a frozen car and press **E** to scrape the windscreen (scraping sound, ice shavings), or press **E** again while scraping to get straight in: then you drive half blind until the heater clears the glass from the bottom up (about 20 s). A car you have driven stays clear for a few hours.
- Cold days: in winter, on autumn mornings and evenings and on early spring mornings you and the people near you breathe out little clouds of mist.
- Polder weather: rain showers roll in now and then, with grey skies, falling rain and the sound of it.
- A day and night cycle (one real second is one game minute): sunsets, stars, lit windows, street lamps and headlights. The length of the day follows the season as in Emmeloord: in winter the sun rises at about 08:30 and is down before 17:00 (and stays low, with long shadows), in summer it is light from about 05:30 to 22:00.
- A canal with a bridge, a park with a pond, and 12 orange polder coins to find.
- Background music: "Emmeloord, Vrijbaan" (made by Ron with Suno, `music.mp3`), looping quietly under the game sounds from the start menu on. **N** or the pause menu turns it off; the choice is saved.

Streets, squares, parking, water, parks, building footprints, shops, trees and street lamps come from OpenStreetMap (© OpenStreetMap contributors, ODbL, https://www.openstreetmap.org/copyright), for the whole town, about 5.1 by 5.3 km around the Poldertoren (12,700 buildings, 6,000 real addresses, neighbourhood names in the top-left corner). Far-away parts of town are drawn as simple blocks and only nearby tiles are drawn in full, so it stays smooth on phones; traffic and cyclists follow you around town. Building heights and roof shapes (eave and ridge height, ridge direction) are measured values from the 3D BAG (© 3D BAG by the 3D geoinformation group, TU Delft, CC BY 4.0, https://3dbag.nl), matched to the OpenStreetMap buildings by their BAG id with `tools/bag3d.py`; about 95 % of buildings have them. Facades, colours and the polder outside the town are approximated.
