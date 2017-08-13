##################
# Kate and Wills #
##################

year = eval(input("What year would you like to start at?\nYear: "))
times = eval(input("How many years would you like to see? "))
loops = 0

if year > 2011:
    while loops < times:
        newYear = year + loops
        marriedYears = newYear - 2011
        if marriedYears == 1:
            print("On April 29th " + str(newYear) + ", they will have been married for " + str(marriedYears) + " year.")
        else:
            print("On April 29th " + str(newYear) + ", they will have been married for " + str(marriedYears) + " years.")
        loops += 1
else:
    print("They aren't married yet!")
