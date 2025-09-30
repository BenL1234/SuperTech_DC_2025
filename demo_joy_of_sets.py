#! /usr/bin/env python3
# Author: DCameron
# Description: This script will demo HOWTO create, and grow, and shrink
# and combine sets (Unordered Collection with Unique values)
"""
    Docstring:
"""

marvel_fans = {'ayo', 'charles', 'arash', 'zubin', 'diren', 'arash', 'sage', 'donald'}
dc_fans = set() # Create an empty SET

# Grow a set..
dc_fans.add('donald')
dc_fans.add('ben')
dc_fans.add('deenesh')

# Shrink a SET..
# dc_fans.pop() # RANDOMLY remove a value
# comic_fans = dc_fans.copy() # Copies SET
# comic_fans.clear() # Empty the SET

print(f"Fans of Marvel = {marvel_fans}")
print(f"Fans of DC = {dc_fans}")
print("-" * 60)

# COMBINE SETS using SET operations/methods (Remember VENN diagrams)
print(f"Fans of Marvel OR DC = {marvel_fans.union(dc_fans)}")
print(f"Fans of Marvel AND DC = {marvel_fans.intersection(dc_fans)}")
print(f"Fans of ONLY Marvel = {marvel_fans.difference(dc_fans)}")
print(f"Fans of ONLY Marvel OR DC = {marvel_fans.symmetric_difference(dc_fans)}")
print("-" * 60)
# COMBINE SETS using SET OPERATORS (Remember VENN diagrams)
print(f"Fans of Marvel OR DC = {marvel_fans | dc_fans}")
print(f"Fans of Marvel AND DC = {marvel_fans & dc_fans}")
print(f"Fans of ONLY Marvel = {marvel_fans - dc_fans}")
print(f"Fans of ONLY Marvel OR DC = {marvel_fans ^ dc_fans}")