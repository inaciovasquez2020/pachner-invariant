from pathlib import Path

p = Path("docs/status/NEXT_G2_UPGRADE_GATE.md")
s = p.read_text()

def test_status_conditional():
    assert "Status: Conditional" in s

def test_cycles_found_gate():
    assert "cycles_found has concrete values for n=4,5,6,7" in s

def test_generated_by_candidate_G2_gate():
    assert "generated_by_candidate_G2 has concrete coverage results for n=4,5,6,7" in s

def test_certificates_gate():
    assert "certificates records explicit candidate-family witnesses" in s
