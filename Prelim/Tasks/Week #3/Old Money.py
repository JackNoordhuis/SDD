#############
# Old Money #
#############

print("Let's travel back in time with a suit case of money!")

travelTo = eval(input("What year should we travel back to?\nYear: "))
if travelTo < 2017:
    yearDiff = 2017 - travelTo
    money = eval(input("How much money are we bringing with us?\nMoney: "))
    increase = 0.025 * yearDiff
    print("In the year " + str(travelTo) + " you would've had $" + str(round((increase + 1) * money, 2)) + " worth of buying power!")
else:
    print("We can't travel forwards in time!")

