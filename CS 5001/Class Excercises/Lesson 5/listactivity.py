# Michael Arthur Mills
# Fall 2023, CS 5001
# Class code Problem


#make a for loop that prints out the first 100 even numbers
def for_counter():
    for counter in range (200):
        if (counter%2 == 0):
            print(counter)
            

# make a function that asks the user for a number and then prints out the sum of the numbers from 1 to that number using a loop

def for_loop():
    num = int(input("Enter an integer"))
    total = 0
    for count in range(num, 0, -1):
            total += count
    print ("The sum of the numbers from 1 to" + str(num) + " is " + str(total))
            
# make a function that has an integer parameter and calculates teh factorial of that number (ie 5! is 1*2*3*4*5)
def factorial(num):
    result = 1
    for count in range(1, num+1):
        result *= count
    return result


def star():
    for i in range (1,11):
        for j in range(i):
            print("*", end='')
        print()
    
            
def main():
    #for_counter()
    #for_loop()
    star()
    
    
# write a loop that prints the same triangle, 
# but upside down (10 * across the top down to 1 at the bottom


#write a loop that prints a right triangle of *, right justified, with the largest one being 10 * across from 1 * at the otp

#write a loop 

if __name__== "__main__":
        main()