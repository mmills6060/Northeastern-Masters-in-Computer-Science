# Michael Arthur Mills
# Spring 2023, CS 5001
# Lab 7 code file


from Lab7HosoyaTriangle import computeTriangle
from Lab7HosoyaTriangle import printTriangle

import unittest
levels = 5
triangle = computeTriangle(levels)
# tests for computeTriangle
class test_computeTriangle(unittest.TestCase):
    def test_compute_triangle(self):
        difference = computeTriangle(levels)
        self.assertEqual(difference, [[1], [1, 1], [2, 1, 2], [3, 2, 2, 3], [5, 3, 4, 3, 5], [8, 5, 6, 6, 5, 8]])  

# tests for printTriangle
class test_printTriangle(unittest.TestCase):
    def test_printTriangle(self):
        difference = printTriangle(triangle)
        self.assertEqual(difference, None)
# tests for computeTriangle
class test_computeTriangleNegativeLevel(unittest.TestCase):
    def test_computeTriangle_negative_level(self):
        difference = computeTriangle(-1)
        self.assertNotEqual(difference, [[1], [1, 1], [2, 1, 2], [3, 2, 2, 3], [5, 3, 4, 3, 5], [8, 5, 6, 6, 5, 8]])  

# tests for printTriangle
class test_computeTriangle_negative_level(unittest.TestCase):
    def test_computeTriangle_negative_level(self):
        difference = printTriangle(triangle)
        self.assertEqual(difference, None)

def main():
    unittest.main()
if __name__ == '__main__':
    main()
