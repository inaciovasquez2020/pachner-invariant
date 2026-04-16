from pathlib import Path

def test_pachner_localization_program_status_doc():
    s = Path("docs/status/PACHNER_LOCALIZATION_PROGRAM_STATUS.md").read_text()
    assert "Status: Conditional" in s
    assert "support-diameter functional on Pachner loops" in s
    assert "bounded local generation for relations and coherences" in s
