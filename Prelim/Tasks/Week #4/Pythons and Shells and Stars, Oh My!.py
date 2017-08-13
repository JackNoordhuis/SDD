########################################
# Pythons and Shells and Stars, Oh My! #
########################################

userInput = input("Enter: ").lower()

shells = userInput.count("shell")
stars = userInput.count("star")

if shells == stars:
    print("Just drive.")
else:
    print("CRASH!")
