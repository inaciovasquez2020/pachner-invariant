from pathlib import Path
import json

p = Path("docs/data/g2_enumeration.json")
data = json.loads(p.read_text())

b = json.loads(Path("docs/data/f7_cycle_basis.json").read_text())

data["status"] = "conditional"
data["cycles_found"]["7"] = {
    "exact_cycle_rank": b["cycle_rank"],
    "basis_cycle_lengths": b["basis_cycle_lengths"],
    "graph_artifact": "docs/data/f7_exact_graph.json",
    "basis_artifact": "docs/data/f7_cycle_basis.json"
}
data["generated_by_candidate_G2"]["7"] = {
    "full_coverage_verified": None,
    "note": "exact graph and cycle basis computed; generator classification pending"
}
data["certificates"]["7"] = {
    "type": "partial_exact_surface",
    "graph_artifact": "docs/data/f7_exact_graph.json",
    "basis_artifact": "docs/data/f7_cycle_basis.json"
}

Path("docs/data/g2_enumeration.json").write_text(json.dumps(data, indent=2))
print("updated docs/data/g2_enumeration.json with n=7 partial exact evidence")
