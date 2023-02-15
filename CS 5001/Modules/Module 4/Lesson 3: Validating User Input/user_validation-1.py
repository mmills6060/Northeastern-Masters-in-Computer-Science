''' Align Online
    CS5001
    Sample code -- using while loops to validate user input
'''


def main():

    # Validation 1: Re-prompt until they enter a positive int
    value = int(input("Please enter a positive int\n"))
    while value <= 0:
        value = int(input("That was not positive, go again\n"))
    print("Thank you!")

    # Validation 2: Re-prompt until they enter an int between 1 and 9
    value = int(input("Please enter a number 1-9\n"))
    while value < 1 or value > 9:
        value = int(input("That was not 1-9\n"))
    print("You got it, thanks!")

    # Validation 3: Re-prompt until they enter either 'L' or 'R'
    choice = input("Please enter L or R\n")
    while choice != "L" and choice != "R":
        choice = input("Not a valid option, try again\n")
    print("That was valid!")


main()
