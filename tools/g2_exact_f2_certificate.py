from pathlib import Path
import json

# Exact certificate scaffold:
# builds canonical next object needed for closure:
# edge-incidence vectors for local generators.

out = {
  "status": "conditional",
  "field": "F2",
  "targets": {
    "F6": {
      "cycle_rank": 8,
      "required_exact_input": [
        "enumerate every square commutation cycle as edge-incidence vector",
        "enumerate every pentagon cycle as edge-incidence vector",
        "row-reduce generator matrix over F2",
        "verify rank = 8"
      ],
      "closure_if_verified":
        "CycleSpace(F6)=<square,pentagon>"
    },
    "F7": {
      "cycle_rank": 43,
      "required_exact_input": [
        "enumerate every square commutation cycle as edge-incidence vector",
        "enumerate every pentagon cycle as edge-incidence vector",
        "row-reduce generator matrix over F2",
        "verify rank = 43"
      ],
      "closure_if_verified":
        "CycleSpace(F7)=<square,pentagon>"
    }
  },
  "single_remaining_wall":
    "construct exact generator incidence matrices"
}

Path("docs/data/g2_exact_f2_certificate.json").write_text(json.dumps(out, indent=2))
print("wrote docs/data/g2_exact_f2_certificate.json")
