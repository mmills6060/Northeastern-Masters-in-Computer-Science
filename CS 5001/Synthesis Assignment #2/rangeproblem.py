# a problem that involves range over a list

def total_points(points):
    total = 0
    for i in range(len(points)):
        total += points[i]
    return total

points = [6, 3, 4, 2, 5, 4, 6, 7, 8, 4, 5]
print("Total points for the tennis academy are: " + str(total_points(points)))
















    

