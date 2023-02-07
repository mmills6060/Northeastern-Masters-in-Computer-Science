# Michael Arthur Mills
# Spring 2023, CS 5001
# Lab 3 code file

#import packages
import sys

# assign the variable number to the second word input in command line terminal
# check for user input

if len( sys.argv ) > 1:
    # re-assign the value if the user provided one
    number = ( sys.argv[1] )
    my_number = int(number)
else:
    #if user did not re-assign value use a standard value of 10
    number = "10"
    my_number = int(number)
# calculate whether a number is odd or even
def oddOrEven( number ):
    print('determining if ' + number + ' is odd or even:')
    # if statement
    if my_number%2==0:
        print(number + " is even.") 
    else:
        print(number + " is odd.")

def main():
# call the function
    oddOrEven(number)

if __name__ == "__main__":
    main()
