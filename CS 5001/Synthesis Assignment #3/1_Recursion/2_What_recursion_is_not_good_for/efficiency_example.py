# Michael Arthur Mills
# April 7. 2023
# CS 5001

# This is an example of bad efficiency


def power_recursive(x, n):
    if n == 0:
        return 1
    elif n % 2 == 0:
        return power_recursive(x * x, n // 2)
    else:
        return x * power_recursive(x * x, (n - 1) // 2)

