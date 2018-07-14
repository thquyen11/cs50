


def main():
    a="Raymond rang me up at the office. He said that a friend of histo whom he'd spoken about meinvited me to spend next Sunday at his little seaside bungalow just outside Algiers. I told him I'd have been delighted; only I had promised to spend Sunday with a girl. Raymond promptly replied that she could come, too. In fact, his friend's"
    b="Raymond called me at the office. He told me that a friend of his (he'd spoken to him about me) had invited me to spend the day Sunday at his little beach house, near Algiers. I said I'd really like to, but I'd promised to spend the day with a girlfriend. Raymond immediately told me she was invited too. His friend's wife would be very glad not to be alone with a bunch of men."

    substrings(a,b, 5)

def substrings(a, b, n):
    """Return substrings of length n in both a and b"""

    # TODO
    substrsA = set()
    first = 0
    last = n
    while (True):
        print("while loop A running")
        print("first {}, last {}, len {}".format(first,last,len(a)))
        substrsA.add(a[first:last])
        first = n
        last = first + n
        print("first {}, last {}, len {}".format(first,last,len(a)))
        if last > len(a):
            substrsA.add(a[first:len(a)])
            break;

    substrsB = set()
    first = 0
    last = n
    while (True):
        print("while loop B running")
        substrsB.add(b[first:last])
        first = n
        last = first + n
        if last > len(b):
            substrsB.add(b[first:len(b)])
            break;

    return substrsA & substrsB

if __name__ == "__main__":
    main()