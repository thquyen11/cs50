import sys
from cs50 import get_float


def main():
    __quarter = 0
    __dime = 0
    __nickel = 0
    __penny = 0
    __changeOut = 0
    __changeIn = 0

    while True:
        # print("Input change: ", end="")
        # __changeIn = float(sys.stdin.readline())
        __changeIn = get_float("Input change: ")
        __cents = round(__changeIn * 100)
        if __changeIn >= 0:
            break

    __quarter = 1
    while __cents >= 25:
        __cents -= 25
        __changeOut += 1
        __quarter += 1

    __dime = 1
    while __cents >= 10:
        __cents -= 10
        __changeOut += 1
        __dime += 1

    __nickel = 1
    while __cents >= 5:
        __cents -= 5
        __changeOut += 1
        __nickel += 1

    __penny = 1
    while __cents >= 1:
        __cents -= 1
        __changeOut += 1
        __penny += 1

    print(__changeOut)


if __name__ == "__main__":
    main()
