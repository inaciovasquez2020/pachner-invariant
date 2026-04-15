from pathlib import Path

def test_pachner_invariant_status():
    s = Path("docs/status/PACHNER_INVARIANT_STATUS.md").read_text()
    assert "Status: OPEN" in s
    assert "general 2--3 move edge-degree package" in s
    assert "associated frontier lemmas" in s
    assert "If the general 2--3 move package is proved and placeholder / axiom dependence is removed" in s
