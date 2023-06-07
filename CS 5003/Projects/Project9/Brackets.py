# File which will hold a stack data strcture
# Created by Lindsay Jamieson
# 4/4/2023
# Implemented by Michael Mills

from Stack import Stack

def check_brackets(s):

    bracket_stack = Stack(len(s))
    for bracket in s:
        if bracket in "([{<":
            bracket_stack.push(bracket)
        elif bracket in ")]}>":
            popped_bracket = bracket_stack.pop()
            if not popped_bracket:
                return False
            elif (bracket == ")" and popped_bracket == "(") or \
                (bracket == "]" and popped_bracket == "[") or \
                (bracket == "}" and popped_bracket == "{") or \
                (bracket == ">" and popped_bracket == "<"):
                continue
            else:
                return False
    return bracket_stack.end == 0

def main():
    s = input("Enter a string: ")
    if check_brackets(s):
        print("The string contains a valid set of brackets.")
    else:     
        print("The string does not contain a valid set of brackets.")

if __name__ == "__main__":
    main()