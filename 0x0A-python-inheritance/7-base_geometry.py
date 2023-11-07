#!/usr/bin/python3

"""Defines a base geometry class BaseGeometry"""


class BaseGeometry:
    """A class representing  a base geometry"""

    def area(self):
        """method not implemented yet"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates value"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
