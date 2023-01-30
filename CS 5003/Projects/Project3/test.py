# Michael Arthur Mills
# Fall 2023, CS 5001
# Testing CS 5003 Project 3




import subprocess

test_number = 0

while test_number < 100:
    subprocess.run(["python3", "CS 5003\Projects\Project3\guessacard.py", "Red",])
    subprocess.run(["python3", "CS 5003\Projects\Project3\guessacard.py", "Black",])
    print(test_number)
    test_number += 1