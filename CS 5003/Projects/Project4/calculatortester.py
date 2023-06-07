# Gregory Valcourt
# 1/31/2023
# CS5001 Recitation SP23
# A program to demonstrate testing of files
# testing calculator.py

#I'm using calc to shorten up what I type
import calculator as calc
#You don't have to use unittest; I just like the information it tells me.
import unittest

# Tests if certain operators return correctly with correct values
def testOperatorCheckGood():
    val1=2
    val2=2
    operator="+"
    assert calc.operatorCheck(val1, operator, val2) == "you asked for 4"
    operator="*"
    assert calc.operatorCheck(val1, operator, val2) == "you asked for 4"
    print("No errors in testOperatorCheckGood()\n\n\n")





#A really fancy way to do testing
#modified from https://realpython.com/python-testing/#writing-your-first-test
class TestOperatorCheck(unittest.TestCase):
    def test_operator_check_plus(self):
        """
        Test that it can return the right values with plus
        """
        #set values
        val1=2
        val2=2
        operator="+"
        #create result
        result = calc.operatorCheck(val1, operator, val2)
        #check if it is correct
        self.assertEqual(result, "you asked for 4")
        
    def test_operator_check_star(self):
        """
        Test that it can return the right values with star
        """
        val1=2
        val2=2
        operator="*"
        result = calc.operatorCheck(val1, operator, val2)
        self.assertEqual(result, "you asked for 4")

    def test_operator_check_handled_issue(self):
        """
        Test that it can return the right values with handled issue of no $ character and vals as strings
        """
        val1=2
        val2=2
        operator="$"
        result = calc.operatorCheck(val1, operator, val2)
        self.assertEqual(result, "I don't understand")

        val1="2"
        val2="2"
        operator="*"
        result = calc.operatorCheck(val1, operator, val2)
        self.assertEqual(result, "I don't understand")


    def test_operator_check_broken(self):
        """
        Test that unittest returns an expected failure
        """
        val1="2"
        val2="2"
        operator="*"
        result = calc.operatorCheck(val1, operator, val2)
        self.assertEqual(result, "you asked for 4") #"I don't understand" is the correct value


def main():
    testOperatorCheckGood()

if __name__ == "__main__":
    main()
    unittest.main()
