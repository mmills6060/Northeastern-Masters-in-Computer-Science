''' Align Online
    CS5001
    Sample code -- define a Car class
'''


class Car:
    ''' class: Car
        Attributes: make, model, year price
        Methods: add a feature (changes the price)
    '''

    def __init__(self, make, mod, year=2019, price=25000.0):
        '''
        Constructor -- creates an new instance of a car
        Parameters:
           self -- the current object
           make -- the initial make of this car
           model -- the initial model of this car
           year (optional) -- the initial year of this car
           price (optional) -- the initial price of this car
        '''
        self.make = make
        self.model = mod
        self.year = year
        self.price = price

    def add_feature(self, item):
        '''
        Method -- add a feature to this car
        Parameters:
           self -- the current object
           item -- the feature to add to this car
        Returns nothing
        '''
        if item == "heated seats":
            self.price += 200
        elif item == "power steering":
            self.price += 350
