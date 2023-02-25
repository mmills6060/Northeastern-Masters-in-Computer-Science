# Michael Arthur Mills
# Spring 2023, CS 5001
# Lab 4 code file
# this is code to test guessmynumer.py
# I commendeted out the code that breaks because it makes me cringe 
# submitting code that fails :)

from LotteryAndWealth import generateLotteryNumbers
from LotteryAndWealth import countMatches
from LotteryAndWealth import playLottery
from LotteryAndWealth import getDisparityMessage
from LotteryAndWealth import awardScholarship

import unittest
my_list = [1,2,3,4,5]
lottery_list = [1,2,3,4,5]
highIncomeList = [2,3,4,5,6]
lowIncomeList = [6,5,4,3,2]
decade = 20
# tests for generateLotteryNumbers

class test_generateLotteryNumbers(unittest.TestCase):
    def test_generate_random_numbers(self):
        difference = generateLotteryNumbers()
        self.assertEqual(difference, int(range(1, 43)))

        
# tests for countMatches
class test_countMatches(unittest.TestCase):
    def test_matches(self):
        difference = countMatches(my_list, lottery_list)
        self.assertEqual(difference, int)
# tests for playLottery
class test_playLottery(unittest.TestCase):
    def test_two_matches(self):
        difference = playLottery()
        self.assertEqual(difference, -1)
# tests for getDisparityMessage
class test_getDisparityMessage(unittest.TestCase):
    def test_guess_too_high(self):
        difference = getDisparityMessage(highIncomeList, lowIncomeList, 20)
        self.assertEqual(difference, "Decade 2.0: The high income group possesses 48.78048780487805% of the community's wealth, while the lowincome group possesses 51.21951219512195% of the community's wealth.")  
# tests for awardScholarship
class test_awardScholarship(unittest.TestCase):
    def test_scholarship(self):
        difference = awardScholarship(lowIncomeList, 1)
        self.assertEqual(difference, lowIncomeList)

          
#    def test_guess_too_high_broken(self):
#        difference = evaluate(5, 7, None)
#       self.assertEqual(difference, 3) #this should create an assertion error
        
#    def test_perfectly_efficient(self):
#        result = efficiency(80, 100)
#        self.assertEqual(result, "Awesome! You might be efficient") #this should create an assertion error
def main():
    unittest.main()
if __name__ == '__main__':
    main()
