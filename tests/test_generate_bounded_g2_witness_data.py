import json
import subprocess
import sys
from pathlib import Path


def test_generate_bounded_g2_witness_data_three_generators(tmp_path):
    script = Path("tools/generate_bounded_g2_witness_data.py")

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
    assert "HALT: generated three-generator witness data only" in (
        result.stdout + result.stderr
    )

    for n, expected_rank in [(6, 8), (7, 43)]:
        path = tmp_path / f"bounded_g2_witness_data_n{n}.json"
        assert path.exists()

        data = json.loads(path.read_text())
        assert data["schema"] == "BoundedG2WitnessData"
        assert data["field"] == "F2"
        assert data["n"] == n
        assert data["expected_rank"] == expected_rank
        assert data["status"] == "candidate_only"
        assert len(data["generators"]) == 3
        assert {g["generator"] for g in data["generators"]} == {
            "artifact_cycle_basis",
            "graph_simple_cycles_4_5",
            "spanning_tree_fundamental_cycles",
        }
        assert data["witness_candidates"]
        assert all(
            witness["admissible_bounded_G2"] is False
            for witness in data["witness_candidates"]
        )
        assert "three_generator_agreement_count" in data["summary"]


def test_generated_witness_data_does_not_create_raw_certificates(tmp_path):
    script = Path("tools/generate_bounded_g2_witness_data.py")

    subprocess.run(
        [
            sys.executable,
            str(script),
            "--n",
            "6",
            "--output-dir",
            str(tmp_path),
        ],
        text=True,
        capture_output=True,
        check=True,
    )

    assert not (tmp_path / "Cert_6.json").exists()
    assert not (tmp_path / "Cert_7.json").exists()
    assert (tmp_path / "bounded_g2_witness_data_n6.json").exists()
