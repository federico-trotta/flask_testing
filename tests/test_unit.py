import unittest
import sys
import os

# Add the parent directory to sys.path to import app.py
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import add_numbers, multiply_numbers

class TestMathFunctions(unittest.TestCase):
    """Unit tests for math functions with broad test cases."""

    def test_add_numbers_valid(self):
        """Test the add_numbers function with valid numeric inputs."""
        # Test with positive integers
        self.assertEqual(add_numbers(1, 2), 3)
        # Test with negative integers
        self.assertEqual(add_numbers(-1, -1), -2)
        # Test with zero
        self.assertEqual(add_numbers(0, 0), 0)
        # Test with positive floats
        self.assertEqual(add_numbers(1.5, 2.5), 4.0)
        # Test with negative floats
        self.assertEqual(add_numbers(-1.5, -2.5), -4.0)
        # Test with mixed integer and float
        self.assertEqual(add_numbers(1, 2.5), 3.5)
        # Test with very large numbers
        self.assertEqual(add_numbers(1e20, 1e20), 2e20)
        # Test with very small numbers
        self.assertAlmostEqual(add_numbers(1e-20, 1e-20), 2e-20)

    def test_add_numbers_invalid(self):
        """Test the add_numbers function with invalid (non-numeric) inputs."""
        # Test with strings (letters)
        with self.assertRaises(TypeError):
            add_numbers('a', 'b')
        # Test with strings that look like numbers
        with self.assertRaises(TypeError):
            add_numbers('1', '2')
        # Test with None
        with self.assertRaises(TypeError):
            add_numbers(None, 2)
        # Test with lists
        with self.assertRaises(TypeError):
            add_numbers([1, 2], 3)
        # Test with dictionaries
        with self.assertRaises(TypeError):
            add_numbers({'a': 1}, {'b': 2})
        # Test with boolean values
        with self.assertRaises(TypeError):
            add_numbers(True, False)

    def test_multiply_numbers_valid(self):
        """Test the multiply_numbers function with valid numeric inputs."""
        # Test with positive integers
        self.assertEqual(multiply_numbers(2, 3), 6)
        # Test with negative integers
        self.assertEqual(multiply_numbers(-2, -3), 6)
        # Test with positive and negative integers
        self.assertEqual(multiply_numbers(-2, 3), -6)
        # Test with zero
        self.assertEqual(multiply_numbers(0, 100), 0)
        # Test with positive floats
        self.assertEqual(multiply_numbers(2.5, 4), 10.0)
        # Test with negative floats
        self.assertEqual(multiply_numbers(-2.5, -4), 10.0)
        # Test with mixed integer and float
        self.assertEqual(multiply_numbers(3, 0.5), 1.5)
        # Test with very large numbers
        self.assertEqual(multiply_numbers(1e10, 1e10), 1e20)
        # Test with very small numbers
        self.assertAlmostEqual(multiply_numbers(1e-10, 1e-10), 1e-20)

    def test_multiply_numbers_invalid(self):
        """Test the multiply_numbers function with invalid (non-numeric) inputs."""
        # Test with strings (letters)
        with self.assertRaises(TypeError):
            multiply_numbers('a', 'b')
        # Test with strings that look like numbers
        with self.assertRaises(TypeError):
            multiply_numbers('1', '2')
        # Test with None
        with self.assertRaises(TypeError):
            multiply_numbers(None, 2)
        # Test with lists
        with self.assertRaises(TypeError):
            multiply_numbers([1, 2], 3)
        # Test with dictionaries
        with self.assertRaises(TypeError):
            multiply_numbers({'a': 1}, {'b': 2})
        # Test with boolean values
        with self.assertRaises(TypeError):
            multiply_numbers(True, False)

if __name__ == '__main__':
    unittest.main()