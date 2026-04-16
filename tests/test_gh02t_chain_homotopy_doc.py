from pathlib import Path

def test_gh02t_chain_homotopy_doc():
    s = Path("docs/math/GH02T_CHAIN_HOMOTOPY_COHERENCE.md").read_text()
    assert "GH02t input" in s
    assert "\\Psi_p-\\Psi_q=\\partial_2^T H_{p,q}" in s
    assert "\\mathcal F:\\mathcal G_{\\mathrm{Pachner}}\\to \\mathbf{Ab}" in s
    assert "Conditional on GH02t" in s
