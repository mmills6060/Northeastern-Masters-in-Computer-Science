# File which will hold a stack data strcture
# 4/4/2023
# Implemented by Michael Mills


# create unittest that tests stack.py which includes valid strings, invalid strings, and empty strings

import unittest
from Stack import Stack
from Brackets import check_brackets

class TestCheckBrackets(unittest.TestCase):
    def test_valid_strings(self):
        self.assertTrue(check_brackets("()"))
        self.assertTrue(check_brackets("()[]{}"))
        
    def test_invalid_strings(self):
        self.assertFalse(check_brackets("(]"))
        self.assertFalse(check_brackets("([)]"))
    def test_empty_strings(self):
        self.assertTrue(check_brackets(""))
def main():
    unittest.main()

if __name__ == "__main__":
    main()