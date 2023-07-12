#!/usr/bin/python3
"""
This a script that tests if the object is an instance of,
or if the object is an instance of a class
that it was inherited from
"""


def is_kind_of_class(obj, a_class):
    """
    Returns True if the object is an instance of, or if the object is
    an instance of a class that it was inherited from,
    """

    return isinstance(obj, a_class)
