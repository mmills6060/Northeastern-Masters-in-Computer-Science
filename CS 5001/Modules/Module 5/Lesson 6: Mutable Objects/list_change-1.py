''' Align Online
    CS5001
    Sample code -- example code demonstrating the effect of passing
    a multable object into a function
'''


def change(param):
    print("At start of change, param =", param)
    param = [101, 102, 103]
    print("At end of change, param =", param)


def main():
    data = [1, 2, 3]

    print("Before calling change, data =", data)
    change(data)
    print("After calling change, data =", data)
    print()


main()


