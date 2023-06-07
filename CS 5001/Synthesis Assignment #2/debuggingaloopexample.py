# example of debugging a loop   

def main():
    i = 0
    while i < 3:
        print(i)

main()

def fixed():
    i = 0
    while i < 3:
        print(i)
        i = i + 1
fixed()