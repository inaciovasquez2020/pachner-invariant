from pathlib import Path
import json

out = {
    "status": "conditional",
    "tested_n": [4,5,6,7],
    "cycles_found": {},
    "generated_by_candidate_G2": {},
    "note": "stub registry awaiting actual enumerator"
}

Path("docs/data/g2_enumeration_stub.json").write_text(
    json.dumps(out, indent=2)
)
print("wrote docs/data/g2_enumeration_stub.json")
