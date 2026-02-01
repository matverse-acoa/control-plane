#!/usr/bin/env python3

import json
import subprocess
from pathlib import Path

ORG = "matverse-acoa"


def list_repos():
    out = subprocess.check_output(
        ["gh", "repo", "list", ORG, "--json", "name,sshUrl"],
        text=True,
    )
    return json.loads(out)


def clone_if_missing(repo):
    path = Path("repos") / repo["name"]

    if path.exists():
        return "exists"

    subprocess.run(
        ["git", "clone", repo["sshUrl"], str(path)],
        check=True,
    )

    return "cloned"


def run():
    Path("repos").mkdir(exist_ok=True)

    repos = list_repos()

    report = {}

    for repo in repos:
        report[repo["name"]] = clone_if_missing(repo)

    Path("state").mkdir(exist_ok=True)

    with open("state/discovery.json", "w", encoding="utf-8") as handle:
        json.dump(report, handle, indent=2)


if __name__ == "__main__":
    run()
