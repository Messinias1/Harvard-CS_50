from cs50 import get_int

while True:
    userInput = get_int("Height: ")
    if userInput >= 1 and userInput <= 8:
        break

for height in range(userInput):
    for space in range(userInput - height - 1):
        print(" ", end="")
    for hashtag in range(height + 1):
        print("#", end="")
    print("")