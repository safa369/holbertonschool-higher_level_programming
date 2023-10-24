#!/usr/bin/python3
"""module of pascal tringle"""


def pascal_triangle(n):
    """function that return a list of list of integers
    Args:
        n(int): integer
    Return:
        list of list of integers"""
    triangle = []
    if n <= 0:
        return triangle
    elif type(n) is not int:
        n = int(n)
    else:
        for i in range(1, n+1):
            list = []
            c = 1
            for j in range(1, i + 1):
                list.append(c)
                c = c * (i - j) // j
            triangle.append(list)
        return triangle
