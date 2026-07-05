"""
Basic validation test for app.py.

This runs app.py as a subprocess and checks:
1. It exits without error (return code 0)
2. It prints the expected message
"""

import subprocess
import sys


def test_app_runs_without_error():
    result = subprocess.run(
        [sys.executable, "app.py"],
        capture_output=True,
        text=True,
    )

    assert result.returncode == 0, f"app.py exited with error: {result.stderr}"
    assert "Cloud CI Pipeline Running" in result.stdout, (
        f"Expected output not found. Got: {result.stdout}"
    )
    assert "Vera Eshun" in result.stdout, (
        f"Expected author line not found. Got: {result.stdout}"
    )

    print("test_app_runs_without_error: PASSED")


if __name__ == "__main__":
    test_app_runs_without_error()