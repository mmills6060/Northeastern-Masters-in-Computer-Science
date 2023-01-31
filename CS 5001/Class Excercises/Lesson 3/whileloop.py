# CS5001

def computeAverage():
        num_inputs = 0
        total = 0
        grade = int(input("Enter a grade or -1 to quit "))

        average = total/num_inputs
        print("The average grade was: " + str(average))

        while(grade != -1):
            total += grade
            nun_inputs += 1
            grade = int(input(("Enter a grade or -1 to quit ")))

        # after the loop, compute average and print
        if(num_inputs>0):
            average = total/num_inputs
        else:
            average = 0
        print("The average grade was: " + str(average))

computeAverage()
