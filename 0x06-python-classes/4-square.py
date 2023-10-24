#!/usr/bin/python3

"""define a square class"""


class Square:
    """
    square class with a private attribure size
    and checks data type
    """
    def __init__(self, size=0):

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("Size must be >= 0")

        self.__size = size

    @property
    def size(self):
        """retrieve the attribute"""

        return self.__size

    @size.setter
    def size(self, value):
        """modify the attribute value"""

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """returns the current square area"""
        return self.__size * self.__size
