# Michael Arthur Mills
# Spring 2023, CS 5001
# An example of a function.
# determine if a given number is odd or even

def odd_or_even(num):
    if num % 2 == 0:
        return "even"
    else:
        return "odd"

result = odd_or_even(4)
print(result) # Output: 'even'
result = odd_or_even(5)
print(result) # Output: 'odd'