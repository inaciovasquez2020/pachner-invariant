from pathlib import Path

def test_post_thetaz_closure_status():
    s = Path("docs/status/POST_THETAZ_CLOSURE_STATUS.md").read_text(encoding="utf-8")
    assert "ThetaZ sharp-criterion route closed." in s
    assert "186 tests passed." in s

def test_general_descent_frontier_exists():
    s = Path("docs/math/GENERAL_DESCENT_BEYOND_THETAZ.md").read_text(encoding="utf-8")
    assert "Status: Open Frontier." in s
    assert "vertexDeg T p + vertexDeg T q <= 10" in s
