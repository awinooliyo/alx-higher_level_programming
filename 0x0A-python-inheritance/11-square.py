#!/usr/bin/python3

"""Importing Rectangle"""

Rectangle = __import__('9-rectangle').Rectangle


"""Write a class Square that inherits from Rectangle"""


class Square(Rectangle):
    """A subclass of a Rectangle"""

    def __init__(self, size):
        """Initialize private attribute size and validate it"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """Returns area of a square"""
        return self.__size ** 2

    def __str__(self):
        """Return and print description of square"""
        return str("[Square] {:d}/{:d}".format(self.__size, self.__size))
