from cs50 import get_string
from sys import argv


def main():

    # TODO
    if len(argv) != 2:
        print("Usage: python bleep.py file")
        exit(1)

    userInput = get_string("What line would you like to censor? \n")

    path = "banned.txt"
    banned_file = open(path,'r')
    file_word_list = banned_file.read()

    inputList = userInput.split()
    print(inputList)
    # print(file_word_list)

    for word in inputList:
        if word.lower() in file_word_list:
            hashed = "*" * len(word)
            print(userInput.replace(word, hashed))


if __name__ == "__main__":
    main()
