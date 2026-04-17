from pathlib import Path

p = Path("docs/status/CANONICAL_STOPPING_POINT.md")
s = p.read_text()

def test_status():
    assert "Status: Conditional" in s

def test_verified_block():
    assert "origin/main synced" in s
    assert "lake build passes" in s
    assert "pytest passes" in s

def test_remaining_layer():
    assert "actual G_2 cycle enumeration, coverage, and certificates" in s

def test_pause_recommendation():
    assert "Pause structural edits until new mathematical evidence exists." in s
