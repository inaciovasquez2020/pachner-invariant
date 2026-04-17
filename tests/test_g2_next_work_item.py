from pathlib import Path

p = Path("docs/status/G2_NEXT_WORK_ITEM.md")
s = p.read_text()

def test_status_conditional():
    assert "Status: Conditional" in s

def test_n5_task_present():
    assert "enumerate d=2 flip-graph cycles for n=5" in s

def test_coverage_task_present():
    assert "test candidate-family G_2 coverage" in s

def test_no_promotion_gate():
    assert "Do not promote beyond Conditional until n=5 evidence is concrete." in s
