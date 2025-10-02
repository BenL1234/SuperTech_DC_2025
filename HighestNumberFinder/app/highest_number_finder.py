#! /usr/bin/env python3
# Author: DCameron
# Description: This script will demo
"""
    Docstring:
"""

class HighestNumberFinder:
    def find_highest_number(self, numbers):
        highest_number = numbers[0]
        if len(numbers) > 1:
            if numbers[1] > highest_number:
                highest_number = numbers[1]
        return highest_number