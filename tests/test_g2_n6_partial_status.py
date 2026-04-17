from pathlib import Path

p = Path("docs/status/G2_N6_PARTIAL_STATUS.md")
s = p.read_text()

def test_status_conditional():
    assert "Status: Conditional" in s

def test_exact_evidence_present():
    assert "cycle rank(F6) = 8" in s
    assert "basis cycle lengths are [5, 4, 5, 7, 7, 5, 5, 7]" in s

def test_registry_targets_present():
    assert "docs/data/f6_exact_graph.json" in s
    assert "docs/data/f6_cycle_basis.json" in s
    assert "docs/data/g2_enumeration.json" in s

def test_upgrade_gate_present():
    assert "Do not promote beyond Conditional until n=6 full coverage is certified." in s
