#!/usr/bin/python3

"""Checks if an object is an instance of a class
or an inherited class
"""


def is_kind_of_class(obj, a_class):
    """Returns True if the object is an instance of a class
    or a class that inherited from, otherwise False
    """
    return (isinstance(obj, a_class))
