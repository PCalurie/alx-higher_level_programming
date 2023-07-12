#!/usr/bin/python3
"""This Module contains a function that writes and overwrites
from a utf-8 file """


def write_file(filename="", text=""):
    """ Function that writes from a utf-8 file

    Args:
        filename: filename
        text: text to be written

    Return:
        Number of char written in a file

    """

    with open(filename, 'w', encoding="utf-8") as f:
        num_chars = f.write(text)
        return num_chars
