#################
# ASCII Bowling #
#################

length = eval(input("Length: "))

loops = 0

while loops < length:
    print("." * loops + "O" + "." * (length - loops - 1) + "I")
    loops += 1

print("." * length + "X\nHit!")

