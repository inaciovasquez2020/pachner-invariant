import subprocess
import sys

def test_frontier_status_check_passes():
    subprocess.run(
        [sys.executable, "scripts/check_frontier_status.py"],
        check=True,
    )
