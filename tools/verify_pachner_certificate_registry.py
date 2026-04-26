#!/usr/bin/env python3
import json
from pathlib import Path

registry_path = Path("artifacts/pachner_cert/pachner_certificate_registry.json")
data = json.loads(registry_path.read_text(encoding="utf-8"))

if data.get("certificate") != "Pachner certified frontier registry":
    raise SystemExit("Wrong certificate registry name")

if data.get("status") != "PENDING_DESCENT_CERTIFICATE_EVALUATION":
    raise SystemExit("Registry must remain pending until descent certificates are verified")

locked = data.get("locked_theorem", {})
if locked.get("global_descent_claim") is not False:
    raise SystemExit("Forbidden global descent claim")
if locked.get("topological_invariant_claim") is not False:
    raise SystemExit("Forbidden topological invariant claim")

lean = Path("PachnerInvariant/allEdges_count_eq_edgeDeg_countP.lean").read_text(encoding="utf-8")
frontier = Path("PachnerInvariant/frontier.lean").read_text(encoding="utf-8")
doc = Path("docs/status/PACHNER_CERTIFICATE_EVALUATION_REGISTRY.md").read_text(encoding="utf-8")

required_lean = [
    "theorem allEdges_count_eq_edgeDeg_countP",
]

required_frontier = [
    "import PachnerInvariant.allEdges_count_eq_edgeDeg_countP",
    "theorem allEdges_pachner23_count_delta",
    "theorem edgeDeg_pachner23_delta",
    "theorem edgeDeg_pachner23_eq_expected",
]

required_doc = [
    "Status: Pending descent certificate evaluation",
    "allEdges_count_eq_edgeDeg_countP",
    "allEdges_pachner23_count_delta",
    "edgeDeg_pachner23_delta",
    "edgeDeg_pachner23_eq_expected",
    "PENDING\\_DESCENT\\_CERTIFICATE\\_EVALUATION",
    "No global Pachner descent theorem is asserted.",
    "No new topological invariant theorem is asserted.",
    "No count-bridge axiom remains live in the current theorem-level chain.",
]

for s in required_lean:
    if s not in lean:
        raise SystemExit(f"Missing Lean count-bridge literal: {s}")

for s in required_frontier:
    if s not in frontier:
        raise SystemExit(f"Missing frontier theorem/import literal: {s}")

missing_doc = [s for s in required_doc if s not in doc]
if missing_doc:
    raise SystemExit("Missing Pachner certificate registry doc literals:\n" + "\n".join(missing_doc))

pending = data.get("pending_certificates", {})
for key in ["theta_delta_closure", "penalty_control", "global_descent_gate"]:
    if pending.get(key, {}).get("verified") is not False:
        raise SystemExit(f"{key} must remain unverified until actual certificate is supplied")

for forbidden in [
    "axiom allEdges_count_eq_edgeDeg_countP",
    "global Pachner descent theorem is proved",
    "topological invariant theorem is proved",
]:
    if forbidden in doc:
        raise SystemExit(f"Forbidden overclaim/stale literal present: {forbidden}")

print("Pachner certificate registry PASS")
