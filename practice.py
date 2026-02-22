# Q14.
# - Ask the user to enter numbers continuously.
# - Stop when they enter "stop".
# - At the end, print:

# Total numbers entered \       length of list
# Maximum Number \              list.max()
# Minimum Number                list.min()


userData = []

while True:
    userInput = input("Please enter a number or stop to exit: ")

    if userInput == "stop":
        print("Thanks for using")
        break
    else:
        userData.append(int(userInput))

print("Total enter numbers are:", len(userData))
print("Sum of number is:", sum(userData))
print("Max of number is:", max(userData))
print("Min of number is:", min(userData))
