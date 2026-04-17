from pathlib import Path
import json

p = Path("docs/data/g2_enumeration.json")
data = json.loads(p.read_text())

# Manual seed placeholders for first nontrivial evidence layer.
data["cycles_found"] = {
    "4": 0,
    "5": None,
    "6": None,
    "7": None
}

data["generated_by_candidate_G2"] = {
    "4": True,
    "5": None,
    "6": None,
    "7": None
}

data["certificates"]["4"] = {
    "reason": "quadrilateral flip graph has no nontrivial closed circuit"
}

data["note"] = "n=4 seeded; replace remaining None by actual outputs"

Path("docs/data/g2_enumeration.json").write_text(
    json.dumps(data, indent=2)
)

print("seeded docs/data/g2_enumeration.json")
