from pathlib import Path

def test_simsve_al2_status_doc():
    s = Path("docs/status/SIMSVE_AL2_STATUS.md").read_text()
    assert "Status: OPEN" in s
    assert "zero-stub looping" in s
    assert "support theorem" in s
