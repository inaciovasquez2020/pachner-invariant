from pathlib import Path

def test_theta_invariant_surface():
    s = Path("docs/structure/INVARIANT_FORMAL_SPEC.md").read_text()
    assert "Θ(T, λ)" in s
    assert "deg_e" in s
    assert "deg_v" in s
    assert "(deg_e(T) - 3)^2" in s
    assert "(deg_v(T) - 6)^2" in s
