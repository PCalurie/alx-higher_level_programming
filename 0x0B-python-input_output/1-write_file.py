#!/usr/bin/python3
""" Module that contains a function that writes to a utf-8 file
"""


def write_file(filename="", text=""):
    """ Function that writes to a utf-8 file

    Args:
        filename: name of the file
        text: text to write

    Returns
        Number of chars: num_chars

    """

    with open(filename, 'w', encoding="utf-8") as f:
        num_chars = f.write(text)
        return num_chars
