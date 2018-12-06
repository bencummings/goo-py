"""
Completed solution for the 'mimic' exercise featured within Google's Python
course.

This script reads the contents of the specified file, generates a dictionary of
words (which are mapped to a list of proceding words), and then simulates the
language used in the specified file by using the dictionary of words and random
selections.

Usage:
    python 06_mimic.py <file_path>
"""


import os
import random
import sys


def generate_dict(file_content):
    """
    Generates and returns a dictionary of words mapped to a list of proceding
    words.
    """

    # Converts all of the words to lowercase and strips the punctuation.
    words = [word.lower().strip(".,:;-`'\"!?()[]") for word in file_content.split()]

    dict = {}

    # Maps each word to the trailing word (or words).
    for i in range(len(words)):
        # Provides a seed for a word that lacks a trailing word.
        # Typically, this occurs when the last word within a file is unique.
        if i == 0:
            dict[""] = [words[i]]

        # Adds and initialises the word if it's absent within the words dictionary.
        if words[i] not in dict:
            dict[words[i]] = []

        # Maps the last word, if unique, to the seed created earlier.
        if i == len(words) - 1:
            # The word being mapped to an empty list indicates it is unique.
            if not dict[words[i]]:
                dict[words[i]].append("")
        else:
            dict[words[i]].append(words[i + 1])

    return dict


def print_dict(dict, seed):
    """
    Generates output based on the dictionary of words and initial seed.
    """

    output = ""

    if dict:
        section_length = 200  # Unit in words.
        paragraph_length = 3  # Unit in sentences.
        sentence_length = 15  # Unit in words.
        count = 0

        while count < section_length:
            # Selects a random word from the seed's mapped list.
            word = random.choice(dict[seed])

            # Processes and appends the word to the output.
            # Skips the word if it is of zero length.
            if word != "":
                count += 1

                # Determines if the word is at the start of a sentence.
                # Adds appropriate formatting.
                if count % sentence_length == 1:
                    output += word.capitalize()
                else:
                    output += word

                # Determines if the word is at the end of a sentence, paragraph, or section.
                # Adds appropriate punctuation.
                if count % sentence_length == 0 or count == section_length:
                    if count % (sentence_length * paragraph_length) == 0:
                        output += ".\n\n"
                    else:
                        output += ". "
                else:
                    output += " "

            # Updates the seed to continue the chain.
            seed = word

    print output


def main():
    """
    Does the magic.
    """

    # Ensures the argument count is valid.
    if len(sys.argv) != 2:
        print "Error. Invalid argument count."
        sys.exit(1)

    file_path = sys.argv[1]

    # Ensures the file path argument is valid.
    if not os.path.exists(file_path):
        print "Error. Invalid file path."
        sys.exit(1)

    file = None

    # Opens, reads, and closes the file.
    try:
        file = open(file_path, "r")
        file_content = file.read()
    except:
        print "Error. Unable to read the file."
        sys.exit(1)
    finally:
        if file:
            file.close()

    # Generates the output.
    print_dict(generate_dict(file_content), "")


if __name__ == "__main__":
    main()