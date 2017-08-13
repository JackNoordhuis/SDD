######################
# Short & long names #
######################


# Declare our get name response function
def get_name_response(name):
    length = len(name)
    if length > 8:
        return "you have a long name!"
    elif length >= 4:
        return "nice to meet you!"
    else:
        return "you have a short name!"

# Ask the user for their name
userName = input("What is your name?\nName: ")

# Respond with the users name and the respective response
print("Hello " + userName + ", " + get_name_response(userName))

# Print our footer
print("*" * 40)
