# Michael Arthur Mills
# April 7. 2023
# CS 5001

# Example of our debugged code 

def count_down(n):
    if n == 0:
        print("Blastoff!")
    else:
        print(n)
        print("Calling count_down(", n-1, ")")
        count_down(n-1)

def main():
    count_down(3)

if __name__ == "__main__":
    main()