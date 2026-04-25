import subprocess
import sys
from pathlib import Path


def test_relation_witness_classifier_rejects_candidate_exports(tmp_path):
    create_script = Path("tools/create_bounded_g2_cert_data.py")
    classify_script = Path("tools/classify_bounded_g2_relation_witnesses.py")

    subprocess.run(
        [
            sys.executable,
            str(create_script),
            "--n",
            "6",
            "7",
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
            str(classify_script),
            str(tmp_path / "Cert_6.candidate.json"),
            str(tmp_path / "Cert_7.candidate.json"),
        ],
        text=True,
        capture_output=True,
    )

    assert result.returncode != 0
    output = result.stdout + result.stderr
    assert '"status": "HALT"' in output
    assert "inadmissible_witnesses" in output
    assert "Existing cycle basis has not been classified as admissible bounded-G2 elementary relations." in output


def test_relation_witness_classifier_halts_on_missing_file():
    classify_script = Path("tools/classify_bounded_g2_relation_witnesses.py")

    result = subprocess.run(
        [
            sys.executable,
            str(classify_script),
            "docs/data/Cert_6.candidate.json",
        ],
        text=True,
        capture_output=True,
    )

    assert result.returncode != 0
    assert "HALT: missing candidate certificate file: docs/data/Cert_6.candidate.json" in (
        result.stdout + result.stderr
    )
