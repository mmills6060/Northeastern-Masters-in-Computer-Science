# Michael Arthur Mills
# Spring 2023, CS 5001
# an example of a return statement.

import random

def simulate_tennis_match(player1, player2):
    winner = determine_winner(player1, player2)
    return winner

def determine_winner(player1, player2):
    return random.choice([player1, player2])

print(simulate_tennis_match("Roger Federer", "Rafael Nadal")) 

# outputs either "Roger Federer" or "Rafael Nadal" randomly