#!/usr/bin/python3
for i in range(1, 10):
    print("{:02d}, ".format(i), end='')
for i in range(10, 90):
    if i % 10 < i/10:
        continue
    elif i % 10 == i / 10:
        continue
    if i < 89:
        print("{:02d}, ".format(i), end='')
print("89")
