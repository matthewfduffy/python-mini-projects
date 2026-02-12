# Anagram checker
# An anagram is a word or phrase formed by rearranging the letters of another.
# e.g. 'cinema' can be formed by using the letters in 'iceman'

from collections import Counter

# Option 1 - No Function:
word1 = "below"
word2 = "elbow"

print('anagram') if Counter(word1) == Counter(word2) else print('not an anagram')

# Option 2 - Function
def anagram_checker(str1, str2):
    return True if Counter(str1) == Counter(str2) else False


print(anagram_checker('window', 'glass'))