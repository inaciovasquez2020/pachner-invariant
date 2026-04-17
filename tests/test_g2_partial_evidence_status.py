from pathlib import Path

p = Path("docs/status/G2_PARTIAL_EVIDENCE_STATUS.md")
s = p.read_text()

def test_status_conditional():
    assert "Status: Conditional" in s

def test_n4_certified():
    assert "n=4: seeded trivial evidence recorded." in s

def test_open_n5_n6_n7():
    assert "n=5: cycle enumeration pending" in s
    assert "n=6: cycle enumeration pending" in s
    assert "n=7: cycle enumeration pending" in s

def test_upgrade_condition():
    assert "Do not promote beyond Conditional" in s
