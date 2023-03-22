''' Align Online
    CS5001
    Sample code -- test suit for a class. Imports from
    car.py, and tests the Car class by creating objects,
    calling methods on those objects, and
    making sure the values of the attributes are what we expect.
'''

from car import Car
import unittest

class CrashTest(unittest.TestCase):
    def test_init(self):
        car = Car("Herbie", "Lovebug", price = 400.0)
        self.assertEqual(car.make, "Herbie")
        self.assertEqual(car.model, "Lovebug")
        self.assertEqual(car.year, 2019)
        self.assertAlmostEqual(car.price, 400.0)

    def test_add_feature(self):
        car = Car("Herbie", "Lovebug", price = 100.0)
        car.add_feature("heated seats")
        self.assertAlmostEqual(car.price, 300.0)

        car.add_feature("power steering")
        self.assertAlmostEqual(car.price, 650.0)


def main():
    unittest.main(verbosity = 3)

main()
