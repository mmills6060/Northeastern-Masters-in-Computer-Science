def example():
    var = 10
    while(var >= 5):
        print("current variable value: ", var)
        var -=1
    print("Good bye!")
example()

def main():
    var =10
    while (var>=-1):
        print(var)
        var -=1
    print("my number is not negative")
main()


def computeaverage():
    # before the loop
    num_input = 1
    total = 0
    grade = int(input("Enter a grade or -1 to quit "))
    #  #loop through all the grades and add to total
    while (grade != -1):
        total += grade
        num_input += 1
        grade = int(input("Enter a grade or -1 to quit"))
        # after the loop-compute average to print
    if (num_input > 0):
        average = total/num_input
    else:
        average = 0
    print("The average grade was: " + str(average))


computeaverage()
