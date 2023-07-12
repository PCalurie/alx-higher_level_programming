#!/usr/bin/python3
"""This module defines a class BaseGeometry with a public instance area"""


class BaseGeometry:
    """A parent class for geometry objects"""

    def area(self):
        """Raises an exception with the message area() if not successful"""
        raise Exception("area() is not implemented")
