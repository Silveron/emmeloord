"""Real addresses (addr:street + addr:housenumber) for the whole town -> ADDR_RAW json {street: "x,z,num|..."}"""
import json, math, re, os, sys
sys.argv=['x']
d = json.load(open('/home/user/osm2/all.json')); N, W = d['nodes'], d['ways']
LAT0, LON0 = 52.70996, 5.75090; ky = 111320.0; kx = ky * math.cos(math.radians(LAT0))
RX0, RX1, RZ0, RZ1 = map(int, os.environ['REGION'].split(','))
def xyll(la, lo): return ((lo - LON0) * kx - 3.44, -(la - LAT0) * ky - 3.35)
A = {}
def add(st, num, x, z):
    if not (RX0 + 20 < x < RX1 - 20 and RZ0 + 20 < z < RZ1 - 20): return
    A.setdefault(st, {}).setdefault(num, (x, z))
for nid, (la, lo, t) in N.items():
    if 'addr:street' in t and 'addr:housenumber' in t: add(t['addr:street'], t['addr:housenumber'], *xyll(la, lo))
for wid, (nds, t) in W.items():
    if 'addr:street' in t and 'addr:housenumber' in t:
        p = [N[n] for n in nds if n in N]
        if p: add(t['addr:street'], t['addr:housenumber'], *xyll(sum(a[0] for a in p) / len(p), sum(a[1] for a in p) / len(p)))
key = lambda n: (int(re.match(r'\d*', n).group() or 0), n)
out = {}; tot = 0; full = 0
for st in sorted(A):
    nums = sorted(A[st], key=key)
    full += len(nums)
    keep = []
    for i, n in enumerate(nums):
        x, z = A[st][n]
        step = 2 if math.hypot(x, z) < 950 else 3
        if i % step == 0: keep.append('%d,%d,%s' % (round(x), round(z), n))
    out[st] = '|'.join(keep); tot += len(keep)
s = json.dumps(out, ensure_ascii=False, separators=(',', ':'))
open(os.environ['OUT'], 'w').write(s)
print('streets', len(out), 'addresses', full, 'kept', tot, 'bytes', len(s.encode()))
