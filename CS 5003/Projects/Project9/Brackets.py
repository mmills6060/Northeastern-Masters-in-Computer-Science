# File which will hold a stack data strcture
# Created by Lindsay Jamieson
# 4/4/2023
# Implemented by Michael Mills

def check_brackets(s):
    stack = []
    open_brackets = set(['(', '{', '[', '<'])
    close_brackets = set([')', '}', ']', '>'])
    bracket_map = {'(': ')', '{': '}', '[': ']', '<': '>'}

    for char in s:
        if char in open_brackets:
            stack.append(char)
        elif char in close_brackets:
            if len(stack) == 0:
                return False
            else:
                last_open_bracket = stack.pop()
                if bracket_map[last_open_bracket] != char:
                    return False

    return len(stack) == 0

def main():
    s = input("Enter a string: ")
    if check_brackets(s):
        print("The string contains a valid set of brackets.")
    else:
        print("The string does not contain a valid set of brackets.")

if __name__ == "__main__":
    main()