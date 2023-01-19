# Michael Arthur Mills
# Fall 2023, CS 5001
# Lab 2 code file
# Practicing good code style and more complex functions

#ask the user to input four words
firstword = input("Please provide your first word ")
secondword = input("Please provide your second word --> ")
thirdword = input("Please provide your third word --> ")
fourthword = input("Please provide your fourth word --> ")

#determine alphabetical order
if secondword>thirdword:
    if secondword>fourthword:           
        if thirdword>fourthword:
            if secondword>firstword:
                if thirdword>firstword:
                    print(firstword,fourthword,thirdword,secondword)
                else:
                    print(fourthword,firstword,thirdword,secondword)
            else:
                print(thirdword,fourthword,secondword,firstword)
        else:
            if secondword>firstword:
                if fourthword>firstword:
                    if thirdword>firstword:
                        print(firstword,thirdword,fourthword,secondword)
    else:
        if fourthword>firstword:
            if secondword>firstword:
                if thirdword>firstword:
                    print(firstword,thirdword,fourthword,secondword)
        else: 
            if secondword>firstword:
                if fourthword>firstword:
                    if thirdword>firstword:
                        print(firstword,thirdword,fourthword,secondword)
            else:
else:
    if thirdword>fourthword:
        if secondword>fourthword:
            if thirdword>firstword:
                if secondword>firstword:
                    print(firstword,secondword,fourthword,thirdword)
    else:
        if fourthword>firstword:
            print(secondword,thirdword,fourthword,firstword)
#print the results from what was determined
print()
