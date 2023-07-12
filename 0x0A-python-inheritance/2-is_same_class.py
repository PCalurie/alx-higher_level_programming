#!/usr/bin/python3
"""
This a script that checks if the object
is exactly an instance of the class specified
"""


def is_same_class(obj, a_class):
    """
    Returns True if the object is exactly an instance of the specified class
    """

    return type(obj) is a_class
