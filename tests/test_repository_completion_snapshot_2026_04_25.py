import json
import subprocess
import sys
from pathlib import Path


SNAPSHOT = Path("docs/status/REPOSITORY_COMPLETION_SNAPSHOT_2026_04_25.md")
CERT6 = Path("docs/data/Cert_6.with_witnesses.json")
CERT7 = Path("docs/data/Cert_7.with_witnesses.json")


def test_repository_completion_snapshot_scope():
    text = SNAPSHOT.read_text(encoding="utf-8")
    assert "Status: EXECUTABLE-SURFACE COMPLETE." in text
    assert "does not claim full PachnerInvariant theorem-layer completion" in text
    assert "bounded-G2 exact-rank certification is executable-certified for n in {6,7}" in text
    assert "It does not close unrelated or future PachnerInvariant theorem-layer obligations." in text


def test_repository_completion_snapshot_certified_rank_claims():
    text = SNAPSHOT.read_text(encoding="utf-8")
    assert "rank_M = 8" in text
    assert "nullity_d1 = 8" in text
    assert "rank_M = 43" in text
    assert "nullity_d1 = 43" in text
    assert r"\dim_{\mathbb F_2} Z_1(F_6;\mathbb F_2)=8" in text
    assert r"\dim_{\mathbb F_2} Z_1(F_7;\mathbb F_2)=43" in text


def test_repository_completion_snapshot_certificates_exist():
    for path, n, expected_rank in [(CERT6, 6, 8), (CERT7, 7, 43)]:
        assert path.exists()
        data = json.loads(path.read_text(encoding="utf-8"))
        assert data["certificate_schema"] == "BoundedG2RankCert"
        assert data["field"] == "F2"
        assert data["n"] == n
        assert data["expected_rank"] == expected_rank
        assert data["relation_witnesses"]


def test_repository_completion_snapshot_verifiers_pass():
    commands = [
        [sys.executable, "tools/verify_admissible_bounded_g2_predicate.py", str(CERT6), str(CERT7)],
        [sys.executable, "tools/classify_bounded_g2_relation_witnesses.py", str(CERT6), str(CERT7)],
        [sys.executable, "tools/verify_bounded_g2_rank_cert.py", str(CERT6), str(CERT7)],
    ]

    for command in commands:
        result = subprocess.run(command, text=True, capture_output=True, check=True)
        report = json.loads(result.stdout)
        assert report["status"] == "PASS"
