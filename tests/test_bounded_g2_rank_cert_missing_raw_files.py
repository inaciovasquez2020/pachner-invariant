import subprocess
import sys
from pathlib import Path


def test_bounded_g2_rank_cert_halts_without_raw_certificates():
    script = Path("tools/verify_bounded_g2_rank_cert.py")
    assert script.exists()

    result = subprocess.run(
        [
            sys.executable,
            str(script),
            "docs/data/Cert_6.json",
            "docs/data/Cert_7.json",
        ],
        text=True,
        capture_output=True,
    )

    assert result.returncode != 0
    assert "HALT: missing raw certificate file: docs/data/Cert_6.json" in (
        result.stdout + result.stderr
    )
