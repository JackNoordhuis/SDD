#############
# Lift Off! #
#############

import time

count = eval(input("Enter approximate time till lift off.\nTime: "))

print("Counting down...")
while count > 0:
    time.sleep(1)
    print(str(count) + "...")
    count -= 1

print("Lift off!")
