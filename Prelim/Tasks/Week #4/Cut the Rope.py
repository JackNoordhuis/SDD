################
# Cut the Rope #
################

import math

length = eval(input("Rope length: "))

if length % 2 == 0:
    half = round(length / 2)
    print("o" * half + "\n" + "o" * half)
else:
    longHalf = math.ceil(length / 2)
    shortHalf = math.floor(length / 2)
    print("o" * longHalf + "\n" + "o" * shortHalf)
