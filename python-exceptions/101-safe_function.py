#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        f = fct(*args)
        return f
    except Exception as e:
        print("Exeption: {}".format(e), file=sys.stderr)
        return None
