''' Align Online
    CS5001
    Sample code -- creating objects out of a defined class.

    This file imports coffee.py, where the class should be defined.
'''
from coffee import Coffee


def main():
    my_cup = Coffee("black coffee")
    print(my_cup)
    print("...")

    your_cup = Coffee("unicorn frappe", size="S")
    print(your_cup)


main()
