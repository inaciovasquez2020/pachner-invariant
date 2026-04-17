from pathlib import Path

p = Path("docs/math/D2_FLIP_GRAPH_CIRCUIT_FRONTIER.md")
s = p.read_text()

def test_status_conditional():
    assert "Status: Conditional" in s

def test_target_present():
    assert "finite bounded local generating set G_2" in s

def test_diameter_form_present():
    assert "support diameter at most C_2" in s

def test_role_present():
    assert "d=2 test surface for bounded local generation" in s
