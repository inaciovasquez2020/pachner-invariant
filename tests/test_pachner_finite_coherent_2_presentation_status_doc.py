from pathlib import Path

def test_pachner_finite_coherent_2_presentation_status_doc():
    s = Path("docs/status/PACHNER_FINITE_COHERENT_2_PRESENTATION_STATUS.md").read_text()
    assert "Status: Conditional" in s
    assert "finite coherent 2-presentability of the Pachner move groupoid" in s
    assert "Completion truth condition" in s
