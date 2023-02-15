''' Align Online
    CS5001
    Sample code -- using loops to create a simple website-ish
'''


def choose_menu():
    ''' Function: choose_menu
        Parameters: none
        Returns: nothing
    '''
    print("L -- Login\n"
          "R -- Register\n"
          "Q -- Quit\n")
    choice = input("Enter your choice now\n")
    return choice


def main():
    while True:
        option = choose_menu()
        if option == "Q":
            break

    print("Thanks for using our website!\n")


main()
