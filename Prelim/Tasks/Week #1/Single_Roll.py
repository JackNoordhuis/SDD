import random

minInt = 1

maxInt = 6

roll = random.randint(minInt, maxInt)
chance = minInt / maxInt * 100

print("You rolled a " + str(roll) + "! There is a " + str(round(chance, 2)) + "% chance of rolling a " + str(roll) + "!")

input("\n\nPress any key to exit...")
