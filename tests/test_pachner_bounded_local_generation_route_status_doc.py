from pathlib import Path

def test_pachner_bounded_local_generation_route_status_doc():
    s = Path("docs/status/PACHNER_BOUNDED_LOCAL_GENERATION_ROUTE_STATUS.md").read_text()
    assert "Status: Conditional" in s
    assert "bounded local generation for relations and coherences in the Pachner move groupoid" in s
    assert "Forbidden overclaim" in s
