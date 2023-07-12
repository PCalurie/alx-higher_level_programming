#!/usr/bin/python3
"""a child class Square that inherits from parent Rectangle"""

# Import Rectangle from 9-rectangle.py module
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A child class that represents a square"""

    def __init__(self, size):
        """Initializes a square with size"""
        # Validate size as a +ve integer
        self.integer_validator("size", size)
        # Assign size to a private attribute
        self.__size = size
        # Call the parent class constructor with width and height equal to size
        super().__init__(size, size)

    def area(self):
        """Return the area of the square"""
        return self.__size ** 2

    def __str__(self):
        """Return the string representing the square"""
        return "[Square] {}/{}".format(self.__size, self.__size)
