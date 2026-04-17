from pathlib import Path
import json

p = Path("docs/data/f6_cycle_basis.json")
data = json.loads(p.read_text())

basis = data["basis_cycles"]

classified = []
for i, cyc in enumerate(basis):
    L = cyc["cycle_length"]
    if L == 4:
        typ = "square_commutation"
        generated = True
    elif L == 5:
        typ = "pentagon"
        generated = True
    elif L == 7:
        typ = "derived_candidate"
        generated = None
    else:
        typ = "unknown"
        generated = None
    classified.append({
        "index": i,
        "cycle_length": L,
        "type": typ,
        "generated_by_G2": generated,
        "cycle_vertices": cyc["cycle_vertices"]
    })

summary = {
    "status": "conditional",
    "n": 6,
    "cycle_rank": data["cycle_rank"],
    "classified_cycles": classified,
    "counts": {
        "square_commutation": sum(1 for c in classified if c["type"]=="square_commutation"),
        "pentagon": sum(1 for c in classified if c["type"]=="pentagon"),
        "derived_candidate": sum(1 for c in classified if c["type"]=="derived_candidate")
    },
    "coverage_known": {
        "local_generators_verified": sum(1 for c in classified if c["generated_by_G2"] is True),
        "pending": sum(1 for c in classified if c["generated_by_G2"] is None)
    },
    "note": "4- and 5-cycles classified as local G2 generators; 7-cycles require explicit decomposition proof."
}

Path("docs/data/f6_cycle_classification.json").write_text(json.dumps(summary, indent=2))
print("wrote docs/data/f6_cycle_classification.json")
print(summary["counts"])
print(summary["coverage_known"])
