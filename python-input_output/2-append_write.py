#!/usr/bin/python3
"""module to appends strings """


def append_write(filename="", text=""):
    """function that appends strings at the end of file
    Args:
        filename(str): the name of file
        text(str): the text to append it into the file"""
    with open(filename, 'a', encoding="utf8") as f:
        return f.write(text)
