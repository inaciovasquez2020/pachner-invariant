from pathlib import Path

p = Path("docs/status/PACHNER_LOCALIZATION_PROGRAM_STATUS.md")
s = p.read_text()

def test_status_conditional():
    assert "- Status: Conditional" in s

def test_remaining_theorem_present():
    assert "Remaining theorem: bounded local generation for relations and coherences" in s

def test_frontier_lock_link_present():
    assert "Frontier lock: docs/math/BOUNDED_LOCAL_GENERATION_FRONTIER.md" in s
