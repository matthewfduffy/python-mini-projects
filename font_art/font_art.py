"""
Prints user input in the terminal in an artistic font.
Relies on pyfiglet package

# $ pip install pyfiglet
"""
# import os
from pyfiglet import Figlet



text = Figlet(font='slant')

art_word = input("Enter any word or phrase: \n")

print(text.renderText(art_word))
