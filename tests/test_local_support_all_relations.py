import json
import subprocess
import sys
from pathlib import Path


def test_local_support_all_relations_mode_runs_and_reports_complete_or_halt(tmp_path):
    create_script = Path("tools/create_bounded_g2_cert_data.py")
    local_script = Path("tools/local_support_from_relation.py")

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
    output = tmp_path / "all_witnesses_n6.json"

    result = subprocess.run(
        [
            sys.executable,
            str(local_script),
            "--input",
            str(candidate),
            "--all",
            "--output",
            str(output),
        ],
        text=True,
        capture_output=True,
    )

    combined = result.stdout + result.stderr

    if result.returncode == 0:
        assert output.exists()
        report = json.loads(output.read_text())
        assert report["schema"] == "BoundedG2AllLocalSupportWitnesses"
        assert report["field"] == "F2"
        assert report["n"] == 6
        assert report["status"] == "PASS"
        assert report["failure_count"] == 0
        assert report["relation_count"] == report["witness_count"]
        assert report["witnesses"]
        assert all(w["admissible_bounded_G2"] is True for w in report["witnesses"])
        assert all(
            w["relation_rule"]
                in {
                    "bounded_G2_square",
                    "bounded_G2_pentagon",
                    "bounded_G2_decomposed_heptagon",
                    "bounded_G2_decomposed_composite",
                }
            for w in report["witnesses"]
        )
    else:
        assert '"schema": "BoundedG2AllLocalSupportWitnesses"' in combined
        assert '"status": "HALT"' in combined
        assert "relation is not a simple local 4- or 5-cycle in the endpoint graph" in combined


def test_local_support_all_relations_mode_accepts_explicit_square_certificate(tmp_path):
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
                "relation_type": "cycle_basis_candidate",
                "witness_id": "w0",
            }
        ],
        "relation_witnesses": [],
        "expected_rank": 8,
        "status": "raw_candidate_unverified",
    }

    inp = tmp_path / "square_cert.json"
    out = tmp_path / "square_all_witnesses.json"
    inp.write_text(json.dumps(cert), encoding="utf-8")

    result = subprocess.run(
        [
            sys.executable,
            "tools/local_support_from_relation.py",
            "--input",
            str(inp),
            "--all",
            "--output",
            str(out),
        ],
        text=True,
        capture_output=True,
    )

    assert result.returncode == 0
    report = json.loads(out.read_text())
    assert report["schema"] == "BoundedG2AllLocalSupportWitnesses"
    assert report["status"] == "PASS"
    assert report["relation_count"] == 1
    assert report["witness_count"] == 1
    assert report["failure_count"] == 0
    assert report["witnesses"][0]["relation_rule"] == "bounded_G2_square"
