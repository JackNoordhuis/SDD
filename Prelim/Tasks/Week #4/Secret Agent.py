################
# Secret Agent #
################

message = input("Enter secret message to decode\nMessage: ")
length = len(message)
loops = 0
word = ""

while loops < length :
    if not loops % 2:
        word += message[loops] + " "
        loops += 2

print(word)
