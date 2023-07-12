#!/usr/bin/python3
"""This Module contains a function that reads from a file """


def read_file(filename=""):
    """ Function that reads from a utf-8 file

    Args:
        filename: filename

    Raises
        Exception: when the file can be opened

    """

    with open(filename, 'r', encoding="utf-8") as f:
        contents = f.read()
        print(cotents, end="")
