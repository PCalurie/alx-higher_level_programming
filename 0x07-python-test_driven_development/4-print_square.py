#!/usr/bin/python3
"""

This module is composed by a function that prints a square with the char #

"""


def print_square(size):
    """ Function that prints a square with the char #

    Args:
        size: size of the square printed

    Returns:
        Nothing

    Raises:
        TypeError: If size is not an int


    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        print("#" * size)
