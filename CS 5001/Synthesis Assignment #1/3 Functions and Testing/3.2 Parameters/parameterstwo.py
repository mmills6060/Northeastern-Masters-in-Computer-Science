# Michael Arthur Mills
# Spring 2023, CS 5001
# an example of a parameter, that takes various words 
# and sorts them alphabetically

def sort_alphabetically(words):
    words.sort()
    return words

inputtedwords = ['Try', 'not', 'do', 'or','do','not', 'there', 'is', 'no','try']
sorted_words = sort_alphabetically(inputtedwords)
print(sorted_words) 

# Output: ['Try', 'do', 'do', 'is', 'no', 'not', 'not', 'or', 'there', 'try']