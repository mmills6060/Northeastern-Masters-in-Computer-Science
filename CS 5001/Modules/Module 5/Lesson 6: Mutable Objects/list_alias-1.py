''' Align Online
    CS5001
    Sample code -- example code demonstrating the affect of aliasing
'''


def main():
    data = [1, 2, 3]

    print("Creating alias of data")
    alias = data
    print("Creating copy of data")
    copy = data.copy()
    print()

    print("data  =", data)
    print("alias =", alias)
    print("copy  =", copy)
    print()

    print("Setting first element in alias")
    alias[0] = 1001
    print("Setting first element of copy")
    copy[0] = -50
    print()

    print("data  =", data)
    print("alias =", alias)
    print("copy  =", copy)


main()
