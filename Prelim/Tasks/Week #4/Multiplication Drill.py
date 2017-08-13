########################
# Multiplication Drill #
########################

number = eval(input("Enter a number to multiply\nNumber: "))

loops = 0

while loops < 12:
    loops += 1
    print(str(number) + " x " + str(loops) + " = " + str(number * loops))

