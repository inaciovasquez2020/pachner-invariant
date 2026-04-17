from pathlib import Path

s = Path("docs/status/CURRENT_SINGLE_FRONTIER.md").read_text()

def test_status():
    assert "Status: Conditional" in s

def test_current_frontier():
    assert "unconditional general descent theorem" in s

def test_conditional_cases_closed():
    assert "All conditional <=10 vertex-sum cases are closed." in s

def test_locked_layers():
    assert "repository layers are executable and locked" in s
