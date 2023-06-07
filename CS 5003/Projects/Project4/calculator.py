# Gregory Valcourt
# September 27, 2022; revised 1/31/2023
# CS5001 Recitation FA22; revised SP23
# A program to demonstrate while loops
# also, a calculator


#evaluates user input and creates the calculation
def operatorCheck(val1, operator, val2):
    if type(val1) != int or type(val1) != int:
        return(str("I don't understand"))

    if operator == "+":
        return(str("you asked for " + str(val1+val2)))
    elif operator == "*":
        return(str("you asked for " + str(val1*val2)))
    elif operator == "/":
        return(str("you asked for " + str(val1/val2)))
    elif operator == "-":
        return(str("you asked for " + str(val1-val2)))
    elif operator == "//":
        return(str("you asked for " + str(val1//val2)))
    elif operator == "%":
        return(str("you asked for " + str(val1%val2)))
    else:
        return(str("I don't understand"))


def main():

    #I am using a flag here to set an exit point. I am using False so that our code ends if
    #exitflag==True, which is how I would understand it. We also need to set the condition
    #before the while checks for it.
    exitflag = False
    while exitflag == False:
        raw = input("type a math problem into the console with each number"+
        " and action separated by a space.\nOnly one operator at a time.\n-->\t")
        if raw.lower() == "exit":
            #this is our break condition
            print("ending calculations")
            exitflag = True
            continue #continue says to the program "go back to the start of the loop"
        
        #consider calculation like sys.argv, only that we have collected it from input
        calculation = raw.split()

        if len(calculation) < 2 or len(calculation) > 3 or calculation[0].isnumeric()==False or calculation[2].isnumeric()==False:
            #simple error checking
            print("I don't understand")
            continue

        #Non-essential calculator stuff from here to the end of the loop
        val1 = int(calculation[0])
        val2 = int(calculation[2])
        operator = calculation[1]
        print(operatorCheck(val1, operator, val2))


if __name__ == "__main__":
    main()