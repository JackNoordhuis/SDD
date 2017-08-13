######################
# Exponential Growth #
######################

cells = eval(input("How many cells should we start with?\nStarting cells: "))
cycles = eval(input("How many cycles?\nCycles: "))
cyclesRun = 0
overtaken = False

while cyclesRun < cycles:
    cyclesRun += 1
    cells *= 2
    print("Cells have multiplied! There are now " + str(cells) + " cells!")
    if cells >= 7371861300 and overtaken is False:
        print("The cells have overtaken the world in " + str(cycles) + " cycles!")
        overtaken = True

print("The cells have stopped cycling!")
