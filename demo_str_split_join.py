#! /usr/bin/env python3
# Author: DCameron
# Description: This script will demo HOWTO split and rejoin strings
# using the str.split() and str.join() methods.
"""
    Docstring:
"""

# Sample line from /etc/passwd in Linux  for the root user account
line = "root:x:0:0:The Super User:/root:/bin/bash"

# I want to modify str! But strings are IMMUTABLE!
fields = line.split(":") # Returns a LIST = MUTABLE!
fields[4] = "The Administrator"
fields[6] = "/bin/zsh"

line = ":".join(fields) # Returns a NEW string!
print("Modified str =", line)