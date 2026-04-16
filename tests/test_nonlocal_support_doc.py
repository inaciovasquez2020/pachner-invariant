from pathlib import Path

def test_nonlocal_support_doc():
    s = Path("docs/math/NONLOCAL_SUPPORT_THEOREM.md").read_text()
    assert "Δ_inc(e) = 0" in s
    assert "local edge set" in s
