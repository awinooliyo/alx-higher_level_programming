#!/usr/bin/python3

"""The module inherits from list"""


class MyList(list):
    """A class that inherits from list"""
    def print_sorted(self):
        """prints the sorted list"""
        print(sorted(self))
