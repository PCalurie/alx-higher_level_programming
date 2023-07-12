#!/usr/bin/python3
"""This module defines a class BaseGeometry with a public instance area"""


class BaseGeometry:
    """A parent class for geometry objects"""

    def area(self):
        """Raises an exception with the message area() if not successful"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Assume name is always a string"""
        # Check if value is an integer
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        # Check if value is greater than 0
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
