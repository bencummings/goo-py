"""
Completed solutions for the first set of basic string exercises featured within
Google's Python course.

Usage:
    python 01_string_a.py
"""


def donuts(n):
    """
    Conditionally outputs (prints) the quantity of donuts.
    """

    prefix = "Number of donuts: "

    if n < 10:
        return prefix + str(n)

    return prefix + "Many"


def both_ends(s):
    """
    Returns the string inclusive of only the initial two characters and the
    final two characters. The string must contain at least two characters.
    """

    if len(s) < 2:
        return ""

    return s[:2] + s[-2:]


def fix_start(s):
    """
    Returns the string with any occurances of the initial character (excluding
    the initial character itself) being replaced with an asterisk.
    """

    return s[0] + s[1:].replace(s[0], "*")


def mix_up(a, b):
    """
    Returns a string containing both words, but with the initial two characters
    being switched.
    """

    # Assumes that both strings (a, b) have a minimum length of two characters.
    return b[:2] + a[2:] + " " + a[:2] + b[2:]


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

    print "Function: donuts"
    test(donuts(4), "Number of donuts: 4")
    test(donuts(9), "Number of donuts: 9")
    test(donuts(10), "Number of donuts: Many")
    test(donuts(99), "Number of donuts: Many")

    print "\nFunction: both_ends"
    test(both_ends("spring"), "spng")
    test(both_ends("hello"), "helo")
    test(both_ends("a"), "")
    test(both_ends("xyz"), "xyyz")

    print "\nFunction: fix_start"
    test(fix_start("babble"), "ba**le")
    test(fix_start("aardvark"), "a*rdv*rk")
    test(fix_start("google"), "goo*le")
    test(fix_start("donut"), "donut")

    print "\nFunction: mix_up"
    test(mix_up("mix", "pod"), "pox mid")
    test(mix_up("dog", "dinner"), "dig donner")
    test(mix_up("gnash", "sport"), "spash gnort")
    test(mix_up("pezzy", "firm"), "fizzy perm")


if __name__ == "__main__":
    main()