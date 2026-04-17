from pathlib import Path
import json

p = Path("docs/data/g2_enumeration.json")
data = json.loads(p.read_text())

data["status"] = "conditional"
if "tested_n" not in data:
    data["tested_n"] = [4, 5, 6, 7]

data["cycles_found"]["5"] = 1
data["generated_by_candidate_G2"]["5"] = {
    "full_coverage_verified": True,
    "generator_family": ["pentagon"],
    "reason": "F5 exact graph has cycle rank 1 and is a single pentagon"
}
data["certificates"]["5"] = {
    "type": "exact",
    "graph_artifact": "docs/data/f5_exact_graph.json",
    "status_note": "unique rank-1 cycle identified with pentagon generator"
}

Path("docs/data/g2_enumeration.json").write_text(json.dumps(data, indent=2))
print("updated docs/data/g2_enumeration.json with exact n=5 evidence")
