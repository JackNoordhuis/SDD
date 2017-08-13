#################
# Eliza Therapy #
#################

import re

latestInput = input("Hello, my name is Eliza. What would you like to talk about?\n")

loop = True

while loop:
    latestInput = latestInput.lower()
    if latestInput.endswith("?"):
        latestInput = latestInput[:-1]
    if "feel" in latestInput:
        latestInput = input("Do you often feel that way?\n")
    elif "i am " in latestInput:
        result = re.match(r"i am (\w*)", latestInput, re.M | re.I)
        latestInput = input("How long have you been " + result.group(1) + "?\n")
    elif "you " in latestInput and " me" in latestInput:
        result = re.match(r"(.*) you (.*) me", latestInput, re.M | re.I)
        latestInput = input("What makes you think I " + result.group(2) + " you?\n")
    elif "go away" in latestInput:
        print("I hope I have helped you!\n")
        loop = False
    else:
        latestInput = input("Please go on\n")
