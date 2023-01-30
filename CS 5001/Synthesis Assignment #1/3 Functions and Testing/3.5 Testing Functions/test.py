# Michael Arthur Mills
# Spring 2023, CS 5001

# an example of testing functions
# The function that we are going to test
def add(x, y):
    return x + y

# test case for the add function
def test_add():
    # test inputs and expected outputs
    test = [
        (4, 2, 6),(6, 2, 8),(-2, -2, -4)
    ]

    # test 1
    x, y, expected = test[0]
    result = add(x, y)
    if result == expected:
        print("Success")
    else:
        print("Failed")


    # test 2
    x, y, expected = test[1]
    result = add(x, y)
    if result == expected:
        print("Success")
    else:
        print("Failed")

    # test 3
    x, y, expected = test[2]
    result = add(x, y)
    if result == expected:
        print("Success")
    else:
        print("Failed")
        
# run the test
test_add()
