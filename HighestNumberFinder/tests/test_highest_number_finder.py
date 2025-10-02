#! /usr/bin/env python3
# Author: DCameron
# Description: This script will demo
"""
    Docstring:
"""
import unittest
from HighestNumberFinder.app.highest_number_finder import HighestNumberFinder

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

    def test_find_highest_in_list_two_descending_result_first_item(self):
        # Structure TestCases TDD - AAAs
        # Arrange
        input_value = [13, 4]
        expected_result = 13
        cut = HighestNumberFinder() # Class Under Test

        # Act
        actual_result = cut.find_highest_number(input_value)

        # Assert
        self.assertEqual(actual_result, expected_result)

    def test_find_highest_in_list_two_ascending_result_second_item(self):
        # Structure TestCases TDD - AAAs
        # Arrange
        input_value = [4, 13]
        expected_result = 13
        cut = HighestNumberFinder() # Class Under Test

        # Act
        actual_result = cut.find_highest_number(input_value)

        # Assert
        self.assertEqual(actual_result, expected_result)

if __name__ == "__main__":
    unittest.main()