####################
# Days of the Week #
####################


# Declare our get name day function
def get_day_name(number):
    # Use a dictionary to find the day name (I dun like long if-else's)
    return {
        "1": "Monday",
        "2": "Tuesday",
        "3": "Wednesday",
        "4": "Thursday",
        "5": "Friday",
        "6": "Saturday",
        "7": "Sunday"
    }.get(number)

# Ask the user to enter a day number
dayNumber = input("Enter a day number.\nDay: ")

# Tell the user what the name of the day is
print("Day " + dayNumber + " is called " + get_day_name(dayNumber))

# Print out footer
print("*" * 40)
