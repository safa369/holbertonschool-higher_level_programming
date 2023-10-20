#!/usr/bin/python3
"""module to write in file name"""


def write_file(filename="", text=""):
    """function write in file
    Args:
        filename(str): the name of file
        text(str): the text to write it into the file"""
    with open(filename, 'w', encoding="utf8") as f:
        return f.write(text)
