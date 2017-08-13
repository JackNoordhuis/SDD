#########################
# Pass with Distinction #
#########################


# Declare our get score function
def get_score(x):
    if x >= 85:
        return "HD"
    elif x >= 75:
        return "D"
    elif x >= 65:
        return "CR"
    elif x >= 50:
        return "P"
    return "F"

# Ask their user for their score and tell them their mark
print("Score: " + get_score(eval(input("Please input your score.\nScore: "))))

# Print our footer
print("*" * 40)
