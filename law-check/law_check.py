#!/usr/bin/env python3

import sys

ALLOWED = {
    "Atlas",
    "core",
    "papers",
    "cassandra-wrapped-core",
    "QEX",
    "Cassandra-run",
    "foundation",
    "organismo",
}


def check(repo):
    if repo not in ALLOWED:
        return "BLOCK"

    return "PASS"


if __name__ == "__main__":
    repo = sys.argv[1]

    verdict = check(repo)

    print(verdict)

    if verdict != "PASS":
        sys.exit(1)
