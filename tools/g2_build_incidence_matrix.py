from pathlib import Path
import json

# This script ONLY prepares raw incidence structures.
# It does NOT claim span, rank, or closure.

def load(path):
    return json.loads(Path(path).read_text())

f6 = load("docs/data/f6_exact_graph.json")
f7 = load("docs/data/f7_exact_graph.json")

def edges_from_adj(adj):
    edges = set()
    for u, nbrs in adj.items():
        u = int(u)
        for v in nbrs:
            a,b = sorted((u,v))
            edges.add((a,b))
    return sorted(edges)

def placeholder_generator_rows(edges):
    # Placeholder: each edge becomes a trivial basis vector
    # Replace later with square/pentagon incidence construction
    return [[1 if i==j else 0 for j in range(len(edges))] for i in range(len(edges))]

def build(graph):
    edges = edges_from_adj(graph["adjacency"])
    return {
        "vertices": graph["vertices"],
        "edge_count": len(edges),
        "edges": edges,
        "generator_matrix_placeholder": placeholder_generator_rows(edges),
        "note": "PLACEHOLDER ONLY: true square/pentagon generators not yet encoded"
    }

out = {
    "F6": build(f6),
    "F7": build(f7),
    "status": "incomplete",
    "warning": "No rank or span claims are computed here."
}

Path("docs/data/g2_incidence_matrix_raw.json").write_text(json.dumps(out, indent=2))
print("wrote docs/data/g2_incidence_matrix_raw.json")
