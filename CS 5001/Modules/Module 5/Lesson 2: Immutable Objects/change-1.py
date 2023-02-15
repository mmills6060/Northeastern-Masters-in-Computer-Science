''' Align Online
    CS5001
    Sample code -- example code to demonstrate how immutable objects,
    like strings, are affected by function calls.
'''


def change(x):
    print("At start of change, x =", x)
    x = "see ya"
    print("At end of change, x =", x)


def main():
    x = "howdy"
    print("Before calling change, x =", x)
    change(x)
    print("After calling change, x =", x)


main()
