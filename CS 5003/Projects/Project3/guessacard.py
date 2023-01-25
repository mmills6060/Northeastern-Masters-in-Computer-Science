# Michael Arthur Mills
# Fall 2023, CS 5001
# Lab 2 code file

import random
def getSuit():
    # pick a random suit for a card. 
    suits = ['Diamonds', 'Hearts', 'Clubs', 'Spades']
    random_suit = random.choice(suits)
    return random_suit

def getValue():
    # pick a random value for a card
    value = ['Ace', '2', '3', '4','5', '6', '7', '8', '9' , '10' , 'Jack' , 'Queen', 'King']
    random_value = random.choice(value)
    return random_value
def printCard():
    # print out the value of the card (ie Ace of Spades or 10 of Clubs)
    # to the user based on the value and suit that are the parameters.
    print (getValue() + " of " + getSuit())
    pass
def color():
    if getSuit() == "Diamonds":
        color = "red"
    else:     
        if getSuit() == "Hearts":
            color = "red"
        else:
            if getSuit() == "Clubs":
                color = "black"
            else:
                if getSuit() == "Spades":
                    color = "black"
    print(color)

    
def main():
    getSuit()
    getValue()
    printCard()
    color()
#remember to put in the lines to call main() that are described in part 6
if __name__ == "__main__":
    main()