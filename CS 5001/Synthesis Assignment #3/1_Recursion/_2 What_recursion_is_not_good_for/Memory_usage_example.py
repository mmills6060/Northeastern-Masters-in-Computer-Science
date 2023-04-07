# Michael Arthur Mills
# April 7. 2023
# CS 5001

# This is an example of bad memory with recursion

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(1000))