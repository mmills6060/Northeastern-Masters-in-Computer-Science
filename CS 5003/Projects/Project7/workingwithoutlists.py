# Michael Arthur Mills
# Spring 2023, CS 5001
# Lab 7 code file

def computeTriangle( levels , m ):
    ''' This function is recursive.  It will compute the levels of Hosoya's triangle.
    It does NOT print Hosoya's triangle.  Remember that each location in the
    triangle is the sum of the two diagonally above it with the top two rows being:
    1
    1 1
    Input: The number of rows to generate
    Output: The triangle as a list of lists.'''
    # Base case
    if ((levels == 0 and m == 0) or
        (levels == 1 and m == 0) or
        (levels == 1 and m == 1) or
        (levels == 2 and m == 1)):
                return 1
     
    # Recursive step
    if levels > m:
        return computeTriangle(levels - 1, m) + computeTriangle(levels - 2, m)
 
    elif m == levels:
        return computeTriangle(levels - 1, m - 1) + computeTriangle(levels - 2,    m - 2)
 
    else:
        return 0
         
# Print the Hosoya triangle of height n.
def printTriangle( levels ):
    ''' This function will print a left justified copy of Hosoya's triangle.
    Input: triangle - the values to be printed, levels - the height of the triangle
    Output: NONE'''
    for i in range(levels):
        for j in range(i + 1):
            print(computeTriangle(i, j) , end = " ")
        print("\n", end = "")
         

def main(): 
    '''This is the main control function for the program.
    You should ask the user how many levels and then compute the triangle
    recursively. Then you should print the triangle.'''

    levels = int(input("Enter the height of the triangle  --> "))
    printTriangle(levels)

if __name__ == "__main__":
    main()