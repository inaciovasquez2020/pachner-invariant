import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def test_pachner_valid23_theorem_surface():
    result = subprocess.run(
        ["python3", "scripts/verify_pachner_valid23_theorem_surface.py"],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=True,
    )
    assert "pachner Valid23 theorem surface: PASS" in result.stdout
