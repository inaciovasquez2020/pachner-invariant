import json
import subprocess
import sys
from pathlib import Path


def test_admissible_bounded_g2_predicate_rejects_candidate_witnesses(tmp_path):
    create_script = Path("tools/create_bounded_g2_cert_data.py")
    predicate_script = Path("tools/verify_admissible_bounded_g2_predicate.py")

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

    result = subprocess.run(
        [
            sys.executable,
            str(predicate_script),
            str(tmp_path / "Cert_6.candidate.json"),
        ],
        text=True,
        capture_output=True,
    )

    assert result.returncode != 0
    output = result.stdout + result.stderr
    assert '"status": "HALT"' in output
    assert "witness does not assert admissible_bounded_G2=true" in output


def test_admissible_bounded_g2_predicate_accepts_minimal_valid_local_witness(tmp_path):
    cert = {
        "certificate_schema": "BoundedG2RankCert",
        "field": "F2",
        "n": 6,
        "vertices": [0, 1, 2, 3],
        "edges": [
            {"edge_id": 0, "source": 0, "target": 1, "move_token": "e0"},
            {"edge_id": 1, "source": 1, "target": 2, "move_token": "e1"},
            {"edge_id": 2, "source": 2, "target": 3, "move_token": "e2"},
            {"edge_id": 3, "source": 3, "target": 0, "move_token": "e3"},
        ],
        "relations": [
            {
                "relation_id": 0,
                "edge_indices_mod2": [0, 1, 2, 3],
                "relation_type": "bounded_G2_square",
                "witness_id": "w0",
            }
        ],
        "relation_witnesses": [
            {
                "witness_id": "w0",
                "admissible_bounded_G2": True,
                "relation_rule": "bounded_G2_square",
                "local_support": [0, 1, 2, 3],
                "bounded_G2_layer": True,
                "uses_only_local_flips": True,
                "closed_local_loop": True,
                "edge_indices_mod2": [0, 1, 2, 3],
            }
        ],
        "expected_rank": 8,
        "status": "raw_candidate_unverified",
    }

    path = tmp_path / "valid_local_witness.json"
    path.write_text(json.dumps(cert), encoding="utf-8")

    result = subprocess.run(
        [
            sys.executable,
            "tools/verify_admissible_bounded_g2_predicate.py",
            str(path),
        ],
        text=True,
        capture_output=True,
    )

    assert result.returncode == 0
    assert '"status": "PASS"' in (result.stdout + result.stderr)
