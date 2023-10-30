#!/usr/bin/python3


"""
The module is text_indentation
Prints a text with 2 new lines after each of these characters: ., ? and :
"""


def text_indentation(text):
    """
    Prints a text
    Args:
        text(string)
    no space at the beginning or end of each printed line
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    count = 0
    while count < len(text) and text[count] == " ":
        count = count + 1

    while count < len(text):
        print(text[count], end="")
        if text[count] == "\n" or text[count] in ".?:":
            if text[count] in ".?:":
                print("\n")
            count = count + 1
            while count < len(text) and text[count] == " ":
                count = count + 1
            continue
        count = count + 1
