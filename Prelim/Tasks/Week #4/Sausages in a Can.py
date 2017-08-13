#####################
# Sausages in a Can #
#####################

rows = eval(input("Rows: "))
loops = 0

while loops < rows:
    loops += 1
    print("Row " + str(loops) + ": " + str((3 * loops * (loops - 1) + 1)))
