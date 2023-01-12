# Michael Arthur Mills
# Fall 2023, CS 5001
# Lab 2 code file
# Practicing good code style and more complex functions



#ask the user to input the numbers
firstnumber = float(input("Please provide your first number "))
secondnumber = float(input("Please provide your second number --> "))
thirdnumber = float(input("Please provide your third number --> "))
#Determine in min, max, and average based on the inputted numbers
biggest = max(firstnumber, secondnumber, thirdnumber)
smallest = min(firstnumber, secondnumber, thirdnumber)
average = (firstnumber + secondnumber + thirdnumber) / 3
#print the results from what was determined
print("The biggest number is:", biggest)
print("The smallest number is:", smallest)
print("The average is:", average)


# I recommend that you write out your algorithm in comments.
# Then write the code for each comment directly below it.