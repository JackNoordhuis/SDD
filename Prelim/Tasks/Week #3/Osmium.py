##########
# Osmium #
##########

import math

radius = eval(input("Radius (cm): "))
height = eval(input("Height (cm): "))

volume = math.pi * height * radius ** 2
mass = volume * 22.59

price = mass * 13

print(str(round(mass, 4)) + " grams of Osmium will cost $" + str(round(price, 2)))
