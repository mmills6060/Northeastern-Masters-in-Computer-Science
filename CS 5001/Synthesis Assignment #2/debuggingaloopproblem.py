# example of debugging a loop   

def main():
    i = 1
    while i <= 11:
        print(i)
        i += 1
    print("I just counted to 10!")

main()

def fixed():
    i = 1
    while i <= 10:
        print(i)
        i += 1
    print("I just counted to 10!")
fixed()