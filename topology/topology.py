#!/usr/bin/env python3

import json
from pathlib import Path

ROOT = Path("repos")


def scan_repo(repo):
    files = 0
    dirs = 0

    for path in repo.rglob("*"):
        if path.is_file():
            files += 1
        elif path.is_dir():
            dirs += 1

    return {
        "files": files,
        "dirs": dirs,
    }


def run():
    topology = {}

    for repo in ROOT.iterdir():
        if repo.is_dir():
            topology[repo.name] = scan_repo(repo)

    Path("state").mkdir(exist_ok=True)

    with open("state/topology.json", "w", encoding="utf-8") as handle:
        json.dump(topology, handle, indent=2)


if __name__ == "__main__":
    run()
