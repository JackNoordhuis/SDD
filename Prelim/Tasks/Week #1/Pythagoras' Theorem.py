#######################
# Pythagoras' Theorem #
#######################


# Function and other help from http://stackoverflow.com/a/8546631
# Check if three integers are equivalent to a right angle using Pythagoras' Theorem
def is_right_angled(a, b, c):
    a, b, c = sorted([a, b, c])
    return abs(a * a + b * b - c * c) < 0.1

# Define our default variables
lengths = []
inputs = ["a", "b", "c"]

# Ask the user for an input until we have the required amount
while len(lengths) < len(inputs):
    lengths.append(eval(input(inputs[len(lengths)] + ": ")))

# Check to see if our triangle is right angled and print a message accordingly
if is_right_angled(lengths[0], lengths[1], lengths[2]):
    print("Right angle!")
else:
    print("Not a right angle.")
