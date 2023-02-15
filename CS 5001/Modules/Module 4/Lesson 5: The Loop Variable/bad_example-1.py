''' Align Online
    CS5001
    Sample code -- the following loops is NOT a good example.
    The code reads 10 positive values in from the keyboard.
'''


def main():
    counter = 1
    while counter != -1:
        value = int(input("Enter value: "))
        if value > 0:
            counter += 1
        if counter > 10:
            counter = -1
    print("Done!")


main()
