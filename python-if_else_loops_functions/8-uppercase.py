#!/usr/bin/python
def uppercase(str):
    for x in str:
        c = ord(x)
        if c <= 122 and c >= 97:
            c -= 32
        print("{:c}".format(c), end='')
    print()
