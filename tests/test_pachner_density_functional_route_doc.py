from pathlib import Path

def test_pachner_density_functional_route_doc():
    s = Path("docs/math/PACHNER_DENSITY_FUNCTIONAL_ROUTE.md").read_text()
    assert "# Conditional: density-functional route for Pachner coherence" in s
    assert "The density-functional route is a sufficient conditional reduction" in s
    assert "Do not assert descent holds." in s
    assert "In \\(d=2\\), squares" in s
    assert "Conditional." in s
