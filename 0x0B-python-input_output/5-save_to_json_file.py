#!/usr/bin/python3
""" Module that writes an Object to a text file using
a JSON representation
"""
import json


def save_to_json_file(my_obj, filename):
    """ Function that writes an object to a text file
    by a JSON representation

    Args:
        my_obj: objec to write
        filename: textfile name

    Returns:
        my_obj: text writen injson rep

    """
    with open(filename, 'w', encoding="utf-8") as f:
        json.dump(my_obj, f)
