# Michael Arthur Mills
# Fall 2023, CS 5001
# Lab 2 code file

import random

def guessthecolor():
# Asking the user to choose a color, asking the user
# to try again if inputted incorrectly.
# Returning the value of the color globally
    color = input("Please guess a oolor (Black or Red) -->  ")
    question = False    
    while question == False:
        if color in ["Black" , "Red"]:
            question = True
        else:
            question = False
        if question == True:    
            print ("You chose " + color)
            return color
        else:
            if question == False:
                print  ("Please ensure that you are using correct spelling and capitalization.")
                color = input("Please guess a oolor (Black or Red) -->  ")

def resultofgame(color,suits):
# Printing the result of whether or not the chosen 
# color is equal to the color of the card pulled
    if color == getColor(suits):
        print ("You chose the correct color")
    else:
        print ("You did not choose the correct color")
        
def getSuit():
# pick a random suit for a card. 
    suits = ['Diamonds', 'Hearts', 'Clubs', 'Spades']
    return random.choice(suits)

def getValue():
# pick a random value for a card
    value = ['Ace', '2', '3', '4','5', '6', '7', '8', '9' , '10' , 'Jack' , 'Queen', 'King']
    return random.choice(value)

def printCard(value, suits):
# print out the value of the card (ie Ace of Spades or 10 of Clubs)
# to the user based on the value and suit that are the parameters.
    print("You pulled a(n) " + value + " of " + suits + " from the deck of cards")
    pass

def getColor(suit):
# Determining the color of the card based on whether it is Spades/Clubs or Diamonds/Hearts
    if suit in ["Spades", "Clubs"]:
        return "Black"
    else:
        return "Red"
def main():
    suit = getSuit()
    value = getValue()
    color = guessthecolor()
    printCard(value, suit)
    resultofgame(color, suit)

#remember to put in the lines to call main() that are described in part 6
if __name__ == "__main__":
    main()