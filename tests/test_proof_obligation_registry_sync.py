from pathlib import Path

def test_proof_obligation_registry_sync():
    s = Path("docs/status/PROOF_OBLIGATION_REGISTRY.md").read_text()
    assert "O1. Edge-incidence delta theorem" in s
    assert "O5. ΔΘ expansion theorem" in s
    assert "O8. Claim-boundary note" in s
