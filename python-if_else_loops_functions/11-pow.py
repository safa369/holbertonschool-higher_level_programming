#!/usr/bin/python3
def pow(a, b):
    p = 1
    if b < 0:
        return (0.0001)
    else:
        for i in range(0, b):
            p *= a
        return (p)
