# immutable object problem


def change(x):
    x = "after"
    print(x)
def main():
    x = "before"
    print(x)
    change(x)
    print(x)
main()

    

