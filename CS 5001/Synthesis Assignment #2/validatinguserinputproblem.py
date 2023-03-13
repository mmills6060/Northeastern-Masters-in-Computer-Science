# -practice problem vlaidating user input

def validatecar():
    car = input("Enter Ferrari or Lamborghini: ")
    while car != "Ferrari" and car != "Lamborghini":
        car = input("Enter a valid car: ")
    print ("Your car is", car)

validatecar()