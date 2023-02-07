# Michael Arthur Mills
# Spring 2023, CS 5001
# Lab 4 code file

# what if the same number is inputted by the user? It is neither hotter nor colder
# colder is chosen even when there is just one number inputted by user
import random
new_distance = 0
distance = 0
# def distance_from_real_number(new_distance, old_distance):
# return(new_distance - old_distance)


def guessmynumber():
    old_distance = 0
    number = random.randint(0, 10)
    print(number)
    usernumber = input("Please guess a number --> ")
    if int(usernumber) == number:
        print("success")
    else:
        usernumber = input(
            "You guessed incorrectly, please guess another number --> ")
    if int(usernumber) == number:
        print("success")
    else:
        old_distance = int(usernumber)
        while int(usernumber) != number:
            new_distance = abs(int(usernumber) - int(number))
            if old_distance == new_distance:
                print("You chose the same incorrect number, for some reason ")
            if old_distance > new_distance:
                print("Getting warmer")
            else:
                if new_distance > old_distance:
                    print("Getting colder")
            usernumber = input("Choose another number --> ")
            old_distance = new_distance
        else:
            print("success")


def main():
   guessmynumber()
   # distance_from_real_number(new_distance, old_distance)


# remember to put in the lines to call main() that are described in part 6
if __name__ == "__main__":
    main()
