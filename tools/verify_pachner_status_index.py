#!/usr/bin/env python3
from pathlib import Path

doc = Path("docs/status/PACHNER_STATUS_INDEX.md").read_text(encoding="utf-8")

required = [
    "Status: Frozen pending descent certificate values",
    "count bridge theorem surface locked",
    "2--3 edge-degree chain theorem-level present",
    "certificate registry pending descent/topological-invariant certificates",
    "docs/status/PACHNER_COUNT_BRIDGE_THEOREM_STATUS_2026_04_26.md",
    "docs/status/PACHNER_CERTIFICATE_EVALUATION_REGISTRY.md",
    "docs/status/PACHNER_CERTIFICATE_VALUE_GATE.md",
    "artifacts/pachner_cert/pachner_certificate_registry.json",
    "tools/verify_pachner_count_bridge_theorem_status.py",
    "tools/verify_pachner_certificate_registry.py",
    "allEdges_count_eq_edgeDeg_countP",
    "allEdges_pachner23_count_delta",
    "edgeDeg_pachner23_delta",
    "edgeDeg_pachner23_eq_expected",
    "theta/descent closure",
    "penalty-control or equivalent local descent condition",
    "global descent gate",
    "PENDING\\_DESCENT\\_CERTIFICATE\\_EVALUATION",
    "No global Pachner descent theorem is asserted.",
    "No new topological invariant theorem is asserted.",
    "No further Pachner theorem-strengthening step is admissible without new descent certificate values.",
]

missing = [s for s in required if s not in doc]
if missing:
    raise SystemExit("Missing Pachner status-index literals:\n" + "\n".join(missing))

for forbidden in [
    "global Pachner descent theorem is proved",
    "topological invariant theorem is proved",
    "Pachner invariant is solved",
]:
    if forbidden in doc:
        raise SystemExit(f"Forbidden Pachner overclaim literal present: {forbidden}")

print("Pachner status index PASS")
