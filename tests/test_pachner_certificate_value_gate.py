import subprocess
import sys
from pathlib import Path


def test_pachner_certificate_value_gate_doc_locked() -> None:
    text = Path("docs/status/PACHNER_CERTIFICATE_VALUE_GATE.md").read_text(encoding="utf-8")
    assert "Status: Pending descent certificate values" in text
    assert "count bridge theorem surface locked" in text
    assert "2--3 edge-degree chain theorem-level present" in text
    assert "PENDING\\_DESCENT\\_CERTIFICATE\\_EVALUATION" in text
    assert "No global Pachner descent theorem is asserted." in text
    assert "No stronger claim is valid without actual descent certificate values." in text


def test_pachner_certificate_value_gate_verifier_passes() -> None:
    result = subprocess.run(
        [sys.executable, "tools/verify_pachner_certificate_value_gate.py"],
        check=True,
        capture_output=True,
        text=True,
    )
    assert "Pachner certificate value gate PASS" in result.stdout
