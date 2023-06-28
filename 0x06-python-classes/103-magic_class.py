#!/usr/bin/python3
"""This module defines a public class Square"""


import math


class MagicClass:
    """This class represents a MagicClass with a private
    instance attribute of radius."""

    def __init__(self, radius=0):
        """Initializes the MagicClass with the given radius.
        Args:
            radius (float): The radius of the MagicClass circle. Default 0.
        Raises:
            TypeError: If the radius is not a num.
        """
        if not isinstance(radius, (int, float)):
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """Calculate and return the area of the MagicClass circle.
        Returns:
            float: The area parameter of the MagicClass circle.
        """
        return math.pi * self.__radius ** 2

    def circumference(self):
        """Calculate and return the circumference of MagicClass circle.
        Returns:
            float: The circumference parameter of the MagicClass circle.
        """
        return 2 * math.pi * self.__radius
