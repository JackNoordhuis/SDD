############################
# Debug the longest string #
############################

a = input("first string? ")
b = input("second string? ")
c = input("third string? ")

longest = ""
if len(a) >= len(longest):
    longest = a
if len(b) > len(longest):
    longest = b
if len(c) > len(longest):
    longest = c

print("The longest line was " + longest)
