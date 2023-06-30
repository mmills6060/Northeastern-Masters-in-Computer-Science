import time
import csv


def fibonacci_iterative(n):
    if n <= 0:
        return -1  # Invalid input

    if n == 1 or n == 2:
        return 1

    prev, curr = 1, 1
    fibonacci_series = []
    for _ in range(1, n + 1):
        fibonacci_series.append(curr)
        prev, curr = curr, prev + curr

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


n = 100
option = 0  # 0 = Print everything, 1 = Print final result, 2 = Print nothing

if option == 0:
    fibonacci_series, final_result = fibonacci_iterative(n)
    print("Fibonacci iterative:")
    with open('fibonacci_data.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['n', 'Elapsed Time - Python'])
        start_time = time.time()
        for i, result in enumerate(fibonacci_series, start=1):

            end_time = time.time()
            elapsed_time = end_time - start_time
            writer.writerow([i, elapsed_time])
            print(f"{elapsed_time:.15f}")
    print()

    fibonacci_series, final_result = fibonacci_recursive(n)
    print("Fibonacci recursive:")
    for i, result in enumerate(fibonacci_series, start=1):
        print(f"F({i}) = {result}")
        start_time = time.time()
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"Elapsed Time: {elapsed_time:.6f} seconds")
    print()

    fibonacci_series, final_result = fibonacci_dynamic(n)
    print("Fibonacci dynamic programming:")
    for i, result in enumerate(fibonacci_series, start=1):
        print(f"F({i}) = {result}")
        start_time = time.time()
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"Elapsed Time: {elapsed_time:.6f} seconds")
    print()

    print_fibonacci_series(n)

elif option == 1:
    fibonacci_series, final_result = fibonacci_iterative(n)
    print(f"The {n}th Fibonacci number is: {final_result}")
    start_time = time.time()
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Elapsed Time: {elapsed_time:.6f} seconds")

elif option == 2:
    pass
