from pathlib import Path

def test_pachner_finite_presentation_axiom_doc():
    s = Path("docs/math/PACHNER_MOVE_FINITE_PRESENTATION_AXIOM.md").read_text()
    assert "finite presentation" in s
    assert "GH02t holds" in s
    assert "\\mathcal F:\\mathcal G_{\\mathrm{Pachner}}\\to \\mathbf{Ab}" in s
    assert "Axiom (external input)" in s
