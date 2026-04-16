from pathlib import Path

def test_gh02t_reduction_doc():
    s = Path("docs/math/GH02T_REDUCTION_TO_FINITE_PRESENTABILITY.md").read_text()
    assert "GH02t is equivalent to the assertion that every loop in \\(\\mathcal P\\) is null-homologous" in s
    assert "Inverse cancellation" in s
    assert "Disjoint move commutation" in s
    assert "Local bistellar relations" in s
    assert "GH02t reduces to finite presentability of the Pachner move 2-complex" in s
    assert "Conditional." in s
