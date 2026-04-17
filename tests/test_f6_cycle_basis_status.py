from pathlib import Path

p = Path("docs/status/F6_CYCLE_BASIS_STATUS.md")
s = p.read_text()

def test_status_conditional():
    assert "Status: Conditional" in s

def test_rank_present():
    assert "cycle rank(F6) = 8" in s

def test_lengths_present():
    assert "basis cycle lengths are [5, 4, 5, 7, 7, 5, 5, 7]" in s

def test_open_gate_present():
    assert "do not promote beyond Conditional until the certificates are written." in s
