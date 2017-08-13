####################
# Can I afford it? #
####################

# Declare our money as a float
myMoney = 11.0

# Check to see if we can afford x amount of mars bars @ $2.10/each
if eval(input("How many mars bars would you like to buy?\nMars bars: ")) * 2.10 <= myMoney:
    # We can afford em!
    print("Buy them!")
else:
    # Nope, better go get some more pocket money
    print("You can't afford that many :c")

# Print our footer
print("*" * 40)
