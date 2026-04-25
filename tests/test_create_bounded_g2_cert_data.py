import json
import subprocess
import sys
from pathlib import Path


def test_create_bounded_g2_cert_data_exports_candidates_only(tmp_path):
    script = Path("tools/create_bounded_g2_cert_data.py")
    assert script.exists()

    result = subprocess.run(
        [
            sys.executable,
            str(script),
            "--n",
            "6",
            "7",
            "--output-dir",
            str(tmp_path),
        ],
        text=True,
        capture_output=True,
    )

    assert result.returncode == 0
    assert "HALT: created candidate data only" in (result.stdout + result.stderr)

    c6 = tmp_path / "Cert_6.candidate.json"
    c7 = tmp_path / "Cert_7.candidate.json"

    assert c6.exists()
    assert c7.exists()

    for path, n, rank in [(c6, 6, 8), (c7, 7, 43)]:
        data = json.loads(path.read_text())
        assert data["certificate_schema"] == "BoundedG2RankCert"
        assert data["field"] == "F2"
        assert data["n"] == n
        assert data["expected_rank"] == rank
        assert data["status"] == "raw_candidate_unverified"
        assert data["vertices"]
        assert data["edges"]
        assert data["relations"]
        assert data["relation_witnesses"]
        assert all(
            witness["admissible_bounded_G2"] is False
            for witness in data["relation_witnesses"]
        )


def test_candidate_data_is_rejected_by_certificate_verifier(tmp_path):
    create_script = Path("tools/create_bounded_g2_cert_data.py")
    verify_script = Path("tools/verify_bounded_g2_rank_cert.py")

    subprocess.run(
        [
            sys.executable,
            str(create_script),
            "--n",
            "6",
            "--output-dir",
            str(tmp_path),
        ],
        text=True,
        capture_output=True,
        check=True,
    )

    candidate = tmp_path / "Cert_6.candidate.json"

    result = subprocess.run(
        [sys.executable, str(verify_script), str(candidate)],
        text=True,
        capture_output=True,
    )

    assert result.returncode != 0
    assert "relation witness is not admissible bounded-G2" in (
        result.stdout + result.stderr
    )
