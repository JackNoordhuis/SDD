##################
# Cut along here #
##################

# Ask the user how many dashes per sequence there should be and generate the dashes
dashes = "-" * eval(input("How many dashes should be in each sequence?\nDashes: "))
# Ask the user how many spaces there should be in between each sequence and generate the spaces
spaces = " " * eval(input("How many spaces should be in between each sequence?\nSpaces: "))
# Ask the user how many sequences there should be and generate the result
sequence = (dashes + spaces) * eval(input("How many sequences should there be?\nSequences: "))

# Print the result!
print("Result:\n" + sequence + "8<")
