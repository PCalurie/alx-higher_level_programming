#!/usr/bin/python3
"""This module defines a class of Square"""


class Square:
    """This class represents a square with private instance attribute of size"""

    def __init__(self, size=0):
        """Instantializes the square with the given size"""
        self.size = size  # Note the use of the setter in the func

    @property
    def size(self):
        """Returns the size of the specified square"""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size of the given square"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns the area of the current square"""
        return self.__size ** 2
