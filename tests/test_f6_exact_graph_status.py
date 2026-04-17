from pathlib import Path

p = Path("docs/status/F6_EXACT_GRAPH_STATUS.md")
s = p.read_text()

def test_status_conditional():
    assert "Status: Conditional" in s

def test_graph_counts_present():
    assert "flip graph F6 has 14 vertices" in s
    assert "flip graph F6 has 21 edges" in s
    assert "F6 is connected" in s
    assert "cycle rank(F6) = 8" in s

def test_interpretation_present():
    assert "the n=6 flip graph exact surface is now computed" in s

def test_upgrade_gate_present():
    assert "do not promote beyond Conditional until the certificates are written." in s
