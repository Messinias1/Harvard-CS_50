from cs50 import get_string
import sys


def main():

    if len(sys.argv) != 2:
        print("Usage: python key")
        exit(1)

    key = int(sys.argv[1])
    if key < 0:
        printf("Key must be a positive number")
        exit(1)

    plaintext = get_string("plaintext: ")

    print("ciphertext: ", end="")

    for i in range(0, len(plaintext)):
        if plaintext[i].islower() and plaintext[i].isalpha():
            print(chr((ord(plaintext[i]) - 97 + key) % 26 + 97), end="")

        elif plaintext[i].isupper() and plaintext[i].isalpha():
            print(chr((ord(plaintext[i]) - 65 + key) % 26 + 65), end="")

        else:
            print(plaintext[i])
    print()


if __name__ == '__main__':
    main()
