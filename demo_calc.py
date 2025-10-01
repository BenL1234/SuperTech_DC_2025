#! /usr/bin/env python3
# Author: DCameron
# Description: This script is a VERY Basic Calculator App with few functions!
# Comments for the developer/coder
"""
    Basic Calculator App with add, multiply and divide features
"""

def add(*args):
    """ Return SUM of all arguments as a float """
    sum = 0
    for num in args:
        sum += num
    return float(sum)

def mul(*args):
    """ Return PRODUCT of all arguments as a float """
    total = 1
    for num in args:
        total *= num
    return float(total)

def div(x, z):
    """ Return QUOTIENT of x divided by z to 3 decimal places """
    return round(x/z, 3)


print(f"4 + 3 + 2 + 1 = {add(4, 3, 2, 1)}")
print(f"4 * 3 * 2 = {mul(4, 3, 2)}")
print(f"4 / 3 = {div(4, 3)}")

# Alternatively we could define a SIMPLE, short function without
# using the def statement
l_div = lambda x, z: round(x/z, 3)
print(f"5 / 4 = {l_div(5, 4)}")
