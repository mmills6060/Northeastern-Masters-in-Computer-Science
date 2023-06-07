# Michael Arthur Mills
# Spring 2023, CS 5001
# an example of the concept of scope, using a local and global variable

x = 10

def yearsofexperience():
    x = 5 # this x is local variable
    print("Years of experience: ", x)

print("Years of experience: ", x)
yearsofexperience()
print("Years of experience: ", x)

# Output
# Years of experience:  10
# Years of experience:  5
# Years of experience:  10