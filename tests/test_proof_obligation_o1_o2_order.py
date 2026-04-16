from pathlib import Path

def test_proof_obligation_o1_o2_order():
    s = Path("docs/status/PROOF_OBLIGATION_REGISTRY.md").read_text()
    assert "O1. Edge-incidence delta theorem" in s
    assert "O2. Vertex-incidence delta theorem" in s
