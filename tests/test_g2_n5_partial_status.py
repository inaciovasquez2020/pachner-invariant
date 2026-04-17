from pathlib import Path

p = Path("docs/status/G2_N5_PARTIAL_STATUS.md")
s = p.read_text()

def test_status_conditional():
    assert "Status: Conditional" in s

def test_n4_certified_present():
    assert "n=4: trivial seeded evidence recorded." in s

def test_n5_partial_present():
    assert "n=5: pentagon candidate recorded." in s
    assert "n=5: full coverage not verified." in s

def test_open_items_present():
    assert "n=5: concrete cycle count" in s
    assert "n=5: full candidate-family coverage" in s
    assert "n=5: explicit decomposition certificates" in s
    assert "n=6: pending" in s
    assert "n=7: pending" in s

def test_upgrade_gate_present():
    assert "Do not promote beyond Conditional until n=5 has concrete cycle counts," in s
