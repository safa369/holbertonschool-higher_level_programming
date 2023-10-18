#!/usr/bin/python3
"""model of function that print a text"""


def text_indentation(text):
    """function that print a text
    Args:
        text(str): text to print it
    Raises:
        text must be a string
    Returns:
        None"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    
    for ind, i in enumerate(text):
        if i in ".?:":
            print(i, end="")
            print("\n")
            print()
        elif i == " ":
            if text[ind - 1] in ".?:":
                continue
            else:
                print(i, end="")
        else:
            print(i, end="")
        