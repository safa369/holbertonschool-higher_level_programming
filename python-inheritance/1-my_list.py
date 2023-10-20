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
        new_list = self.copy()
        new_list = sorted(new_list)
        print(new_list)

