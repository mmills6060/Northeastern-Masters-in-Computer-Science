# Michael Arthur Mills
# Spring 2023, CS 5001
# calculate the price of dinner with local and global variables

# Define tax rate as a global variable
tax_rate = 0.05

def costofdinner(entree_price, drink_price):
    subtotal = entree_price +  drink_price
    tax = subtotal * tax_rate
    total_cost = subtotal + tax
    return total_cost

# Define the prices of the items
entree_price = 10.50
drink_price = 2.50

# Call the function and save the result in a variable
total_cost = costofdinner(entree_price, drink_price)

# Print the total cost
print("Total cost: $" + str(total_cost))