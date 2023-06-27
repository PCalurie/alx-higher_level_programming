#!/usr/bin/python3
class Square:
    def __init__(self, size=0):
        self.size = size
    @size.setter
    def size(self, value):
        """Sets the size of the square"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
# Public instance method
    def area(self):
        """Returns the current square area"""
        return self.__size ** 2
