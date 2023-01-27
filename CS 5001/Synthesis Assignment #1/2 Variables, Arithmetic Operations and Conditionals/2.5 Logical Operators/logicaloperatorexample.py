# Michael Arthur Mills
# Fall 2023, CS 5001


# An example of a logical operator

x = 5
y = 10

if x > 0 and y > 0:
    print("Both x and y are positive numbers")
else:
    print("Either x or y, or both, are not positive numbers")

# Another example of a logical operator

x = 5
if x > 0 or x < -10:
    print("x is either positive or less than -10")
else:
    print("x is between -10 and 0")

x = -5
if not (x > 0):
    print("x is not positive")
else:
    print("x is positive")