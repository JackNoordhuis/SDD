###############
# Cheerleader #
###############

userInput = list(input("Cheer: ").lower())

for letter in userInput:
    print("Give me a " + letter + ", " + letter + "!")

word = "".join(userInput)
print("What does it spell?\n" + word.upper())
