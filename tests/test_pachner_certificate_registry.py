import json
import subprocess
import sys
from pathlib import Path


def test_pachner_certificate_registry_json_locked() -> None:
    data = json.loads(Path("artifacts/pachner_cert/pachner_certificate_registry.json").read_text(encoding="utf-8"))
    assert data["status"] == "PENDING_DESCENT_CERTIFICATE_EVALUATION"
    assert data["count_bridge"]["allEdges_count_eq_edgeDeg_countP"]["theorem_level_present"] is True
    assert data["edge_degree_chain"]["allEdges_pachner23_count_delta"]["theorem_level_present"] is True
    assert data["edge_degree_chain"]["edgeDeg_pachner23_delta"]["theorem_level_present"] is True
    assert data["edge_degree_chain"]["edgeDeg_pachner23_eq_expected"]["theorem_level_present"] is True
    assert data["locked_theorem"]["global_descent_claim"] is False
    assert data["locked_theorem"]["topological_invariant_claim"] is False


def test_pachner_certificate_registry_doc_locked() -> None:
    text = Path("docs/status/PACHNER_CERTIFICATE_EVALUATION_REGISTRY.md").read_text(encoding="utf-8")
    assert "Status: Pending descent certificate evaluation" in text
    assert "allEdges_count_eq_edgeDeg_countP" in text
    assert "edgeDeg_pachner23_eq_expected" in text
    assert "PENDING\\_DESCENT\\_CERTIFICATE\\_EVALUATION" in text
    assert "No global Pachner descent theorem is asserted." in text
    assert "No new topological invariant theorem is asserted." in text
    assert "No count-bridge axiom remains live in the current theorem-level chain." in text


def test_pachner_certificate_registry_verifier_passes() -> None:
    result = subprocess.run(
        [sys.executable, "tools/verify_pachner_certificate_registry.py"],
        check=True,
        capture_output=True,
        text=True,
    )
    assert "Pachner certificate registry PASS" in result.stdout
