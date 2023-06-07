# Michael Arthur Mills
# April 7. 2023
# CS 5001

# An example of an execution path

def sum_of_natural_numbers(n):
    sum = 0
    for i in range(1, n+1):
        sum += i
    return sum

print(sum_of_natural_numbers(10))
