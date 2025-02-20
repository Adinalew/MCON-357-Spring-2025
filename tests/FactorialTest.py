#Adina Lew
#Testing Factorial

import unittest
from exercises.Factorial import *

class FactorialTestCases(unittest.TestCase):
    def test_factorial_recursive_zero(self):
        result = factorial_recursive(0, 1000, 1)
        self.assertEqual(result, 1)

    def test_factorial_recursive_one(self):
        result = factorial_recursive(1, 1000, 0)
        self.assertEqual(result, 1)

    def test_validate_input_negative_numbers(self):
        value, error_message = process_input("-5")
        self.assertIsNone(value)
        self.assertEqual(error_message, "Number cannot be negative")

    def test_factorial_recursive_positive_numbers(self):
        result = factorial_recursive(4, 1000, 4)
        self.assertEqual(result, 24)
        result = factorial_recursive(5, 1000, 5)
        self.assertEqual(result, 120)

    def test_factorial_recursive_larger_numbers(self):
        result = factorial_recursive(11, 1000, 11)
        self.assertEqual(result, 39916800)

    def test_factorial_recursive_before_recursion_limit(self):
        result = factorial_recursive(30, 1000, 30)
        self.assertEqual(result, 265252859812191058636308480000000)

    def test_factorial_recursive_after_recursion_limit(self):
        result = factorial_recursive(1000, 1000, 1000)
        self.assertEqual(result, None)

if __name__ == "__main__":
    unittest.main()