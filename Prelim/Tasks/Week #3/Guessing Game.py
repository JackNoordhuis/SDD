#################
# Guessing Game #
#################

print("Let's play a guessing game!")

doLoop = True

while doLoop:
    if "electricity" in input("What is my favourite food?\nGuess: ").lower():
        doLoop = False
    else:
        print("Not even close")

print("You guessed it! Buzzzz")
