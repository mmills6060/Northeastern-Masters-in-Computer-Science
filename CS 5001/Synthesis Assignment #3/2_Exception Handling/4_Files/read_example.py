# Michael Arthur Mills
# April 7. 2023
# CS 5001

# An example of reading a txt file

# Open the file in read-only mode
with open('example.txt', 'r') as file:

    # Read the contents of the file into a string
    contents = file.read()

# Print the contents of the file
print(contents)
