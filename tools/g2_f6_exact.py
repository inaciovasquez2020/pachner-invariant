from itertools import combinations
from pathlib import Path
import json

# ---------- convex n-gon triangulations ----------

def all_diagonals(n):
    out = []
    for i in range(n):
        for j in range(i+1, n):
            if j == i+1:
                continue
            if i == 0 and j == n-1:
                continue
            out.append((i,j))
    return out

def cross(e1,e2):
    (a,b),(c,d)=e1,e2
    return (a<c<b<d) or (c<a<d<b)

def noncrossing(diags):
    L=list(diags)
    for i in range(len(L)):
        for j in range(i+1,len(L)):
            if cross(L[i],L[j]):
                return False
    return True

def triangulations(n):
    need = n - 3
    ds = all_diagonals(n)
    out = []
    for comb in combinations(ds, need):
        if noncrossing(comb):
            out.append(tuple(sorted(comb)))
    return out

# ---------- flips ----------
def graph_of_triangulations(n):
    Ts = triangulations(n)
    idx = {T:i for i,T in enumerate(Ts)}
    allT = set(Ts)
    allD = all_diagonals(n)
    adj = {i:set() for i in range(len(Ts))}

    for T in Ts:
        i = idx[T]
        S = set(T)
        for d in T:
            base = tuple(sorted(x for x in T if x != d))
            for e in allD:
                if e in S:
                    continue
                cand = tuple(sorted(base + (e,)))
                if cand in allT:
                    j = idx[cand]
                    if i != j:
                        adj[i].add(j)
                        adj[j].add(i)
    return Ts, adj

def edge_count(adj):
    return sum(len(v) for v in adj.values()) // 2

def components(adj):
    seen=set()
    c=0
    for v in adj:
        if v in seen:
            continue
        c += 1
        stack=[v]
        seen.add(v)
        while stack:
            x=stack.pop()
            for y in adj[x]:
                if y not in seen:
                    seen.add(y)
                    stack.append(y)
    return c

def cycle_rank(V,E,C):
    return E - V + C

Ts, adj = graph_of_triangulations(6)
V = len(Ts)
E = edge_count(adj)
C = components(adj)
R = cycle_rank(V,E,C)

out = {
    "status":"conditional",
    "n":6,
    "vertices":V,
    "edges":E,
    "components":C,
    "cycle_rank":R,
    "triangulations":[list(map(list,t)) for t in Ts],
    "adjacency":{str(k):sorted(list(v)) for k,v in adj.items()},
    "note":"Exact finite graph surface for F6. Next step: explicit cycle basis + G2 coverage."
}

Path("docs/data/f6_exact_graph.json").write_text(json.dumps(out, indent=2))
print("wrote docs/data/f6_exact_graph.json")
print("V =",V,"E =",E,"components =",C,"cycle_rank =",R)
