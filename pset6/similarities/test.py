def main():
    a = "foobar"
    b = "bar"

    print(substrings(a, b, 3))


def substrings(a, b, n):
    """Return substrings of length n in both a and b"""

    # TODO
    substrsA = set()
    first = 0
    # last = n

    # print("lena {}, lenb {}".format(len(a), len(b)))

    if n > len(a) or n > len(b):
        return substrsA

    while (True):
        substrsA.add(a[first:first + n])
        first = first + 1
        # last = last + n
        if first + n > len(a):
            # substrsA.add(a[first:len(a)])
            break;

    substrsB = set()
    first = 0
    # last = n
    while (True):
        substrsB.add(b[first:first + n])
        first = first + 1
        # last = last + n
        if first + n > len(b):
            # substrsB.add(b[first:len(b)])
            break;

    return substrsA & substrsB


if __name__ == "__main__":
    main()
