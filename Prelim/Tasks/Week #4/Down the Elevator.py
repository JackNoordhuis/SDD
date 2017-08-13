#####################
# Down the Elevator #
#####################

departure = eval(input("Departure floor: "))
destination = eval(input("Destination floor: "))

if departure > destination:
    required = departure - destination
    loops = 0
    while loops <= required:
        print(str(departure - loops))
        loops += 1

else:
    required = destination - departure
    loops = 0
    while loops <= required:
        print(str(departure + loops))
        loops += 1

