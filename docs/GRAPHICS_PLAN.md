# Emmeloord Vrijbaan: realistic graphics plan

*Written 2026-11-21 for Ron. This is a plan only; nothing in it is built yet.*

The goal: when you stand on De Deel, drive down the Lange Nering or come over the A6 viaduct at the Zwolse Vaart, the game should look like a sunny (or rainy) afternoon in the real Emmeloord, and not like a game that is "pretty good for the browser". It has to keep working from the GitHub Pages link and on phones.

The plan has ten phases. Each phase can be shipped on its own, makes a visible difference, and has a check at the end (before/after screenshots from fixed spots and a performance measurement). Phases 1 to 3 give the biggest jump for the least risk and should come first.

---

## Contents

1. [What "realistic" means for Emmeloord](#1-what-realistic-means-for-emmeloord)
2. [Where the graphics are today](#2-where-the-graphics-are-today)
3. [What holds the look back](#3-what-holds-the-look-back)
4. [Rules for this work](#4-rules-for-this-work)
5. [Performance budgets (phones first)](#5-performance-budgets-phones-first)
6. [The phases](#6-the-phases)
   - [Phase 0: Measuring stick](#phase-0-measuring-stick)
   - [Phase 1: Colour and light that are right](#phase-1-colour-and-light-that-are-right)
   - [Phase 2: Engine upgrade (Three.js r128 to current)](#phase-2-engine-upgrade-threejs-r128-to-current)
   - [Phase 3: Dutch streets at kerb height](#phase-3-dutch-streets-at-kerb-height)
   - [Phase 4: Roads and water in 3D (A6 viaducts, sunken canals)](#phase-4-roads-and-water-in-3d-a6-viaducts-sunken-canals)
   - [Phase 5: Buildings with real heights, roofs and eras](#phase-5-buildings-with-real-heights-roofs-and-eras)
   - [Phase 6: Trees, hedges and grass](#phase-6-trees-hedges-and-grass)
   - [Phase 7: Shadows, ambient occlusion and night light](#phase-7-shadows-ambient-occlusion-and-night-light)
   - [Phase 8: Water, rain and wet streets](#phase-8-water-rain-and-wet-streets)
   - [Phase 9: Cars, buses and people up close](#phase-9-cars-buses-and-people-up-close)
   - [Phase 10: Camera, post-processing and the far horizon](#phase-10-camera-post-processing-and-the-far-horizon)
7. [Order and schedule](#7-order-and-schedule)
8. [What is needed from Ron](#8-what-is-needed-from-ron)
9. [Risks](#9-risks)
10. [Appendix: OpenStreetMap facts used in this plan](#10-appendix-openstreetmap-facts-used-in-this-plan)

---

## 1. What "realistic" means for Emmeloord

Realism here is not "more polygons". It is getting the things right that your eye checks first:

| What the eye checks | What Emmeloord actually looks like (sources below) | Today in the game |
| --- | --- | --- |
| **Colour and brightness** | Dark red-brown brick, grey klinkers, green verges, soft northern light, big skies. Pale things (concrete, white fascia boards) are bright but never glowing. | Pale surfaces glow and look washed out (known bug). |
| **Ground** | Most residential streets are klinkers (paving stones), not asphalt; pavements are raised with kerbs; red cycle paths; bollards everywhere. | All car streets are asphalt (except De Deel), everything is one flat sheet at y = 0, no kerbs. |
| **Shape of the town** | Almost all houses are from 1943 to 1972 (rebuilding era of the Noordoostpolder), in rows, with pitched roofs. Flats are low. | Heights are guessed; roof direction is guessed for rows. |
| **Height differences** | The town is flat, but the A6 runs on bridges over the Zwolse Vaart, Marknesserweg and Kamperweg; the Muntweg (N351) crosses over the A6; canals lie below their banks. | Everything is flat, including the A6 (open issue in `IMPROVEMENTS.md`). |
| **Contact** | Buildings, cars and trees sit *on* the ground: dark contact shadows, damp edges, dirt along walls. | Plinths exist; little contact darkening except SSAO on High. |
| **Distance** | Flat polder horizon with blue haze, wind turbines, farm yards with tree rows. | Fog does this reasonably; far buildings are one-colour blocks. |

The "facts" column comes from OpenStreetMap (see the appendix) and from the facts already recorded in `IMPROVEMENTS.md`. Anything that needs a photo to get right (exact brick colours, roof tile colours per street, shop fronts) is marked as **needs Ron's photos** below, and will not be guessed.

---

## 2. Where the graphics are today

A quick inventory of the rendering code in `index.html` (Three.js r128 from cdnjs, one file, no build step). Line numbers are from commit `c6e79e3`.

| Area | What exists | Where |
| --- | --- | --- |
| Renderer | WebGL renderer, antialias on, PCF soft shadows, sRGB output, ACES filmic tone mapping at exposure 0.9 | `index.html:261` |
| Lights | One hemisphere light (sky/ground), one directional sun with a single 2048 shadow map covering about 190 × 190 m around the player | `index.html:274` |
| Sky | Shader dome blending three CC0 photo skies (day, dusk, overcast) by time and rain, sun disc and halo; stars at night | `index.html:283` |
| Image-based light | The sky dome is rendered into a PMREM environment every few seconds and lights all PBR materials | `index.html:311`, `updateEnv` |
| Materials | `MeshStandardMaterial` everywhere through `Lam()`; flat colours through `lm()`; facade atlases (2 × 2 cells per style) with normal maps; CC0 Poly Haven photo textures for brick, klinker, asphalt, pavement, grass, roof (Medium and High) | `index.html:689`, `loadPhotoTextures` |
| Ground | One grass plane; streets, pavements, squares and water are flat ribbons and polygons at heights between 0.012 and 0.07 m, grouped in 500 m tiles | `index.html:846` |
| Buildings | 12,700 OSM footprints, walls in 300 m tiles, gabled roofs for small houses in rows, plinths, fascia boards; one-colour far LOD beyond 260/400/560 m | `index.html:950` |
| Landmarks | Poldertoren (hand-modelled), 't Voorhuys, Polderfontein, four churches, De Leeuwen | `index.html:1157` and on |
| Trees | 13,000 OSM trees, instanced trunks, limbs and card-based crowns with wind sway, 150 m chunks, seasons | `index.html:1413` |
| Water | `MeshPhongMaterial` with a procedural normal map | `index.html:880` |
| People and cars | Rigged CC0 Quaternius characters; extruded car bodies with metallic paint; buses; far-car LOD | `index.html:1905`, `2020`, `2146` |
| Weather | Rain (streaks, wet glossy streets), morning mist, wind gusts, four seasons, snow on grass and roofs | `index.html:4707` |
| Post (High only) | SSAO from depth, bloom, colour grading, vignette, FXAA | `index.html:4484` |
| Quality levels | Low / Medium / High (`setQuality`), adaptive pixel ratio, auto step-down when slow | `index.html:4580` |

Measured performance (from `IMPROVEMENTS.md`): the phone start view on Medium draws **463 draw calls / 0.90 M triangles**; the busiest view (Kettingplein looking west, Medium) about **1,170 draw calls**. JS heap after loading is about **290 MB**.

---

## 3. What holds the look back

Ordered by how much each one costs the picture.

1. **Flat colours are treated as linear light.** `lm(0xRRGGBB)` and vertex colours go straight into the shader without sRGB conversion, so a "light grey" hex colour becomes much brighter than intended. This is why the garage forecourt, lamp posts and tree trunks look washed out. The tower was fixed by hand; the rest of the game was not (`IMPROVEMENTS.md`, 06:45 run).
2. **The ground is one flat sheet.** No kerbs, no raised pavements, no gutters. In a Dutch street the 10 to 12 cm kerb and its shadow line is one of the strongest cues.
3. **Wrong street surface.** In the centre, OSM tags 168 of 185 residential streets and 125 of 187 unclassified streets as `paving_stones` (klinkers); the game draws them as asphalt.
4. **Everything is flat, including the A6.** The A6 bridges and the N351 overpass are tagged in OSM (see appendix) but drawn at ground level.
5. **Building heights are guessed.** Only 3 of 1,625 buildings in the centre have a `height` tag and 11 have `building:levels`. OSM has no roof shapes either (2 of 1,625). Houses all end up with similar heights.
6. **One shadow map for everything.** 190 m across at 2048 px is about 9 cm per texel on Medium, so shadows near the camera are soft and blocky, and nothing beyond 95 m casts a shadow.
7. **Water is a Phong plane at ground level** with no reflection of the banks, trees or houses. Real Emmeloord canals are mirror-like on calm days.
8. **Far town is one-colour blocks** without roofs, which reads as "game" from the Poldertoren gallery.
9. **FXAA only, and only on High.** Thin things (lamp posts, railings, power lines, tree branches) shimmer when moving.
10. **Old engine.** Three.js r128 (2021) lacks colour management by default, `BatchedMesh`, the newer tone mappers (AgX, Neutral), `MeshPhysicalMaterial` clear coat improvements, and several speed-ups.

---

## 4. Rules for this work

- **OpenStreetMap is the truth for positions.** Real things go where OSM puts them; if OSM does not have it, ask Ron or leave it out. Never guess a location.
- **Photos are the truth for looks.** Colours and styles of real buildings are matched to Ron's photos and drone video ("Emmeloord van Boven"), not invented.
- **Phones first.** Every phase states its cost on Medium on a phone. If it does not fit, it goes to High only.
- **Measure before and after.** Every change is checked with the fixed screenshot spots and draw-call/triangle/frame-time numbers from Phase 0.
- **Ship in small steps, straight to `main`**, as Ron prefers; log each step in `IMPROVEMENTS.md`.
- **Fallbacks stay.** If a texture or model fails to load, the procedural version stays (as today with `loadPhotoTextures` and `loadRigs`).
- **CC0 or self-made assets only**, credited in `assets/CREDITS.md`.

---

## 5. Performance budgets (phones first)

Target devices: a mid-range Android phone from about 2021 (Adreno 610/618 or Mali-G57 class) and an iPhone 12 or newer. Laptops with integrated graphics for High.

| Budget | Low | Medium (phone default) | High (laptop default) |
| --- | --- | --- | --- |
| Frame rate target | 30 fps on old phones | 30 fps solid, 60 on iPhone 12+ | 60 fps on integrated GPU |
| Frame time (GPU) | ≤ 28 ms | ≤ 25 ms | ≤ 14 ms |
| Draw calls, typical view | ≤ 300 | ≤ 550 | ≤ 1,200 |
| Draw calls, busiest view | ≤ 500 | ≤ 900 | ≤ 1,800 |
| Triangles in view | ≤ 0.5 M | ≤ 1.2 M | ≤ 3 M |
| GPU texture memory | ≤ 80 MB | ≤ 160 MB | ≤ 400 MB |
| Shadow maps | 1 × 1024 | 2 cascades × 1024 | 3 cascades × 2048 |
| Post passes | none | 1 combined pass (tone map, grade, FXAA) | AO, bloom, TAA, grade |
| Extra download | 0 | ≤ +8 MB over today | ≤ +20 MB over today (lazy loaded) |
| JS heap after load | ≤ 250 MB | ≤ 300 MB | ≤ 450 MB |
| Load to first frame | ≤ 6 s on 4G | ≤ 8 s on 4G | ≤ 10 s |

How the budgets are kept:

- **Compressed textures (KTX2 / Basis Universal).** Photo textures are now JPEG, which the GPU stores uncompressed (a 1024² texture with mipmaps is about 5.6 MB). KTX2 with ETC1S/UASTC is 4 to 8 times smaller on the GPU. This is the single biggest enabler for richer materials on phones. `KTX2Loader` and its transcoder are vendored into `assets/lib/`.
- **Merging and instancing.** Static things per 300 m tile go into one mesh per material; repeated things (bollards, kerbs stones, lamp posts, bins) are instanced. After the engine upgrade, `BatchedMesh` lets different meshes share one draw call.
- **Distance tiers.** Near (full detail, ≤ 120 m), mid (simplified, ≤ 400 m), far (impostors/blocks). Every new feature says what it does in each tier.
- **Per-feature switches.** Every new effect gets its own flag inside `setQuality`, so the auto step-down can turn off the most expensive one first.

---

## 6. The phases

Each phase has: **goal**, **steps**, **Emmeloord detail**, **cost**, and **done when**.

### Phase 0: Measuring stick

**Goal:** make "more realistic" measurable, so every later step can be judged in minutes.

Steps:

1. **Fixed camera spots** in `window.__game.shots`: a list of named positions, camera angles, time of day, weather and season. Proposed set (all real places, positions from OSM / the existing game data):
   - De Deel, looking at the Poldertoren from the bus station.
   - Lange Nering, from 't Voorhuys looking into the shopping street.
   - Kettingplein on a Thursday morning (market).
   - A residential street in Emmelhage (the terraces from 1940s to 1950s).
   - The Zwolse Vaart crossing of the A6 (for Phase 4).
   - The Poldertoren gallery at 43.4 m looking south over the town (skyline and far LOD).
   - The garage forecourt (pale concrete, the washed-out reference).
   - De Deel at night, in rain, and at dusk.
2. **A benchmark script** (`tools/bench.js`, Playwright, as the daily runs already use) that visits each spot at Low, Medium and High and writes draw calls, triangles, textures in GPU memory and frame time to a JSON file, plus a screenshot.
3. **Before/after sheets**: a side-by-side image per spot, saved in `runs/` in project files, like the existing `graphics-before-after.png` images.
4. **Reference photos**: Ron's photos and frames from the drone video for each spot, stored next to the shots, so the comparison is "game vs real", not "game vs game".

Cost: none in the game. **Done when** the script produces a sheet for all spots in one run.

---

### Phase 1: Colour and light that are right

**Goal:** fix the washed-out look and get a believable Dutch daylight balance. This is the highest-value, lowest-cost phase.

Steps:

1. **One colour pipeline.** Convert every flat colour and every vertex colour from sRGB to linear when it is created: `lm()`, `C()`, all vertex colour buffers in `GB`/`TGB`, the LOD wall colours (`LOD_WALL`), car paints, bus liveries. One helper `srgb(hex)`; afterwards grep for raw `new THREE.Color(0x` and `color:0x` and fix the rest. (After Phase 2 this happens automatically through Three.js colour management.)
2. **Albedo table.** Real materials reflect a known share of light. Clamp every material to a measured range so nothing is brighter than the real thing:

   | Material | Real albedo (approx.) | Use for |
   | --- | --- | --- |
   | Fresh snow | 0.80 to 0.90 | snow only |
   | White paint (fascia, window frames) | 0.70 to 0.80 | fascia boards, kozijnen |
   | Light concrete | 0.35 to 0.50 | Poldertoren plinth, kerbs, forecourt |
   | Grey klinker / pavement tile | 0.20 to 0.30 | streets, pavements |
   | Red-brown brick | 0.15 to 0.25 | most houses |
   | Asphalt (old / new) | 0.10 / 0.05 | roads |
   | Grass | 0.15 to 0.25 | verges, parks |
   | Tree bark | 0.10 to 0.20 | trunks (today they look pale grey) |

   A small debug view (`__game.albedoCheck()`) paints any pixel brighter than its allowed albedo in magenta, so overshoot is easy to find.
3. **Light balance.** Today the hemisphere light (0.74) plus IBL plus the sun all add up, which flattens shading on pale surfaces. Move to: sun as the key light, IBL from the photo sky as the only fill, and the hemisphere light only as a cheap fallback on Low. Sun intensity and colour follow the real sun height for 52.7° N (low and warm in winter, high and white in June).
4. **Exposure.** A slow auto exposure (luminance measured on a 16 × 16 downsample, adapted over 1 to 2 s) so walking out of the shade of a tree, or into a building passage, looks like a camera; clamped so night stays dark. On Low a fixed exposure per time of day.
5. **Tone mapping.** Keep ACES for now; switch to AgX or Neutral after the engine upgrade (Phase 2), which keep pale colours from turning yellow-white.
6. **Specular on rough surfaces.** Lower `envMapIntensity` and raise roughness on brick, concrete and klinker (they are not shiny); keep reflections for glass, paint and wet surfaces.

Emmeloord detail: brick and roof colours are checked against Ron's photos of the centre and the drone video (needs Ron's photos for the residential neighbourhoods).

Cost: none at runtime (maybe 1 small pass for auto exposure on Medium/High).

**Done when:** the garage forecourt, lamp posts, tree trunks and the Poldertoren plinth are no brighter than their albedo range in the check view, and the before/after sheet shows the centre with richer colour and no glowing pale surfaces.

---

### Phase 2: Engine upgrade (Three.js r128 to current)

**Goal:** get the modern tools that the later phases need, without changing how the game looks yet.

Why: r128 is from 2021. Current Three.js gives colour management (hex colours are sRGB automatically), `BatchedMesh` (many different meshes in one draw call), better PMREM, AgX and Neutral tone mapping, physical light units, improved `MeshPhysicalMaterial` (clear coat for car paint, sheen, transmission for glass), `CSM`-style cascaded shadows in the addons, and many fixes. It also removes the reliance on cdnjs carrying the version (cdnjs is blocked in the cloud tests anyway).

Steps:

1. **Vendor Three.js** (a pinned current release) into `assets/lib/three.module.min.js`, with the addons the game uses (GLTFLoader, SkeletonUtils, KTX2Loader, BufferGeometryUtils), and load it with an import map. No build step, the game still runs from GitHub Pages and a plain `http.server`.
2. **Port the breaking changes** in one go: `outputEncoding` → `outputColorSpace`; `texture.encoding` → `texture.colorSpace`; light intensities (physically correct lighting is default; multiply old intensities by π as the starting point); `#include <encodings_fragment>` → `<colorspace_fragment>` in the sky shader (the known trap from the graphics memory: without it PMREM goes black); `onBeforeCompile` hooks for wind, snow and wet roads need the new shader chunk names; WebGL 1 support is gone (WebGL 2 is available on every phone from the last 7 years).
3. **Re-test everything** with the Phase 0 shots: the look should match the Phase 1 result within a small tolerance before any new feature is added.

Cost: a heavy refactor, but no runtime cost; usually a few percent faster.

**Done when:** all shots match the Phase 1 sheet, all gameplay features work (cars, buses, police, kermis rides, lift, achievements), and the game loads on Ron's phone.

---

### Phase 3: Dutch streets at kerb height

**Goal:** make the streets read as Dutch streets from one glance: klinkers, kerbs, red cycle paths, shark-teeth, bollards.

Steps:

1. **Surface from OSM.** Add `surface` to the road export in `tools/convert.py` and to the binary format. Draw `paving_stones` car streets with the klinker material (most residential streets), `asphalt` with asphalt, `concrete:plates` with concrete slabs. Keep the brown klinkers on the De Deel car park as today.
2. **Raised pavements and kerbs.** Pavement polygons and footways beside car streets go up to +0.12 m, with a kerb stone along the edge (a short extruded profile with a bevel, light concrete, instanced per 1 m piece or merged per tile). Where OSM has `barrier=kerb` nodes (743 in the centre) with `kerb=lowered/flush`, the kerb drops to road level, which is where crossings and driveways are. Cars and the player get a small step up/down (the physics already handles height for bridges).
3. **Gutters and drains.** A darker, slightly wet band of 30 cm along kerbs (a decal strip with its own roughness), drain gratings every ~25 m, manhole covers in the middle of streets (instanced decals).
4. **Road markings from OSM:**
   - Shark-teeth (*haaientanden*) at every `highway=give_way` (85 in the centre), facing the approach.
   - Zebra crossings at `highway=crossing` with `crossing=zebra/marked` (62 crossing nodes in the centre).
   - Red cycle lanes on streets tagged `cycleway=lane` (24 in the centre) and dashed edge lines.
   - Stop lines at the 28 traffic signals already used by the game.
   - Edge lines and centre lines on the polder roads and the A6 (dashed 3-9 pattern, as on Dutch roads).
5. **Street furniture from OSM, instanced:** `barrier=bollard` (483 in the centre), `amenity=waste_basket` (35), `man_made=street_cabinet` (21), `barrier=block` (31), `man_made=planter` and `barrier=planter`, `barrier=hedge` lines (39), `barrier=fence` and `barrier=wall`, `barrier=guard_rail` (8). All are cheap boxes/cylinders, instanced per tile.
6. **Detail textures.** Klinker and asphalt get a second, larger-scale detail map (stains, oil spots under parking spaces, tyre wear in the driving lanes) so large areas don't show a repeating pattern. Same trick for grass.
7. **Parking spaces**: `amenity=parking_space` areas (465 in the centre) get white bay lines.

Cost: kerbs and markings are one merged mesh per tile (+2 to 4 draw calls per near tile); furniture +5 instanced draw calls per tile. Triangles +100 to 200 k in the centre. Fits Medium.

**Done when:** the Emmelhage and Lange Nering shots show klinker streets, raised pavements and kerb shadows, and draw calls on the phone start view stay within budget.

---

### Phase 4: Roads and water in 3D (A6 viaducts, sunken canals)

**Goal:** fix the known "A6 is flat" problem and give the town its few but important height differences.

Emmeloord detail (from OSM, see appendix for ids):

- The **A6** runs north-south about 1.4 to 1.5 km east of the Poldertoren (game x ≈ 1,400 to 1,500).
- It crosses **over** the **Zwolse Vaart** on a bridge at about (1,436, 237), over the **Marknesserweg** and its cycle path at about (1,423, -92), and over the **Kamperweg** at about (1,455, 719).
- The **Muntweg (N351)** crosses **over** the A6 near the north edge, at about (1,343, -1,720), with on and off ramps (`motorway_link`).
- At the south end, the **Viaduct Vogelbek** (about 1,647, 2,043) carries the A6 over the N50 junction.
- The **Kamperbrug** at about (1,320, 240) is a movable bridge over the Zwolse Vaart for the Kamperweg and its cycle path.
- The canals that meet in Emmeloord (Lemstervaart, Zwolse Vaart, Urkervaart, Espelervaart, Marknesservaart) are drawn at ground level today.

Steps:

1. **Height along roads.** Give every road vertex a height: 0 by default; for ways with `bridge=*` and `layer=1`, the deck height (6.0 m for motorway over road, 5.5 m over canals, from Dutch clearance rules); approaches ramp up at 4 % (motorways) or 5 % (local roads), following the connected ways in the road graph (`GNODES`/`GEDGES`). Export this in `convert.py` as a height per point.
2. **Embankments.** Ramps sit on earth embankments (talud) with grass slopes of 1:2, built as a strip mesh on both sides of the ramp. OSM `man_made=embankment` lines near the A6 are used where they exist.
3. **Bridge decks and supports.** Concrete deck with edge beams, guard rails and lamp posts on the A6; round or wall-type piers under the deck every ~20 m; abutments where the ramp meets the deck. Shapes are standard Dutch viaduct types; **needs Ron's photos** for the exact look of the Zwolse Vaart bridge and the Kamperbrug.
4. **Physics.** `groundY(x, z, layer)` replaces "y = 0" for cars, buses, the player, AI traffic and the GPS. At crossings the layer from OSM decides whether you are on the deck or under it. Camera collision also checks the deck underside.
5. **Sunken canals.** Water surface 1.2 to 1.5 m below the bank, with a sloped or sheet-piled bank (*damwand*) in the centre and grass slopes outside. The ground mesh around water polygons gets a skirt down to the water level. Bridges over canals in town (the ones already marked `bridge=yes`, e.g. Nagelerweg, Europalaan, Urkerweg) get a small rise.
6. **Extend the A6.** Today the motorway stops at the map edge; extend it past the edge for a few hundred metres and fade it into the fog so it does not end in a wall.

Cost: some hundred extra triangles per bridge, one merged mesh per tile; physics lookups use the existing segment grid. Medium-safe.

**Done when:** you can drive up the ramp, over the A6 viaduct at the Zwolse Vaart, look down at the water, and drive under the Muntweg overpass; canals sit below their banks.

---

### Phase 5: Buildings with real heights, roofs and eras

**Goal:** buildings that have the right size and shape, and the right style for when they were built.

Emmeloord detail:

- OSM gives a `start_date` for most buildings (from the Dutch BAG register). In the centre: **471 from the 1940s, 417 from the 1950s, 298 from the 1960s**, 99 from the 1970s, then far fewer. Emmeloord is a rebuilding-era town, and the plan should show that.
- OSM has almost no heights or roof shapes (see section 3). The Dutch **3D BAG** (3dbag.nl, open data from TU Delft, built from the national laser scan AHN) has a measured height and roof shape for every building in the Netherlands. This is the right source; it is **blocked by the cloud network policy right now** (see section 8).

Steps:

1. **Real heights and roofs (3D BAG).** Add a preprocessing step `tools/bag3d.py` that downloads the 3D BAG tiles for the town once, matches each building to the OSM footprint by BAG id (OSM `ref:bag`) or by overlap, and stores: eave height, ridge height, roof type (flat, single slope, gable, hipped) and ridge direction. The game uses these instead of the guesses. The 3D BAG LoD 2.2 also has actual roof surfaces; for near tiles those can be used directly (more triangles, still fine per tile).
2. **Era styles from `start_date`,** each matched to photos before it is used (**needs Ron's photos per era**; the list below is what to photograph, not what to assume):
   - 1943 to 1960 rebuilding-era terraces and semi-detached houses.
   - 1960s and 1970s flats and terraces.
   - 1980s and 1990s housing.
   - 2000s and later (newer neighbourhoods, e.g. the larger numbers of 2000s buildings).
   Each style is a facade atlas (2 × 2 cells as today, so neighbours differ), a roof material, window proportions and frame colour.
3. **Depth on facades.** Near buildings (≤ 60 m) get real window reveals: windows set 10 to 12 cm into the wall, with sills and lintels as geometry, so the sun casts small shadows on the facade. Mid distance uses parallax occlusion mapping on the existing atlas; far uses the flat atlas.
4. **Interior mapping** for windows: a small shader trick that shows a fake room behind each window (a 2 × 2 atlas of room images: living room, kitchen, office, shop), different per window, with parallax as you move. Big realism win at night and in shopping streets; one texture, no extra draw calls.
5. **Roof detail:** gutters and downpipes, chimneys and ventilation pipes (ventilation is common on post-war houses), dormers where the 3D BAG roof surface shows them, ridge tiles. Roof colours by era; **needs photos** (red and black pantiles both exist; which street has which is not known).
6. **Better far LOD:** the far version keeps the roof shape and two colours (wall and roof) instead of one block, so the view from the Poldertoren gallery shows a town of roofs. One draw call per tile as today.
7. **Shop fronts on the Lange Nering, Korte Nering and De Deel**: real shop names from OSM (already in `EMM_DATA.shops`) on signs, glass shop windows with interior mapping. Shop logos are left out (no brand imitation).

Cost: real heights and roofs cost nothing at runtime. Window reveals +30 to 60 % triangles on near buildings only; interior mapping is a shader cost on window pixels. Medium gets reveals within 40 m and no parallax; High gets everything.

**Done when:** an Emmelhage street, a 1960s street and the centre each look like their photos, and building heights match 3D BAG.

---

### Phase 6: Trees, hedges and grass

**Goal:** vegetation that looks like the green, leafy Emmeloord streets in the drone video.

Emmeloord detail: OSM has 1,060 trees in the centre alone, all `leaf_type=broadleaved`, and no species. The municipality may publish a tree register (*bomenregister*) with species; if it exists and is open data, species can be used per tree. Until then trees stay generic broadleaved types, as today.

Steps:

1. **Trunk and bark colour** fixed with Phase 1 (dark grey-brown, not pale grey), bark normal map.
2. **Better crowns near the camera:** a few real 3D tree models (CC0 or made in Blender, about 3 to 5 k triangles with leaf cards) for the nearest 60 m, three or four shapes (round street tree, columnar, poplar for the polder rows, young tree). Leaf cards get translucency (light through leaves when looking towards the sun) and a darker inner crown.
3. **Impostors for far trees:** each tree type rendered from 8 angles into an atlas (octahedral impostor); far trees are one quad each, lit with a baked normal map. This replaces the "simpler crowns beyond 320 m" and lets trees be visible much further (the polder tree rows on the horizon matter for the look).
4. **Hedges** from OSM `barrier=hedge` (39 in the centre) as boxes with a leafy texture and normal map; private gardens get low hedges or fences only where OSM has them.
5. **Grass:** near the camera (≤ 25 m) a field of instanced grass blades or shells that sway with the existing `WIND`; mid distance a detail texture with colour variation (mown verges are uniform, park lawns and ditch sides are patchy); flowerbeds from OSM `landuse=flowerbed`.
6. **Ditches (*sloten*)** along the polder roads and field edges, where OSM has `waterway=ditch/drain` (the Munttocht and Onderduikerstocht run near the A6, for example): a narrow sunken strip of dark water with reeds.

Cost: near 3D trees are instanced per type (4 to 8 draw calls), impostors one draw call per chunk; grass blades only on Medium within 15 m and on High within 30 m.

**Done when:** a residential street with street trees and the polder edge look like the drone video stills.

---

### Phase 7: Shadows, ambient occlusion and night light

**Goal:** objects that sit on the ground, crisp shadows near the camera, and nights lit by the real street lamps.

Steps:

1. **Cascaded shadow maps:** 2 cascades on Medium (near 40 m at 1024, far 200 m at 1024), 3 on High (25 / 100 / 400 m at 2048). Near shadows go from about 9 cm per texel to about 4 cm; distant buildings finally cast shadows on each other. Cascades update in turns (near every frame, far every 2 to 4 frames) to save time.
2. **Baked ambient occlusion** in the geometry, at no runtime cost: darkening at wall bases, under eaves, in window reveals, under the car body and around tree trunks, as vertex colours or a small AO channel in the facade atlas. This gives Medium most of what SSAO gives High.
3. **Better screen-space AO on High:** ground-truth AO (GTAO) at half resolution with a temporal filter, replacing the current 12-sample SSAO.
4. **Contact shadows** under cars, buses and people (blob shadows exist for cars; extend them and fade them with the sun).
5. **Night light:** the 7,400 OSM street lamps keep their glow and light pools; in addition the 8 to 16 lamps nearest the camera become real point/spot lights (clustered so they cost little), so cars, people and facades are actually lit by them. Lit windows get variation per room and turn on and off over the evening; shop windows on the Lange Nering stay lit until closing time.
6. **Headlights** cast light on the road and the facades for the player's car (exists) and, on High, for the nearest few AI cars.
7. **Light from the sky at dusk:** the IBL already follows the sky; add a blue-hour ambient tint and a short, warm low sun on facades facing west.

Cost: cascades are the main cost (Medium: one more 1024 shadow pass, about 1.5 to 3 ms on a phone). Baked AO is free. Clustered lights only on High; Medium keeps glows and pools.

**Done when:** at noon on De Deel the shadows of the market stalls and benches are crisp, and at night the Lange Nering is lit by its lamps and shop windows.

---

### Phase 8: Water, rain and wet streets

**Goal:** canals that reflect the town, and rain that really changes the streets.

Steps:

1. **Water shader:** physically based water (Fresnel, sky reflection from the IBL, depth-tinted colour, small wind ripples that follow `WIND`), replacing the Phong plane.
2. **Planar reflection on High** for the canal nearest the camera (one extra render of the nearby scene at quarter resolution, only when water is in view); screen-space reflections as a cheaper option for Medium.
3. **Rain on water:** expanding ripple rings (a ripple normal texture animated in the shader).
4. **Wet streets 2.0:** today rain makes streets darker and glossier everywhere. Add a puddle mask (low spots along kerbs and in klinker hollows, from a noise texture plus the gutter strip of Phase 3) where reflection is mirror-like, and a drying phase after the shower when puddles stay longest.
5. **Spray and splashes:** cars throw up spray from the wheels (exists for some lights); add drops hitting the ground as small splashes near the camera.
6. **Snow 2.0:** snow on roof slopes and car roofs, tyre tracks, cleared roads and white verges (snow already settles on grass and roofs).

Cost: water shader is cheap; planar reflection is High only and costs about 20 to 30 % of a frame when visible, so it is limited to the canal within 80 m.

**Done when:** the Zwolse Vaart and the canals in the centre mirror the houses and trees on calm days, and a shower turns the centre into wet, reflective klinkers.

---

### Phase 9: Cars, buses and people up close

**Goal:** vehicles and people that hold up when the camera is close (third person, car chase, bench sitters).

Steps:

1. **Car paint** with a clear coat (`MeshPhysicalMaterial` after Phase 2), metallic flakes, dirt on the lower doors; glass that shows a dark interior with seats and a steering wheel instead of plain tint.
2. **Better car shapes:** the extruded bodies stay for far cars; near cars (≤ 40 m) get a smoother body with wheel arches, light units as separate glass, and real tyres with sidewall text normal map. CC0 car models were tried and looked toy-like (`IMPROVEMENTS.md`); this time the near model is made to match the current proportions, generic and without brand logos.
3. **Buses:** the real liveries of the bus lines in Emmeloord (lines 71, 77, 146, 315 already follow their OSM routes); livery colours **need Ron's photos** of a bus at the bus station.
4. **People:** more variety (several CC0 rigged bodies, men, women, children, elderly), clothes with fabric normal maps, hair; people beyond 70 m become impostor sprites with a walk cycle (one draw call for all far people).
5. **Bikes**: Dutch city bikes (*omafiets*) with mudguards, chain guard, carrier and lights, for parked bikes (already merged) and cyclists.

Cost: near-only detail, swapped by distance like the existing car LOD (`carLOD` in `syncCar`). People impostors save draw calls (~65 people in busy views today).

**Done when:** a close-up of the player's car and a cyclist passing at the Kettingplein look natural in the shot sheet.

---

### Phase 10: Camera, post-processing and the far horizon

**Goal:** a filmic final image and a horizon that feels endless.

Steps:

1. **Temporal anti-aliasing (TAA)** on High instead of FXAA: removes shimmer on lamp posts, railings, branches and window frames. Medium gets a better FXAA in the single combined pass.
2. **Colour grading with a lookup table (LUT)** matched to the drone video: the video frames and game frames of the same spots are compared and a 32³ LUT is made, so the colours of the game match the real footage.
3. **Motion blur** (per-object, light) at high speed in a car, and **depth of field** in the Poldertoren lift and the gallery (sharp town, soft foreground railing).
4. **Aerial perspective:** distance haze tinted by the sky (blue on clear days, white-grey in mist) instead of plain fog, plus **height fog** in the morning mist that lies in the polder and leaves the Poldertoren top in the sun.
5. **The far horizon:** beyond the map edge, a low ring of impostor farm yards, tree rows and wind turbines at their **real OSM positions** (`generator:source=wind`; today the turbine rows are placed in invented rows just outside town, which should be replaced by the OSM positions). Flat fields with crop strips matching the season (tulips in spring).
6. **Clouds:** the photo skies stay; add volumetric-looking cloud shadows moving over the town and polder (a scrolling shadow texture on the ground and buildings), which is very typical of Dutch skies.
7. **Sun glare and lens:** a subtle sun glare when looking towards the sun, light shafts through tree crowns on High.

Cost: TAA and grading are part of the High post chain (≈ 2 to 3 ms on integrated graphics). Cloud shadows are a texture lookup in every material. Horizon impostors one or two draw calls.

**Done when:** the gallery shot from the Poldertoren looks like a frame from "Emmeloord van Boven".

---

## 7. Order and schedule

The improvement runs (01:17 and 06:45 daily, 11:52 Mon to Fri) can each take one step. A step is shipped to `main` and logged in `IMPROVEMENTS.md` as usual.

| Order | Phase | Runs (estimate) | Why this order |
| --- | --- | --- | --- |
| 1 | Phase 0: measuring stick | 1 | Everything after it is checked with it. |
| 2 | Phase 1: colour and light | 2 | Fixes the washed-out look, biggest gain for least work. |
| 3 | Phase 2: engine upgrade | 2 to 3 | Unlocks colour management, BatchedMesh, physical materials, better shadows. Do it before adding new shaders, so they are written once. |
| 4 | Phase 3: streets and kerbs | 3 | The ground is most of every screenshot. |
| 5 | Phase 4: A6 and canals in 3D | 3 | Known open issue; needs the road height work. |
| 6 | Phase 7: shadows and AO | 2 | Cascades and baked AO make everything from phases 3 and 4 sit right. |
| 7 | Phase 5: buildings | 4 to 6 | Biggest step; real heights depend on 3D BAG access, era styles on photos. |
| 8 | Phase 6: trees and grass | 3 | |
| 9 | Phase 8: water and rain | 2 | |
| 10 | Phase 9: vehicles and people | 3 | |
| 11 | Phase 10: post and horizon | 2 to 3 | Final polish; LUT is made last, on top of everything else. |

That is roughly 27 to 33 runs, about two to three weeks at the current pace. Ron's photo requests (section 8) can be handled whenever they arrive; phases that need them can start with the parts that don't.

---

## 8. What is needed from Ron

1. **Photos** (phone photos are fine), ideally on a sunny day and some in rain:
   - A residential street from the 1940s/50s (e.g. in Emmelhage), one from the 1960s/70s, and one from the 2000s.
   - The Zwolse Vaart bridge of the A6 and the Kamperbrug; the Muntweg overpass.
   - A canal bank in the centre (to see if it has sheet piling or a grass slope).
   - A bus at the bus station (livery).
   - Close-ups of a kerb, a klinker street, a red cycle path.
2. **Network access** for the cloud environment, so the preprocessing tools can fetch open data (the game itself will not need these at runtime):
   - `3dbag.nl` and `api.3dbag.nl` (building heights and roof shapes), currently refused by the proxy.
   - Optionally the municipality's open data portal, if it publishes a tree register.
3. **Okay on the engine upgrade (Phase 2).** It is a big change under the hood; nothing changes for the player if it goes well, but it touches every part of the game.

---

## 9. Risks

| Risk | What could happen | Mitigation |
| --- | --- | --- |
| Engine upgrade breaks things | Shaders (sky, wind, snow, wet roads) or GLTF characters stop working | Do it in one focused step with the Phase 0 sheet as the test; keep the r128 version on a tag to roll back. |
| Phones get slower | Frame rate drops on Medium | Every feature has a flag; budgets in section 5 are checked by the bench script; auto step-down turns off the most expensive flags first. |
| Download gets too big | Slow first load on 4G | KTX2 textures; lazy loading for High-only assets after the game starts; models in GLB with mesh compression decoded by a vendored decoder. |
| Colour change alters the whole look | Ron prefers the old colours | Phase 1 is shown with before/after sheets before moving on; colours checked against his photos. |
| Real-world detail is wrong | A bridge or style that doesn't match reality | OSM for positions, photos for looks, nothing guessed; open questions go to Ron. |
| 3D BAG stays blocked | Heights remain guesses | Fallback: estimate heights from `start_date` era and building type, but mark them as estimates in the code and the log. |
| Physics on bridges | Cars falling through ramps or snagging on kerbs | `groundY` with layer from OSM, smoothing at joints, tests driving every bridge in the bench script. |

---

## 10. Appendix: OpenStreetMap facts used in this plan

Fetched on 2026-11-21 from the OpenStreetMap API (© OpenStreetMap contributors, ODbL). Game coordinates use the existing convention: origin at the Poldertoren (52.709931 N, 5.750939 E), x is metres east, z is metres south (north is -z).

**Centre area (bounding box 5.742 to 5.756 E, 52.706 to 52.714 N):**

- 1,625 buildings: 830 `house`, 656 `yes`, 31 `retail`, 31 `commercial`, 29 `industrial`, 25 `apartments`.
- Heights: 3 with `height` (the Poldertoren 43.4 m platform, 6.6 m, 10 m); 11 with `building:levels`; 2 with `roof:shape` (both flat).
- Build years (`start_date`): 1940s 471, 1950s 417, 1960s 298, 1970s 99, 1980s 85, 1990s 33, 2000s 139, 2010s 38, 2020s 36. Most common single years: 1943 (155), 1955 (116), 1947 (114), 1953 (98), 1963 (93).
- Street surfaces: residential streets 168 `paving_stones` / 16 `asphalt`; unclassified 125 / 62; tertiary and secondary all asphalt; service roads 253 `paving_stones` / 27 `asphalt`; footways 1,087 `paving_stones`; cycleways 159 `asphalt` / 68 `paving_stones`.
- Street furniture nodes: 1,060 trees (all `leaf_type=broadleaved`), 743 `barrier=kerb`, 691 street lamps, 483 bollards, 85 give-way, 62 crossings, 35 waste baskets, 32 benches, 31 blocks, 28 traffic signals, 21 street cabinets, 13 flagpoles, 11 bus stops, 6 fountains, 5 artworks (De Leeuwen).
- Lines and areas: 465 `amenity=parking_space`, 39 hedges, 33 fences, 23 walls, 8 guard rails, 15 planters, 154 `landuse=grass`, 24 `cycleway=lane` streets.
- Poldertoren: OSM way 266435887, `man_made=water_tower`, `tower:type=bell_tower`, `start_date=1957`, `height=43.4`. Polderfontein: way 902694671, marble, Johan Verhage, 2020.
- Canals in the centre: Urkervaart, Espelervaart.
- Bridges in the centre (`bridge=yes`): Nagelerweg, Europalaan, Nagelerstraat, Urkerweg, Rietstraat, Nagelerbrug (cycleway), Rijnstraat (cycleway), and several foot and cycle bridges.

**A6 corridor (5.768 to 5.778 E, 52.683 to 52.732 N):**

| Crossing | Game position (x, z) | What crosses what | OSM ways |
| --- | --- | --- | --- |
| Zwolse Vaart | (1,436, 237) | A6 on a bridge over the canal | 6518719, 6518722 (`bridge=yes`, `layer=1`) |
| Marknesserweg | (1,423, -92) | A6 on a bridge over the road and its cycle path | 6518728, 6518975 |
| Kamperweg | (1,455, 719) | A6 on a bridge over the road and cycle path | 6518724, 6518732 |
| Muntweg (N351) | (1,343, -1,720) | Muntweg on a bridge over the A6, with ramps | 6518961, 6518965, 601089904 to 601089915, 601791999 to 601792001; cycle bridges 47228507, 47228527 |
| Viaduct Vogelbek | (1,647, 2,043) | A6 and a ramp over the N50 junction | 6518706, 6518704, 984889695 |
| Kamperbrug | (1,320, 240) | Kamperweg and cycle path over the Zwolse Vaart, movable bridge | 727241727, 727241728, 727241731 |

Other: the Lemstervaart and Zwolse Vaart canals, the Munttocht and Onderduikerstocht drains, `man_made=embankment` lines beside the A6.
