#!/usr/bin/python3

"""converting from JSON string to python data structure"""

import json
"""provides the functions needed for conversion"""


def from_json_string(my_str):
    """Returns the Python object representation of a JSON string"""
    return json.loads(my_str)
