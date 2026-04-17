from pathlib import Path

def test_general_descent_theorem_status():
    s = Path("docs/math/GENERAL_DESCENT_THEOREM.md").read_text()
    assert "Status: Conditional." in s
    assert "vertexDeg T p + vertexDeg T q <= 10" in s

    assert "For lam > 0," in s
