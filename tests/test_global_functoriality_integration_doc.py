from pathlib import Path

def test_global_functoriality_integration_doc():
    s = Path("docs/math/GLOBAL_FUNCTORIALITY_INTEGRATION.md").read_text()
    assert "\\mathcal F(X):=\\varinjlim_{S\\in\\mathcal I_X} H_1^S(X)." in s
    assert "f_{S,T}:H_1^S(X)\\to H_1^T(Y)" in s
    assert "\\phi^Y_{T,T'}\\circ f_{S,T}=f_{S,T'}" in s
    assert "f_{S',T}\\circ \\phi^X_{S,S'}=f_{S,T}" in s
    assert "\\mathcal F(f)([x]_S):=[f_{S,T}(x)]_T" in s
    assert "not a full functor" in s
