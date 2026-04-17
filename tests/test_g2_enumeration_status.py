from pathlib import Path

p = Path("docs/status/G2_ENUMERATION_STATUS.md")
s = p.read_text()

def test_status_conditional():
    assert "Status: Conditional" in s

def test_stub_statement_present():
    assert "Current registry artifact is a stub." in s

def test_upgrade_conditions_present():
    assert "replace cycles_found by actual enumerated cycle counts" in s
    assert "replace generated_by_candidate_G2 by actual coverage data" in s
    assert "attach explicit candidate-family certification results for n = 4,5,6,7." in s
