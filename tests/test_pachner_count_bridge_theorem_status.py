import subprocess
import sys
from pathlib import Path


def test_pachner_count_bridge_theorem_status_doc_locked() -> None:
    text = Path("docs/status/PACHNER_COUNT_BRIDGE_THEOREM_STATUS_2026_04_26.md").read_text(encoding="utf-8")
    assert "Status: Theorem-level bridge synchronized" in text
    assert "allEdges_count_eq_edgeDeg_countP" in text
    assert "allEdges_pachner23_count_delta" in text
    assert "edgeDeg_pachner23_delta" in text
    assert "edgeDeg_pachner23_eq_expected" in text
    assert "Lean build: PASS" in text
    assert "pytest: 295/295 passed" in text
    assert "No global Pachner descent theorem is asserted here." in text
    assert "No new topological invariant theorem is asserted here." in text


def test_pachner_count_bridge_theorem_status_verifier_passes() -> None:
    result = subprocess.run(
        [sys.executable, "tools/verify_pachner_count_bridge_theorem_status.py"],
        check=True,
        capture_output=True,
        text=True,
    )
    assert "Pachner count bridge theorem status PASS" in result.stdout
