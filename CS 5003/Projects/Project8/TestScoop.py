# File which will hold the implementation of Scoop
# Created by Michael Mills
# 3/29/2022


from Scoop import Scoop
import unittest

class CrashTest(unittest.TestCase):
    def test_init(self):
      pass

    def test_Volume(self):
        scoop = Scoop(2)
        expected_volume = 33.493333333333333
        actual_volume = scoop.volume()
        self.assertAlmostEqual(actual_volume, expected_volume)

def main():
    unittest.main(verbosity = 3)

main()
         
        