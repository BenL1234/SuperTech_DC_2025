#! /usr/bin/env python3
# Author: DCameron
# Description: This script is a VERY Basic Calculator App with few functions!
# Comments for the developer/coder
"""
    Basic Calculator App with add, multiply and divide features
"""
import sys

def add(*args):
    """ Return SUM of all arguments as a float
    >>> add(4, 3, 2, 1)
    10.0
    >>> add(10, 20)
    30.0
    """
    sum = 0
    for num in args:
        sum += num
    return float(sum)

def mul(*args):
    """ Return PRODUCT of all arguments as a float
    >>> mul(4, 3)
    12.0
    """
    total = 1
    for num in args:
        total *= num
    return float(total)

def div(x, z):
    """ Return QUOTIENT of x divided by z to 3 decimal places
    >>> div(4, 3)
    1.333
    """
    return round(x/z, 3)

def main():
    print("----------- Basic Calc Examples ------------")
    print(f"4 + 3 + 2 + 1 = {add(4, 3, 2, 1)}")
    print(f"4 * 3 * 2 = {mul(4, 3, 2)}")
    print(f"4 / 3 = {div(4, 3)}")
    print("--------------------------------------------")
    return None

# Namespace Trick
if __name__ == "__main__":
    # EXECUTE ONLY if ran directly as a program
    # Ignored if imported as a module
    main()
    sys.exit(0)