from pathlib import Path


CALL = Path("docs/status/CALL_TO_ARMS_2026_04_25.md")


def test_call_to_arms_scope_and_boundary():
    text = CALL.read_text(encoding="utf-8")

    assert "Status: PUBLIC VERIFICATION INVITATION." in text
    assert "This is not a claim of full PachnerInvariant theorem-layer completion." in text
    assert "bounded-G2 exact-rank surface for n in {6,7}" in text
    assert "It claims only that the current executable bounded-G2 exact-rank surface for n in {6,7} is certified and reproducible." in text


def test_call_to_arms_contains_reproduction_commands():
    text = CALL.read_text(encoding="utf-8")

    assert "tools/verify_admissible_bounded_g2_predicate.py" in text
    assert "tools/classify_bounded_g2_relation_witnesses.py" in text
    assert "tools/verify_bounded_g2_rank_cert.py" in text
    assert "python3 -m pytest -q" in text


def test_call_to_arms_contains_exact_rank_targets():
    text = CALL.read_text(encoding="utf-8")

    assert r"\dim_{\mathbb F_2} Z_1(F_6;\mathbb F_2)=8" in text
    assert r"\dim_{\mathbb F_2} Z_1(F_7;\mathbb F_2)=43" in text
    assert "rank(M_6)=nullity(∂_1)=8" in text
    assert "rank(M_7)=nullity(∂_1)=43" in text
