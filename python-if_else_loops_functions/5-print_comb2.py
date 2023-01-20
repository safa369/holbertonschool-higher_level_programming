#!/usr/bin/python3
for i in range(0, 100):
    if i == 0:
        print("00,", end='')
    elif i == 99:
        print(" 99")
    else:
        print(" %2d," % (i), end='')
