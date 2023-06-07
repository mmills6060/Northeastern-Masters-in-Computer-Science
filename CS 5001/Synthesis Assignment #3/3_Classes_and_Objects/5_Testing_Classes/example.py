# Michael Arthur Mills
# April 7. 2023
# CS 5001

# Unit test for the class computer

import unittest

from problem import computer

class TestComputer(unittest.TestCase):
    def test_computer(self):
        # create a computer
        my_computer = computer()
        # test the initial values
        self.assertEqual(my_computer.name, "Alienware")
        self.assertEqual(my_computer.size, "16")
        self.assertEqual(my_computer.price, 2500)
        # test the add_on method
        my_computer.add_on("Mouse")
        self.assertEqual(my_computer.price, 2650)
        my_computer.add_on("Keyboard")
        self.assertEqual(my_computer.price, 2850)

if __name__ == '__main__':
    unittest.main()

    