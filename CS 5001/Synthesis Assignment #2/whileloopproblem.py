# write a program that asks the user to enter to input a positive integer, and continues to ask the user to input a positive integer until the user inputs the negative integer. 
# When the user inputs a negative integer, the sum of all of the positive integers will be printed.  

# variables
num = 0
even_sum = 0

# ask user for input
while num >= 0:
    num = int(input("Enter a positive integer (or a negative integer to finish): "))
    if num % 2 == 0 and num >= 0:
        even_sum += num

# Print the sum of even integers
print("The sum of the even integers is:", even_sum)