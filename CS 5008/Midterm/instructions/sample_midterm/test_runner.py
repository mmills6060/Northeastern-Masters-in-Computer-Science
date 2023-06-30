"""
The following python "script" can be ran to help collect 
process time for multiple iterations. External scripts like this are 
common in research.    


Sample execution would be to write out the standard out (print) to a file. For example

python3 test_runner.py 30 csv  > pascal_run.csv

python3 test_runner.py 30 > pascal_table.md
"""

import subprocess
import time
import sys
import math
from typing import Union

COMMON_ARG_FORMAT = "./pascal.out {n} {algo} 0"
FORMAT = "markdown"
TIMEOUT = 60
COMMON_ARG_PYTHON = "python3 pascal.py --algo {algo} {n}"  # I also used  pypy3 as it is faster than python
PYTHON_SET = ('iterative', 'recursive', 'dp')

LAST_RUN_TRACKER = {"0": 0.0, "1": 0.0, "2": 0.0, "iterative": 0.0, "recursive": 0.0, "dp": 0.0}


def run_single(n: int, typ: Union[int, str], command=COMMON_ARG_FORMAT) -> float:
    """Run a single instance collecting the total execution time

    Args:
        command:
        n (int): the row to generate
        typ (int): the type of algorithm to use

    Returns:
        float: the time it took, or nan if TIMEOUT is reached first
    """
    command = command.format(n=n, algo=typ)
    if math.isnan(LAST_RUN_TRACKER[str(typ)]):
        return math.nan  # skip running if we are already timing out
    try:
        start = time.time()
        subprocess.run(command.split(), timeout=TIMEOUT)
        end = time.time()
        result = end - start

    except subprocess.TimeoutExpired:
        result = math.nan
    LAST_RUN_TRACKER[str(typ)] = result
    return result


def build_row(n: int) -> str:
    """Builds a row to print to the screen either in csv format or markdown

    Args:
        n (int): the row to build in the triangle

    Returns:
        str: a markdown formatted or csv string of the result
    """
    results_lst = []
    for t in range(0, 3):
        result = run_single(n, t)
        results_lst.append("-" if math.isnan(result) else f"{result:.5f}")
    iterative, recursive, dynamic_programming = results_lst

    results_lst = []
    for t in PYTHON_SET:
        result = run_single(n, t, COMMON_ARG_PYTHON)
        results_lst.append("-" if math.isnan(result) else f"{result:.5f}")
    iterative_p, recursive_p, dynamic_programming_p = results_lst

    if FORMAT == "markdown":
        return f"| {n:<4} | {iterative.center(8, ' ')} | {recursive.center(8, ' ')} | {dynamic_programming.center(8, ' ')} |" \
            + f"{iterative_p.center(8, ' ')} | {recursive_p.center(8, ' ')} | {dynamic_programming_p.center(8, ' ')} |"
    return f"{n},{iterative},{recursive},{dynamic_programming},{iterative_p},{recursive_p},{dynamic_programming_p}"


def table_header() -> str:
    """Returns a markdown table header for this data set"""
    if FORMAT == "markdown":
        return "| n | Iterative C | Recursive C | Dynamic Programming  C | Iterative P | Recursive P | Dynamic Programming  P |\n" + \
            "|--|:--:|:--:|:--:|:--:|:--:|:--:|"
    return "n,Iterative C,Recursive C,Dynamic Programming C,Iterative P,Recursive P,Dynamic Programming P"


def main(n):
    print(table_header())
    for i in range(1, n + 1, 500): ## If you use this script, you will want to change this range!! 
        print(build_row(i))


# note while using argv directly, there are better tools for this like pip click as shown in pascal.py
if __name__ == "__main__":
    _n = 30 if len(sys.argv) < 2 else int(sys.argv[1])
    if len(sys.argv) == 3:
        FORMAT = "csv"
    main(_n)
