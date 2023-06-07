# Michael Arthur Mills
# April 7. 2023
# CS 5001

# example of iterating over a dictionary
# create a dictionary of tennis players and their rankings
rankings = {
    "Roger Federer": 1,
    "Rafael Nadal": 2,
    "Novak Djokovic": 3,
    "Dominic Thiem": 4
}

# iterate over the dictionary
for player in rankings:
    print(player, "is ranked", rankings[player])
    
