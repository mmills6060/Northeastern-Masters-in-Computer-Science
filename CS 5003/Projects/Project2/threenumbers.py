# Michael Arthur Mills
# Fall 2023, CS 5001
# Lab 2 code file
# Practicing good code style and more complex functions


def main():
#ask the user to input the numbers
    firstnumber = int(input("Please provide your first number "))
    secondnumber = int(input("Please provide your second number --> "))
    thirdnumber = int(input("Please provide your third number --> "))

#Determine the min, max, based on the inputted numbers, print the result
    if firstnumber>secondnumber:
        if secondnumber>thirdnumber:
            print("The biggest number is:", firstnumber)
            print("The smallest number is:", thirdnumber)
        else:
            if firstnumber>thirdnumber:
                print("The biggest number is:", firstnumber)
                print("The smallest number is:", secondnumber)
            else:
                print("The biggest number is:", thirdnumber)
                print("The smallest number is:", secondnumber)
    else: 
            if secondnumber>thirdnumber:
                print("The biggest number is:", secondnumber)
                print("The smallest number is:", thirdnumber)
            else:
                if firstnumber>thirdnumber:
                    print("The biggest number is:", firstnumber)
                    print("The smallest number is:", thirdnumber)
                else:
                    print("The biggest number is:", thirdnumber)
                    print("The smallest number is:", firstnumber)

#print the average
    print("The average is:", (firstnumber + secondnumber + thirdnumber)/3),

main()