import json
import subprocess
import sys
from pathlib import Path


def test_local_support_all_relations_accepts_f6_decomposed_heptagons(tmp_path):
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

    assert result.returncode == 0, result.stdout + result.stderr
    report = json.loads(output.read_text())

    assert report["schema"] == "BoundedG2AllLocalSupportWitnesses"
    assert report["field"] == "F2"
    assert report["n"] == 6
    assert report["status"] == "PASS"
    assert report["relation_count"] == 8
    assert report["witness_count"] == 8
    assert report["failure_count"] == 0

    witnesses = report["witnesses"]
    by_id = {w["relation_id"]: w for w in witnesses}

    assert set(by_id) == set(range(8))

    for rid in {3, 4, 7}:
        witness = by_id[rid]
        assert witness["admissible_bounded_G2"] is True
        assert witness["relation_rule"] == "bounded_G2_decomposed_heptagon"
        assert witness["decomposes_over_F2_into_square_pentagon"] is True
        assert witness["decomposition"]
        assert all(
            s["relation_rule"] in {"bounded_G2_square", "bounded_G2_pentagon"}
            for s in witness["decomposition"]
        )

    for rid in {0, 1, 2, 5, 6}:
        assert by_id[rid]["relation_rule"] in {"bounded_G2_square", "bounded_G2_pentagon"}


def test_admissible_predicate_accepts_all_f6_decomposed_witnesses_after_merge(tmp_path):
    create_script = Path("tools/create_bounded_g2_cert_data.py")
    local_script = Path("tools/local_support_from_relation.py")
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

    candidate = tmp_path / "Cert_6.candidate.json"
    witnesses_path = tmp_path / "all_witnesses_n6.json"
    merged = tmp_path / "Cert_6.with_witnesses.json"

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
