from pathlib import Path

def test_structural_stack_status():
    s = Path("docs/status/STRUCTURAL_STACK_STATUS.md").read_text()
    assert "Status: LOCKED" in s
