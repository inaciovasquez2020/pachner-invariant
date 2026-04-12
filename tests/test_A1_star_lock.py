from pathlib import Path

def test_A1_star_lock():
    d = Path("docs/math/A1_STAR_NORMALIZED_EDGE_INJECTIVITY.md").read_text()
    assert "implying A1, hence the count bridge A" in d
