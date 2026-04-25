import json
import subprocess
import sys
from pathlib import Path


STATUS = Path("docs/status/BOUNDED_G2_EXACT_RANK_CERTIFICATION_2026_04_25.md")
CERT6 = Path("docs/data/Cert_6.with_witnesses.json")
CERT7 = Path("docs/data/Cert_7.with_witnesses.json")


def test_status_document_scope_and_exact_claims():
    text = STATUS.read_text(encoding="utf-8")

    assert "Status: EXECUTABLE-CERTIFIED for n in {6,7}." in text
    assert "bounded-G2 exact-rank certification only" in text
    assert "does not claim full PachnerInvariant theorem-layer completion" in text
    assert "dim_{\\mathbb F_2} Z_1(F_6;\\mathbb F_2)=8" in text
    assert "dim_{\\mathbb F_2} Z_1(F_7;\\mathbb F_2)=43" in text
    assert "It does not close unrelated PachnerInvariant obligations." in text


def test_bounded_g2_cert_files_exist_and_have_expected_targets():
    for path, n, expected_rank in [(CERT6, 6, 8), (CERT7, 7, 43)]:
        assert path.exists()
        data = json.loads(path.read_text(encoding="utf-8"))
        assert data["certificate_schema"] == "BoundedG2RankCert"
        assert data["field"] == "F2"
        assert data["n"] == n
        assert data["expected_rank"] == expected_rank
        assert data["relation_witnesses"]


def test_bounded_g2_rank_certificates_verify():
    result = subprocess.run(
        [
            sys.executable,
            "tools/verify_bounded_g2_rank_cert.py",
            str(CERT6),
            str(CERT7),
        ],
        text=True,
        capture_output=True,
        check=True,
    )

    report = json.loads(result.stdout)
    assert report["status"] == "PASS"

    by_n = {r["n"]: r for r in report["reports"]}

    assert by_n[6]["rank_M"] == 8
    assert by_n[6]["nullity_d1"] == 8
    assert by_n[6]["rank_equals_nullity"] is True
    assert by_n[6]["target_rank_passed"] is True

    assert by_n[7]["rank_M"] == 43
    assert by_n[7]["nullity_d1"] == 43
    assert by_n[7]["rank_equals_nullity"] is True
    assert by_n[7]["target_rank_passed"] is True
