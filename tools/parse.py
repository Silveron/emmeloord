import xml.etree.ElementTree as ET, glob, json, sys
nodes={}; ways={}; rels={}
for f in sorted(glob.glob('/home/user/osm2/t_*.osm')):
    for ev,el in ET.iterparse(f):
        if el.tag=='node':
            nodes[el.get('id')]=(float(el.get('lat')),float(el.get('lon')),{t.get('k'):t.get('v') for t in el.findall('tag')})
            el.clear()
        elif el.tag=='way':
            ways[el.get('id')]=([n.get('ref') for n in el.findall('nd')],{t.get('k'):t.get('v') for t in el.findall('tag')})
            el.clear()
        elif el.tag=='relation':
            rels[el.get('id')]=([(m.get('type'),m.get('ref'),m.get('role')) for m in el.findall('member')],{t.get('k'):t.get('v') for t in el.findall('tag')})
            el.clear()
json.dump({'nodes':nodes,'ways':ways,'rels':rels},open('/home/user/osm2/all.json','w'))
print(len(nodes),len(ways),len(rels))
