''' Align Online
    CS5001
    Sample code -- importing distance function from another file for testing

   This version of testing uses conditionals, so hopefully you've
    watched those videos already. (If not, check out the other
    testing file, because you don't need conditionals under your
    belt in order to write good tests!)
'''

from distance import euclidean

EPSILON = 0.001

def test_euclidean(x1, y1, x2, y2, expected):
    ''' function test_euclidean
        Parameters: two points and an expected value
        Returns: true if actual == expected, false otherwise
        Does: calls the euclidean distance function and compares
              actual vs expected to determine success
    '''
        
    print('Testing points (', x1, ', ', y1, '), (', x2, ', ', y2, ')', sep = '')
    actual = euclidean(x1, y1, x2, y2)
    return abs(actual - expected) < EPSILON

def run_distance_tests():
    ''' function run_distance_tests
        Parameters: none
        Returns: an int, number of tests that failed
    '''
    num_fail = 0
    
    # Test 1: (0, 0), (0, 0). Expected: 0
    if (test_euclidean(0, 0, 0, 0, 0.0)):
        print('PASSED! :)')
    else:
        print('FAILED :(')
        num_fail += 1

    # Test 2: (2, -1), (-2, 2). Expected: 5
    if (test_euclidean(2, -1, -2, 2, 5.0)):
        print('PASSED! :)')
    else:
        print('FAILED :(')
        num_fail += 1

    # Test 3: (0, 0), (1, 1). Expected: 1.414
    if (test_euclidean(0, 0, 1, 1, 1.414)):
         print('PASSED! :)')
    else:
        print('FAILED :(')
        num_fail += 1

    # Test 4: (-5.2, 3.8), (-13.4, 0.2). Expected: 8.955
    if (test_euclidean(-5.2, 3.8, -13.4, 0.2, 8.955)):
        print('PASSED! :)')
    else:
        print('FAILED :(')
        num_fail += 1

    return num_fail
    
def main():
    print('Testing Euclidean distance functions...\n\n')
    failures = run_distance_tests()
    if failures == 0:
        print('Everything passed, great job functions!')
    else:
        print('Something went wrong, go back and fix pls.')
    

main()
