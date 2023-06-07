# Michael Arthur Mills
# Spring 2023, CS 5001
# an example of the concept of scope, using a local and global variable

def milesrun():
    miles = 6 
    print(miles)

def milesrun2():
    print(miles) 

milesrun()
milesrun2()

# Output
# 6
# NameError: name 'x' is not defined