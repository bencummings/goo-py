"""
Completed solution for the 'word count' exercise featured within Google's Python
course.

This script reads the contents of the specified file, and then generates and
outputs a dictionary of words and associated counts.

Usage:
    python 05_word_count.py [--all] [--top] <file_path>
"""


import os
import sys


def get_count(file_content):
    """
    Generates and returns a dictionary of words and associated counts based on
    the file content.
    """

    words = {}

    # Converts all of the words to lowercase, strips punctuation, and then determines the occurances.
    for word in [word.lower().strip(".,:;-`'\"!?()[]") for word in file_content.split()]:
        # Adds and initialises the word if it's absent within the words dictionary.
        if word not in words:
            words[word] = 0

        words[word] += 1

    return words


def print_all(file_content):
    """
    Outputs (prints) all of the words and associated counts in ascending
    alphabetical order.
    """

    words = get_count(file_content)

    # Sorts the keys alphabetically ascending.
    for word in sorted(words):
        print word + " " + str(words[word])

    print "\nDisplaying all of the " + str(len(words)) + " words."


def print_top(file_content):
    """
    Outputs (prints) a limited selection of words and associated counts in
    descending numerical order.
    """

    words = get_count(file_content)
    limit = 20
    count = 0

    # Sorts the keys by the corresponding value numerically descending.
    for word in sorted(words, key=lambda word: words[word], reverse=True):
        print word + " " + str(words[word])

        count += 1

        if count == limit:
            break

    print "\nDisplaying the top " + str(count) + " words only."


def main():
    """
    Does the magic.
    """

    # Ensures the argument count is valid.
    if len(sys.argv) != 3:
        print "Error. Invalid argument count."
        sys.exit(1)

    option = sys.argv[1]

    # Ensures the option argument is valid.
    if option not in ["--all", "--top"]:
        print "Error. Invalid option."
        sys.exit(1)

    file_path = sys.argv[2]

    # Ensures the file path argument is valid.
    if not os.path.exists(file_path):
        print "Error. Invalid file path."
        sys.exit(1)

    # Opens, reads, and closes the file.
    file = None

    try:
        file = open(file_path, "r")
        file_content = file.read()
    except:
        print "Error. Unable to read the file."
        sys.exit(1)
    finally:
        if file:
            file.close()

    # Selects the processing operation based on the option argument.
    if option == "--all":
        print_all(file_content)
    else:
        print_top(file_content)


if __name__ == "__main__":
    main()