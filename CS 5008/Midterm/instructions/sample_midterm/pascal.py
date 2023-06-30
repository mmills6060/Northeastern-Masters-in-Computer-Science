"""
Example file solving the pascal triangle using python.
Author: Albert Lionelle
Semester: Spring 2023
"""
from enum import Enum
from typing import List
from functools import lru_cache
import click
import sys

STACK_LIMIT = 1000
sys.setrecursionlimit(100000)


class PascalType(Enum):
    DP = 2
    RECURSIVE = 1
    ITERATIVE = 0


@lru_cache(maxsize=None)
def pascal_dp(n: int, i: int) -> int:
    """
    Solves the pascal triangle using simple recursion and built
    in memoization
    Args:
        n: the nth row
        i: the item in the row

    Returns:
        the addition of n-1, i + n-1, i-1
    """
    if n == i or i == 0:
        return 1
    return pascal_dp(n - 1, i) + pascal_dp(n - 1, i - 1)


def pascal_r(n: int, i: int) -> int:
    """
    Solves the pascal triangle using simple recursion
    Args:
        n (int): the nth row
        i (int): the item in the row

    Returns:
        the addition of n-1, i + n-1, i-1
    """
    if n == i or i == 0:
        return 1
    return pascal_r(n - 1, i) + pascal_r(n - 1, i - 1)


def recursive_pascal(n: int, print_it: bool, func=pascal_r) -> List[int]:
    """

    Args:
        func:
        n:
        print_it:

    Returns:

    """
    result = []
    if print_it:
        for line in range(0, n):
            result = []
            for i in range(0, line + 1):
                tmp = func(line, i)
                print(tmp, end=' ')
                if line + 1 == n:
                    result.append(tmp)
            print()
    else:
        if n > STACK_LIMIT:  # due to stack limit size, tabulate data first
            steps = n // STACK_LIMIT
            for step in range(1, steps):
                new_n = step * STACK_LIMIT
                for i in range(0, new_n + 1):
                    func(new_n, i)
        n = n - 1  # due to counting by 0
        for i in range(0, n + 1):
            result.append(func(n, i))
    return result


def get_pascal_triangle(n: int, print_it: bool = False, version: PascalType = PascalType.ITERATIVE) -> List[int]:
    """
    Generates the nth row in the pascal triangle based on the
    method requested

    Args:
        n: the row to generate
        print_it:  print out all rows as being generated
        version:  the type/method of generation

    Returns:
        the nth row of the pascal triangle
    """
    if version == PascalType.RECURSIVE:
        return recursive_pascal(n, print_it)
    if version == PascalType.DP:
        return recursive_pascal(n, print_it, pascal_dp)
    # assumed else due to returns, Iterative version
    arr: List[List] = []
    for i in range(0, n):
        arr.append([])
        for j in range(0, i + 1):
            if i == j or j == 0:
                arr[i].append(1)
            else:
                arr[i].append(arr[i - 1][j - 1] + arr[i - 1][j])
            if print_it:
                print(arr[i][-1], end=' ')
        if print_it:
            print()
    return arr[n - 1]


# click does not work on the khoury servers, instead if you are writing
# a script for the khoury servers you will want to use argparse or just
# sys.argv (seen in test_runner.py)

@click.command()
@click.argument("n", type=click.IntRange(min=0, max=50000, clamp=True))
@click.option("--algo", type=click.Choice(['recursive', 'dp', 'iterative'], case_sensitive=False), default='iterative')
@click.option("--print-type", type=click.Choice(['all', 'none', 'single'], case_sensitive=False), default='none')
def main(n: int, algo: str, print_type: str):
    """
    Prints the string the Nth row/ generates the nth row of the pascal triangle.

    Args:
        algo:
        print_type:
        n: the nth row to generate
    """
    print_it = print_type == 'all'
    t = PascalType.ITERATIVE
    if algo == 'recursive':
        t = PascalType.RECURSIVE
    elif algo == 'dp':
        t = PascalType.DP
    tri = get_pascal_triangle(n, print_it, t)
    if print_type == 'single':
        print(tri)

    # print(get_pascal_triangle(3000, False, PascalType.DP)[-2])


if __name__ == "__main__":
    main()
