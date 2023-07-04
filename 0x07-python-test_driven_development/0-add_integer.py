#!/usr/bin/python3
"""

This module is composed by a function that adds 2 nums

"""


def add_integer(a, b=98):
    """ Function that adds two ins &/ float numbers

    Args:
        a: 1st number
        b: 2nd number

    Returns:
        The addition of the two numbers

    Raises:
        TypeError: If a or b aren't int or float numbers

    """

    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    return (a + b)
