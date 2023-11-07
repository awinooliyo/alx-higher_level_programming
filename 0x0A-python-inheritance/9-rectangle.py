#!/usr/bin/python3

"""Inherits from baseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """a class defining the rectangle using BaseGeometry"""

    def __init__(self, width, height):
        """Initialize a new Rectangle
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """Returns area of a ractangle and overrides area() from superclass"""
        return self.__width * self.__height

    def __str__(self):
        """Returns a human readable string representation"""
        return str("[Rectangle] {}/{}".format(self.__width, self.__height))
