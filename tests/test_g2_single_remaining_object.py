from pathlib import Path

p = Path("docs/status/G2_SINGLE_REMAINING_OBJECT.md")
s = p.read_text()

def test_status_conditional():
    assert "Status: Conditional" in s

def test_single_remaining_object_present():
    assert "Single remaining object:" in s
    assert "n=5, n=6, and n=7" in s

def test_current_state_present():
    assert "n=4: certified seeded evidence" in s
    assert "n=5: partial seeded evidence only" in s
    assert "n=6: pending" in s
    assert "n=7: pending" in s

def test_upgrade_gate_present():
    assert "Do not promote beyond Conditional until n=5,6,7 have concrete cycle counts," in s
