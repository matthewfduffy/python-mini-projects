""" Takes two strings as input and returns a count of non-unique characters """
def commonCharacterCount(string1, string2):
	temp = list(string2)
	count = 0

	for char in string1:
		if char in temp:
			temp.remove(char)
			count += 1

	return count


print(commonCharacterCount("ABCDCDC", "CDC"))
# Original
# def commonCharacterCount(string1, string2):
# 	count = 0
# 	word2 = list(string2)
# 	for letter in string1:
# 		if letter in word2:
# 			word2.remove(letter)
# 			count += 1
# 	print(count)