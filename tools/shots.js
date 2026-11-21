// Fixed screenshot spots + draw-call numbers (graphics plan, phase 0).
// Usage: node tools/shots.js <outdir> [quality 0|1|2] [label]
//   serves the repo on :8123 (Three.js is vendored in assets/lib, so no network is needed).
// Writes <outdir>/<label>-<spot>.png and <outdir>/<label>.json with draw calls and triangles per spot.
const { chromium } = require('playwright');
const http = require('http'), fs = require('fs'), path = require('path');
const ROOT = path.resolve(__dirname, '..');
const OUT = path.resolve(process.argv[2] || 'shots');
const Q = +(process.argv[3] ?? 1), LABEL = process.argv[4] || 'q' + Q;
fs.mkdirSync(OUT, { recursive: true });

// spots: real places; positions from the game's OSM data (named roads / places) or OSM coordinates (see docs/GRAPHICS_PLAN.md)
const SPOTS = [
  { id: 'deel', at: [48, -66], look: [0, 0], time: 12 },
  { id: 'langenering', road: 'Lange Nering', time: 12 },
  { id: 'emmelhage', place: 'Emmelhage', time: 12 },
  { id: 'kettingplein', at: [500, -168], look: [440, -168], time: 12 },
  { id: 'garage', at: [238, 22], look: [240, 50], time: 12 },
  { id: 'a6-zwolsevaart', at: [1345, 252], look: [1436, 237], time: 12 },
  { id: 'deel-dusk', start: true, look: [0, 0], time: 19.6 },
  { id: 'deel-night', start: true, look: [0, 0], time: 22.5 },
  { id: 'deel-rain', start: true, look: [0, 0], time: 14, rain: 1 },
];

const mime = { '.html': 'text/html', '.js': 'text/javascript', '.jpg': 'image/jpeg', '.png': 'image/png', '.glb': 'model/gltf-binary', '.mp3': 'audio/mpeg', '.json': 'application/json' };
const srv = http.createServer((q, r) => {
  const p = path.join(ROOT, decodeURIComponent(q.url.split('?')[0]).replace(/^\/$/, '/index.html'));
  if (!p.startsWith(ROOT) || !fs.existsSync(p)) { r.writeHead(404); return r.end(); }
  r.writeHead(200, { 'content-type': mime[path.extname(p)] || 'application/octet-stream' }); fs.createReadStream(p).pipe(r);
}).listen(8123);

(async () => {
  const b = await chromium.launch({ args: ['--use-angle=swiftshader', '--enable-unsafe-swiftshader', '--ignore-gpu-blocklist'] });
  const pg = await b.newPage({ viewport: { width: 1280, height: 720 } });
  if (process.env.THREE_JS) await pg.route('**/three.min.js', r => r.fulfill({ path: process.env.THREE_JS, contentType: 'text/javascript' }));
  await pg.route('**/fonts.googleapis.com/**', r => r.fulfill({ body: '', contentType: 'text/css' }));
  pg.on('pageerror', e => console.log('PAGEERROR', e.message));
  await pg.goto('http://localhost:8123/index.html');
  await pg.waitForFunction(() => window.__game, null, { timeout: 120000 });
  await pg.evaluate(q => { localStorage.clear(); __game.start(); __game.setQuality(q); }, Q);
  await pg.waitForTimeout(8000); // photo textures and characters load in the background
  const res = {};
  for (const s of SPOTS.filter(s => !process.env.SPOTS || process.env.SPOTS.split(',').includes(s.id))) {
    const info = await pg.evaluate(s => {
      const G = __game, D = G.dbg(), P = G.P;
      let x, z, tx, tz;
      if (s.start) { x = G.START.x; z = G.START.z; [tx, tz] = s.look; }
      else if (s.at) { [x, z] = s.at; [tx, tz] = s.look; }
      else if (s.road) {
        const rs = D.ROADS.filter(r => r.n === s.road); const r = rs.sort((a, b) => b.p.length - a.p.length)[0];
        const i = Math.floor((r.p.length - 1) / 2), a = r.p[i], c = r.p[i + 1] || r.p[i - 1];
        x = a[0]; z = a[1]; tx = c[0]; tz = c[1];
      } else if (s.place) {
        const pl = window.EMM_DATA.places.find(p => p[2] === s.place);
        let best = null, bd = 1e9;
        for (const r of D.ROADS) if (r.c === 0 && r.n && r.w < 6) for (let i = 0; i < r.p.length - 1; i++) { const d = Math.hypot(r.p[i][0] - pl[0], r.p[i][1] - pl[1]); if (d < bd) { bd = d; best = [r.p[i], r.p[i + 1]]; } }
        [x, z] = best[0]; [tx, tz] = best[1];
      }
      P.x = x; P.z = z; P.y = 0; P.h = Math.atan2(tx - x, tz - z);
      G.setCam(P.h, 0.2); G.setRain(s.rain || 0); G.setTime(s.time);
      return { x, z };
    }, s);
    await pg.waitForTimeout(3500);
    const st = await pg.evaluate(() => { const r = __game.renderer; r.info.autoReset = false; return new Promise(ok => requestAnimationFrame(() => { r.info.reset(); requestAnimationFrame(() => { const i = r.info.render; const o = { calls: i.calls, tris: i.triangles, tex: r.info.memory.textures, geo: r.info.memory.geometries }; r.info.autoReset = true; ok(o); }); })); });
    await pg.screenshot({ path: path.join(OUT, `${LABEL}-${s.id}.png`) });
    res[s.id] = Object.assign(info, st);
    console.log(s.id, JSON.stringify(res[s.id]));
  }
  fs.writeFileSync(path.join(OUT, LABEL + '.json'), JSON.stringify(res, null, 1));
  await b.close(); srv.close();
})().catch(e => { console.error(e); process.exit(1); });
