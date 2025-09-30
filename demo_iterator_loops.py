#! /usr/bin/env python3
# Author: DCameron
# Description: This script will demo HOWTO ITERATE through a
# collection/sequence (str/tuple/list/dict/set) using
# an ITERATOR for loop.
"""
    Docstring:
"""
import sys
#           0            1               2           3       4
heroes = ['JFK', 'marie antoinette', 'm.jackson', 'ozzie', 'pele',
          'malcolm X', 'kobe', 'diana']

# Iterate through the collection/List using
# an ITERATOR for loop
for name in heroes:
    print(name, end="\n")

# Iterate through the collection/List and MODIFY the objects
# using an ITERATOR for loop and an index
idx = 0
for name in heroes:
    print(name.upper(), end="\n")
    heroes[idx] = name.upper()
    idx += 1
print("Heroes =", heroes)

# using an ITERATOR for loop and built-in emumerate() function
for (idx, name) in enumerate(heroes, start=0):
    print(name.title(), end="\n")
    heroes[idx] = name.title()
print("Heroes =", heroes)

try:
    sys.exit(0) # Explicit EXIT with return code (0=success, 1-255=error code)
except SystemExit:
    print("Quitting..")

# sys.exit("Goodbye") # Explicit EXIT with "expression"->STDERR(red) + return code 1