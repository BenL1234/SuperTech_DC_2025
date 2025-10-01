#! /usr/bin/env python3
# Author: DCameron
# Description: This script will demo HOWTO emulate BLOCK scope using
# Python's Context Resource Manager (with statement)
"""
    Docstring:
"""
movies = {'kymran': ['indiana jones', 'bridget jones', 'mamma mia'],
          'charles': ['puss in boots', 'the last wish', 'django unchained'],
          'diren': ['top gun', 'wolf of wall street', 'rio'],
          'donald': ['lotr', 'the hobbit', 'star wars']
}

# Open file handle for WRITING in TEXT mode
with open(r"c:\labs\projects\Sky_SuperTech_DC_2025\movies.txt", mode="wt") as fh_out:
    for name in movies.keys():
        print(f"{name} {movies[name]}", end="\n")
        fh_out.write(f"{name} {movies[name]}\n")
    # End of BLOCK, fh_out is now closed!

print("-" * 60)

with open(r"c:\labs\projects\Sky_SuperTech_DC_2025\movies.txt", mode="rt") as fh_in:
    for line in fh_in:
        print(line, end="")
