# Michael Arthur Mills
# April 7. 2023
# CS 5001


# This is an example of recursion

def count_characters(string):
    if string == "":
        return 0
    else:
        return 1 + count_characters(string[1:])
    