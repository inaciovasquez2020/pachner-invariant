from pathlib import Path
import json
from collections import deque

p = Path("docs/data/f6_exact_graph.json")
data = json.loads(p.read_text())

adj = {int(k): set(v) for k, v in data["adjacency"].items()}
n = data["vertices"]

root = 0
parent = {root: None}
depth = {root: 0}
tree_edges = set()
q = deque([root])

while q:
    x = q.popleft()
    for y in sorted(adj[x]):
        if y not in parent:
            parent[y] = x
            depth[y] = depth[x] + 1
            tree_edges.add(tuple(sorted((x, y))))
            q.append(y)

def path_to_root(v):
    out = []
    while v is not None:
        out.append(v)
        v = parent[v]
    return out

def tree_path(u, v):
    pu = path_to_root(u)
    pv = path_to_root(v)
    su = set(pu)
    lca = next(w for w in pv if w in su)
    left = pu[:pu.index(lca) + 1]
    right = pv[:pv.index(lca)]
    return left + right[::-1]

all_edges = set()
for u in adj:
    for v in adj[u]:
        if u < v:
            all_edges.add((u, v))

non_tree_edges = sorted(all_edges - tree_edges)

basis = []
for u, v in non_tree_edges:
    path = tree_path(u, v)
    cyc = path + [u]
    basis.append({
        "chord": [u, v],
        "cycle_vertices": cyc,
        "cycle_length": len(cyc) - 1
    })

out = {
    "status": "conditional",
    "n": 6,
    "vertices": n,
    "tree_edge_count": len(tree_edges),
    "non_tree_edge_count": len(non_tree_edges),
    "cycle_rank": len(basis),
    "basis_cycles": basis,
    "note": "Fundamental cycle basis extracted from exact F6 flip graph. Classification into G2 generators remains open."
}

Path("docs/data/f6_cycle_basis.json").write_text(json.dumps(out, indent=2))
print("wrote docs/data/f6_cycle_basis.json")
print("cycle_rank =", len(basis))
print("cycle_lengths =", [b["cycle_length"] for b in basis])
