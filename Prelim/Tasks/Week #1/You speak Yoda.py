##################
# You speak Yoda #
##################

# Imports
import re

# Declare our default variables
words = []
count = 0

# Compile our basic regex pattern (we do this outside the loop so it is only compiled once)
pattern = re.compile(r"\A[a-z]+\Z")

# Ask our user to input words until there we have four *valid* words
while count < 4:
    # Ask the user to input a word and assign it to a variable
    userInput = input("Please input a word.\nWord: ").lower()
    # Check to make sure the word is some actual text (very basic regex check)
    if pattern.match(userInput):
        # Increase our count
        count += 1
        # Append our word to our list (array) of words
        words.append(userInput)
    else:
        # Tell the user that they must enter a valid word
        print("You must input a valid word!\n")

# Print our Yoda-fied message!
print("Yoda: " + words[2] + " " + words[3] + " " + words[0] + " " + words[1])
