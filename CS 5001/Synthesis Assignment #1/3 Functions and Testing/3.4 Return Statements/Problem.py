# Michael Arthur Mills
# Spring 2023, CS 5001
# develop a function that calculates the total score.

def calculate_jazz_rating(tonescore, temposcore, rhythmscore):
    audition_rating = tonescore + temposcore + rhythmscore
    return 'This jazz auditioner has a rating of ' + str(audition_rating) + '/30.'

print(calculate_jazz_rating(7, 10, 8))