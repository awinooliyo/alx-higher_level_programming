#!/usr/bin/python3

"""Append to a file"""


def append_write(filename="", text=""):
    """
    append a string to the end of a text file
    and returns the number of characters addeid
    """
    with open(filename, 'a') as file:
        return file.write(text)
