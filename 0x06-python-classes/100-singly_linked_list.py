#!/usr/bin/python3
"""this module defines a class of square"""


class Square:
    """
    this class represents a square with private
    instance attributes of size and position.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Instantiate the square with the given size and position.

        Args:
            size (int): The size of the square. Default is 0.
            position (tuple): The position of the square Default is (0, 0).
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """
        Retrieves the size of square.

        Returns:
            int: The size of square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the size of square.

        Args:
            value (int): The size of square.

        Raises:
            TypeError: If the value is not an int.
            ValueError: If the value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an int")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """
        Retrieves the position of square.

        Returns:
            tuple: The position of square.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Sets the position of square.

        Args:
            value (tuple): The position of square.

        Raises:
            TypeError: If the value is not a tuple of 2 +ve int
        """
        if not isinstance(value, tuple) or len(value) != 2 or\
                not all(isinstance(val, int) for val in value) or\
                not all(val >= 0 for val in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        Returns the current area of square

        Returns:
            int: The area of square
        """
        return self.__size ** 2

    def my_print(self):
        """
        Prints square with the character '#'.

        If size is equal to 0, print an empty line.
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
        Returns the string representing square.

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
