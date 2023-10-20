#!/usr/bin/python3
"""moule of my list"""


class MyList(list):
    """class of my list
    Attributes:
        list(class): the list to print it
    Args:None
    Raises: the element of list must be integer
    Rteurn:ascending list"""

    def print_sorted(self):
        """function to print sorted list"""
        print(sorted(self))
