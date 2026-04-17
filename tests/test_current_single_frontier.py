from pathlib import Path

p = Path("docs/status/CURRENT_SINGLE_FRONTIER.md")
s = p.read_text()

def test_status():
    assert "Status: Conditional" in s

def test_only_remaining_frontier():
    assert "only remaining first-class frontier" in s

def test_g2_present():
    assert "General descent theorem not yet formalized under explicit admissibility hypotheses." in s

def test_locked_layers():
    assert "repository layers are executable and locked" in s
