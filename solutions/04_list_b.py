"""
Completed solutions for the second set of basic list exercises featured within
Google's Python course.

Usage:
    python 04_list_b.py
"""


def remove_adjacent(nums):
    """
    Returns a new list without adjacent duplicate items (elements).
    """

    collapsed_nums = []

    for i in range(len(nums)):
        if i == 0 or nums[i] != nums[i - 1]:
            collapsed_nums.append(nums[i])

    return collapsed_nums


def linear_merge(list1, list2):
    """
    Merges two lists into a single list sorted in ascending order.
    """

    merged = []

    total_count = len(list1) + len(list2)
    list1_count = 0
    list2_count = 0

    while (list1_count + list2_count) < total_count:
        list1_append = True

        if list1_count == len(list1) or (list2_count != len(list2) and list2[list2_count] < list1[list1_count]):
            list1_append = False

        if list1_append:
            merged.append(list1[list1_count])
            list1_count += 1
        else:
            merged.append(list2[list2_count])
            list2_count += 1

    return merged


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

    print "Function: remove_adjacent"
    test(remove_adjacent([1, 2, 2, 3]), [1, 2, 3])
    test(remove_adjacent([2, 2, 3, 3, 3]), [2, 3])
    test(remove_adjacent([]), [])

    print "\nFunction: linear_merge"
    test(linear_merge(["aa", "xx", "zz"], ["bb", "cc"]), ["aa", "bb", "cc", "xx", "zz"])
    test(linear_merge(["aa", "xx"], ["bb", "cc", "zz"]), ["aa", "bb", "cc", "xx", "zz"])
    test(linear_merge(["aa", "aa"], ["aa", "bb", "bb"]), ["aa", "aa", "aa", "bb", "bb"])


if __name__ == "__main__":
    main()