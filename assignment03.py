'''
Write code that will print out the anagrams (words that use the same
letters) from a paragraph of text.

'''
from itertools import combinations


def anagrams(sentence):
    # spliting the sentence into words
    wordList = sentence.split(' ')
    # list of all the possible combination of 2 words
    comb = list(combinations(wordList, 2))
    s = 0
    for i in comb:
        str1 = list(i[0])
        str1.sort()
        str2 = list(i[1])
        str2.sort()
        if str1 == str2:
            s = s + 1
    return s


sen = 'This is cat and dan si tac'
sentence = sen.upper()

angms = anagrams(sentence)
print(f'There are {angms} anagrams')
