# Michael Arthur Mills
# April 7. 2023
# CS 5001

# write a block of code 
# that counts the number of characters in a string recursively.

def count_char(string, char):
    if string == '':
        return 0
    elif string[0] == char:
        return 1 + count_char(string[1:], char)
    else:
        return count_char(string[1:], char)