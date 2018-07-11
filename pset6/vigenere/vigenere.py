from cs50 import get_string
import sys


def main():
    if len(sys.argv) != 2:
        print("only 1 argument is accepted")
        sys.exit(1)

    keyWord = sys.argv[1]
    if not keyWord.isalpha():
        print("only alphabet is accepted")
        sys.exit(1)

    # Main Program
    plaintext = get_string("Input text: ")
    # print("plaintext: ", plaintext)

    counter = 0
    print("ciphertext: ", end="")
    for i in range(0, len(plaintext)):
        if (plaintext[i].isalpha()):
            counterKey = counter % len(keyWord)
            key = 0
            if keyWord[counterKey].isupper():
                key = ord(keyWord[counterKey]) - 65
            else:
                key = ord(keyWord[counterKey]) - 97

            # print("key: ", key)

            if (plaintext[i].isupper()):
                # plaintext[i] = 65 + (plaintext[i] - 65 + key) % 26
                print(chr(65 + (ord(plaintext[i]) - 65 + key) % 26), end="")
            else:
                # plaintext[i] = 97 + (plaintext[i] - 97 + key) % 26
                print(chr(97 + (ord(plaintext[i]) - 97 + key) % 26), end="")

            counter += 1
    print()


if __name__ == "__main__":
    main()