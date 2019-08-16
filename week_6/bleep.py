from cs50 import get_string
from sys import argv


def main():

    # TODO
    if len(argv) != 2:
        print("Usage: python bleep.py file")
        exit(1)

    userInput = get_string("What line would you like to censor? \n")


if __name__ == "__main__":
    main()
