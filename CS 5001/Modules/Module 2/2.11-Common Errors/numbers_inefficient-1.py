"""
CS 5001: Intensive Foundations of Computer Science
Module: Boolean Expressions & Conditionals
Lesson 3-24 Multiway Conditionals

This program prints exactly one message for a number between 1 and 5.

In this version of the program, the sequential if statements all must run
one after the other making this a less efficient version of this example.
"""


def main():
    number = int(input("Enter integer between 1 and 5 (inclusive)"))

    if number == 1:
        print("one")
    if number == 2:
        print("two")
    if number == 3:
        print("three")
    if number == 4:
        print("four")
    if number == 5:
        print("five")
    print("Done")


main()
