# Michael Arthur Mills
# Spring 2023, CS 5001
# an example of a return statement without an expression

def function():
    if condition:
        return

def condition():
    pass
result = function()
print(result) 

# Output
# None