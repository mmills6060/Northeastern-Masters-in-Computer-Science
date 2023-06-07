# Michael Arthur Mills
# Spring 2023, CS 5001


# The function that we are going to test
def Total_Yardage(x, y):
    return x + y

# test case for the add function
def Test_Total_Yardage():
    # test inputs and expected outputs
    Test_Yardage = [
        (4000, 694, 4694),
        (5000, 250, 5250),
    ]

    # test Tom Brady 1
    x, y, expected = Test_Yardage[0]
    result = Total_Yardage(x, y)
    if result == expected:
        print("Success - The algorithm to calculate Tom Brady's passing yards matches what's expected")
    else:
        print("Failed")


    # test Patrick Mahomes 2
    x, y, expected = Test_Yardage[1]
    result = Total_Yardage(x, y)
    if result == expected:
        print("Success - The algorithm to calculate Patrick Mahomes' passing yards matches what's expected")
    else:
        print("Failed")

        
# run the test
Test_Total_Yardage()
