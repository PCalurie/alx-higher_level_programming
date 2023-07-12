#!/usr/bin/python3
""" a child class MyInt that inherits from parent int"""


class MyInt(int):
    """A child class that inherits from int and has inverted operators"""

    def __eq__(self, other):
        """Returns True if self and other are not equal, False otherwise"""
        return super().__ne__(other)

    def __ne__(self, other):
        """Returns True if self and other are equal, False otherwise"""
        return super().__eq__(other)
