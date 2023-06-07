"""
CS 5001: Intensive Foundations of Computer Science
Module: Boolean Expressions & Conditionals
Lesson 3-24 Multiway Conditionals

This program prints exactly one message for a number between 1 and 5.

This is the program we started with in Lesson 3-2.
"""


def main():
    number = int(input("Enter integer between 1 and 5 (inclusive)"))

    if number == 1:
        print("one")
    else:
        if number == 2:
            print("two")
        else:
            if number == 3:
                print("three")
            else:
                if number == 4:
                    print("four")
                else:
                    print("five")

    print("Done")


main()
