# Michael Arthur Mills
# Spring 2023, CS 5001
# Lab 3 code file

# To run code,in terminal, "python3 guesscard.py Red"
import random
import sys

def guessthecolor():
# Asking the user to choose a color, asking the user
# to try again if inputted incorrectly.
# Returning the value of the color globally
    color = sys.argv[1]
    # commenting out first line because we are supposed to have this 
    # via terminal and not internal
    #color = input("Please guess a oolor (Black or Red) -->  ")
    question = False    
    while question == False:
        if color == "Black":
            question = True
        else:
            if color == "Red":
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
    number = random.randint(0,3)
    if number == 0:
        suits = 'Diamonds'
    elif number == 1:
        suits = 'Hearts'        
    elif number == 2:
        suits = 'Clubs'        
    elif number == 3:
        suits = 'Spades'
    else:
        print("Error, random number not recognized as correlating to suit")            
    return suits

    # commenting out the below code because we have not covered lists yet
    # suits = ['Diamonds', 'Hearts', 'Clubs', 'Spades']
    # return random.choice(suits)
    # need to write code that has a value that is a random index point

def getValue():
# pick a random value for a card

    number = random.randint(0,12)
    if number == 0:
        value = 'Ace'
    elif number == 1:
        value = '2'        
    elif number == 2:
        value = '3'        
    elif number == 3:
        value = '4'   
    elif number == 4:
        value = '5'
    elif number == 5:
        value = '6'        
    elif number == 6:
        value = '7'        
    elif number == 7:
        value = '8' 
    elif number == 8:
        value = '9'
    elif number == 9:
        value = '10'        
    elif number == 10:
        value = 'Jack'        
    elif number == 11:
        value = 'Queen' 
    elif number == 12:
        value = 'King'
    return value

    # commenting out the below code because we have not covered lists yet
    # value = ['Ace', '2', '3', '4','5', '6', '7', '8', '9' , '10' , 'Jack' , 'Queen', 'King']
    # return random.choice(value)

def printCard(value, suits):
# print out the value of the card (ie Ace of Spades or 10 of Clubs)
# to the user based on the value and suit that are the parameters.
    print("You pulled a(n) " + value + " of " + suits + " from the deck of cards")


def getColor(suit):
# Determining the color of the card based on whether it is Spades/Clubs or Diamonds/Hearts
   
    if suit == "Spades":
        return "Black"
    elif suit == "Clubs":
        return "Black"
    elif suit == "Diamonds":
        return "Red"
    elif suit == "Hearts":
        return "Red"                
    # commenting this out because we are not allowed to use "in" yet
    # if suit in ["Spades", "Clubs"]:
    #    return "Black"
    #else:
    #   return "Red"
def main():
    suit = getSuit()
    value = getValue()
    color = guessthecolor()
    printCard(value, suit)
    resultofgame(color, suit)

#remember to put in the lines to call main() that are described in part 6
if __name__ == "__main__":
    main()