from pathlib import Path
import json

# Canonical executable wall-isolation artifact.
# This does NOT fake the proof. It encodes the exact next certificate object.

f6 = json.loads(Path("docs/data/f6_exact_graph.json").read_text())
f7 = json.loads(Path("docs/data/f7_exact_graph.json").read_text())

def edge_count(graph):
    seen = set()
    for u, nbrs in graph["adjacency"].items():
        u = int(u)
        for v in nbrs:
            a, b = sorted((u, v))
            seen.add((a, b))
    return len(seen)

out = {
    "status": "conditional",
    "field": "F2",
    "generator_types": [
        "square_commutation",
        "pentagon"
    ],
    "targets": {
        "F6": {
            "vertices": f6["vertices"],
            "edges": edge_count(f6),
            "cycle_rank_required": 8,
            "matrix_shape_goal": "num_generators x 21",
            "certificate_condition": "rank(generator_matrix)=8"
        },
        "F7": {
            "vertices": f7["vertices"],
            "edges": edge_count(f7),
            "cycle_rank_required": 43,
            "matrix_shape_goal": "num_generators x 84",
            "certificate_condition": "rank(generator_matrix)=43"
        }
    },
    "single_remaining_wall":
        "Enumerate every square/pentagon generator as an edge-incidence row vector."
}

Path("docs/data/g2_generator_matrix_wall.json").write_text(json.dumps(out, indent=2))
print("wrote docs/data/g2_generator_matrix_wall.json")
