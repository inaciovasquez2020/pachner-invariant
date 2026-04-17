from pathlib import Path
import json

p = Path("docs/data/g2_enumeration.json")
data = json.loads(p.read_text())

data["status"] = "conditional"
data["cycles_found"]["6"] = {
    "exact_cycle_rank": 8,
    "basis_cycle_lengths": [5, 4, 5, 7, 7, 5, 5, 7],
    "graph_artifact": "docs/data/f6_exact_graph.json",
    "basis_artifact": "docs/data/f6_cycle_basis.json"
}
data["generated_by_candidate_G2"]["6"] = {
    "full_coverage_verified": None,
    "observed_local_cycle_lengths": [4, 5, 7],
    "note": "exact graph and basis computed; generator classification still open"
}
data["certificates"]["6"] = {
    "type": "partial_exact_surface",
    "graph_artifact": "docs/data/f6_exact_graph.json",
    "basis_artifact": "docs/data/f6_cycle_basis.json",
    "status_note": "classification into pentagon/square/derived combinations pending"
}

Path("docs/data/g2_enumeration.json").write_text(json.dumps(data, indent=2))
print("updated docs/data/g2_enumeration.json with exact n=6 partial evidence")
