# Michael Arthur Mills
# April 7. 2023
# CS 5001

# an example of printing objects
class website:
    ''' Class website
    Attributes: name, topic, price
    Methods: add_on
    '''
    def __init__(self):
        '''
        Constructor -- creates new instances of website
        Parameters:
        self -- the current object
        website_name -- the initial name of this website
        topic (optional) -- the initial topic of this website
        '''
        self.name = "Ebay"
        self.topic = "Online Marketplace"
        self.price = 500
    def add_on(self, adder):
        '''
        Method -- add elements to this website
        Parameters:
        self -- the current object
        adder -- the element to add
        '''
        if adder == "About Us":
            self.price += 150
        elif adder == "Contact Us":
            self.price += 200

from website import website

def main():
    website1 = website()
    website1.add_on("About Us")
    website1.add_on("Contact Us")
    print(website1.name)
    print(website1.topic)
    print(website1.price)

