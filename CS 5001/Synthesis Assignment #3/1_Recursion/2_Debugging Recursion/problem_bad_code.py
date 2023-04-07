# Michael Arthur Mills
# April 7. 2023
# CS 5001

# Example of buggy code that should determine lowest grade

def find_min(lst):
    if len(lst) == 1:
        return lst[0]
    else:
        mid = len(lst) // 2
        left_min = find_min(lst[:mid])
        right_min = find_min(lst[mid:])
        return min(left_min, right_min)
