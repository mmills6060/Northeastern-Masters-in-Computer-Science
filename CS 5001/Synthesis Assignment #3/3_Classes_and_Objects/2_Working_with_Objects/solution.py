# Michael Arthur Mills
# April 7. 2023
# CS 5001

# An example of how to work with objects
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hi(self):
        print("Hello, my name is", self.name)
    
    # add a characteristic about this person
    def is_old(self):
        if self.age > 100:
            print(self.name, "is old")
        else:
            print(self.name, "is not old")
    # add a characteristic about this person
    def is_young(self):
        if self.age < 20:
            print(self.name, "is young")
        else:
            print(self.name, "is not young")
