"""
CS 5001: Intensive Foundations of Computer Science
Module: Boolean Expressions & Conditionals
Lesson 3-2: Conditional Expressions
This program calculates the number of slices each person can eat
when n pizzas are ordered.
This is the program we started with in Lesson 3-2.
"""
def main():
    # get two integers from the user
    pizzas = int(input("How many pizzas did you order? "))
    people = int(input("How many people are there? "))
    # multiply by 8 slices per pie and divide
    slices = pizzas * 8 / people
    print(pizzas, "pizzas split between", people, "can have", slices, "slices")
main()