"""Convert downloaded OSM tiles of Emmeloord into a compact data blob for the game.
Coordinates: metres, x east, z south, origin = Poldertoren centre."""
import json, math, collections, heapq, sys

d = json.load(open('/home/user/osm2/all.json'))
N, W, R = d['nodes'], d['ways'], d['rels']
LAT0, LON0 = 52.70996, 5.75090
ky = 111320.0; kx = 111320.0 * math.cos(math.radians(LAT0))
# shift so the tower footprint centre is the origin
TX, TZ = 3.44, 3.35
def xy(n):
    lat, lon, _ = N[n]
    return ((lon - LON0) * kx - TX, -(lat - LAT0) * ky - TZ)

import os
RX0, RX1, RZ0, RZ1 = map(int, os.environ.get('REGION', '-900,920,-760,760').split(','))
def inreg(p, m=0): return RX0 - m <= p[0] <= RX1 + m and RZ0 - m <= p[1] <= RZ1 + m

def clip_seg(a, b):
    x0, z0 = a; x1, z1 = b; dx, dz = x1 - x0, z1 - z0
    t0, t1 = 0.0, 1.0
    for p, q in ((-dx, x0 - RX0), (dx, RX1 - x0), (-dz, z0 - RZ0), (dz, RZ1 - z0)):
        if p == 0:
            if q < 0: return None
        else:
            r = q / p
            if p < 0:
                if r > t1: return None
                t0 = max(t0, r)
            else:
                if r < t0: return None
                t1 = min(t1, r)
    return (x0 + dx * t0, z0 + dz * t0), (x0 + dx * t1, z0 + dz * t1)

def clip_line(pts):
    out = []; cur = []
    for a, b in zip(pts, pts[1:]):
        c = clip_seg(a, b)
        if not c:
            if cur: out.append(cur); cur = []
            continue
        ca, cb = c
        if not cur: cur = [ca]
        elif math.dist(cur[-1], ca) > 1e-6: out.append(cur); cur = [ca]
        cur.append(cb)
        if math.dist(cb, b) > 1e-6: out.append(cur); cur = []
    if cur: out.append(cur)
    return [l for l in out if len(l) >= 2]

def dp(pts, eps):
    if len(pts) < 3: return pts
    a, b = pts[0], pts[-1]
    dx, dz = b[0] - a[0], b[1] - a[1]; L = math.hypot(dx, dz) or 1e-9
    best, bi = -1, 0
    for i in range(1, len(pts) - 1):
        p = pts[i]
        dd = abs((p[0] - a[0]) * dz - (p[1] - a[1]) * dx) / L if L > 1e-9 else math.dist(p, a)
        if dd > best: best, bi = dd, i
    if best > eps: return dp(pts[:bi + 1], eps)[:-1] + dp(pts[bi:], eps)
    return [a, b]

def area(p):
    s = 0
    for i in range(len(p)):
        a, b = p[i], p[(i + 1) % len(p)]; s += a[0] * b[1] - b[0] * a[1]
    return s / 2

def ring(nds):
    pts = [xy(n) for n in nds if n in N]
    if len(pts) > 2 and pts[0] == pts[-1]: pts = pts[:-1]
    return pts

def assemble(ways_list):
    """join open ways (lists of node ids) into closed rings"""
    segs = [list(w) for w in ways_list if len(w) >= 2]
    rings = []
    while segs:
        cur = segs.pop(0)
        changed = True
        while cur[0] != cur[-1] and changed:
            changed = False
            for i, s in enumerate(segs):
                if s[0] == cur[-1]: cur += s[1:]
                elif s[-1] == cur[-1]: cur += s[::-1][1:]
                elif s[-1] == cur[0]: cur = s + cur[1:]
                elif s[0] == cur[0]: cur = s[::-1] + cur[1:]
                else: continue
                segs.pop(i); changed = True; break
        if cur[0] == cur[-1]: rings.append(cur)
    return rings

# ---------------------------------------------------------------- polygons
def polys_of(pred):
    out = []
    for wid, (nds, t) in W.items():
        if pred(t) and len(nds) > 3 and nds[0] == nds[-1]:
            out.append((ring(nds), t, wid))
    for rid, (mem, t) in R.items():
        if t.get('type') == 'multipolygon' and pred(t):
            outers = [W[m[1]][0] for m in mem if m[0] == 'way' and m[2] in ('outer', '') and m[1] in W]
            for r in assemble(outers): out.append((ring(r), t, 'r' + rid))
    return out

def poly_clip_ok(p): return any(inreg(q) for q in p)

def is_water(t): return t.get('natural') == 'water' or t.get('waterway') == 'riverbank' or t.get('landuse') in ('basin', 'reservoir')
GREEN_KEYS = {('landuse', 'grass'): 0, ('leisure', 'park'): 0, ('leisure', 'garden'): 0, ('landuse', 'flowerbed'): 2,
              ('leisure', 'playground'): 0, ('leisure', 'pitch'): 3, ('landuse', 'forest'): 1, ('natural', 'wood'): 1,
              ('natural', 'scrub'): 1, ('natural', 'shrubbery'): 1, ('landuse', 'meadow'): 0, ('landuse', 'recreation_ground'): 0,
              ('landuse', 'cemetery'): 0, ('leisure', 'sports_centre'): 3, ('landuse', 'village_green'): 0, ('landuse', 'farmland'): 4}
def green_kind(t):
    for (k, v), c in GREEN_KEYS.items():
        if t.get(k) == v: return c
    return None
def paved_kind(t):
    if t.get('building'): return None
    if t.get('amenity') == 'parking' and t.get('parking', 'surface') == 'surface': return 1  # asphalt/parking
    if t.get('highway') == 'pedestrian' and t.get('area') == 'yes': return 0
    if t.get('area:highway') in ('pedestrian', 'footway'): return 0
    if t.get('place') == 'square': return 0
    if t.get('public_transport') == 'platform' and t.get('area') == 'yes': return 2
    if t.get('amenity') == 'bus_station' or (t.get('public_transport') == 'station' and t.get('area') == 'yes'): return 1
    if t.get('area:highway') == 'traffic_island': return 2
    if t.get('landuse') in ('retail',) : return None
    return None

def simp_poly(p, eps):
    if len(p) < 4: return p
    q = dp(p + [p[0]], eps)[:-1]
    return q if len(q) >= 3 else p

def enc(pts, s=5):
    """delta-encode points at 1/s metre resolution"""
    o = []; px = pz = 0
    for x, z in pts:
        ix, iz = round(x * s), round(z * s)
        o += [ix - px, iz - pz]; px, pz = ix, iz
    return ','.join(map(str, o))

water = []
for p, t, wid in polys_of(is_water):
    if poly_clip_ok(p) and abs(area(p)) > 30: water.append(enc(simp_poly(p, 0.5)))
green = []
for p, t, wid in polys_of(lambda t: green_kind(t) is not None and 'building' not in t):
    if poly_clip_ok(p) and abs(area(p)) > 20: green.append([green_kind(t), enc(simp_poly(p, 0.4))])
paved = []
for p, t, wid in polys_of(lambda t: paved_kind(t) is not None):
    if poly_clip_ok(p) and abs(area(p)) > 6: paved.append([paved_kind(t), enc(simp_poly(p, 0.3))])

# ---------------------------------------------------------------- buildings
def levels_h(t, kind, a):
    if 'height' in t:
        try: return float(t['height'].split()[0])
        except: pass
    if 'building:levels' in t:
        try: return float(t['building:levels'].split(';')[0]) * 3.0 + 0.6
        except: pass
    return None

edgecount = collections.Counter()
blds = []
for p, t, wid in polys_of(lambda t: 'building' in t and t.get('building') not in ('roof', 'construction', 'static_caravan', 'houseboat')):
    if wid == '266435887': continue  # Poldertoren is modelled by hand
    if not all(inreg(q, 0) for q in p): continue
    a = abs(area(p))
    if a < 16: continue
    k = t.get('building')
    blds.append((p, t, wid, a, k))
    if not wid.startswith('r'):
        nds = W[wid][0]
        for u, v in zip(nds, nds[1:]): edgecount[frozenset((u, v))] += 1

# shops -> which building they are in
shops = []
for nid, (la, lo, t) in N.items():
    if 'shop' in t or t.get('amenity') in ('restaurant', 'cafe', 'fast_food', 'bank', 'pharmacy', 'ice_cream', 'pub'):
        x, z = xy(nid)
        if inreg((x, z)): shops.append((x, z, t.get('shop') or t.get('amenity')))

def pip(x, z, p):
    c = False
    for i in range(len(p)):
        a, b = p[i], p[i - 1]
        if (a[1] > z) != (b[1] > z) and x < (b[0] - a[0]) * (z - a[1]) / (b[1] - a[1] + 1e-12) + a[0]: c = not c
    return c

KIND = {'house': 0, 'terrace': 0, 'detached': 0, 'semidetached_house': 0, 'residential': 0, 'bungalow': 0,
        'apartments': 1, 'dormitory': 1, 'retail': 2, 'commercial': 2, 'office': 2, 'supermarket': 2, 'hotel': 2,
        'industrial': 3, 'warehouse': 3, 'sports_centre': 3, 'service': 4, 'garage': 4, 'garages': 4, 'shed': 4,
        'school': 5, 'civic': 5, 'public': 5, 'church': 6, 'chapel': 6, 'kindergarten': 5, 'college': 5, 'hospital': 5}
bout = []
shopbld = set()
for (x, z, s) in shops:
    for i, (p, t, wid, a, k) in enumerate(blds):
        xs = [q[0] for q in p]; zs = [q[1] for q in p]
        if min(xs) - 1 < x < max(xs) + 1 and min(zs) - 1 < z < max(zs) + 1 and pip(x, z, p): shopbld.add(i); break

centre_d = lambda p: math.hypot(sum(q[0] for q in p) / len(p), sum(q[1] for q in p) / len(p))
for i, (p, t, wid, a, k) in enumerate(blds):
    kind = KIND.get(k)
    dc = centre_d(p)
    if kind is None:  # building=yes
        if a < 45: kind = 4
        elif dc < 450 and a > 120: kind = 2
        elif a > 1200: kind = 3
        else: kind = 0
    h = levels_h(t, kind, a)
    if h is None:
        h = {0: 6.0 if a > 40 else 3.2, 1: 10.5, 2: 7.5 if dc < 500 else 6.5, 3: 7.5, 4: 2.8, 5: 7.5, 6: 11}[kind]
        if kind == 0 and a > 220: h = 7.0
        if kind == 2 and a > 1500: h = 9
    h = round(min(h, 40), 1)
    shop = 1 if (i in shopbld or (kind == 2 and dc < 450)) else 0
    ps = simp_poly(p, 0.25)
    if area(ps) < 0: ps = ps[::-1]   # make winding consistent (positive area)
    # interior walls: edges whose node pair appears in two buildings
    inner = []
    if not wid.startswith('r') and len(ps) == len(p):
        nds = W[wid][0][:-1]
        if area(p) < 0: nds = nds[::-1]
        for j in range(len(nds)):
            if edgecount[frozenset((nds[j], nds[(j + 1) % len(nds)]))] > 1: inner.append(j)
    roof = 0
    if kind == 0 and len(ps) == 4 and a < 600:
        # near-rectangular -> gabled roof
        ang = []
        for j in range(4):
            a1 = ps[j]; b1 = ps[(j + 1) % 4]; c1 = ps[(j + 2) % 4]
            v1 = (b1[0] - a1[0], b1[1] - a1[1]); v2 = (c1[0] - b1[0], c1[1] - b1[1])
            ang.append(abs(v1[0] * v2[0] + v1[1] * v2[1]) / (math.hypot(*v1) * math.hypot(*v2) + 1e-9))
        if max(ang) < 0.12: roof = 1
    bout.append([kind, h, roof, shop, enc(ps), inner])


BEDGES = []
for p, t, wid, a, k in blds:
    for i in range(len(p)):
        BEDGES.append((p[i], p[(i + 1) % len(p)]))
BGRID = collections.defaultdict(list)
for e in BEDGES:
    for gx in range(int(min(e[0][0], e[1][0]) // 20) - 1, int(max(e[0][0], e[1][0]) // 20) + 2):
        for gz in range(int(min(e[0][1], e[1][1]) // 20) - 1, int(max(e[0][1], e[1][1]) // 20) + 2):
            BGRID[(gx, gz)].append(e)
def ray_hit(x, z, dx, dz, maxd=14):
    best = maxd
    cand = set()
    for s in range(0, int(maxd) + 20, 10):
        px, pz = x + dx * s, z + dz * s
        for e in BGRID.get((int(px // 20), int(pz // 20)), []): cand.add(e)
    for (a, b) in cand:
        ex, ez = b[0] - a[0], b[1] - a[1]
        den = dx * ez - dz * ex
        if abs(den) < 1e-9: continue
        t = ((a[0] - x) * ez - (a[1] - z) * ex) / den
        u = ((a[0] - x) * dz - (a[1] - z) * dx) / den
        if 0 < t < best and 0 <= u <= 1: best = t
    return best
def ped_width(pts):
    ws = []
    for a, b in zip(pts, pts[1:]):
        L = math.dist(a, b)
        if L < 1: continue
        dx, dz = (b[0] - a[0]) / L, (b[1] - a[1]) / L
        for f in (0.25, 0.5, 0.75):
            x, z = a[0] + (b[0] - a[0]) * f, a[1] + (b[1] - a[1]) * f
            l = ray_hit(x, z, -dz, dx); r = ray_hit(x, z, dz, -dx)
            ws.append(max(l, r))
    if not ws: return 6.0
    ws.sort(); m = ws[len(ws) // 2]
    return max(5.0, min(24.0, 2 * m + 0.5))

# ---------------------------------------------------------------- roads
CAR = {'motorway': 9, 'trunk': 9, 'primary': 8, 'secondary': 7.5, 'tertiary': 6.5, 'unclassified': 5.6, 'residential': 5.2,
       'living_street': 4.6, 'service': 3.6, 'busway': 6.0, 'motorway_link': 6, 'primary_link': 6, 'secondary_link': 6, 'tertiary_link': 6}
CLS = {'cycleway': 2.3, 'footway': 1.8, 'pedestrian': 6.0, 'path': 1.6, 'track': 3.0, 'platform': 2.5, 'bridleway': 1.6}
names = []
nidx = {}
def name_i(n):
    if not n: return -1
    if n not in nidx: nidx[n] = len(names); names.append(n)
    return nidx[n]

# ---------------------------------------------------------------- road heights (graphics plan phase 4)
# bridges (bridge=*, layer>=1) get a deck height: 6.5 m where they cross over a street (viaducts like the A6 over the Marknesserweg),
# 1.5 m for the movable Kamperbrug style crossings of the big canals by main roads, 0.8 m for small town bridges over water;
# the height then runs down along every connected road or path at a fixed grade (3.5 % main roads, 5 % streets, 6 % paths)
def _lay(t):
    try: return int(t.get('layer', '1' if t.get('bridge') else '0'))
    except: return 1 if t.get('bridge') else 0
HWAYS = {}
for wid, (nds, t) in W.items():
    hw = t.get('highway')
    if (hw in CAR or hw in CLS) and t.get('area') != 'yes' and not t.get('tunnel') and _lay(t) >= 0: HWAYS[wid] = ([n for n in nds if n in N], t)
nways = collections.defaultdict(list)
for wid, (nds, t) in HWAYS.items():
    for n in nds: nways[n].append(wid)
SEGG = collections.defaultdict(list)
for wid, (nds, t) in HWAYS.items():
    if t.get('highway') in CAR and _lay(t) == 0 and not t.get('bridge'):
        for a, b in zip(nds, nds[1:]):
            pa, pb = xy(a), xy(b)
            for gx in range(int(min(pa[0], pb[0]) // 50), int(max(pa[0], pb[0]) // 50) + 1):
                for gz in range(int(min(pa[1], pb[1]) // 50), int(max(pa[1], pb[1]) // 50) + 1): SEGG[(gx, gz)].append((pa, pb))
def _cross(p1, p2, p3, p4):
    d = lambda a, b, c: (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])
    return d(p1, p2, p3) * d(p1, p2, p4) < 0 and d(p3, p4, p1) * d(p3, p4, p2) < 0
def over_road(nds):
    for a, b in zip(nds, nds[1:]):
        pa, pb = xy(a), xy(b)
        for gx in range(int(min(pa[0], pb[0]) // 50), int(max(pa[0], pb[0]) // 50) + 1):
            for gz in range(int(min(pa[1], pb[1]) // 50), int(max(pa[1], pb[1]) // 50) + 1):
                for q1, q2 in SEGG.get((gx, gz), ()):
                    if _cross(pa, pb, q1, q2): return True
    return False
MAJOR = {'motorway', 'trunk', 'primary', 'secondary', 'motorway_link', 'trunk_link', 'primary_link', 'secondary_link'}
def grade(t):
    hw = t.get('highway'); return 0.035 if hw in MAJOR else 0.05 if hw in CAR else 0.06
NH = {}
heap = []
for wid, (nds, t) in HWAYS.items():
    if not t.get('bridge') or t.get('bridge') == 'no' or _lay(t) < 1 or len(nds) < 2: continue
    # a motorway bridge over a canal must clear shipping (the Kamperbrug next to it is movable), so it is as high as a viaduct
    H = 6.5 if over_road(nds) or t.get('highway') in ('motorway', 'motorway_link', 'trunk') else (1.5 if t.get('highway') in MAJOR else 0.8)
    for n in nds:
        if NH.get(n, 0) < H: NH[n] = H; heapq.heappush(heap, (-H, n))
while heap:
    h, n = heapq.heappop(heap); h = -h
    if NH.get(n, 0) > h + 1e-9: continue
    for wid in nways[n]:
        nds, t = HWAYS[wid]; g = grade(t)
        i = nds.index(n)
        for j in (i - 1, i + 1):
            if 0 <= j < len(nds):
                m = nds[j]; hh = h - math.dist(xy(n), xy(m)) * g
                if t.get('bridge') and t.get('bridge') != 'no' and _lay(t) >= 1: hh = max(hh, NH.get(m, 0))
                if hh > NH.get(m, 0) + 1e-6: NH[m] = hh; heapq.heappush(heap, (-hh, m))
print('raised nodes', sum(1 for v in NH.values() if v > 0.05))
def clip_line_h(pts):
    """clip a list of (x, z, h) to the region, interpolating h"""
    out = []; cur = []
    for a, b in zip(pts, pts[1:]):
        c = clip_seg(a[:2], b[:2])
        if not c:
            if cur: out.append(cur); cur = []
            continue
        ca, cb = c; L = math.dist(a[:2], b[:2]) or 1e-9
        ha = a[2] + (b[2] - a[2]) * math.dist(a[:2], ca) / L; hb = a[2] + (b[2] - a[2]) * math.dist(a[:2], cb) / L
        if not cur: cur = [(ca[0], ca[1], ha)]
        elif math.dist(cur[-1][:2], ca) > 1e-6: out.append(cur); cur = [(ca[0], ca[1], ha)]
        cur.append((cb[0], cb[1], hb))
        if math.dist(cb, b[:2]) > 1e-6: out.append(cur); cur = []
    if cur: out.append(cur)
    return [l for l in out if len(l) >= 2]
def densify(pts, step=8.0):
    o = [pts[0]]
    for a, b in zip(pts, pts[1:]):
        L = math.dist(a[:2], b[:2]); k = max(1, int(math.ceil(L / step)))
        for i in range(1, k + 1): f = i / k; o.append((a[0] + (b[0] - a[0]) * f, a[1] + (b[1] - a[1]) * f, a[2] + (b[2] - a[2]) * f))
    return o
road_h = {}
roads = []   # [cls, width, nameIdx, flags, enc]
KLINKER_SURF = {'paving_stones', 'sett', 'bricks', 'cobblestone', 'unhewn_cobblestone', 'paving_stones:30'}
CLASSCODE = {**{k: 0 for k in CAR}, 'cycleway': 1, 'footway': 2, 'path': 2, 'pedestrian': 3, 'track': 4, 'platform': 2, 'bridleway': 2}
for wid, (nds, t) in W.items():
    hw = t.get('highway')
    if hw not in CAR and hw not in CLS: continue
    if t.get('area') == 'yes': continue
    if hw == 'footway' and t.get('footway') == 'crossing': pass
    if t.get('tunnel') or t.get('layer', '0').startswith('-'): continue
    pts = [xy(n) for n in nds if n in N]
    if hw in CAR:
        w = CAR[hw]
        if hw == 'service' and t.get('service') == 'parking_aisle': w = 5.0
        if hw == 'service' and t.get('service') in ('driveway',): w = 3.0
        lanes = t.get('lanes')
        try:
            ln = int(lanes)
            if hw in ('secondary', 'primary', 'tertiary'): w = max(w if ln >= 2 else 0, ln * 3.2)
        except: pass
        if t.get('oneway') == 'yes' and hw in ('secondary', 'primary', 'tertiary') and (lanes in (None, '1')): w = 4.2
    else:
        w = CLS[hw]
        if hw == 'pedestrian':
            w = ped_width(pts)
    flags = (1 if t.get('bridge') else 0) | (2 if t.get('oneway') == 'yes' else 0) | (4 if t.get('junction') == 'roundabout' else 0)
    if hw in CAR and t.get('surface') in KLINKER_SURF: flags |= 8   # klinker street (graphics plan phase 3)
    hn = [NH.get(n, 0.0) for n in nds if n in N]
    if max(hn) > 0.05:
        for seg in clip_line_h(densify([(p[0], p[1], h) for p, h in zip(pts, hn)])):
            road_h[len(roads)] = [q[2] for q in seg]
            roads.append([CLASSCODE[hw], round(w, 1), name_i(t.get('name') or t.get('ref', '')), flags | 16, enc([q[:2] for q in seg]), hw])
        continue
    for seg in clip_line(pts):
        s = dp(seg, 0.15)
        roads.append([CLASSCODE[hw], round(w, 1), name_i(t.get('name', '')), flags, enc(s), hw])

# ---------------------------------------------------------------- road graph for traffic
GRAPH_HW = {'primary', 'secondary', 'tertiary', 'unclassified', 'residential', 'living_street', 'primary_link', 'secondary_link', 'tertiary_link'}
use = collections.Counter()
gways = []
for wid, (nds, t) in W.items():
    if t.get('highway') in GRAPH_HW and t.get('area') != 'yes' and t.get('access') not in ('no', 'private'):
        nn = [n for n in nds if n in N]
        if len(nn) < 2: continue
        gways.append((nn, t))
        for n in nn: use[n] += 1
        use[nn[0]] += 1; use[nn[-1]] += 1
gnodes = {}; gn_list = []
def gid(n):
    if n not in gnodes: gnodes[n] = len(gn_list); gn_list.append(xy(n))
    return gnodes[n]
edges = []
for nn, t in gways:
    start = 0
    for i in range(1, len(nn)):
        if use[nn[i]] > 1 or i == len(nn) - 1:
            seg = nn[start:i + 1]
            pts = [xy(n) for n in seg]
            if all(inreg(p, -5) for p in pts):
                hw = t['highway']; w = CAR.get(hw, 5)
                ow = 1 if (t.get('oneway') == 'yes' or t.get('junction') == 'roundabout') else 0
                if t.get('oneway') == '-1': pts = pts[::-1]; seg = seg[::-1]; ow = 1
                L = sum(math.dist(a, b) for a, b in zip(pts, pts[1:]))
                rank = {'primary': 3, 'secondary': 3, 'tertiary': 2, 'unclassified': 1}.get(hw, 0)
                edges.append([gid(seg[0]), gid(seg[-1]), ow, rank, name_i(t.get('name', '')), L, dp(pts, 0.6), w, t.get('lanes')])
            start = i
# keep only the largest connected component
adj = collections.defaultdict(list)
for i, e in enumerate(edges):
    adj[e[0]].append(i); adj[e[1]].append(i)
seen = set(); comps = []
for s in range(len(gn_list)):
    if s in seen or s not in adj: continue
    st = [s]; comp = set([s]); seen.add(s)
    while st:
        u = st.pop()
        for ei in adj[u]:
            e = edges[ei]
            for v in (e[0], e[1]):
                if v not in seen: seen.add(v); comp.add(v); st.append(v)
    comps.append(comp)
big = max(comps, key=len)
edges = [e for e in edges if e[0] in big]
used_nodes = sorted(set([e[0] for e in edges] + [e[1] for e in edges]))
remap = {o: i for i, o in enumerate(used_nodes)}
gn_out = [gn_list[o] for o in used_nodes]
for e in edges: e[0] = remap[e[0]]; e[1] = remap[e[1]]

# ring route for the time trial: Dijkstra through waypoints
def nearest_node(x, z, minrank=2):
    best, bi = 1e9, None
    for e in edges:
        if e[3] < minrank: continue
        for k in (0, 1):
            p = gn_out[e[k]]; dd = math.dist(p, (x, z))
            if dd < best: best, bi = dd, e[k]
    return bi
def dijkstra(a, b, minrank=2):
    out = collections.defaultdict(list)
    for i, e in enumerate(edges):
        if e[3] < minrank: continue
        out[e[0]].append((e[1], i, False))
        if not e[2]: out[e[1]].append((e[0], i, True))
    dist = {a: 0}; prev = {}; pq = [(0, a)]
    while pq:
        dd, u = heapq.heappop(pq)
        if u == b: break
        if dd > dist.get(u, 1e18): continue
        for v, ei, rev in out[u]:
            nd = dd + edges[ei][5]
            if nd < dist.get(v, 1e18): dist[v] = nd; prev[v] = (u, ei, rev); heapq.heappush(pq, (nd, v))
    path = []; u = b
    while u != a:
        pu, ei, rev = prev[u]
        pts = edges[ei][6][::-1] if rev else edges[ei][6]
        path = pts[1:] + path if path else pts[:]
        if path and path[0] != pts[0]: path = pts[:-1] + path
        u = pu
    return path
WP = [(-10, 45), (-35, -110), (100, -205), (500, -228), (850, -140), (520, -40)]
ringpts = []
nodes_wp = [nearest_node(x, z) for x, z in WP]
for i in range(len(WP)):
    seg = dijkstra(nodes_wp[i], nodes_wp[(i + 1) % len(WP)])
    ringpts += seg if not ringpts else seg[1:]
ringpts = dp(ringpts, 1.0)

# ---------------------------------------------------------------- point features
trees = []; lamps = []; benches = []; flags = []; lions = []; bikes = []; parked = []
for nid, (la, lo, t) in N.items():
    x, z = xy(nid)
    if not inreg((x, z)): continue
    if t.get('natural') == 'tree': trees.append((x, z))
    elif t.get('highway') == 'street_lamp': lamps.append((x, z))
    elif t.get('amenity') == 'bench': benches.append((x, z))
    elif t.get('man_made') == 'flagpole': flags.append((x, z))
    elif t.get('name') == 'De Leeuwen': lions.append((x, z))
for wid, (nds, t) in W.items():
    if t.get('natural') == 'tree_row':
        pts = [xy(n) for n in nds if n in N]
        for a, b in zip(pts, pts[1:]):
            L = math.dist(a, b); k = max(1, int(L / 9))
            for j in range(k): trees.append((a[0] + (b[0] - a[0]) * j / k, a[1] + (b[1] - a[1]) * j / k))
    if t.get('amenity') == 'parking_space':
        p = ring(nds)
        if len(p) == 4 and inreg(p[0]):
            cx = sum(q[0] for q in p) / 4; cz = sum(q[1] for q in p) / 4
            e1 = (p[1][0] - p[0][0], p[1][1] - p[0][1]); e2 = (p[2][0] - p[1][0], p[2][1] - p[1][1])
            L1, L2 = math.hypot(*e1), math.hypot(*e2)
            ax = e1 if L1 > L2 else e2
            if 3.5 < max(L1, L2) < 7: parked.append((round(cx, 1), round(cz, 1), round(math.atan2(ax[0], ax[1]), 2)))
    if t.get('amenity') == 'bicycle_parking' and nds[0] == nds[-1]:
        p = ring(nds)
        if p and inreg(p[0]): bikes.append(enc(p))


# landuse (built-up areas) for the minimap: 0 residential, 1 industrial, 2 commercial/retail
LU={'residential':0,'industrial':1,'commercial':2,'retail':2}
landuse=[]
for p, t, wid in polys_of(lambda t: t.get('landuse') in LU):
    if poly_clip_ok(p) and abs(area(p)) > 400: landuse.append([LU[t['landuse']], enc(simp_poly(p, 2.0))])
places=[]
for nid, (la, lo, t) in N.items():
    if t.get('place') in ('neighbourhood','quarter','suburb') and t.get('name'):
        x, z = xy(nid)
        if inreg((x, z)): places.append([round(x), round(z), t['name'], t['place']])

areas=[]
for p, t, wid in polys_of(lambda t: t.get('landuse') in ('industrial','commercial','retail') and t.get('name')):
    if poly_clip_ok(p) and abs(area(p)) > 20000: areas.append([t['name'], enc(simp_poly(p, 4.0), 1)])
import base64
buf=bytearray()
def vu(n):
    n=int(n)
    while True:
        b=n&127; n>>=7
        if n: buf.append(b|128)
        else: buf.append(b); return
def vs(n): n=int(n); vu((n<<1) if n>=0 else ((-n<<1)-1))
def pts_out(pts, s):
    vu(len(pts)); px=pz=0
    for x,z in pts:
        ix,iz=round(x*s),round(z*s); vs(ix-px); vs(iz-pz); px,pz=ix,iz
def dec(e, s=5):
    v=list(map(int,e.split(','))); o=[]; x=z=0
    for i in range(0,len(v),2): x+=v[i]; z+=v[i+1]; o.append((x/s,z/s))
    return o
# section order is mirrored by the decoder in index.html
vu(len(roads))
for ri,(c,w,ni,fl,e,hw) in enumerate(roads):
    vu(c); vu(round(w*10)); vs(ni); vu(fl); pts_out(dec(e), 2 if c==2 else 5)
    if fl & 16:
        for h in road_h[ri]: vu(max(0, round(h * 20)))
vu(len(water))
for e in water: pts_out(dec(e),2)
vu(len(green))
for k,e in green: vu(k); pts_out(dec(e),2)
vu(len(paved))
for k,e in paved: vu(k); pts_out(dec(e),4)
vu(len(bout))
for kind,h,roof,shop,e,inner in bout:
    vu(kind); vu(round(h*10)); vu(roof|(shop<<1)); pts_out(dec(e),4); vu(len(inner))
    for j in inner: vu(j)
pts_out(gn_out,2)
vu(len(edges))
for e in edges:
    vu(e[0]); vu(e[1]); vu(e[2]|(e[3]<<1)); vs(e[4]); pts_out(e[6],2)
pts_out(ringpts,2)
for L in (trees,lamps,benches,flags,lions): pts_out(L,2 if L in (trees,lamps) else 5)
vu(len(parked))
for x,z,a in parked: vs(round(x*2)); vs(round(z*2)); vs(round(a*100))
vu(len(bikes))
for e in bikes: pts_out(dec(e),4)
vu(len(landuse))
for k,e in landuse: vu(k); pts_out(dec(e),1)
# ---------------------------------------------------------------- street details (graphics plan phase 3)
# give-way lines (haaientanden): position, heading towards the junction, road width; zebra crossings: position, road heading, width
car_of = collections.defaultdict(list)
for wid, (nds, t) in W.items():
    if t.get('highway') in CAR and t.get('area') != 'yes':
        for i, n in enumerate(nds): car_of[n].append((wid, i))
def road_w(t):
    hw = t['highway']; w = CAR[hw]
    try:
        ln = int(t.get('lanes'))
        if hw in ('secondary', 'primary', 'tertiary'): w = max(w if ln >= 2 else 0, ln * 3.2)
    except: pass
    if t.get('oneway') == 'yes' and hw in ('secondary', 'primary', 'tertiary') and t.get('lanes') in (None, '1'): w = 4.2
    return w
give = []; zebra = []; bollards = []; bins = []; cabinets = []; kerbcuts = []
for nid, (la, lo, t) in N.items():
    x, z = xy(nid)
    if not inreg((x, z), -2): continue
    hw = t.get('highway')
    if t.get('barrier') == 'bollard': bollards.append((x, z))
    elif t.get('amenity') == 'waste_basket': bins.append((x, z))
    elif t.get('man_made') == 'street_cabinet': cabinets.append((x, z))
    if (t.get('barrier') == 'kerb' and t.get('kerb') in ('lowered', 'flush', 'no')) or hw == 'crossing': kerbcuts.append((x, z))
    if hw in ('give_way', 'stop', 'crossing') and car_of.get(nid):
        wid, i = car_of[nid][0]; nds, wt = W[wid]
        nn = [n for n in nds if n in N]
        if len(nn) < 2 or nid not in nn: continue
        i = nn.index(nid); w = road_w(wt)
        if hw == 'crossing':
            if not (t.get('crossing') in ('zebra', 'marked', 'uncontrolled') or t.get('crossing_ref') == 'zebra' or t.get('crossing:markings') in ('zebra', 'yes')): continue
            a = xy(nn[max(0, i - 1)]); b = xy(nn[min(len(nn) - 1, i + 1)])
            zebra.append((x, z, math.atan2(b[0] - a[0], b[1] - a[1]), w))
        else:
            d = t.get('direction')
            fwd = True if d == 'forward' else False if d == 'backward' else (len(nn) - 1 - i) <= i
            j = min(len(nn) - 1, i + 1) if fwd else max(0, i - 1)
            if j == i: continue
            b = xy(nn[j]); give.append((x, z, math.atan2(b[0] - x, b[1] - z), w))
hedges = []
for wid, (nds, t) in W.items():
    if t.get('barrier') == 'hedge':
        pts = [xy(n) for n in nds if n in N]
        for seg in clip_line(pts): hedges.append(enc(dp(seg, 0.3)))
def ang_out(L):
    vu(len(L))
    for x, z, a, w in L: vs(round(x * 4)); vs(round(z * 4)); vu(round((math.degrees(a) % 360) * 2)); vu(round(w * 10))
ang_out(give); ang_out(zebra)
for L in (bollards, bins, cabinets, kerbcuts): pts_out(L, 4)
vu(len(hedges))
for e in hedges: pts_out(dec(e), 4)
print('give', len(give), 'zebra', len(zebra), 'bollards', len(bollards), 'bins', len(bins), 'cabinets', len(cabinets), 'kerbcuts', len(kerbcuts), 'hedges', len(hedges))
b64=base64.b64encode(bytes(buf)).decode()
meta={'region':[RX0,RX1,RZ0,RZ1],'names':names,'shops':[[round(x,1),round(z,1),s] for x,z,s in shops],'places':places,'areas':areas}
open(os.environ.get('OUT','/home/user/test/emm-data.js'),'w').write('window.EMM_DATA='+json.dumps(meta,separators=(',',':'),ensure_ascii=False)+';\nwindow.EMM_BIN="'+b64+'";\n')
print('bin',len(buf),'b64',len(b64),'roads',len(roads),'bld',len(bout),'trees',len(trees),'lamps',len(lamps),'bench',len(benches),'parked',len(parked),'edges',len(edges),'water',len(water),'green',len(green),'paved',len(paved),'names',len(names))
