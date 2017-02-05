#################
# Mah Nà Mah Nà #
#################

# Declare our default variables
count = 0
requiredInputs = ["do do de do do", "do do de do", "do do de do do"]

# Keep asking for an input until we have received enough user inputs
while len(requiredInputs) > count:
    # Check to make sure the user has sung the correct lyrics
    if requiredInputs[count] != input("mahna mahna? ").lower():
        # Send them a shaking head message, why u do dis
        print("[Head shake]")
    # Increase our input count
    count += 1

# Print the rest of our tune out
print("de do do!\nde do do!\nde do do do, do do, do-oo do!")
