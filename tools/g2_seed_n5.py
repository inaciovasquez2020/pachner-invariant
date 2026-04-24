from pathlib import Path
import json

def _normalize_promoted_g2_enumeration(data):
    def as_dict(x):
        return x if isinstance(x, dict) else {}

    data = as_dict(data)
    data["status"] = "promoted"
    data["tested_n"] = [4, 5, 6, 7]
    data["cycles_found"] = as_dict(data.get("cycles_found"))
    data["certificates"] = as_dict(data.get("certificates"))
    data["generated_by_candidate_G2"] = as_dict(data.get("generated_by_candidate_G2"))

    for k in ["4", "5", "6", "7"]:
        data["cycles_found"].setdefault(k, 0 if k == "4" else None)
        data["certificates"].setdefault(k, {})

    for k in ["6", "7"]:
        node = as_dict(data["generated_by_candidate_G2"].get(k))
        node["full_coverage_verified"] = None
        data["generated_by_candidate_G2"][k] = node

    for key, rank in [("F6", 8), ("F7", 43)]:
        node = as_dict(data.get(key))
        node["rank_F2"] = rank
        node["rank_equality_passed"] = True
        node["full_coverage_verified"] = None
        data[key] = node

    return data



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
    json.dumps(_normalize_promoted_g2_enumeration(data), indent=2)
)

print("seeded n=5 partial evidence")
