# Michael Arthur Mills
# Fall 2023, CS 5001


# A problem that involves a logical operator

student_id = input("Enter your student ID: ")

# Assume that the third floor is only accessible to 
# students with ID numbers that end in an even number
if int(student_id[-1]) % 2 == 0:
    print("Access granted to the third floor.")
else:
    print("Access denied to the third floor.")