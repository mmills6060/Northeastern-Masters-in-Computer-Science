"""
Module: Boolean Expressions & Conditionals
Lesson 3-6: Common Errors

This code attempts to find the maximum of five values entered into the keyboard.
It does this by checking each value against the other four values.

There is an error in this code.  Can you find it?
"""


def main():
    first = int(input("Enter first number: "))
    second = int(input("Enter second number: "))
    third = int(input("Enter third number: "))
    fourth = int(input("Enter fourth number: "))
    fifth = int(input("Enter fifth number: "))

    # compute the maximum
    if first >= second and first >= third and first >= fourth and first >= fifth:
        max = first
    elif second >= first and second >= third and second >= fourth and second >= fifth:
        max = second
    elif third >= first and third >= second and third >= fourth and third >= fifth:
        max = third
    elif fourth >= first and fourth >= second and fourth >= fourth and fourth >= fifth:
        max = fourth
    else:
        max = fifth
    # print result
    print("Maximum number is", max)


main()
