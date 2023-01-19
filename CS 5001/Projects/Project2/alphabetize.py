# Michael Arthur Mills
# Fall 2023, CS 5001
# Lab 2 code file
# Ask the user for 4 words.  Then print them out in alphabetical order 
# (using < and > will compare the alphabetical order of the words).

#ask the user to input four words
firstword = input("Please provide your first word ")
secondword = input("Please provide your second word --> ")
thirdword = input("Please provide your third word --> ")
fourthword = input("Please provide your fourth word --> ")

#determine alphabetical order and print
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
                        print(thirdword,firstword,fourthword,secondword)
                else:
                    print(thirdword,fourthword,firstword,secondword)
            else:
                print(thirdword,fourthword,secondword,firstword)
    else:
        if fourthword>firstword:
            if secondword>firstword:
                if thirdword>firstword:
                    print(firstword,thirdword,fourthword,secondword)
                else:
                    print(thirdword,firstword,fourthword,secondword)
            else:
                print(thirdword,fourthword,firstword,secondword)
        else: 
            print(thirdword,secondword,fourthword,firstword)

else:
    if thirdword>fourthword:
        if secondword>fourthword:
            if thirdword>firstword:
                if secondword>firstword:
                    if fourthword>firstword:
                        print(firstword,fourthword,secondword,thirdword)
                    else:
                        print(fourthword,firstword,secondword,thirdword)

                else:
                    print(fourthword,secondword,firstword,thirdword)
            else:
                print(fourthword,secondword,thirdword,firstword)
        else:
            if thirdword>firstword:
                if fourthword>firstword:
                    if secondword>firstword:
                        print(firstword,secondword,fourthword,thirdword)
                    else:
                        print(secondword,firstword,fourthword,thirdword)
                else:
                    print(secondword,fourthword,firstword,thirdword)
            else:
                print(secondword,fourthword,thirdword,firstword)
    else:
        if fourthword>firstword:
            if thirdword>firstword:
                if secondword>firstword:
                    print(firstword,secondword,thirdword,fourthword)
                else:
                    print(secondword,firstword,thirdword,fourthword)
            else:
                print(secondword,thirdword,firstword,fourthword)
        else:
            print(secondword,thirdword,fourthword,firstword)


