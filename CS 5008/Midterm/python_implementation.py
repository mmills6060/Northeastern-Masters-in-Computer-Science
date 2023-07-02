import sys
import time
import csv


def fibonacci_iterative(n):
    fibonacci_series = []
    a, b = 0, 1

    for _ in range(n):
        fibonacci_series.append(a)
        a, b = b, a + b

    curr = a

    return fibonacci_series, curr


def fibonacci_recursive(n):
    if n <= 0:
        return -1  # Invalid input

    if n == 1 or n == 2:
        return 1

    fibonacci_series = []
    for i in range(1, n + 1):
        fibonacci_series.append(_fibonacci_recursive_helper(i))

    return fibonacci_series, _fibonacci_recursive_helper(n)


def _fibonacci_recursive_helper(n):
    if n == 1 or n == 2:
        return 1

    return _fibonacci_recursive_helper(n - 1) + _fibonacci_recursive_helper(n - 2)


def fibonacci_dynamic(n):
    if n <= 0:
        return -1  # Invalid input
    if n == 1 or n == 2:
        return 1
    memo = [-1] * (n + 1)
    fibonacci_series = []
    for i in range(1, n + 1):
        fibonacci_series.append(_fibonacci_dynamic_helper(i, memo))
    return fibonacci_series, _fibonacci_dynamic_helper(n, memo)


def _fibonacci_dynamic_helper(n, memo):
    if n == 1 or n == 2:
        return 1
    if memo[n] != -1:
        return memo[n]
    memo[n] = _fibonacci_dynamic_helper(n - 1, memo) + _fibonacci_dynamic_helper(n - 2, memo)
    return memo[n]


def print_fibonacci_series(n):
    if n <= 0:
        return  # Invalid input

    prev, curr = 0, 1
    print(f"Fibonacci series from 1 to {n}:")
    for _ in range(1, n + 1):
        prev, curr = curr, prev + curr
    print()

def main(n:int, algo: str, print_type:str):
# print the n'th row 

# Args:
#   algo:
#   print_type: 
#   n: the nth row to generate
    print_it = print_type == 'all'
    result = fibonacci_iterative(n)
    if algo == 'recursive':
        result = fibonacci_recursive(n)
    elif algo == 'dp':
        result = fibonacci_dynamic(n)
if __name__ == "__main__":
    _n = 30 if len(sys.argv) < 2 else int(sys.argv[1])
    algo = "iterative"  # Replace with the desired algorithm
    print_type = "csv"  # Replace with the desired print type
    main(_n, algo, print_type)
