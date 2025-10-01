#! /usr/bin/env python3
# Author: DCameron
# Description: This script will demo
"""
    Docstring:
"""

with (open(r"c:\labs\words", mode="rt") as fh_in):
    for (line_num, line) in enumerate(fh_in, start=1):
        if line.startswith("Y") and line.rstrip("\n").endswith("n") and "town" in line:
            print(line_num, line, end="")
