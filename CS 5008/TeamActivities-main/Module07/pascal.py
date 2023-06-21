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

EXEC = ["./pascal.out"] 
COMMON_ARG_FORMAT = "{n} {type} 0"
FORMAT = "markdown"
TIMEOUT = 60

LAST_RUN_TRACKER = [0.0, 0.0, 0.0]

def run_single(n: int, typ: int) -> float:
    """Run a single instance collecting the total execution time

    Args:
        n (int): the row to generate
        typ (int): the type of algorithm to use

    Returns:
        float: the time it took, or nan if TIMEOUT is reached first
    """
    args = COMMON_ARG_FORMAT.format(n=n, type=typ)
    if math.isnan(LAST_RUN_TRACKER[typ]): return math.nan  # skip running if we are already timing out
    try:
        start = time.time()
        subprocess.run(EXEC + args.split(), timeout=TIMEOUT)
        end = time.time()
        result = end - start
        
    except subprocess.TimeoutExpired:
        result = math.nan
    LAST_RUN_TRACKER[typ] = result
    return result

def build_row(n:int) -> str:
    """Builds a row to print to the screen either in csv format or markdown

    Args:
        n (int): the row to build in the triangle

    Returns:
        str: a markdown formatted or csv string of the result
    """
    results_lst = []
    for t in range(0,3):
        result = run_single(n, t)
        results_lst.append("-" if math.isnan(result) else f"{result:.5f}")
    iterative, recursive, dynamic_programming = results_lst 
    if FORMAT == "markdown":
        return f"| {n:<4} | {iterative.center(8, ' ')} | {recursive.center(8, ' ')} | {dynamic_programming.center(8, ' ')} |"
    return f"{n},{iterative},{recursive},{dynamic_programming}"



def table_header() -> str:
    """Returns a markdown table header for this data set"""
    if FORMAT == "markdown":
        return "| n | Iterative | Recursive | Dynamic Programming |\n" + \
               "|--|:--:|:--:|:--:|"
    return "n,Iterative,Recursive,Dynamic Programming"



def main(n):
    print(table_header())
    for i in range(1,n+1):
        print(build_row(i))

## note while using argv directly, there are better tools for this like pip click
if __name__ == "__main__":
    n = 30 if len(sys.argv) < 2 else int(sys.argv[1])   
    if len(sys.argv) == 3:
        FORMAT = "csv"
    main(n)
