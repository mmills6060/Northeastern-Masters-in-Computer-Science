# example of vlaidating user input

def validateage():
    age = int(input("Enter your age: "))
    while age < 0 or age > 100:
        age = int(input("Enter a valid age: "))
    print ("Your age is", age)

validateage()