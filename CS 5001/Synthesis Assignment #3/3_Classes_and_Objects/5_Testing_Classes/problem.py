# Michael Arthur Mills
# April 7. 2023
# CS 5001

# Unit test for the class website

import unittest

from problem import website

class TestWebsite(unittest.TestCase):
    def test_website(self):
        # create a website
        my_website = website()
        # test the initial values
        self.assertEqual(my_website.name, "Google")
        self.assertEqual(my_website.url, "www.google.com")
        self.assertEqual(my_website.price, 1000)
        # test the add_on method
        my_website.add_on("Contact US")
        self.assertEqual(my_website.price, 1100)
        my_website.add_on("About Us")
        self.assertEqual(my_website.price, 1200)

if __name__ == '__main__':
    unittest.main()


    