'''

Create a function, is_palindrome, to determine if a supplied word is
the same if the letters are reversed.

'''


def is_palindrome(word1):
    word2 = word1[-1::-1]
    return "It is palindrome" if word1 == word2 else "It is not palindrome"


word1 = input("Enter the word: ")
word1.lower()
print(is_palindrome(word1))
