from itertools import combinations
from pathlib import Path
import json

# ---------- triangulations of convex polygon on vertices 0..n-1 ----------

def edges_boundary(n):
    return {tuple(sorted((i, (i+1) % n))) for i in range(n)}

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

def cross(a,b):
    (i,j),(k,l)=a,b
    return (i<k<j<l) or (k<i<l<j)

def noncrossing(S):
    L=list(S)
    for x in range(len(L)):
        for y in range(x+1,len(L)):
            if cross(L[x],L[y]):
                return False
    return True

def triangulations(n):
    diags = all_diagonals(n)
    need = n-3
    out=[]
    for comb in combinations(diags, need):
        if noncrossing(comb):
            out.append(tuple(sorted(comb)))
    return out

# ---------- flips ----------
def quadrilateral_flip(T, d):
    others = [x for x in T if x != d]
    verts = sorted(set(sum(([a,b] for (a,b) in T), [])))
    # for n=5 this local rule suffices by brute force search
    used = set(others)
    allD = all_diagonals(5)
    for e in allD:
        if e in used:
            continue
        cand = tuple(sorted(others + [e]))
        if noncrossing(cand):
            return cand
    return None

def build_graph():
    Ts = triangulations(5)
    idx = {T:i for i,T in enumerate(Ts)}
    adj = {i:set() for i in range(len(Ts))}
    for T in Ts:
        i = idx[T]
        for d in T:
            U = quadrilateral_flip(list(T), d)
            if U is not None and U in idx:
                j = idx[U]
                if i != j:
                    adj[i].add(j)
                    adj[j].add(i)
    return Ts, adj

def edge_count(adj):
    return sum(len(v) for v in adj.values()) // 2

def cycle_basis_rank(v,e,c=1):
    return e - v + c

Ts, adj = build_graph()
V = len(Ts)
E = edge_count(adj)
rank = cycle_basis_rank(V,E,1)

out = {
  "status":"conditional",
  "n":5,
  "vertices":V,
  "edges":E,
  "cycle_rank":rank,
  "triangulations":[list(map(list,t)) for t in Ts],
  "adjacency":{str(k):sorted(list(v)) for k,v in adj.items()},
  "note":"Exact finite graph surface for F5. Next step: explicit cycle basis + G2 coverage."
}

Path("docs/data/f5_exact_graph.json").write_text(json.dumps(out, indent=2))
print("wrote docs/data/f5_exact_graph.json")
print("V =",V,"E =",E,"cycle_rank =",rank)
