#!/usr/bin/python3
"""
This a script that checks if the object is an instance of child class
(directly or indirectly) from the specified class
"""


def inherits_from(obj, a_class):
    """
    Returns True if the object is an instance of a child class
    that (directly or indirectly) waas inherited from the specified class
    """

    return issubclass(type(obj), a_class) and type(obj) is not a_class
