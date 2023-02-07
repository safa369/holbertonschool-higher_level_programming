#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    mys_list = []
    count = 0
    for i in range(0, len(my_list) - 1):
        if i % 2 == 0:
            mys_list.insert(i, True)
        else:
            mys_list.insert(i, False)
    return mys_list
