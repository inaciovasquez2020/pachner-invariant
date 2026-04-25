import json
import subprocess
import sys
from pathlib import Path


def test_decompose_bounded_g2_heptagon_relations_reports_f6_obstructions(tmp_path):
    script = Path("tools/decompose_bounded_g2_heptagon_relations.py")
    output = tmp_path / "heptagon_decomposition_n6.json"

    result = subprocess.run(
        [
            sys.executable,
            str(script),
            "--n",
            "6",
            "--output",
            str(output),
        ],
        text=True,
        capture_output=True,
    )

    assert output.exists()
    report = json.loads(output.read_text())

    assert report["schema"] == "BoundedG2HeptagonDecompositionReport"
    assert report["field"] == "F2"
    assert report["n"] == 6
    assert report["heptagon_obstruction_count"] == 3

    relation_ids = {r["relation_id"] for r in report["reports"]}
    assert relation_ids == {3, 4, 7}

    if report["status"] == "PASS":
        assert result.returncode == 0
        assert all(r["decomposes_into_square_pentagon_cycles"] is True for r in report["reports"])
        assert all(r["decomposition"] for r in report["reports"])
    else:
        assert result.returncode != 0
        assert any(r["status"] == "HALT" for r in report["reports"])


def test_decompose_bounded_g2_heptagon_relations_accepts_explicit_xor_case(tmp_path):
    cert = {
        "certificate_schema": "BoundedG2RankCert",
        "field": "F2",
        "n": 6,
        "vertices": list(range(7)),
        "edges": [
            {"edge_id": 0, "source": 0, "target": 1, "move_token": "e0"},
            {"edge_id": 1, "source": 1, "target": 2, "move_token": "e1"},
            {"edge_id": 2, "source": 2, "target": 3, "move_token": "e2"},
            {"edge_id": 3, "source": 3, "target": 0, "move_token": "e3"},
            {"edge_id": 4, "source": 3, "target": 4, "move_token": "e4"},
            {"edge_id": 5, "source": 4, "target": 5, "move_token": "e5"},
            {"edge_id": 6, "source": 5, "target": 6, "move_token": "e6"},
            {"edge_id": 7, "source": 6, "target": 0, "move_token": "e7"},
        ],
        "relations": [
            {
                "relation_id": 0,
                "edge_indices_mod2": [0, 1, 2, 4, 5, 6, 7],
                "witness_id": "w0",
            }
        ],
        "relation_witnesses": [],
        "expected_rank": 8,
        "status": "raw_candidate_unverified",
    }

    path = tmp_path / "xor_case.json"
    out = tmp_path / "xor_case_report.json"
    path.write_text(json.dumps(cert), encoding="utf-8")

    result = subprocess.run(
        [
            sys.executable,
            "tools/decompose_bounded_g2_heptagon_relations.py",
            "--input",
            str(path),
            "--output",
            str(out),
        ],
        text=True,
        capture_output=True,
    )

    assert result.returncode == 0
    report = json.loads(out.read_text())
    assert report["status"] == "PASS"
    assert report["reports"][0]["decomposes_into_square_pentagon_cycles"] is True
