from pathlib import Path

def test_thetaz_sharp_criterion_status():
    s = Path("docs/math/THETAZ_SHARP_CRITERION.md").read_text(encoding="utf-8")
    assert "Status: Conditional." in s
    assert "iff" in s
    assert "vertexDeg T p + vertexDeg T q <= 10" in s
    assert "Universal unconditional descent is false in general." in s
