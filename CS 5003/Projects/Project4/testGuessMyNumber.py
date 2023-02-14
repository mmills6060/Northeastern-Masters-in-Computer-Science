# Michael Arthur Mills
# Spring 2023, CS 5001
# Lab 4 code file
# this is code to test guessmynumer.py
# I commendeted out the code that breaks because it makes me cringe 
# submitting code that fails :)

from guessmyNumber import evaluate
from guessmyNumber import hotter_or_colder
from guessmyNumber import efficiency

import unittest

# tests for evaluate
class test_evaluate(unittest.TestCase):
    def test_guess_too_high(self):
        difference = evaluate(7, 5, None)
        self.assertEqual(difference, 2)

    def test_guess_too_low(self):
        difference = evaluate(3, 5, None)
        self.assertEqual(difference, 2)

    def test_guess_correct(self):
        difference = evaluate(5, 5, None)
        self.assertEqual(difference, 0)

        
#    def test_guess_too_high_broken(self):
#        difference = evaluate(5, 7, None)
#       self.assertEqual(difference, 3) #this should create an assertion error
        
#tests for hotter/colder
class test_hotter_colder(unittest.TestCase):
    def test_not_guessed_before(self):
        result = hotter_or_colder(None, 1)
        self.assertEqual(result, "You have not guessed before")
    def test_getting_colder(self):
        result = hotter_or_colder(1, 2)
        self.assertEqual(result, "You are getting colder")  
    def test_getting_hotter(self):
        result = hotter_or_colder(2, 1)
        self.assertEqual(result, "You are getting hotter")
#    def test_getting_hotter_break(self):
#        result = hotter_or_colder(2, 1)
#        self.assertEqual(result, "You are the same") #this should create an assertion error
                 
#tests for efficiency function
class test_efficiency(unittest.TestCase):
    def test_perfectly_efficient(self):
        result = efficiency(1, 100)
        self.assertEqual(result, "Awesome! You are perfcectly efficient")
    def test_perfectly_efficient(self):
        result = efficiency(25, 100)
        self.assertEqual(result, "Good job! You are very efficient")
    def test_perfectly_efficient(self):
        result = efficiency(50, 100)
        self.assertEqual(result, "Good job! You used a reasonable number of turns")
    def test_perfectly_efficient(self):
        result = efficiency(70, 100)
        self.assertEqual(result, "You are not very efficient")
    def test_perfectly_efficient(self):
        result = efficiency(80, 100)
        self.assertEqual(result, "You are not efficient at all")
#    def test_perfectly_efficient(self):
#        result = efficiency(80, 100)
#        self.assertEqual(result, "Awesome! You might be efficient") #this should create an assertion error
def main():
    unittest.main()
if __name__ == '__main__':
    main()
