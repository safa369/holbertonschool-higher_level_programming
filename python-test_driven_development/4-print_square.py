#!/usr/bin/python3
"""Module function to print square"""


def print_square(size):
    """fonction to print a square
    Args:
        size(int): the size of square
    Raises: size must be integer and >= 0
    Returns: None"""
    if type(size) != int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if size == 0:
        print("", end="")
    for i in range(size):
        print("#" * size)
