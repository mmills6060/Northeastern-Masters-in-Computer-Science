# File which will hold the main function for the IceCreamShoppe project
# Created by Lindsay Jamieson
# 3/29/2022
# Implemented by Michael Mills

import IceCreamShoppe
import Scoop

def main():
    radius1 = float(input("Enter the radius of the first scoop: "))
    radius2 = float(input("Enter the radius of the second scoop: "))
    scoop1 = Scoop.Scoop(radius1)
    scoop2 = Scoop.Scoop(radius2)

    carton_radius = float(input("Enter the radius of the ice cream carton: "))
    carton_height = float(input("Enter the height of the ice cream carton: "))
    shoppe = IceCreamShoppe.IceCreamShoppe(carton_radius, carton_height)

    serving = True
    while serving:
        num_scoops = int(input("How many scoops? "))
        if num_scoops == 1:
            scooper = scoop1
        elif num_scoops == 2:
            scooper = scoop2
        else:
            print("Invalid number of scoops. Please enter 1 or 2.")
            continue
        shoppe.serve(num_scoops, scooper)
        more = input("Do you want more ice cream? (y/n) ")
        if more.lower() == "n":
            serving = False

    print("You used", shoppe.cartonsUsed(), "cartons of ice cream.")

if __name__ == "__main__":
    main()