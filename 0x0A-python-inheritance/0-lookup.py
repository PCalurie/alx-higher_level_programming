#!/usr/bin/python3
"""
A function that returns the list of available attributes
and methods of an object
"""


def lookup(obj):
    """
    This function returns the list of attributes and methods of and obj

    Args:
        obj: The object to get the attributes and methods from.

    Returns:
        A list containing the attributes and methods of the object
    """
    # create an empty list to store attributes of the object.
    elements = []
    # loop through the elements of in the object
    for element in dir(obj):
        # append the element to the list
        elements.append(element)
    # return the list of elements
    return elements
