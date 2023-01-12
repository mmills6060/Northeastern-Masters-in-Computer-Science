# Michael Arthur Mills
# Fall 2023, CS 5001
# Lab 2 code file
# Practicing good code style and more complex functions

#ask the user to input four words
firstword = input("Please provide your first word ")
secondword = input("Please provide your second word --> ")
thirdword = input("Please provide your third word --> ")
fourthword = input("Please provide your fourth word --> ")

#Return a sorted list alphabetically
Allwords = (firstword, secondword, thirdword, fourthword)
Sortedwords = sorted(Allwords)

#print the results from what was determined
print(Sortedwords)
