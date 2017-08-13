#########
# Evens #
#########

lower = eval(input("Please input the lower bound.\nLower Bound: "))
upper = eval(input("Please input the upper bound.\nUpper Bound: ")) + 1
loops = lower

while loops < upper:
    if loops % 2 == 0:
        print(str(loops))
    loops += 1

