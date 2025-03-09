
import unittest
from Dec2Hex import convert_decimal_to_hex  # Adjust according to your actual function

class TestDec2Hex(unittest.TestCase):

    def test_valid_input(self):
        self.assertEqual(convert_decimal_to_hex(255), "FF")

    def test_invalid_input(self):
        self.assertEqual(convert_decimal_to_hex("abc"), "Error: Invalid input. Please enter an integer.")

    def test_no_input(self):
        self.assertEqual(convert_decimal_to_hex(""), "Error: No input provided. Please enter an integer.")

if __name__ == '__main__':
    unittest.main()
