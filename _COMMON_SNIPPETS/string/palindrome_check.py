# determines if a string is a palindrome

# Option 1:
string = 'level'
palindrome = string == string[::-1]

print(palindrome)   # True

# Option 2:
phrase.find(phrase[::-1])

# Option 3:
def palindrome_check(str):
    a = str.lower()     # normalize string
    return a == a[::-1]


print(palindrome_check("hannah"))   # True
print(palindrome_check('Hannah'))   # True 
print(palindrome_check("madaa"))    # False

# Option 4:
def checkPalindrome(inputString):
    check_string = inputString.lower()
    return True if check_string == check_string[::-1] else False
