''' Align Online
    CS5001
    Sample code -- example code demonstrating the effect of modifying
    a multable object in a function
'''


def modify(param):
    print("At start of modify, param =", param)
    param[0] = 42
    print("At end of modify, param =", param)


def main():
    data = [1, 2, 3]

    print("Before calling modify, data =", data)
    modify(data)
    print("After calling modify, data =", data)
    print()


main()
