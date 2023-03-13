# Michael Arthur Mills
# Spring 2023, CS 5001
# Write a recursive function which, given a list of numbers, finds the smallest number in the list.


numbers = [1, 2, 3, 4, 5, 6, 7,]


def find_smallest(numbers):
    if len(numbers) == 1:
        return numbers[0]
    else:
        smallest_remaining = find_smallest(numbers[1:])
        if numbers[0] < smallest_remaining:
            return numbers[0]
        else:
            return smallest_remaining
        
print(find_smallest(numbers))
        
