#######################
# Squaring the Circle #
#######################

import math

radius = eval(input("What is the radius of you circle?\nRadius: "))

print("Egyptian area: " + str((64/81) * ((radius * 2) ** 2)))
print("Real area: " + str(math.pi * (radius ** 2)))
