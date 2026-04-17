from pathlib import Path

p = Path("docs/status/FROZEN_EXECUTABLE_CLOSURE.md")
s = p.read_text()

def test_status():
    assert "Status: Conditional" in s

def test_executable_state():
    assert "lake build passes" in s
    assert "pytest suite passes" in s

def test_open_math_layer():
    assert "actual G_2 enumeration evidence for n=5,6,7" in s

def test_no_stronger_claim():
    assert "No stronger claim permitted without concrete evidence." in s
