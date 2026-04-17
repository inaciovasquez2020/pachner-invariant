from pathlib import Path
import json

def load(path):
    return json.loads(Path(path).read_text())

# We construct a conservative computational certification surface.
# Since explicit edge-incidence generators are not yet encoded in repo data,
# we certify dimension bounds implied by observed local cycles.

f6 = load("docs/data/f6_cycle_classification.json")
f7 = load("docs/data/f7_cycle_basis.json")

f6_rank = f6["cycle_rank"]
f6_local = f6["coverage_known"]["local_generators_verified"]
f6_pending = f6["coverage_known"]["pending"]

f7_rank = f7["cycle_rank"]
lengths = f7["basis_cycle_lengths"]
f7_local_visible = sum(1 for x in lengths if x in (4,5))
f7_long = sum(1 for x in lengths if x not in (4,5))

out = {
    "status": "conditional",
    "field": "F2",
    "generator_family": ["square_commutation", "pentagon"],
    "F6": {
        "cycle_rank": f6_rank,
        "local_basis_cycles_detected": f6_local,
        "pending_long_cycles": f6_pending,
        "conditional_span_statement":
            "If each pending 7-cycle decomposes into local generators, then full span holds."
    },
    "F7": {
        "cycle_rank": f7_rank,
        "visible_local_basis_cycles": f7_local_visible,
        "visible_long_basis_cycles": f7_long,
        "conditional_span_statement":
            "If each long basis cycle decomposes into local generators, then full span holds."
    },
    "next_exact_input_needed":
        "Edge-incidence vectors for every square and pentagon generator."
}

Path("docs/data/g2_span_check.json").write_text(json.dumps(out, indent=2))
print("wrote docs/data/g2_span_check.json")
