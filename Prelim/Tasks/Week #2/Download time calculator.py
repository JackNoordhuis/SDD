############################
# Download time calculator #
############################

# Ask the user how many bytes were downloaded in the past second
currentBytes = eval(input("How many bytes have been downloaded in the past second?\nBytes: "))
# Ask the user how many bytes still need to be downloaded
totalBytes = eval(input("How many bytes are left?\nBytes: "))

# Tell the user approximately how much longer the download will take
print("The download will take approximately " + str(round(totalBytes / currentBytes)) + " seconds to finish!")

# Print our footer
print("*" * 40)
