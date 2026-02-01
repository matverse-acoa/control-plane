#!/usr/bin/env python3

import subprocess
import sys


def deploy(repo):
    subprocess.run(
        ["python3", "../atlas_deploy.py", f"repos/{repo}.zip"],
        check=True,
    )


if __name__ == "__main__":
    repo = sys.argv[1]

    subprocess.run(
        ["python3", "../law-check/law_check.py", repo],
        check=True,
    )

    subprocess.run(
        ["zip", "-r", f"repos/{repo}.zip", f"repos/{repo}"],
        check=True,
    )

    deploy(repo)
