import json
import subprocess
import sys
from pathlib import Path


def test_diagnose_bounded_g2_relation_failures_reports_f6_failed_relations(tmp_path):
    create_script = Path("tools/create_bounded_g2_cert_data.py")
    diag_script = Path("tools/diagnose_bounded_g2_relation_failures.py")

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
        [
            sys.executable,
            str(diag_script),
            "--input",
            str(candidate),
            "--only-failures",
        ],
        text=True,
        capture_output=True,
        check=True,
    )

    report = json.loads(result.stdout)
    assert report["schema"] == "BoundedG2RelationFailureDiagnostics"
    assert report["n"] == 6
    assert report["status"] == "PASS"

    failed_ids = {d["relation_id"] for d in report["diagnostics"]}
    assert {3, 4, 7}.issubset(failed_ids)

    for diag in report["diagnostics"]:
        assert diag["local_support_passed"] is False
        assert diag["failure_reasons"]
        assert diag["edge_indices_mod2"]
        assert diag["endpoints"]
        assert diag["degrees"]


def test_diagnose_bounded_g2_relation_failures_can_run_from_n_argument():
    diag_script = Path("tools/diagnose_bounded_g2_relation_failures.py")

    result = subprocess.run(
        [
            sys.executable,
            str(diag_script),
            "--n",
            "6",
            "--only-failures",
        ],
        text=True,
        capture_output=True,
        check=True,
    )

    report = json.loads(result.stdout)
    assert report["schema"] == "BoundedG2RelationFailureDiagnostics"
    assert report["n"] == 6
    assert report["diagnostic_count"] >= 1
