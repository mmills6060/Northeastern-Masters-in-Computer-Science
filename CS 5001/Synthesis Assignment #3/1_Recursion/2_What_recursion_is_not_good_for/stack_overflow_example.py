# Michael Arthur Mills
# April 7. 2023
# CS 5001

# This is an example of stack overflow

n = 1000000

def recursive_add(n):
    if n == 0:
        return 0
    else:
        return n + recursive_add(n-1)
