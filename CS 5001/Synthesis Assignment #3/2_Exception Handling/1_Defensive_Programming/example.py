# Michael Arthur Mills
# April 7. 2023
# CS 5001

# An example of defensive programming

def age_input(age):
    try:
        age = int(age)
    except (ValueError, TypeError):
        raise ValueError("Invalid age value. Please enter a valid integer.")
        
    return age
