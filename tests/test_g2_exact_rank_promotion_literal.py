from pathlib import Path
import json

def test_g2_exact_rank_promotion_literal():
    frontier = Path("docs/CURRENT_FRONTIER_2026_04.md").read_text(encoding="utf-8")
    readme = Path("README.md").read_text(encoding="utf-8")
    enum_payload = json.loads(Path("docs/data/g2_enumeration.json").read_text(encoding="utf-8"))
    span_payload = json.loads(Path("docs/data/g2_exact_span_check.json").read_text(encoding="utf-8"))

    assert "Status: Exact bounded \\(G_2\\) rank certification complete." in frontier
    assert "\\operatorname{rank}_{\\mathbb F_2}(M_{F6})=8" in frontier
    assert "\\operatorname{rank}_{\\mathbb F_2}(M_{F7})=43" in frontier
    assert "Status: Exact bounded G_2 rank certification complete." in readme

    assert enum_payload["status"] == "promoted"
    assert enum_payload["F6"]["rank_F2"] == 8
    assert enum_payload["F7"]["rank_F2"] == 43
    assert enum_payload["F6"]["rank_equality_passed"] is True
    assert enum_payload["F7"]["rank_equality_passed"] is True

    assert span_payload["F6"]["rank"] == 8
    assert span_payload["F7"]["rank"] == 43
    assert span_payload["F6"]["rank_equality_passed"] is True
    assert span_payload["F7"]["rank_equality_passed"] is True
