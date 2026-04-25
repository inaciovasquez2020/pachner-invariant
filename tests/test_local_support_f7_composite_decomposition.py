import json
import subprocess
import sys
from pathlib import Path


def test_local_support_all_relations_accepts_f7_composite_decompositions(tmp_path):
    create_script = Path("tools/create_bounded_g2_cert_data.py")
    local_script = Path("tools/local_support_from_relation.py")

    subprocess.run(
        [
            sys.executable,
            str(create_script),
            "--n",
            "7",
            "--output-dir",
            str(tmp_path),
        ],
        text=True,
        capture_output=True,
        check=True,
    )

    candidate = tmp_path / "Cert_7.candidate.json"
    output = tmp_path / "all_witnesses_n7.json"

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

    assert result.returncode == 0, result.stdout + result.stderr
    report = json.loads(output.read_text())

    assert report["schema"] == "BoundedG2AllLocalSupportWitnesses"
    assert report["field"] == "F2"
    assert report["n"] == 7
    assert report["status"] == "PASS"
    assert report["relation_count"] == 43
    assert report["witness_count"] == 43
    assert report["failure_count"] == 0

    residual_ids = {14, 15, 22, 23, 24, 29, 32, 35, 38, 39, 42}
    by_id = {w["relation_id"]: w for w in report["witnesses"]}

    assert residual_ids.issubset(by_id)

    for rid in residual_ids:
        witness = by_id[rid]
        assert witness["admissible_bounded_G2"] is True
        assert witness["relation_rule"] == "bounded_G2_decomposed_composite"
        assert witness["decomposes_over_F2_into_square_pentagon"] is True
        assert witness["decomposition"]
        assert witness["composite_edge_count"] in {6, 9}
        assert all(
            s["relation_rule"] in {"bounded_G2_square", "bounded_G2_pentagon"}
            for s in witness["decomposition"]
        )


def test_admissible_predicate_accepts_f7_composite_decompositions_after_merge(tmp_path):
    create_script = Path("tools/create_bounded_g2_cert_data.py")
    local_script = Path("tools/local_support_from_relation.py")
    predicate_script = Path("tools/verify_admissible_bounded_g2_predicate.py")

    subprocess.run(
        [
            sys.executable,
            str(create_script),
            "--n",
            "7",
            "--output-dir",
            str(tmp_path),
        ],
        text=True,
        capture_output=True,
        check=True,
    )

    candidate = tmp_path / "Cert_7.candidate.json"
    witnesses_path = tmp_path / "all_witnesses_n7.json"
    merged = tmp_path / "Cert_7.with_witnesses.json"

    subprocess.run(
        [
            sys.executable,
            str(local_script),
            "--input",
            str(candidate),
            "--all",
            "--output",
            str(witnesses_path),
        ],
        text=True,
        capture_output=True,
        check=True,
    )

    cert = json.loads(candidate.read_text())
    witnesses = json.loads(witnesses_path.read_text())["witnesses"]

    cert["relation_witnesses"] = witnesses
    cert["status"] = "raw_with_witnesses_unverified_rank"
    merged.write_text(json.dumps(cert, indent=2, sort_keys=True), encoding="utf-8")

    result = subprocess.run(
        [
            sys.executable,
            str(predicate_script),
            str(merged),
        ],
        text=True,
        capture_output=True,
    )

    assert result.returncode == 0, result.stdout + result.stderr
    assert '"status": "PASS"' in (result.stdout + result.stderr)
