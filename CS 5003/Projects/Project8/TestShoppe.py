# File which will test the IceCreamShoppe class
# Created by Lindsay Jamieson
# 3/29/2022
# Implemented by Micvhael Mills
from Carton import Carton
from Scoop import Scoop
from IceCreamShoppe import IceCreamShoppe
import unittest

class TestIceCreamShoppe(unittest.TestCase):

    def setUp(self):
        self.shoppe = IceCreamShoppe(4, 6)
        self.scooper = Scoop(2)

    def test_serve(self):
        self.shoppe.serve(2, self.scooper)
        self.assertEqual(self.shoppe.cartons_used, 1)

    def test_cartonsUsed(self):
        self.assertEqual(self.shoppe.cartonsUsed(), 0)
        self.shoppe.serve(3, self.scooper)
        self.assertEqual(self.shoppe.cartonsUsed(), 1)
        self.shoppe.serve(2, self.scooper)
        self.assertEqual(self.shoppe.cartonsUsed(), 2)

def main():
    unittest.main(verbosity = 3)

main()