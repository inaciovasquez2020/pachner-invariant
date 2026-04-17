from pathlib import Path

def test_general_descent_theorem_status():
    s = Path("docs/math/GENERAL_DESCENT_THEOREM.md").read_text()
    assert "Status: Conditional." in s
    assert "theta (pachner23 T a b c p q) lam < theta T lam" in s

    assert "For lam > 0, vertexDeg T p <= 5, and vertexDeg T q <= 5," in s
