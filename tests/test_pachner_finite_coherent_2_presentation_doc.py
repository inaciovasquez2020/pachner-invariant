from pathlib import Path

def test_pachner_finite_coherent_2_presentation_doc():
    p = Path("docs/math/PACHNER_FINITE_COHERENT_2_PRESENTATION_THEOREM.md")
    s = p.read_text()
    assert "finite coherent 2-presentation" in s
    assert "Finite presentability is insufficient" in s
    assert "Conditional." in s
