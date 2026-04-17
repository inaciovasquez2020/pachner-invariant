from pathlib import Path

def test_general_descent_theorem_status():
    s = Path("docs/math/GENERAL_DESCENT_THEOREM.md").read_text()
    assert "Status: NOT FORMALIZED" in s
    assert "theta (pachner23 T a b c p q) lam < theta T lam" in s
