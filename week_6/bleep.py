from cs50 import get_string
from sys import argv


def main():

    # TODO
    if len(argv) != 2:
        print("Usage: python bleep.py file")
        exit(1)

    path = argv[1]
    banned_file = open(path,'r')
    file_word_list = banned_file.read()

    userInput = get_string("What line would you like to censor? \n")

    inputList = userInput.split()
    print(inputList)
    # print(file_word_list)

    censorship = ""

    for word in inputList:
        if word.lower() in file_word_list:
            hashed = "*" * len(word)
            censorship += hashed + " "
        else:
            censorship += word + " "
            # print(userInput.replace(word, hashed))

    print(censorship.strip())


if __name__ == "__main__":
    main()
