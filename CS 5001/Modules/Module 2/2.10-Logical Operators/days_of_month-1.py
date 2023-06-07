"""
CS 5001: Intensive Foundations of Computer Science
Module: Boolean Expressions & Conditionals
Lesson 3-5: Logical Operators

This determines the number of days given a month entered into the keyboard
assuming 3-letter abbreviations.  It then prints the number of days.

This is the program we wrote in Lesson 3-5.
"""


def main():
    month = input("Enter month: ")
    # determine the number of days
    if month == "Feb":
        days = 28
    elif month == "Sep" or month == "Apr" or month == "Jun" or month == "Nov":
        days = 30
    else:
        days = 31
    print(month, "has", days, "days")


main()
