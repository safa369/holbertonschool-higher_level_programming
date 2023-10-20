#!/usr/bin/python3
"""module of read a file"""


def read_file(filename=""):
    """function that read file
    Args:
        filename(str): the name of file to read it"""
    with open(filename, 'r', encoding="utf-8") as f:
        fo = f.read()
        print(fo)
