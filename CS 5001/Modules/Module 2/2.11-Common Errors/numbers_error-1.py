"""
CS 5001: Intensive Foundations of Computer Science
Module: Boolean Expressions & Conditionals
Lesson 3-24 Multiway Conditionals

This program prints exactly one message for a number between 1 and 5.

This program has a logical error.
"""


def main():
    number = int(input("Enter integer between 1 and 5 (inclusive)"))
    answer = "Not in range"

    if number == 1:
        answer = "one"
    elif number == 2:
        answer = "two"
    elif number == 3:
        answer = "three"
    elif number == 4:
        amswer = "four"
    elif number == 5:
        answer = "five"

    print(answer)


main()
