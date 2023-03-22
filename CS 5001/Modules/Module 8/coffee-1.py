''' Align Online
    CS5001
    Sample code -- defining a class, in this case, Coffee
'''


class Coffee:
    ''' Class coffee
        Attributes: name, size, price
        Methods: add_on
    '''

    def __init__(self, coffee_name, size="L"):
        '''
        Constructor -- creates new instances of coffee
        Parameters:
           self -- the current object
           coffee_name -- the initial name of this coffee
           size (optional) -- the initial size of this coffee
        '''
        self.name = coffee_name
        self.size = size
        self.price = 4.95

    def add_on(self, adder):
        '''
        Method -- add elements to this coffee
        Parameters:
           self -- the current object
           adder -- the element to add
        '''
        if adder == "espresso":
            self.price += 1.50
        elif adder == "flavor":
            self.price += .49

    def __str__(self):
        '''
        Method -- returns a string that represents this coffee
        Parameters:
           self -- the current object
        '''
        output = "Drink: " + self.name + "\n" \
                 "Size: " + self.size + "\n" \
                 "Price: $" + str(self.price)
        return output


