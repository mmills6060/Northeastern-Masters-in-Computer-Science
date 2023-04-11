# Michael Arthur Mills
# April 7. 2023
# CS 5001

# example of iterating over a dictionary involving skiers and their lenght of ski
# create a dictionary of skiers and their lenght of ski
ski_lengths = {
    "Michael Mills": 193,
    "John Smith": 170,
    "Bob Jones": 160,
    "David Johnson": 150
}

# iterate over the dictionary
for skier in ski_lengths:
    print(skier, "has a ski length of", ski_lengths[skier])


