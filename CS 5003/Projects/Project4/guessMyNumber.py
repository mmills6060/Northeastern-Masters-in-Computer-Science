# Michael Arthur Mills
# Spring 2023, CS 5001
# Lab 4 code file
# generate a random number, then play a guessing game with user. 
# additional efficiency functionality added as well.

import random
import sys

# evaluate guess function
def evaluate(guess, number, prev_difference):
    difference = abs(guess - number)
    if guess > number:
        print("Your guess is too high")
        hotter_or_colder(prev_difference, difference)
    elif guess < number:
        print("Your guess is too low")
        hotter_or_colder( prev_difference, difference)
    else:
        print("You got it!")
    return difference



# hotter/colder function

def hotter_or_colder(prev_difference, difference):
    if prev_difference is None:
        return("You have not guessed before")
    elif difference > prev_difference:
        return("You are getting colder")
    else:
        return("You are getting hotter")

# efficiency function
def efficiency(turns_used, max_random_number):
    # efficiency_percentile = ((turns_used / max_random_number) * 100)
    # efficiency_percentile = (turns_used / (max_random_number * .5)) * 100
    # I am sure there is a better algorithm to calculate efficiency
    # while ensuring that score is directly proportional to varying 
    # number of turns used but this is good enough for now I think. 
    # a weakness in this equation is if we test on varying max random numbers
    # efficiency_score = (max_random_number / turns_used)
    efficiency_score = 100 - (turns_used / max_random_number) * 100
    print("Turns Used: " + str(turns_used))
    print("Your efficiency score was " + str(efficiency_score))
    if efficiency_score >= 99:
        return("Awesome! You are perfcectly efficient")
    elif efficiency_score >= 75:
        return("Good job! You are very efficient")        
    elif efficiency_score >= 50:
        return("Good job! You used a reasonable number of turns")
    elif efficiency_score >= 30:
        return("You are not very efficient")        
    else:
        return("You are not efficient at all")
        
#main function
def main():
    # assign the variable number to the second word input in command line terminal
# check for user input
    #command line argument that sets max random number
    if len( sys.argv ) > 1:
        # re-assign the value if the user provided one
        max_random_number = int( sys.argv[1] )
    else:
        #if user did not re-assign value use a standard value of 10
        max_random_number = 10
    print("Welcome to the guessing game, written by Michael Arthur Mills")
    random_number = random.randint(1, max_random_number)
    prev_difference = None
    turns_used = 0
    while True:
        guess = int(input("Enter your guess: "))
        difference = evaluate(guess, random_number, prev_difference)
        turns_used += 1
        print(hotter_or_colder(prev_difference, difference))
        if guess == random_number:
            break
        prev_difference = difference
    efficiency(turns_used, max_random_number)
    print(efficiency(turns_used, max_random_number))
    
        
if __name__ == "__main__":
    main()
    
    
# Changed the user input to main instead of def evaluate
# towards the end of writing the program  I realized that there needed
# to be a loop in the main function.
# used Real Python to find self.assertion function
# my equation for efficiency never is 100%, only goes to 99%  
