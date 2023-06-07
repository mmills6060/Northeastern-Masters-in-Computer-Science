# Michael Arthur Mills
# April 7. 2023
# CS 5001

class Car:
    ''' Class car
    Attributes: name, size, price
    Methods: add_on
    '''
    def __init__(self):
        '''
        Constructor -- creates new instances of car
        Parameters:
        self -- the current object
        car_name -- the initial name of this car
        size (optional) -- the initial size of this car
        '''
        self.name = "BMW"
        self.size = "L"
        self.price = 45000
    def add_on(self, adder):
        '''
        Method -- add elements to this car
        Parameters:
        self -- the current object
        adder -- the element to add
        '''
        if adder == "convertible":
            self.price += 10000
        elif adder == "Leather seats":
            self.price += 5000


