#!/usr/bin/env python3

import subprocess

steps = [
    "discovery/discovery.py",
    "topology/topology.py",
]

for step in steps:
    subprocess.run(["python3", step], check=True)
