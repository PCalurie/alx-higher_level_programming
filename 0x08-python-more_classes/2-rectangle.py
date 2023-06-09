#!/usr/bin/python3

"""Define a rectangle class"""


class Rectangle:
    """Define a Rectangle class with private attribute"""

    def __init__(self, width=0, height=0):
        """Initialize a rectangle with the given width and height.

        Args:
            width: The width of the rectangle.
            height: The height of the rectangle.
        """
        self._width = width
        self._height = height

    @property
    def width(self):
        """Return the width of the rectangle."""
        return self._width

    @width.setter
    def width(self, value):
        """Set the width of the rectangle.

        Args:
            value: The new width of the rectangle.

        Raises:
            TypeError: If value is not an int.
            ValueError: If value is less than zero.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self._width = value

    @property
    def height(self):
        """Return the height of the rectangle."""
        return self._height

    @height.setter
    def height(self, value):
        """Set the height of the rectangle.

        Args:
            value: The new height of the rectangle.

        Raises:
            TypeError: If value is not annt.
            ValueError: If value is less than zero.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self._height = value

    def area(self):
        """Return the area of the rectangle"""
        return self.width * self.height

    def perimeter(self):
        """Return the perimeter of the rectangle"""
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)
