# flake8_test.py
import subprocess


def test_flake8():
    result = subprocess.run(
        ['flake8',
         '--count',
         '--ignore=E402,W503',
         '.'],
        stdout=subprocess.PIPE)
    assert result.returncode == 0, "Flake8 found issues in the codebase. Please check the output." # noqa
