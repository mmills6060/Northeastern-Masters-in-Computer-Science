#Project 5
#Spaceman Implementation
#Template created by: Lindsay Jamieson
# Michael Arthur Mills
# February 15, 2023

import random
def pick_random_word():
    '''Pick_random_word will create a word list, choose a random word and return it
    Input: None
    Output: A random word from the list
    '''
    word = ["Banana", "Purple", "Window", "Camera", "Pillow", "Guitar", "Coffee", "Tomato", 
            "Rocket", "Turtle", "Planet", "Dragon", "Orange", "Forest", "Castle", "Reptile", "Sailor",
            "Circus", "Watermelon", "Forest"]
    rand_word = random.choice(word)
    print("The random word is " + rand_word)
    return rand_word
def create_hidden_word(rand_word):
    '''create_hidden_word will create an obfuscated version of the random word
    Input: The random word
    Output: An obfuscated version of the word (ie banana would return ******
    '''
    hidden_word = "*" * len(rand_word)
    print(hidden_word)
    return hidden_word
def word_found(rand_word, new_hidden_word):
    '''word_found will detect whether the random word has been uncovered
    Input: the random word and the hidden version of the word
    Output: True if the hidden word has all been revealed, False otherwise
    '''
    if rand_word == new_hidden_word:
        return True
    else:
        return False


def replace_character(rand_word, hidden_word, user_guess,new_hidden_word,guessed):
    '''Replaces all the occurences of user_guess in hidden_word with user_guess
    Input: the random word, the hidden word so far, and the user guess
    Output: the new hidden word
    '''
    new_hidden_word = ''
    for i in range(len(rand_word)):
        if rand_word[i] == user_guess or rand_word[i] in guessed:
            new_hidden_word += rand_word[i]
            guessed.add(rand_word[i])
        else:
            new_hidden_word += hidden_word[i]
    return new_hidden_word

def main():
    '''Main game playing location'''
    turns_used = 10
    new_hidden_word = ""
    
    print("Welcome to The Spaceman Game, created by Michael Arthur Mills")
    rand_word = pick_random_word()
    hidden_word = (create_hidden_word(rand_word))
    guessed = set() # create emptty set for guessed
    while True:
        if turns_used >= 1:
            user_guess = (input("Enter your guess: "))
            turns_used -= 1
            new_hidden_word = replace_character(rand_word, hidden_word, user_guess,new_hidden_word,guessed)
            if word_found(rand_word, new_hidden_word):
                print("Congratulations, you won the game!")
                break
            print(user_guess)
            print("You have " + str(turns_used) + " turns left.")
            print(new_hidden_word)
        else:
            print("Sorry, better luck next time")
            break
if __name__ == "__main__":
    main() 
