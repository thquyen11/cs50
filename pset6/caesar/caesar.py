import sys
from cs50 import get_string


def main():
    if len(sys.argv) != 2:
        print("Only 1 argument allowed")
        sys.exit(1)

    key = int(sys.argv[1])
    ascii_a = 97
    ascii_z = 122
    ascii_A = 65
    ascii_Z = 90

    # print("Input plain text: ", end="")
    # plaintext = sys.stdin.readline()
    plaintext = get_string("Input plain text: ")

    print("ciphertext: ", end="")
    length = len(plaintext)
    for i in range(0, length):
        ascii = ord(plaintext[i])
        # print(ord(plaintext[i]))
        step = 0
        if (ascii >= ascii_A) and (ascii <= ascii_Z):
            step = (ascii + key - ascii_A) % 26
            ascii = ascii_A + step
        elif (ascii >= ascii_a) and (ascii <= ascii_z):
            step = (ascii + key - ascii_a) % 26
            ascii = ascii_a + step

        print(chr(ascii), end="")

    print()


if __name__ == "__main__":
    main()
