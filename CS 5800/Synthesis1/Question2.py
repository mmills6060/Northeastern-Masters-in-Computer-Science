
import random

def guess_hidden_word(dictionary):
    hidden_word = dictionary[random.randint(0, len(dictionary) - 1)]
    number_of_guesses = 0
    guess = random.choice(dictionary)
    while guess != hidden_word:
        number_of_guesses += 1
        if compare_words(guess, hidden_word):
            guess = dictionary[dictionary.index(guess) + 1]
        else:
            guess = dictionary[dictionary.index(guess) - 1]

    return hidden_word, guess, number_of_guesses

def compare_words(word1, word2):
    for i in range(len(word1)):
        if word1[i] < word2[i]:
            return True
        elif word1[i] > word2[i]:
            return False
    return False

def main():

    dictionary = ["august", "book", "car", "duck", "eagle"]
    hidden_word, guessed_word, number_of_guesses = guess_hidden_word(dictionary)
    print("Number of Guesses: " + str(number_of_guesses))
    print("Guessed Word: " + str(guessed_word))
    print("Hidden Word: " + str(hidden_word))

if __name__ == '__main__':
    main()

