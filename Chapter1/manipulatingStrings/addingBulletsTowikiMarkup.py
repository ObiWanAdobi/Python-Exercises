#Page 157

#Automate adding bullet points to a large list
#Description: The bulletPointAdder.py script will get the text from the clipboard, add a star and space to the beginning of each line, and then paste this new text to the clipboar

#Example: 
    #Input: 
    # Lists of aquarium life
    # Lists of biologists by author abbreviation
    # Lists of cultivars

    #Output: 
    # * Lists of aquarium life
    # * Lists of biologists by author abbreviation
    # * Lists of cultivars

#Step1: Copy and Paste from the Clipboard
import pyperclip
text = pyperclip.paste()

#Step2: Separate lines and add stars
lines = text.split('\n')

for i in range(len(lines)):
    lines[i]  = '* ' + lines[i]

text= '\n'.join(lines)

pyperclip.copy(text)
