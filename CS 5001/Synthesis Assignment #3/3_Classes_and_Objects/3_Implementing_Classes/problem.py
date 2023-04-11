# Michael Arthur Mills
# April 7. 2023
# CS 5001

class computer:
    ''' Class computer
    Attributes: name, size, price
    Methods: add_on
    '''
    def __init__(self):
        '''
        Constructor -- creates new instances of computer
        Parameters:
        self -- the current object
        computer_name -- the initial name of this computer
        size (optional) -- the initial size of this computer
        '''
        self.name = "Alienware"
        self.size = "16"
        self.price = 2500
    def add_on(self, adder):
        '''
        Method -- add elements to this computer
        Parameters:
        self -- the current object
        adder -- the element to add
        '''
        if adder == "Mouse":
            self.price += 150
        elif adder == "Keyboard":
            self.price += 200


