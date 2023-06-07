# example of vlaidating user input

def validatecolor():
    color = input("Enter Blue or Red: ")
    while color != "Blue" and color != "Red":
        color = input("Enter a valid color: ")
    print ("Your color is", color)

validatecolor()