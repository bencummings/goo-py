"""
Completed solution for the 'copy special' exercise featured within Google's
Python course.

This script copies or zips files from specified directories that match the
pattern __XYZ__ where 'XYZ' can be any combination of alpha characters.

Usage:
    python 08_copy_special.py [--copy <copy_path>] [--zip <zip_path>] <in_path> [<in_path>]
"""


import os
import re
import shutil
import sys
import zipfile


def copy_to(file_paths, out_path):
    """
    Copies (i.e. writes) each file specified within the list of file paths (with
    each file path being a tuple containing the parent directory and file name)
    to the desired path.
    """

    for directory_path, file_name in file_paths:
        shutil.copy(os.path.join(directory_path, file_name), out_path)


def get_special_paths(directory_path):
    """
    Generates and returns a list of file paths (with each file path being a
    tuple containing the parent directory and file name) that match the pattern
    __XYZ__ where 'XYZ' can be any combination of alpha characters.
    """

    file_paths = []

    for entry in os.listdir(directory_path):
        # Ensures that the entry is a file (and NOT a directory) and that the name matches the pattern.
        if os.path.isfile(os.path.join(directory_path, entry)) and re.search(r".*__[a-z]+__.*", entry, re.IGNORECASE):
            file_paths.append((directory_path, entry))

    return file_paths


def zip_to(file_paths, out_path):
    """
    Zips each file specified within the list of file paths (with each file path
    being a tuple containing the parent directory and file name) into a single
    combined archive which is written to the desired path.
    """

    archive = zipfile.ZipFile(out_path, "a", zipfile.ZIP_DEFLATED, True)

    for directory_path, file_name in file_paths:
        archive.write(os.path.join(directory_path, file_name), file_name)

    archive.close()


def main():
    """
    Does the magic.
    """

    # Removes the file name of this script from the arguments list.
    del sys.argv[0]

    # Ensures that the copy argument, if specified, is well-formed and valid.
    copy_path = None

    if "--copy" in sys.argv:
        try:
            assert sys.argv[0] == "--copy"
            copy_path = os.path.abspath(sys.argv[1])
            del sys.argv[:2]
        except:
            print "Error. The copy argument is malformed."
            sys.exit(1)

    # Ensures that the output directory path for the copying operation is valid.
    if copy_path:
        if not os.path.exists(copy_path):
            print "Error. Invalid output directory path for the copying operation."
            sys.exit(1)

    # Ensures that the zip argument, if specified, is well-formed and valid.
    zip_path = None

    if "--zip" in sys.argv:
        try:
            assert sys.argv[0] == "--zip"
            zip_path = os.path.abspath(sys.argv[1])
            del sys.argv[:2]
        except:
            print "Error. The zip argument is malformed."
            sys.exit(1)

    # Ensures that the output directory path and file name for the zipping operation are valid.
    if zip_path:
        if not os.path.exists(os.path.dirname(zip_path)):
            print "Error. Invalid output directory path for the zipping operation."
            sys.exit(1)

        if not re.search(r"\.zip$", os.path.basename(zip_path), re.IGNORECASE):
            print "Error. Invalid output file name for the zipping operation."
            sys.exit(1)

    # Ensures that at least one directory path has been specified for processing.
    if not sys.argv:
        print "Error. At least one directory path must be specified for processing."
        sys.exit(1)

    # Converts the remaining arguments (i.e. directory paths) from relative to absolute paths.
    sys.argv = [os.path.abspath(directory_path) for directory_path in sys.argv]

    # Ensures that the specified directory path is (or paths are) valid.
    for directory_path in sys.argv:
        if not os.path.exists(directory_path):
            print "Error. Invalid directory path (or paths)."
            sys.exit(1)

    # Generates the list of absolute file paths (stored as tuples).
    file_paths = []

    for directory_path in sys.argv:
        file_paths += get_special_paths(directory_path)

    # Ensures that there are no duplicate file names. Takes into consideration the case-insensitive nature of Windows.
    file_names = []

    for _directory_path, file_name in file_paths:
        file_name = file_name.lower()

        if file_name in file_names:
            print "Error. Duplicate file names."
            sys.exit(1)

        file_names.append(file_name)

    # Copies the filtered files, if requested, to the output directory path.
    if copy_path:
        try:
            copy_to(file_paths, copy_path)
        except:
            print "Error. Unable to copy the files to the output directory due to insufficient permissions."
            sys.exit(1)

    # Zips the filtered files, if requested, to the output file path.
    if zip_path:
        try:
            zip_to(file_paths, zip_path)
        except:
            print "Error. Unable to create (or append to) the ZIP archive due to insufficient permissions."
            sys.exit(1)

    # Prints the filtered file paths, but only if the copying and zipping operations haven't been specified.
    if not copy_path and not zip_path:
        for file_path in file_paths:
            print file_path

    # OK.
    sys.exit(0)


if __name__ == "__main__":
    main()