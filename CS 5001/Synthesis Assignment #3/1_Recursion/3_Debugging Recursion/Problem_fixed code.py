# Michael Arthur Mills
# April 7. 2023
# CS 5001

def find_min(lst):
    if len(lst) == 1:
        print("Base case reached, returning", lst[0])
        return lst[0]
    else:
        mid = len(lst) // 2
        print("Left half:", lst[:mid])
        left_min = find_min(lst[:mid])
        print("Right half:", lst[mid:])
        right_min = find_min(lst[mid:])
        print("Minimum between", left_min, "and", right_min, "is", min(left_min, right_min))
        return min(left_min, right_min)
