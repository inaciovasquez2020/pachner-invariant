from pathlib import Path

def test_pachner_invariant_status():
    s = Path("docs/status/PACHNER_INVARIANT_STATUS.md").read_text()
    assert "Status: OPEN" in s
    assert "general descent theorem not yet formalized under explicit admissibility hypotheses." in s
    assert "If the general descent theorem is formalized under explicit admissibility hypotheses, then the current frontier closes." in s
