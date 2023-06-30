import unittest
from python_implementation import fibonacci_iterative, fibonacci_recursive, fibonacci_dynamic

class FibonacciTest(unittest.TestCase):

    def test_fibonacci_iterative(self):
        # Test case 1
        result = fibonacci_iterative(1)
        self.assertEqual(result, 1)
        
        # Test case 2
        result = fibonacci_iterative(5)
        self.assertEqual(result, ([1, 2, 3, 5, 8], 13))
        
        # Test case 3
        result = fibonacci_iterative(10)
        self.assertEqual(result, ([1, 2, 3, 5, 8, 13, 21, 34, 55, 89], 144))

    def test_fibonacci_recursive(self):
        # Test case 1
        result = fibonacci_recursive(1)
        self.assertEqual(result, 1)
        
        # Test case 2
        result = fibonacci_recursive(5)
        self.assertEqual(result, ([1, 1, 2, 3, 5], 5))
        
        # Test case 3
        result = fibonacci_recursive(10)
        self.assertEqual(result, ([1, 1, 2, 3, 5, 8, 13, 21, 34, 55], 55))
    
    def test_fibonacci_dynamic(self):
        # Test case 1
        result = fibonacci_dynamic(1)
        self.assertEqual(result, 1)
        
        # Test case 2
        result = fibonacci_dynamic(5)
        self.assertEqual(result, ([1, 1, 2, 3, 5], 5))
        
        # Test case 3
        result = fibonacci_dynamic(10)
        self.assertEqual(result, ([1, 1, 2, 3, 5, 8, 13, 21, 34, 55], 55))

if __name__ == '__main__':
    # Create a test suite
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(FibonacciTest))

    # Create a test runner and print the test results
    runner = unittest.TextTestRunner()
    result = runner.run(suite)
    print(result)
