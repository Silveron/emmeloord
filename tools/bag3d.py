"""Download measured building heights and roof shapes from the 3D BAG (3dbag.nl, TU Delft, CC BY 4.0)
for the game region and boil them down to a few numbers per building (graphics plan, phase 5).

Usage: REGION=-2150,2950,-2400,2950 python3 tools/bag3d.py [out.json]
Writes {bag id: [ground, eave, ridge, h70, roof type, ridge angle, year]} with heights in metres above the
ground (maaiveld), ridge angle in degrees in game coordinates (x east, z south), roof type
0 flat, 1 slanted, 2 mixed/other. convert.py matches buildings by the OSM ref:bag tag.

The 3D BAG API answers at most ~50 buildings per bbox query and its paging is unreliable, so the region
is split into squares and any square with more buildings than returned is split again."""
import json, math, os, sys, urllib.request, concurrent.futures as cf
from pyproj import Transformer

LAT0, LON0 = 52.70996, 5.75090
ky = 111320.0; kx = 111320.0 * math.cos(math.radians(LAT0))
TX, TZ = 3.44, 3.35
RX0, RX1, RZ0, RZ1 = map(int, os.environ.get('REGION', '-2150,2950,-2400,2950').split(','))
OUT = sys.argv[1] if len(sys.argv) > 1 else '/home/user/osm2/bag3d.json'
to_rd = Transformer.from_crs(4326, 28992, always_xy=True)
to_ll = Transformer.from_crs(28992, 4326, always_xy=True)

def game_to_rd(x, z):
    lon = (x + TX) / kx + LON0; lat = LAT0 - (z + TZ) / ky
    return to_rd.transform(lon, lat)

def rd_to_game(X, Y):
    lon, lat = to_ll.transform(X, Y)
    return ((lon - LON0) * kx - TX, -(lat - LAT0) * ky - TZ)

# game-space angle of the RD north axis (the two grids differ by about 1.5 degrees here)
_a, _b = rd_to_game(*game_to_rd(0, 0)), rd_to_game(*(lambda p: (p[0], p[1] + 100))(game_to_rd(0, 0)))
ROT = math.atan2(_b[1] - _a[1], _b[0] - _a[0]) + math.pi / 2   # rotation RD -> game (game z points south)

def fetch(x0, y0, x1, y1):
    url = f'https://api.3dbag.nl/collections/pand/items?bbox={x0:.1f},{y0:.1f},{x1:.1f},{y1:.1f}&limit=50'
    for t in range(4):
        try:
            with urllib.request.urlopen(url, timeout=90) as r: return json.load(r)
        except Exception as e:
            err = e
    raise err

def newell(ring, V):
    nx = ny = nz = 0.0
    for i in range(len(ring)):
        a, b = V[ring[i]], V[ring[(i + 1) % len(ring)]]
        nx += (a[1] - b[1]) * (a[2] + b[2]); ny += (a[2] - b[2]) * (a[0] + b[0]); nz += (a[0] - b[0]) * (a[1] + b[1])
    return nx / 2, ny / 2, nz / 2

def summarise(feat, sc, tr):
    V = [(v[0] * sc[0] + tr[0], v[1] * sc[1] + tr[1], v[2] * sc[2] + tr[2]) for v in feat['vertices']]
    out = {}
    for oid, o in feat['CityObjects'].items():
        if o.get('type') != 'Building': continue
        A = o['attributes']
        g = A.get('b3_h_maaiveld')
        if g is None or A.get('b3_h_dak_70p') is None: continue
        h70 = A['b3_h_dak_70p'] - g
        typ = {'horizontal': 0, 'multiple horizontal': 0, 'slanted': 1}.get(A.get('b3_dak_type'), 2)
        eave, ridge, ang = h70, h70, None
        # roof faces of the LoD 2.2 solid: ridge direction and eave/ridge height of the main (largest) slanted faces
        part = feat['CityObjects'].get(oid + '-0')
        if part:
            geo = [gg for gg in part.get('geometry', []) if gg['lod'] == '2.2']
            if geo:
                gg = geo[0]; sem = gg['semantics']; vals = sem['values'][0]
                c2 = s2 = 0.0; slanted = []
                for fi, face in enumerate(gg['boundaries'][0]):
                    if sem['surfaces'][vals[fi]]['type'] != 'RoofSurface': continue
                    ring = face[0]; nx, ny, nz = newell(ring, V); ar = math.sqrt(nx * nx + ny * ny + nz * nz)
                    if ar < 1: continue
                    hz = math.hypot(nx, ny) / ar
                    if hz < 0.17: continue   # flatter than about 10 degrees
                    th = math.atan2(ny, nx); c2 += math.cos(2 * th) * ar; s2 += math.sin(2 * th) * ar
                    zs = [V[i][2] for i in ring]; slanted.append((ar, min(zs) - g, max(zs) - g))
                if slanted and math.hypot(c2, s2) > 0:
                    slope_dir = math.atan2(s2, c2) / 2          # RD angle of the main downhill direction (mod 180)
                    ridge_rd = slope_dir + math.pi / 2
                    # RD (x east, y north) -> game (x east, z south): mirror y, then grid rotation
                    ang = math.degrees(ROT - ridge_rd) % 180
                    slanted.sort(reverse=True); tot = sum(s[0] for s in slanted)
                    big = [s for s in slanted if s[0] > 0.15 * tot] or slanted[:1]
                    eave = sorted(s[1] for s in big)[len(big) // 2]; ridge = max(s[2] for s in big)
        out[oid.split('.')[-1]] = [round(g, 2), round(eave, 2), round(ridge, 2), round(h70, 2), typ,
                                   None if ang is None else round(ang, 1), A.get('oorspronkelijkbouwjaar')]
    return out

def square(x0, y0, x1, y1, depth=0):
    d = fetch(x0, y0, x1, y1)
    res = {}
    tr = d.get('metadata', {}).get('transform', {})
    for f in d['features']: res.update(summarise(f, tr['scale'], tr['translate']))
    # numberMatched also counts each building's child part, so it is twice the number of buildings
    if d.get('numberReturned', 0) < d.get('numberMatched', 0) // 2 and depth < 7:
        mx, my = (x0 + x1) / 2, (y0 + y1) / 2
        return res, [(x0, y0, mx, my, depth + 1), (mx, y0, x1, my, depth + 1), (x0, my, mx, y1, depth + 1), (mx, my, x1, y1, depth + 1)]
    return res, []

corners = [game_to_rd(x, z) for x in (RX0, RX1) for z in (RZ0, RZ1)]
X0, X1 = min(c[0] for c in corners), max(c[0] for c in corners)
Y0, Y1 = min(c[1] for c in corners), max(c[1] for c in corners)
todo = [(x, y, min(x + 500, X1), min(y + 500, Y1), 0) for x in [X0 + i * 500 for i in range(int((X1 - X0) // 500) + 1)]
        for y in [Y0 + j * 500 for j in range(int((Y1 - Y0) // 500) + 1)]]
allb = {}; n = 0
with cf.ThreadPoolExecutor(8) as ex:
    while todo:
        futs = [ex.submit(square, *t[:4], t[4]) for t in todo]; todo = []
        for f in futs:
            r, more = f.result(); allb.update(r); todo += more; n += 1
        print(n, 'queries,', len(allb), 'buildings', file=sys.stderr)
json.dump(allb, open(OUT, 'w'), separators=(',', ':'))
print(len(allb), 'buildings ->', OUT)
