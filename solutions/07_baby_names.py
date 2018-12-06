"""
Completed solution for the 'baby names' exercise featured within Google's Python
course.

This script extracts a list of baby names and associated ranks for a particular
year, based on a HTML document produced by the Social Security administration,
and optionally generates a summary file.

Usage:
    python 07_baby_names.py [--limit <limit>] [--save-summary] <html_path> [<html_path>]
"""


import os
import re
import sys


def extract_names(file_content):
    """
    Extracts and returns a list (which is alphabetically sorted) containing the
    year, baby names, and associated ranks.
    """

    matches = []

    # Attempts to extract the year.
    # Allows for variations in white-space and letter-casing.
    year_match = re.search(r"popularity\s+in\s+(\d{4})", file_content, re.IGNORECASE)

    # Ensures the year was successfully extracted (as indicated by the MatchObject instance).
    if year_match:
        matches.append(year_match.group(1))
    else:
        raise ValueError

    # Attempts to extract the names and associated ranks.
    # Allows for variations in white-space and letter-casing.
    rankings = re.findall(r"<td>(\d+)</td>\s*<td>([a-z]+)</td>\s*<td>([a-z]+)</td>", file_content, re.IGNORECASE)

    # Ensures the names and associated ranks were successfully extracted (as indicated by the non-empty list).
    if rankings:
        names = {}

        # Unpacks the list of tuples into a dictionary.
        # Accounts for duplicate names by assigning the lowest rank.
        for ranking in rankings:
            rank, male_name, female_name = ranking

            for name in [male_name, female_name]:
                if name not in names or rank < names[name]:
                    names[name] = rank

        # Sorts the names alphabetically in preparation for final output.
        for name in sorted(names):
            matches.append(name + " " + str(names[name]))
    else:
        raise ValueError

    return matches


def main():
    """
    Does the magic.
    """

    # Removes the file name of this script from the arguments list.
    del sys.argv[0]

    # Ensures the limit argument, if specified, is well-formed and valid.
    limit = None

    if "--limit" in sys.argv:
        try:
            assert sys.argv[0] == "--limit"
            # Offsets the limit by 1 to account for the year being the first element within the results list.
            limit = int(sys.argv[1]) + 1
            del sys.argv[:2]
        except:
            print "Error. The limit argument is malformed."
            sys.exit(1)

    # Ensures the summary argument, if specified, is well-formed and valid.
    summary = False

    if "--save-summary" in sys.argv:
        try:
            assert sys.argv[0] == "--save-summary"
            summary = True
            del sys.argv[0]
        except:
            print "Error. The summary argument is malformed."
            sys.exit(1)

    # Ensures that at least one file path has been specified for processing.
    if not sys.argv:
        print "Error. At least one file path must be specified."
        sys.exit(1)

    # Ensures the specified file path is (or paths are) valid.
    for file_path in sys.argv:
        if not os.path.exists(file_path):
            print "Error. Invalid file path (or paths)."
            sys.exit(1)

    # Processes each file and generates the results.
    for file_path in sys.argv:
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

        # Generates the results and writes to a file or standard output.
        try:
            results = "\n".join(extract_names(file_content)[:limit])
        except ValueError:
            print "Error. Invalid file contents. The HTML structure is malformed."
            sys.exit(1)

        if summary:
            in_path, in_file = os.path.split(os.path.abspath(os.path.join(os.getcwd(), file_path)))

            file = None

            # Opens, writes to, and closes the file.
            try:
                file = open(os.path.join(in_path, in_file + ".summary"), "w")
                file.write(results)
            except:
                print "Error. Unable to create or write to the file."
                sys.exit(1)
            finally:
                if file:
                    file.close()
        else:
            print results


if __name__ == "__main__":
    main()