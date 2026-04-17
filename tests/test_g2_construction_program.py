from pathlib import Path

p = Path("docs/math/G2_CONSTRUCTION_PROGRAM.md")
s = p.read_text()

def test_status():
    assert "Status: Conditional" in s

def test_objective():
    assert "Construct an explicit finite family G_2" in s

def test_candidate_classes():
    assert "Pentagon circuit" in s
    assert "Square commutation circuit" in s

def test_upgrade_gate():
    assert "Do not upgrade status unless:" in s
