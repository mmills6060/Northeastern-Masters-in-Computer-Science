# Michael Arthur Mills
# Fall 2023, CS 5001
# Lab 2 code file

import random
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
    print(value + " of " + suits)
    print(getColor(suits))
    pass
def getColor(suit):
    if suit in ["Spades", "Clubs"]:
        return "Black"
    else:
        return "Red"
def main():
    suit = getSuit()
    value = getValue()
    printCard(value, suit)
#remember to put in the lines to call main() that are described in part 6
if __name__ == "__main__":
    main()