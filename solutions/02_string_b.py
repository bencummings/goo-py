"""
Completed solutions for the second set of basic string exercises featured within
Google's Python course.

Usage:
    python 02_string_b.py
"""


def verbing(s):
    """
    Returns a word with 'ing' appended, if it isn't already suffixed with 'ing',
    otherwise appends 'ly'. The word must contain at least three characters.
    """

    if len(s) < 3:
        return s
    else:
        if s[-3:] != "ing":
            return s + "ing"
        else:
            return s + "ly"


def not_bad(s):
    """
    Returns a sentence where any sequences starting with 'not' and ending with
    'bad' are replaced with 'good'.
    """

    not_index = s.find("not")
    bad_index = s.find("bad")

    if not_index != -1 and bad_index != -1:
        if not_index < bad_index:
            return s.replace(s[not_index:bad_index + len("bad")], "good")

    return s


def front_back(a, b):
    """
    Splits two words, and then merges and returns the starts followed by the
    ends.
    """

    a_split = (len(a) // 2) + (len(a) % 2)
    b_split = (len(b) // 2) + (len(b) % 2)

    return a[:a_split] + b[:b_split] + a[a_split:] + b[b_split:]


def test(got, expected):
    """
    Outputs (prints) the test case result.
    """

    if got == expected:
        prefix = " OK "
    else:
        prefix = "  X "

    print "%s Got: %s, Expected: %s" % (prefix, repr(got), repr(expected))


def main():
    """
    Performs the test cases.
    """

    print "Function: verbing"
    test(verbing("hail"), "hailing")
    test(verbing("swiming"), "swimingly")
    test(verbing("do"), "do")

    print "\nFunction: not_bad"
    test(not_bad("This movie is not so bad"), "This movie is good")
    test(not_bad("This dinner is not that bad!"), "This dinner is good!")
    test(not_bad("This tea is not hot"), "This tea is not hot")
    test(not_bad("It's bad yet not"), "It's bad yet not")

    print "\nFunction: front_back"
    test(front_back("abcd", "xy"), "abxcdy")
    test(front_back("abcde", "xyz"), "abcxydez")
    test(front_back("kitten", "donut"), "kitdontenut")


if __name__ == "__main__":
    main()