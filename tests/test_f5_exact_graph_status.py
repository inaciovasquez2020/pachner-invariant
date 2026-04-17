from pathlib import Path

p = Path("docs/status/F5_EXACT_GRAPH_STATUS.md")
s = p.read_text()

def test_status_conditional():
    assert "Status: Conditional" in s

def test_graph_counts_present():
    assert "flip graph F5 has 5 vertices" in s
    assert "flip graph F5 has 5 edges" in s
    assert "cycle rank(F5) = 1" in s

def test_pentagon_present():
    assert "the n=5 flip graph is a single pentagon" in s

def test_upgrade_gate_present():
    assert "do not promote beyond Conditional until the certificate is written." in s
