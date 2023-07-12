#!/usr/bin/python3
"""a class Square that inherits from a base Rectangle"""


# Import Rectangle from 9-rectangle.py module
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A child class that represents a square"""

    def __init__(self, size):
        """Initialize a square with size"""
        # Validate size as a +ve integer
        self.integer_validator("size", size)
        # assign size to a private attribute
        self.__size = size
        # call the parent class constructor with width and height equal to size
        super().__init__(size, size)

    def area(self):
        """Return the area of the square"""
        return self.__size ** 2
