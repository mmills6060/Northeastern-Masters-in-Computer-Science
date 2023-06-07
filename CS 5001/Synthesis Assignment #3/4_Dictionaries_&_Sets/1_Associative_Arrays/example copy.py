# Michael Arthur Mills
# April 7. 2023
# CS 5001

# An example of how we can implement an associative array


def build_associative_array(keys, values):
    assoc = {}
    for i in range(len(keys)):
        assoc[keys[i]] = values[i]
    return assoc

# Test the function with example input
keys = ['BMW', 'Audi', 'Mercedes', 'Porsche']
values = [350, 325, 310, 410]
result = build_associative_array(keys, values)
print(result) 