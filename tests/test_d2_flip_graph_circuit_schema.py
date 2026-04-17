from pathlib import Path

p = Path("docs/math/D2_FLIP_GRAPH_CIRCUIT_SCHEMA.md")
s = p.read_text()

def test_status_conditional():
    assert "Status: Conditional" in s

def test_g2_present():
    assert "Define a finite family G_2" in s

def test_uniform_bound_present():
    assert "There exists C_2 < ∞" in s

def test_completion_condition_present():
    assert "the elementary family G_2 is explicit" in s
