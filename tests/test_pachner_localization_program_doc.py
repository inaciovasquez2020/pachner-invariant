from pathlib import Path

def test_pachner_localization_program_doc():
    s = Path("docs/math/PACHNER_LOCALIZATION_PROGRAM.md").read_text()
    assert "# Conditional: localization program for the Pachner coherence theorem" in s
    assert "Define the energy functional" in s
    assert "E(\\gamma)=(D(\\gamma),L(\\gamma))" in s
    assert "Dimension-2 test case" in s
    assert "bistellar word diagrams" in s
    assert "Conditional." in s
