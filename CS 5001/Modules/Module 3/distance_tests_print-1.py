''' Align Online
    CS5001
    Sample code -- testing Euclidean distance function (should
    be defined in a separate file called distance.py)

    This version of testing doesn't use conditionals, so no sweat
    if you haven't gotten to those modules yet. It just needs a human
    eyeball to read the output and make sure our expected vs actual
    values are pretty close.
'''


from distance import euclidean

def test_euclidean(x1, y1, x2, y2, expected):
    ''' Function test_euclidean
        Params: two points (floats)
        Return: nothing, just print actual vs expected
    '''
    print("Testing points", x1, y1, x2, y2)
    actual = euclidean(x1, y1, x2, y2)
    print("\tExpected......", expected)
    print("\tActual........", actual)

def main():
    # test 1
    test_euc(0, 0, 0, 0, 0.0)

    # test 2
    test_euc(2, -1, -2, 2, 5.0)

    # test 3
    test_euc(0, 0, 1, 1, 1.414)

    # test 3
    test_euc(-5.2, 3.8, -13.4, 0.2, 8.955)

main()
    
