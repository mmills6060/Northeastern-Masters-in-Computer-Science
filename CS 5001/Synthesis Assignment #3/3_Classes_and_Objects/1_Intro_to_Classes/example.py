# Michael Arthur Mills
# April 7. 2023
# CS 5001

# An example of a class with objects
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hi(self):
        print("Hello, my name is", self.name)