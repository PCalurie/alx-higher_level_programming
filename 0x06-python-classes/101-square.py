#!/usr/bin/python3
"""this module defines a class called square"""


class Square:
    """
    this class represents a square with private
    instance attributes of size and position.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes the square with given size and position.

        Args:
            size (int): The size of the square. Default at 0
            position (tuple): The position of square. Default is (0, 0).
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """
        Retrieve the size of the square.

        Returns:
            int: The size of square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Set the size of the square.

        Args:
            value (int): The size param of the square.

        Raises:
            TypeError: If the value is not an int.
            ValueError: If the value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """
        Retrieve the position of square.

        Returns:
            tuple: The position of square.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Sets the position of square.

        Args:
            value (tuple): The position of the square parameter.

        Raises:
            TypeError: If the value is not a tuple of 2 positive ints.
        """
        if not isinstance(value, tuple) or len(value) != 2 or\
                not all(isinstance(val, int) for val in value) or\
                not all(val >= 0 for val in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        Returns the area of the current area of the square.

        Returns:
            int: The area of square.
        """
        return self.__size ** 2

    def my_print(self):
        """
        Prints the square with the char '#'.

        If size is equal to 0, prints an empty line.
        """
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print(' ' * self.__position[0] + '#' * self.__size)

    def __str__(self):
        """
        Returns the string representing the square.

        The square is represented by the '#' char.

        Returns:
            str: The string represents the square.
        """
        result = ""
        if self.__size == 0:
            return result
        else:
            for _ in range(self.__position[1]):
                result += "\n"
            for _ in range(self.__size):
                result += ' ' * self.__position[0] + '#' * self.__size + "\n"
        return result.rstrip()
