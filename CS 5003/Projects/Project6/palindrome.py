# Gregory Valcourt
# September 19, 2022; Revised Feb 6, 2023
# CS5001 Recitation FA22, Revised SP23
# A simple program to illustrate what we want in project 5
# plus, a fun way to check if a user-provided string is a palindrome


def stringacquis():
    '''A function to acquire a string from the user\n
    Makes every letter lowercase and removes whitespace
       Input: none
       Output: the value collected from the user as a string'''

    value = input("What string would you like to check?  ")
    
    value = str(value)

    #removes all punctuation/spaces
    i = 0
    baditemslist = [",", " ", ":", "!", "?", ".", "\n"]
    while i < len(baditemslist):
        value = value.replace(baditemslist[i], "")
        i+=1
    
    value = value.lower()

    return value

def checkforpalindrome(value):
    '''A function to check a string for palindrome-ness
       Input: value (should be a string with no punctuation or whitespace)
       Output: boolean signifying a palindrome or not'''

    i = 0
    j = -1
    half = len(value)//2
    palindrome = True
    while i < half:
        lside = value[i]
        rside = value[j]
        print(lside, rside)
        if lside != rside:
            palindrome = False
            break
        if i == j:
            break
        else:
            i += 1
            j -= 1
    return palindrome

def palindromehandler(veracity):
    '''A function to handle the veracity of palindrome-ness.
    Prints out a phrase whether the word was a palindrome or not.
       Input: veracity (boolean)
       Output: none'''

    if veracity == True:
        print("Yes, this is a palindrome!")
    else:
        print("No, this string is not a palindrome.")

    return None

def main():
    testval = stringacquis()
    veracity = checkforpalindrome(testval)
    palindromehandler(veracity)

if __name__ == "__main__":
    main()