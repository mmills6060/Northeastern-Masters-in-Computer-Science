''' Align Online
    CS5001
    Sample code -- import car.py, which has the class definition
    for Car, and create car objects.

    Never heard of these cars? Please enjoy:
    The Homer: https://images.app.goo.gl/KkyEmaeGAPgY7pRD8
    Lightning McQueen: https://images.app.goo.gl/1vednkG9EzecApH56
'''
from car import Car


def main():
    my_car = Car("Powell Motors", "Homer")
    print("Make:", my_car.make)
    print("Model:", my_car.model)
    print("Year:", my_car.year)
    print("Price:", my_car.price)
    print("\n\n")

    your_car = Car("Lightning", "McQueen")
    print("Make:", your_car.make)
    print("Model:", your_car.model)
    print("Year:", your_car.year)
    print("Price:", your_car.price)

    your_car.add_feature("heated seats")
    print("...after upgrade, your car is now...")
    print("Price:", your_car.price)


main()
