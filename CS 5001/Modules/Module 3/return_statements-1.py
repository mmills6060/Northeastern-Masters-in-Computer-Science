''' Align Online
    CS5001
    Sample code -- practice with return statements,
    and convert Tugboat's weight from stone to pounds.
    (Tugboat says hi.)
'''

def get_pounds_weight(stone_weight):
    ''' Function get_pounds_weight
        Parameters: number, weight in stone
        Return: number, weight in pounds
    '''
    pounds = stone_weight * 14
    return pounds

def main():
    stone = 5.3
    # same variable name as in the f=unction above
    pounds = get_pounds_weight(stone)
    print("Your dog weighs", pounds, "pounds!")

main()
