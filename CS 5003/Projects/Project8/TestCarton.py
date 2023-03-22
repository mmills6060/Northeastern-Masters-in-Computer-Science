# File which will hold the implementation of Carton
# Created by Michael Mills
# 3/29/2022



import unittest
from Scoop import Scoop
from Carton import Carton

class CrashTest(unittest.TestCase):

    def test_hasEnoughFor(self):
        carton = Carton(5, 10)
        scoop = Scoop(2)
        self.assertTrue(carton.hasEnoughFor(scoop))
        scoop2 = Scoop(10)
        self.assertFalse(carton.hasEnoughFor(scoop2))
    def test_remove(self):
        carton = Carton(5, 10)
        scoop = Scoop(2)
        carton.remove(scoop)
        self.assertEqual(carton.remaining, carton.volume - scoop.volume)   
def main():
    unittest.main(verbosity = 3)

main()