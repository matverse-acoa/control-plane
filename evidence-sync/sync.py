#!/usr/bin/env python3

import shutil
from pathlib import Path

SRC = Path("../evidence")
DST = Path("ledger")


def run():
    DST.mkdir(exist_ok=True)

    for path in SRC.glob("*.json"):
        target = DST / path.name

        if not target.exists():
            shutil.copy2(path, target)


if __name__ == "__main__":
    run()
