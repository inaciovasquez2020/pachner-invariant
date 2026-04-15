from pathlib import Path

def test_pachner23_frontier_doc():
    s = Path("docs/math/PACHNER23_FRONTIER.md").read_text()
    assert "OPEN" in s
    assert "general 2--3 move edge-degree package" in s
    assert "placeholder / axiom dependence" in s
    assert "No unconditional full closure is claimed" in s
