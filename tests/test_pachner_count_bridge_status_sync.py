from pathlib import Path


def test_count_bridge_is_not_documented_as_live_axiom() -> None:
    registry = Path("docs/status/PACHNER_FRONTIER_REGISTRY.md").read_text(encoding="utf-8")
    target = Path("docs/math/NEXT_AXIOM_TARGET.md").read_text(encoding="utf-8")
    count_target = Path("docs/math/ALL_EDGES_COUNT_EQ_EDGEDEG_COUNTP_TARGET.md").read_text(encoding="utf-8")

    combined = "\n".join([registry, target, count_target])

    assert "`allEdges_count_eq_edgeDeg_countP` — theorem-level present" in registry
    assert "Do not relabel `allEdges_count_eq_edgeDeg_countP` as a live axiom" in target
    assert "Do not treat this bridge as a live axiom target" in count_target

    forbidden = [
        "axiom allEdges_count_eq_edgeDeg_countP",
        "This is the next axiom target in the Pachner 2--3 frontier.",
        "core 2-3 move delta layer still axiomatic",
        "Replace allEdges_count_eq_edgeDeg_countP by a proved theorem",
    ]
    for phrase in forbidden:
        assert phrase not in combined


def test_count_bridge_theorem_files_exist() -> None:
    lean = Path("PachnerInvariant/allEdges_count_eq_edgeDeg_countP.lean").read_text(encoding="utf-8")
    frontier = Path("PachnerInvariant/frontier.lean").read_text(encoding="utf-8")

    assert "theorem allEdges_count_eq_edgeDeg_countP" in lean
    assert "import PachnerInvariant.allEdges_count_eq_edgeDeg_countP" in frontier
    assert "rw [← allEdges_count_eq_edgeDeg_countP" in frontier
    assert "theorem allEdges_pachner23_count_delta" in frontier
    assert "theorem edgeDeg_pachner23_delta" in frontier
