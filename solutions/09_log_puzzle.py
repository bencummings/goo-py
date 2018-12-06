"""
Completed solution for the 'log puzzle' exercise featured within Google's Python
course.

This script extracts the server name and a list of image URLs from an Apache web
server log file, downloads the images, and then assembles them within a
generated HTML document to solve the puzzle.

Usage:
    python 09_log_puzzle.py --out <out_path> <log_path>
"""


import os
import re
import requests
import sys


def download_images(image_urls, out_path):
    """
    Downloads the images specified within the list of URLs and writes them to
    the desired path (presumably, on non-volatile storage).
    """

    # Creates the out path if it doesn't already exist.
    # Likely redundant due to checking the validity within the main execution context.
    if not os.path.exists(out_path):
        os.makedirs(out_path)

    # Downloads each image from the specified URL.
    for image_url in image_urls:
        try:
            response = requests.get(image_url)
        except:
            raise requests.exceptions.ConnectionError

        if response.status_code != 200:
            raise requests.exceptions.HTTPError

        # Writes each image to the out path.
        image_file = None

        try:
            image_file = open(os.path.join(out_path, os.path.basename(image_url)), "wb")
            image_file.write(response.content)
        except:
            raise IOError
        finally:
            if image_file:
                image_file.close()


def extract_server_name(log_path):
    """
    Extracts the server name from the Apache web server log file name. This
    relies on the convention that the server name is preceded by an initial
    underscore.
    """

    match = re.search(r"_([a-z.]+)", os.path.basename(log_path), re.IGNORECASE)

    if match:
        return match.group(1)
    else:
        raise ValueError


def extract_urls(server_name, log_content):
    """
    Extracts and returns a list of image URLs from the Apache web server log
    file content. Casts to a set to prevent duplicates, and sorts based on the
    final word pattern (excluding the file extension).
    """

    return sorted(set(["https://" + server_name + path for path in re.findall(r"get\s+(.*puzzle.*)\s+http", log_content, re.IGNORECASE)]), key=lambda url: str.split(str.replace(url, ".", "-"), "-")[-2])


def generate_html(image_urls, out_path):
    """
    Generates a HTML document containing the list of image URLs and writes it to
    the desired path (presumably, on non-volatile storage).
    """

    title = "Generated Images"
    img_elements = ""

    # Creates an IMG element for each image URL.
    for image_url in image_urls:
        img_elements += "<img src='" + os.path.basename(image_url) + "' />"

    # Writes the HTML document to the out path.
    html_file = None

    try:
        html_file = open(os.path.join(out_path, "index.htm"), "w")
        html_file.write("<!doctype html><html><head><title>" + title + "</title></head><body>" + img_elements + "</body></html>")
    except:
        raise IOError
    finally:
        if html_file:
            html_file.close()


def main():
    """
    Uses magic to solve the puzzle.
    """

    # Ensures the argument count is valid.
    if len(sys.argv) != 4:
        print "Error. Invalid argument count."
        sys.exit(1)

    # Removes the file name of this script from the arguments list.
    del sys.argv[0]

    # Ensures that the out argument is specified.
    if "--out" not in sys.argv:
        print "Error. The out argument must be specified."
        sys.exit(1)

    # Ensures that the out argument is well-formed and valid.
    try:
        assert sys.argv[0] == "--out"
        out_path = os.path.abspath(sys.argv[1])
        del sys.argv[:2]
    except AssertionError:
        print "Error. The out argument is malformed."
        sys.exit(1)

    # Ensures that the out path is valid (i.e. exists).
    if not os.path.exists(out_path):
        print "Error. Invalid path for the output directory."
        sys.exit(1)

    # Ensures that the log file argument is specified.
    if not sys.argv:
        print "Error. The log file argument must be specified."
        sys.exit(1)

    log_path = os.path.abspath(sys.argv[0])

    # Ensures that the log file path is valid (i.e. exists).
    if not os.path.exists(log_path):
        print "Error. Invalid path for the log file."
        sys.exit(1)

    # Extracts the server name from the log file name.
    try:
        print "Extracting the server name..."
        server_name = extract_server_name(log_path)
    except ValueError:
        print "Error. The log file name is malformed."
        sys.exit(1)

    # Extracts the image URLs from the log file content.
    log_file = None

    try:
        log_file = open(log_path, "r")
        log_content = log_file.read()
    except IOError:
        print "Error. Unable to open (or read) the log file."
        sys.exit(1)
    finally:
        if log_file:
            log_file.close()

    print "Extracting the image URLs..."
    image_urls = extract_urls(server_name, log_content)

    # Ensures there are valid image URLs prior to continuing.
    if not image_urls:
        print "Error. Invalid log file content. No image URLs were found."
        sys.exit(1)

    # Downloads the images to the out path.
    try:
        print "Downloading the images..."
        download_images(image_urls, out_path)
    except requests.exceptions.ConnectionError:
        print "Error. Unable to connect to the server."
        sys.exit(1)
    except requests.exceptions.HTTPError:
        print "Error. Unable to download the image file."
        sys.exit(1)
    except IOError:
        print "Error. Unable to create (or write to) the image file due to insufficient permissions."
        sys.exit(1)

    # Generates the HTML file and saves it to the out path.
    try:
        print "Generating the HTML file..."
        generate_html(image_urls, out_path)
    except IOError:
        print "Error. Unable to create (or write to) the HTML file due to insufficient permissions."
        sys.exit(1)

    # OK.
    print "Done!"
    sys.exit(0)


if __name__ == "__main__":
    main()


# Spoiler: the 'animal' puzzle is the Easter Bunny, and the 'place' puzzle is the Eiffel Tower.