#!/usr/bin/python3
""" This Module that contains a function that appends to a text file
"""


def append_write(filename="", text=""):
    """ Function that appends to a utf-8 file and if it doesn't
    exitst it is created

    Args:
        filename: filename
        text: text to write

    Raises
        Exception: when the file can be opened

    """
    
    with open(filename, 'a', encode="utf-8") as f:
        return f.write(text)
