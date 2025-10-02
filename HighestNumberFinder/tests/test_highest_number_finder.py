#! /usr/bin/env python3
# Author: DCameron
# Description: This script will demo
"""
    Docstring:
"""
import unittest


class TestHighestNumberFinder(unittest.TestCase):
    def test_find_highest_in_list_one_result_single_item(self):
        # Structure TestCases TDD - AAAs
        # Arrange
        input_value = [10]
        expected_result = 10
        cut = HighestNumberFinder() # Class Under Test

        # Act
        actual_result = cut.find_highest_number(input_value)

        # Assert
        self.assertEqual(actual_result, expected_result)

if __name__ == "__main__":
    unittest.main()