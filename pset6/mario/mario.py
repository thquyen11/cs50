import sys
import cs50


def main():
    while True:
        print("Pyramid Height: ", end="")
        # n = sys.stdin.readline()
        # n = int(n)
        n = cs50.get_int()
        if (n >= 0) and (n <= 23):
            break

    for i in range(0, n):
        for j in range(0, n - (i + 1)):
            print(" ", end="")
        for m in range(0, i + 1):
            print("#", end="")
        print("  ", end="")
        for k in range(0, i + 1):
            print("#", end="")
        print()


if __name__ == "__main__":
    main()
