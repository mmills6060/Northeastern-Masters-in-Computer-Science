# Give the code to print out all the locations in a game board which is stored as a list of lists.
grid = [
    ['A1', "A2", "A3"],
    ['B1', "B2", "B3"],
    ['C1', "C2", "C3"]
]

for row in grid:
    for col in row:
        print(col)
