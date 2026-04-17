from pathlib import Path
import json

p = Path("docs/data/g2_enumeration.json")
data = json.loads(p.read_text())

# Conservative placeholder evidence layer for n=5.
# Replace these values only with actual enumerator output.

data["cycles_found"]["5"] = {
    "known_minimal_candidate": "pentagon",
    "count_verified": None
}

data["generated_by_candidate_G2"]["5"] = {
    "pentagon_present": True,
    "full_coverage_verified": None
}

data["certificates"]["5"] = {
    "candidate_cycle": "5-cycle associahedron pentagon",
    "status": "partial seed only"
}

data["note"] = "n=4 seeded; n=5 partial seed added; replace placeholders by actual outputs"

Path("docs/data/g2_enumeration.json").write_text(
    json.dumps(data, indent=2)
)

print("seeded n=5 partial evidence")
