"""
CS 5001: Intensive Foundations of Computer Science
Module: Boolean Expressions & Conditionals
Lesson 3-24 Multiway Conditionals

This program prints exactly one message for a number between 1 and 5.

In this version of the program, we are using a multiway conditional so that 
only once choice executes.
"""


def main():
    number = int(input("Enter integer between 1 and 5 (inclusive)"))

    if number == 1:
        print("one")
    elif number == 2:
        print("two")
    elif number == 3:
        print("three")
    elif number == 4:
        print("four")
    elif number == 5:
        print("five")

    print("Done")


main()
