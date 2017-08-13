#####################
# Introducing Eliza #
#####################

# Ask their user for the name
userName = input("What is your name?\nName: ")
# Say hello and introduce ourselves
print("Hello there " + userName + ", nice to meet you!\nMy name is Eliza.")

# Ask their user how what their mood is
userMood = input("How are you feeling at he moment " + userName + "?\nMood: ")
# Condensate
print("I feel " + userMood + " sometimes too.")

# Ask the user why they feel that way
moodReason = input("Why do you feel " + userMood + ", " + userName + "?\nReason: ")
# Check to see if the user's input ends a question mark
if moodReason.endswith("?"):
    # Only we ask the questions!
    print("Hey! I ask the questions.")
else:
    # Make the user feel somewhat more comfortable
    print("I know how you feel " + userName + ".")

# Print our footer
print("*" * 40)
