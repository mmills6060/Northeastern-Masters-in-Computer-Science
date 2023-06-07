# example of debugging a loop   

def main():
    i = 5
    while i >= 0:
        print(i)
        i -= 1
    print("Done")

main()

def fixed():
    i = 5
    while i >= 1:
        print(i)
        i -= 1
    print("Done")
fixed()