def solution(letters):
    # Take the string and convert it into a list of letters, separated by the comma
    letters = letters.split(", ")

    # Count the occurrences of each letter in the list
    letter_counts = {}
    for letter in letters:
        if letter in letter_counts:
            letter_counts[letter] += 1
        else:
            letter_counts[letter] = 1

    # Find the minimum count among all letters
    min_count = min(letter_counts.values())

    # Create a sorted list of letters
    unique_letters = sorted(set(letters))

    # Create a string with the letters separated by commas
    unique_letters_str = ", ".join(unique_letters)

    # The maximum number of equal parts is the minimum count
    return min_count, unique_letters_str

def main():
    letters = "a, b, c, a, b, c, a, b, c"
    answer, unique_letters = solution(letters)
    print(f"split into {answer} equal parts of {unique_letters}")

    letters = "a, b, a, b, a, b, a, b, a, b"
    answer, unique_letters = solution(letters)
    print(f"split into {answer} equal parts of {unique_letters}")

    letters = "a, b, c, d, e, f, g, h"
    answer, unique_letters = solution(letters)
    print(f"split into {answer} equal parts of {unique_letters}")

if __name__ == "__main__":
    main()
