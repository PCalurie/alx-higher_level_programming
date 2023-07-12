#!/usr/bin/python3
""" A Module that contains a function that returns an object in
a JSON string format of a python data structure
"""
import json


def from_json_string(my_str):
    """ Function that returns an object by a JSON rep

    Args:
        my_str: JSON representation of the obj data

    Returns:
        my_str: return the json str

    """
    return json.loads(my_str)
