from pathlib import Path


def test_mathematical_closure_blocker_is_explicit():
 text = Path('docs/math/PACHNER23_MATHEMATICAL_CLOSURE_BLOCKER.md').read_text(encoding='utf-8')
 assert 'Status: Open.' in text
 assert 'allEdges_count_eq_edgeDeg_countP' in text
 assert 'rawEdges_count_eq_edgeDeg_countP' in text
 assert 'Full mathematical closure requires replacing' in text
