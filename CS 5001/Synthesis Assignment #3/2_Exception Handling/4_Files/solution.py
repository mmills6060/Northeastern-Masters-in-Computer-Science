# Michael Arthur Mills
# April 7. 2023
# CS 5001

# example of first reading and then writing contents to file

# Open the file in read mode
with open('example.txt', 'r') as file:

    # Read the contents of the file into a string
    contents = file.read()

# Modify the contents of the file (in this case, capitalize all words)
modified_contents = ' '.join([word.capitalize() for word in contents.split()])

# Open the file again in write mode
with open('example.txt', 'w') as file:

    # Write the modified contents back to the file
    file.write(modified_contents)
