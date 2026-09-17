import itertools
import json
import networkx as nx
import z3


def root():
    g=nx.Graph();g.add_edges_from(itertools.product(range(3),range(3,6)));g.add_edges_from(itertools.product(range(6,9),range(9,12)));g.add_edge(0,6)
    return g


def variable(g):
    f,p,r,z,a,v,w,q=range(len(g),len(g)+8)
    g.add_edges_from([(f,6),(f,7),(z,3),(z,4),(a,0),(a,1),(q,9),(q,10),(f,p),(f,r),(z,p),(z,r),(a,v),(a,w),(q,v),(q,w),(p,v),(r,w)])
    return p,r,v,w


def selector(g):
    f,a,d,e,k,t,s,r=range(len(g),len(g)+8)
    low=[d,e,k];high=[t,s,r]
    g.add_edges_from([(f,6),(f,7),(a,0),(a,1)]+[(a,v) for v in low]+[(f,v) for v in high]+[(u,v) for i,u in enumerate(low) for j,v in enumerate(high) if i!=j])
    return low,high


def solver(g):
    x=[z3.Bool(f'x{i}') for i in g];s=z3.Solver()
    for i in g:s.add(z3.Sum([z3.If(x[i]!=x[j],1,0) for j in g[i]])<=1)
    return s,x


def check(g,predicate):
    s,x=solver(g);s.add(x[0]==False,predicate(x));status=s.check();assert status!=z3.unknown
    return str(status)

records=[]
for wires,selectors in [(1,0),(0,1),(1,1),(2,2)]:
    g=root();v=[variable(g) for _ in range(wires)];c=[selector(g) for _ in range(selectors)]
    s,x=solver(g);s.add(x[0]==False,x[6]==False,z3.Or(x));assert s.check()==z3.unsat
    relation_checks=0
    for index,(p,r,a,b) in enumerate(v):
        assert check(g,lambda x:z3.And(x[6],z3.Or(x[p]==x[r],x[p]!=x[a],x[r]!=x[b])))=='unsat';relation_checks+=1
    for low,high in c:
        assert check(g,lambda x:z3.And(x[6],z3.Or(z3.Sum([z3.If(x[i],1,0) for i in low])!=1,*[x[i]==x[j] for i,j in zip(low,high)])))=='unsat';relation_checks+=1
    extensions=0
    for vb in itertools.product((0,1),repeat=wires):
      for choice in itertools.product(range(3),repeat=selectors):
        s,x=solver(g);s.add(x[0]==False,x[6])
        for bit,(p,*_) in zip(vb,v):s.add(x[p]==bool(bit))
        for which,(low,_) in zip(choice,c):
          for i,node in enumerate(low):s.add(x[node]==(i==which))
        assert s.check()==z3.sat;extensions+=1
    assert nx.is_bipartite(g) and nx.eccentricity(g,0)<=3
    records.append({'wires':wires,'selectors':selectors,'vertices':len(g),'edges':g.number_of_edges(),'center_eccentricity':nx.eccentricity(g,0),'same_center_nonconstant':'UNSAT','bad_relation_queries':relation_checks,'extensions':extensions})
print(json.dumps(records,indent=2))
