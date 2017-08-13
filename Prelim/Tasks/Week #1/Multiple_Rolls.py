import random

minInt = 1
maxInt = eval(input("\nHow many sides should our dice have?\nSides: "))

rolls = eval(input("\nHow many dice are we going to roll?\nRolls: "))

print("")

rollCount = 0
rolled = []

# Roll the dice until we
while rollCount < rolls:
    rollCount += 1
    roll = random.randint(minInt, maxInt)
    rolled.append(roll)
    print("Roll #" + str(rollCount) + " = " + str(roll))

chance = round(minInt / (maxInt * rolls) * 100, 2)
print("\nThere was a " + str(chance) + "% chance of rolling that combination of numbers!")

input("\n\nPress any key to exit...\n\n")
