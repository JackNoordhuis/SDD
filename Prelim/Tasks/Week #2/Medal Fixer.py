###############
# Medal Fixer #
###############

a = eval(input("a = "))
b = eval(input("b = "))
c = eval(input("c = "))

print("Gold")
if b == a:
    print("Gold")
if b > a:
    print("Silver")
if c == b:
    print("Silver")
else:
    print("Bronze")

# Print our footer
print("*" * 40)
