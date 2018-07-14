from nltk.tokenize import sent_tokenize


def lines(a, b):
    """Return lines in both a and b"""

    # TODO
    linesA = a.split("\n")
    linesB = b.split("\n")
    result = set()

    for lineA in linesA:
        for lineB in linesB:
            if lineA == lineB:
                result.add(lineA)

    return result


def sentences(a, b):
    """Return sentences in both a and b"""

    # TODO
    sentA = set(sent_tokenize(a))
    sentB = set(sent_tokenize(b))

    return sentA & sentB


def substrings(a, b, n):
    """Return substrings of length n in both a and b"""

    # TODO
    substrsA = set()
    first = 0
    # last = n

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
