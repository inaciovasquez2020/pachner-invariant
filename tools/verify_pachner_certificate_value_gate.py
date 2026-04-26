#!/usr/bin/env python3
import json
from pathlib import Path

doc = Path("docs/status/PACHNER_CERTIFICATE_VALUE_GATE.md").read_text(encoding="utf-8")
reg = json.loads(Path("artifacts/pachner_cert/pachner_certificate_registry.json").read_text(encoding="utf-8"))

required_doc_literals = [
    "Status: Pending descent certificate values",
    "count bridge theorem surface locked",
    "2--3 edge-degree chain theorem-level present",
    "certificate registry pending descent/topological-invariant evaluation",
    "theta/descent closure",
    "penalty-control or equivalent local descent condition",
    "global descent gate",
    "PENDING\\_DESCENT\\_CERTIFICATE\\_EVALUATION",
    "No global Pachner descent theorem is asserted.",
    "No new topological invariant theorem is asserted.",
    "No count-bridge axiom remains live in the current theorem-level chain.",
    "No stronger claim is valid without actual descent certificate values.",
]

missing = [s for s in required_doc_literals if s not in doc]
if missing:
    raise SystemExit("Missing Pachner value-gate literals:\n" + "\n".join(missing))

if reg["status"] != "PENDING_DESCENT_CERTIFICATE_EVALUATION":
    raise SystemExit("Registry must remain pending unless certificates are verified")

pending = reg["pending_certificates"]
for key in ["theta_delta_closure", "penalty_control", "global_descent_gate"]:
    if pending[key]["verified"] is not False:
        raise SystemExit(f"{key} must remain unverified until actual certificate values exist")

for forbidden in [
    "global Pachner descent theorem is proved",
    "topological invariant theorem is proved",
    "Pachner invariant is solved",
]:
    if forbidden in doc:
        raise SystemExit(f"Forbidden Pachner overclaim literal present: {forbidden}")

print("Pachner certificate value gate PASS")
