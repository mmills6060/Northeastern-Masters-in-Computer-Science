import sys

number = ( sys.argv[1] )

# calculate whether a number is odd or even
def oddOrEven( number ):
    print('determining if ' + number + ' is odd or even:')

    # if statement
    if my_number%2==0:
        print(number + " is even.") 
    else:
        print(number + " is odd.")

# assign values to variables
my_number = int(number)

# call the function
oddOrEven(number)





