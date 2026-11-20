# Asset credits

The textures and skies in this folder come from [Poly Haven](https://polyhaven.com) and are **CC0** (public domain). They were resized and colour-adjusted for the game.

| File | Source |
|---|---|
| sky_day.jpg | kloofendal_48d_partly_cloudy_puresky (Greg Zaal / Jarod Guest) |
| sky_dusk.jpg | belfast_sunset_puresky |
| sky_overcast.jpg | kloofendal_overcast_puresky |
| brick_red*.jpg | red_brick_03 |
| brick_dark*.jpg | dark_brick_wall |
| brick_buff*.jpg | brick_wall_08 (tinted yellow) |
| klinker*.jpg | herringbone_brick |
| asphalt.jpg, asphalt_n.jpg | clean_asphalt |
| pavement*.jpg | concrete_pavement_02 |
| roof*.jpg | clay_roof_tiles_03 (desaturated so roofs can be tinted) |
| grass*.jpg | leafy_grass (recoloured greener) |

## Characters (`models/`)

Both are **CC0** by [Quaternius](https://quaternius.com), taken from the CC0 copies in the `@netforge/asset-library-files` npm package. They were cut down to the animations the game uses (idle, walk, run, sit, wave), the backpack was removed from the adventurer, and mesh compression was removed so three.js r128 can load them without a decoder.

| File | Source |
|---|---|
| models/people.glb | "Man" (worker) from the Ultimate Animated Character pack, recoloured per pedestrian in code |
| models/hero.glb | "Adventurer" from the Ultimate Modular Men pack, recoloured orange in code |

## Code (`lib/`)

`GLTFLoader.js` and `SkeletonUtils.js` are the MIT-licensed three.js r128 example files (`examples/js/`).
