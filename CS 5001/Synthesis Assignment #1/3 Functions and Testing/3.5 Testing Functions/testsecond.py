# Michael Arthur Mills
# Spring 2023, CS 5001

# another example of testing a function
# example function to test
def is_even(x):
    return x % 2 == 0

# test for the is_even function
def test_is_even():
    # test inputs and expected outputs
    test = [(2, True),(3, False),(0, True)]

    # test 1
    x, expected = test[0]
    result = is_even(x)
    if result == expected:
        print("Success")
    else:
        print("Failed")

    # test 2
    x, expected = test[1]
    result = is_even(x)
    if result == expected:
        print("Success")
    else:
        print("Failed")

    # test 3
    x, expected = test[2]
    result = is_even(x)
    if result == expected:
        print("Success")
    else:
        print("Failed")

# run the test
test_is_even()