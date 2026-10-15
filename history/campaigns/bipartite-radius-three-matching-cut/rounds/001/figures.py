import itertools
from pathlib import Path
from xml.sax.saxutils import escape
out=Path(__file__).resolve().parents[2]/'work/figures'


def draw(name,width,height,positions,edges,labels,open_vertices=()):
    assert len(edges)==len({tuple(sorted(e)) for e in edges})
    assert all(u in positions and v in positions for u,v in edges)
    svg=[f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}"><rect width="100%" height="100%" fill="white"/>']
    for u,v in edges:
        x,y=positions[u];xx,yy=positions[v]
        control = None
        if name=='selector.svg' and (u,v)==(0,6):control=(220,0)
        if name=='selector.svg' and (u,v)==(13,0):control=(-60,190)
        if name=='selector.svg' and (u,v)==(12,6):control=(510,300)
        if name=='selector.svg' and (u,v)==(12,7):control=(465,250)
        if name=='binary.svg' and (u,v)==(14,18):control=(240,290)
        if control:
            svg.append(f'<path d="M{x},{y} Q{control[0]},{control[1]} {xx},{yy}" fill="none" stroke="#555" stroke-width="2"/>')
            continue
        svg.append(f'<line x1="{x}" y1="{y}" x2="{xx}" y2="{yy}" stroke="#555" stroke-width="2"/>')
    for u,(x,y) in positions.items():
        svg.append(f'<circle cx="{x}" cy="{y}" r="6" fill="{"white" if u in open_vertices else "#222"}" stroke="#222" stroke-width="2"/>')
        label,dx,dy=labels.get(u,('',0,0))
        if label:svg.append(f'<text x="{x+dx}" y="{y+dy}" font-family="serif" font-size="18" text-anchor="middle">{escape(label)}</text>')
    svg.append('</svg>');(out/name).write_text(''.join(svg))

positions={};labels={}
for i in range(3):
    positions[i]=(40,35+45*i);positions[i+3]=(110,35+45*i)
    positions[i+6]=(400,35+45*i);positions[i+9]=(470,35+45*i)
    labels[i]=(str(i),-18,5);labels[i+3]=(str(i+3),18,5)
    labels[i+6]=(str(i+6),-18,5);labels[i+9]=(str(i+9),18,5)
positions.update({12:(290,285),13:(160,190),14:(320,190),15:(205,235),16:(160,345),17:(205,285),18:(320,345),19:(290,235)})
labels.update({12:('F',-9,24),13:('A',0,-20),14:('d1',18,0),15:('d2',-23,4),16:('d3',-18,18),17:('T1',-23,5),18:('T2',18,18),19:('T3',20,0)})
low=[14,15,16];high=[17,18,19]
edges=list(itertools.product(range(3),range(3,6)))+list(itertools.product(range(6,9),range(9,12)))+[(0,6)]
edges += [(12,6),(12,7),(13,0),(13,1)]+[(13,v) for v in low]+[(12,v) for v in high]+[(u,v) for i,u in enumerate(low) for j,v in enumerate(high) if i!=j]
assert len(positions)==20 and len(edges)==35
draw('selector.svg',520,385,positions,edges,labels,high)
positions={0:(40,40),1:(100,40),3:(380,40),4:(440,40),6:(40,330),7:(100,330),9:(380,330),10:(440,330),12:(150,240),13:(200,190),14:(100,190),15:(150,100),16:(330,100),17:(280,190),18:(380,190),19:(330,240)}
labels={i:(str(i),0,-16 if y<80 else 27) for i,(x,y) in positions.items() if i<12}
labels.update({12:('f',-18,5),13:('p',0,-17),14:('r',-18,5),15:('z',-18,5),16:('a',20,5),17:('v',0,-17),18:('w',20,5),19:('q',20,5)})
edges=[(12,6),(12,7),(15,3),(15,4),(16,0),(16,1),(19,9),(19,10),(12,13),(12,14),(15,13),(15,14),(16,17),(16,18),(19,17),(19,18),(13,17),(14,18)]
assert len(positions)==16 and len(edges)==18
draw('binary.svg',480,375,positions,edges,labels,[i for i in positions if i<12])
print('Selector: 20 vertices/35 edges including both full reservoirs. Binary: 8 private+8 displayed anchor vertices/18 edges; reservoir-internal edges omitted explicitly.')
