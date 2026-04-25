import json
import subprocess
import sys
from pathlib import Path


def test_local_support_from_relation_returns_first_valid_witness_from_generated_candidate(tmp_path):
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
    output = tmp_path / "first_witness_n6.json"

    result = subprocess.run(
        [
            sys.executable,
            str(local_script),
            "--input",
            str(candidate),
            "--output",
            str(output),
        ],
        text=True,
        capture_output=True,
    )

    assert result.returncode == 0
    assert output.exists()

    report = json.loads(output.read_text())
    assert report["schema"] == "BoundedG2FirstLocalSupportWitness"
    assert report["field"] == "F2"
    assert report["n"] == 6
    assert report["status"] == "PASS"

    witness = report["witness"]
    assert witness["admissible_bounded_G2"] is True
    assert witness["relation_rule"] in {"bounded_G2_square", "bounded_G2_pentagon"}
    assert witness["local_support"]
    assert witness["bounded_G2_layer"] is True
    assert witness["uses_only_local_flips"] is True
    assert witness["closed_local_loop"] is True
    assert witness["edge_indices_mod2"]


def test_local_support_from_relation_does_not_create_raw_certificate(tmp_path):
    local_script = Path("tools/local_support_from_relation.py")
    output = tmp_path / "first_witness_n6.json"

    result = subprocess.run(
        [
            sys.executable,
            str(local_script),
            "--n",
            "6",
            "--output",
            str(output),
        ],
        text=True,
        capture_output=True,
    )

    assert result.returncode == 0
    assert output.exists()
    assert not (tmp_path / "Cert_6.json").exists()
    assert not (tmp_path / "Cert_7.json").exists()
