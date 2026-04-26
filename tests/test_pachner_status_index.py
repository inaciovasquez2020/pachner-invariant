import subprocess
import sys
from pathlib import Path


def test_pachner_status_index_doc_locked() -> None:
    text = Path("docs/status/PACHNER_STATUS_INDEX.md").read_text(encoding="utf-8")
    assert "Status: Frozen pending descent certificate values" in text
    assert "count bridge theorem surface locked" in text
    assert "2--3 edge-degree chain theorem-level present" in text
    assert "certificate registry pending descent/topological-invariant certificates" in text
    assert "allEdges_count_eq_edgeDeg_countP" in text
    assert "edgeDeg_pachner23_eq_expected" in text
    assert "PENDING\\_DESCENT\\_CERTIFICATE\\_EVALUATION" in text
    assert "No global Pachner descent theorem is asserted." in text
    assert "No further Pachner theorem-strengthening step is admissible without new descent certificate values." in text


def test_pachner_status_index_verifier_passes() -> None:
    result = subprocess.run(
        [sys.executable, "tools/verify_pachner_status_index.py"],
        check=True,
        capture_output=True,
        text=True,
    )
    assert "Pachner status index PASS" in result.stdout
