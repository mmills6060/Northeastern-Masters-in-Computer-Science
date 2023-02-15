''' Align Online
    CS5001
    Sample code -- an example of how to print the elements of a matrix,
    a list of lists
'''


def main():
    grades = [
        [98, 88, 89, 97, 78],
        [99, 85, 92, 74, 96],
        [77, 81, 69, 82, 84],
        [95, 79, 69, 76, 87]]
    print(grades)

    print("The grades are:")
    row = 0
    while row < len(grades):
        col = 0
        while col < len(grades[row]):
            print(grades[row][col], end="\t")
            col += 1
        print()
        row += 1
    print("Done!")


main()
