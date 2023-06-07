# Michael Arthur Mills
# Spring 2023, CS 5001
# Lab 7 code file

def computeTriangle(levels):
    ''' This function is recursive.  It will compute the levels of Hosoya's triangle.
    It does NOT print Hosoya's triangle.  Remember that each location in the
    triangle is the sum of the two diagonally above it with the top two rows being:
    1
    1 1
    Input: The number of rows to generate
    Output: The triangle as a list of lists.'''
    
    # Initialize the first three rows of the triangle
    result = [[1], [1, 1], [2, 1, 2]]
    
    # Compute the remaining rows of the triangle
    for i in range(2, levels):
        next_row = []
        
        # Compute the first two values in the row
        for j in range(2):
            next_row.append(result[-1][j] + result[-2][j])
        
        # Compute the remaining values in the row
        for j in range(2, i + 2):
            next_row.append(result[-1][j - 1] + result[-2][j - 2])
        
        # Add the completed row to the triangle
        result.append(next_row)
        
    return result 
        

# Print the Hosoya triangle of height n.
def printTriangle(triangle):
    ''' This function will print a left justified copy of Hosoya's triangle.
    Input: triangle - the values to be printed
    Output: NONE'''
    
    for row in triangle:
        print(" ".join([str(val) for val in row]))
        

def main(): 
    '''This is the main control function for the program.
    You should ask the user how many levels and then compute the triangle
    recursively. Then you should print the triangle.'''
    
    # Get the number of levels from the user
    levels = int(input("Enter the number of levels: "))
    
    # Compute the triangle and print it
    triangle = computeTriangle(levels)
    printTriangle(triangle)

if __name__ == "__main__":
    main()
