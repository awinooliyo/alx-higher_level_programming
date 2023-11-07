#!/usr/bin/python3
"""This module defines a Python class-toJSON function"""


def class_to_json(obj):
    """Returns the dictionary representation of a simple data structure"""
    return obj.__dict__
