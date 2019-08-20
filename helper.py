from nltk.tokenize import sent_tokenize


def lines(a, b):
    """Return lines in both a and b"""

    # TODO
    file1 = set(a.split("\n"))
    file2 = set(b.split("\n"))

    print(file1, file2)
    print(file1 & file2)

    return file1 & file2


def sentences(a, b):
    """Return sentences in both a and b"""

    # TODO
    file1 = set(sent_tokenize(a))
    file2 = set(sent_tokenize(b))
    print(file1, file2)
    return file1 & file2


def substrings(a, b, n):
    """Return substrings of length n in both a and b"""

    # TODO
    file1 = set()
    file2 = set()

    for i in range(len(a) - n + 1):
        file1.add(a[i:i + n])
        # print(file1_sub)
    for i in range(len(b) - n + 1):
        file2.add(b[i:i + n])

    print(file1 & file2)
    return file1 & file2
