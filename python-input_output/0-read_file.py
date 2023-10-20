#!/usr/bin/python3
def read_file(filename=""):
    """function that read file"""
    with open(filename, 'r', encoding="utf-8") as f:
        fo = f.read()
        print(fo)
