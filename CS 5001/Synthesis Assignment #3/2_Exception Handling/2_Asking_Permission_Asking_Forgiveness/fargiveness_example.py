# Michael Arthur Mills
# April 7. 2023
# CS 5001

# An example of asking forgiveness



def exception (age):
    while True:
        try:
            age = int(input("Please enter your age: "))
            if age < 0 or age > 120:
                raise ValueError("Invalid age entered")
            break
        except ValueError as e:
            print("I'm sorry, an error occurred:", e)
            print("Please enter a valid age between 0 and 120.")

