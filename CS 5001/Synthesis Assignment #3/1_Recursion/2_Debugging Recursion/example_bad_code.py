# Michael Arthur Mills
# April 7. 2023
# CS 5001

# an example of a problem with our recursive algorithm

def count_down(n):
    if n == 1:
        print("Blastoff!")
    else:
        
        count_down(n-1)

def main():
    count_down(3)

if __name__ == "__main__":
    main()