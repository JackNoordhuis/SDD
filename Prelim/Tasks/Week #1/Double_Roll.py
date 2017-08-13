import random

minInt = 1
maxInt = 6

first_roll = random.randint(minInt, maxInt)
second_roll = random.randint(minInt, maxInt)
chance = minInt / (maxInt * 2) * 100

print("You rolled a " + str(first_roll) + " and a " + str(second_roll) + "! There is a " + str(round(chance, 2)) + "% chance of rolling a " + str(first_roll) + " and a " + str(second_roll) + "!")

input("\n\nPress any key to exit...")
