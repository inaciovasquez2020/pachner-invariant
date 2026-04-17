from pathlib import Path

p = Path("docs/math/BOUNDED_LOCAL_GENERATION_FRONTIER.md")
s = p.read_text()

def test_status():
    assert "Status: Conditional" in s

def test_contains_remaining_theorem():
    assert "There exists a universal constant C" in s

def test_contains_support_diameter():
    assert "Support-diameter functional" in s

def test_contains_reduction_path():
    assert "flip-graph circuit classification" in s
